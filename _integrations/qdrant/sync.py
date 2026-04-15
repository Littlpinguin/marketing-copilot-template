#!/usr/bin/env python3
"""
sync.py – CLI principal du pipeline Qdrant N2.

Implémente les 6 phases documentées dans runbook.md :
  1. Détection des changements (diff sources ↔ registry via content_hash)
  2. Chunking
  3. Enrichissement (hash, summary, entities, claims, meeting)
  4. Embedding Gemini
  5. Upsert Qdrant
  6. Mise à jour du registre

Usage :
    python3 sync.py --all
    python3 sync.py --source brand --dry-run --limit 2
    python3 sync.py --stats
    python3 sync.py --query "satisfaction des freelances" --top 5
    python3 sync.py --verify
    python3 sync.py --source brand --force
"""

from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path
from typing import Any

# Ensure local imports work
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.http import models as rest

import utils
from embedders import GeminiEmbedder
from enrichers import build_enrichers
from sources import get_connector


def build_qdrant_client(cfg: dict) -> QdrantClient:
    return QdrantClient(
        url=os.environ["QDRANT_URL"],
        api_key=os.environ["QDRANT_API_KEY"],
        timeout=60,
    )


# -----------------------------------------------------------------------------
# Phase 1 — Detect changes
# -----------------------------------------------------------------------------

def detect_changes(source_key: str, source_cfg: dict, full_cfg: dict, registry: dict, force: bool, limit: int | None, logger):
    connector_name = source_cfg["connector"]
    connector = get_connector(connector_name)

    source_cfg_with_key = dict(source_cfg)
    source_cfg_with_key["_key"] = source_key

    new, updated, skipped = [], [], []
    count = 0

    for doc in connector.iter_documents(source_cfg_with_key, full_cfg):
        if limit is not None and count >= limit:
            break
        count += 1

        source_file = doc["source_file"]
        content = doc["content"]
        meta = doc["metadata"]
        chash = utils.content_hash(content)

        existing = registry["entries"].get(source_file)
        base = {"source_file": source_file, "content": content, "metadata": meta, "content_hash": chash}

        if not existing:
            new.append({**base, "action": "new"})
        elif force:
            # Forced re-ingest: treat as update so upsert_chunks deletes old point_ids first.
            updated.append({**base, "action": "update", "existing": existing})
        elif existing.get("content_hash") != chash:
            updated.append({**base, "action": "update", "existing": existing})
        else:
            skipped.append(source_file)

    logger.info("[%s] detected: new=%d, updated=%d, skipped=%d", source_key, len(new), len(updated), len(skipped))
    return new + updated, skipped


# -----------------------------------------------------------------------------
# Phase 2 — Chunking
# -----------------------------------------------------------------------------

def chunk_doc(doc: dict, source_cfg: dict) -> list[dict]:
    strategy = source_cfg.get("chunking", "whole")
    chunks_raw = utils.chunk_text(doc["content"], strategy, source_cfg)
    chunks = []
    for i, text in enumerate(chunks_raw):
        chunk = {
            "source_file": doc["source_file"],
            "chunk_index": i,
            "chunks_total": len(chunks_raw),
            "content": text,
            "metadata": dict(doc["metadata"]),
            "content_hash": doc["content_hash"],
            "action": doc["action"],
        }
        if "existing" in doc:
            chunk["existing"] = doc["existing"]
        chunks.append(chunk)
    return chunks


# -----------------------------------------------------------------------------
# Phase 3 — Enrichment
# -----------------------------------------------------------------------------

def enrich_chunk(chunk: dict, enrichers_list: list) -> None:
    doc_type = chunk["metadata"].get("type", "")
    for enr in enrichers_list:
        if not enr.applies(doc_type):
            continue
        extra = enr.run(chunk["content"], chunk["metadata"])
        if extra:
            chunk["metadata"].update(extra)


# -----------------------------------------------------------------------------
# Phase 4 — Embedding
# -----------------------------------------------------------------------------

def embed_chunks(chunks: list[dict], embedder: GeminiEmbedder, logger) -> list[dict]:
    embedded = []
    for i, chunk in enumerate(chunks, 1):
        try:
            vec = embedder.embed(chunk["content"])
            chunk["_vector"] = vec
            embedded.append(chunk)
        except Exception as e:
            logger.error("Embedding failed for %s chunk %d: %s", chunk["source_file"], chunk["chunk_index"], e)
        if i % 10 == 0:
            logger.info("  embedded %d/%d", i, len(chunks))
    return embedded


# -----------------------------------------------------------------------------
# Phase 5 — Qdrant upsert
# -----------------------------------------------------------------------------

def upsert_chunks(client: QdrantClient, collection: str, chunks: list[dict], registry: dict, logger, batch_size: int = 50):
    # Delete stale points first (for update cases)
    to_delete: list[str] = []
    for chunk in chunks:
        if chunk.get("action") == "update" and chunk.get("chunk_index") == 0:
            existing = chunk.get("existing", {})
            to_delete.extend(existing.get("qdrant_point_ids", []))

    if to_delete:
        logger.info("  deleting %d stale points", len(to_delete))
        client.delete(
            collection_name=collection,
            points_selector=rest.PointIdsList(points=to_delete),
        )

    # Batch upsert
    points = []
    for chunk in chunks:
        meta = chunk["metadata"]
        payload = {
            **meta,
            "content_text": chunk["content"],
            "content_hash": chunk["content_hash"],
            "chunk_index": chunk["chunk_index"],
            "chunks_total": chunk["chunks_total"],
            "ingested_at": utils.now_iso(),
        }
        # Remove None values (Qdrant tolerates them but cleaner)
        payload = {k: v for k, v in payload.items() if v is not None}

        pid = utils.point_uuid(chunk["source_file"], chunk["chunk_index"])
        chunk["_point_id"] = pid
        points.append(rest.PointStruct(id=pid, vector=chunk["_vector"], payload=payload))

    total = len(points)
    for i in range(0, total, batch_size):
        batch = points[i : i + batch_size]
        client.upsert(collection_name=collection, points=batch)
        logger.info("  upserted %d/%d", min(i + batch_size, total), total)


# -----------------------------------------------------------------------------
# Phase 6 — Registry update
# -----------------------------------------------------------------------------

def update_registry(chunks: list[dict], source_key: str, registry: dict) -> None:
    by_file: dict[str, list[dict]] = {}
    for chunk in chunks:
        by_file.setdefault(chunk["source_file"], []).append(chunk)

    for source_file, file_chunks in by_file.items():
        first = file_chunks[0]
        registry["entries"][source_file] = {
            "content_hash": first["content_hash"],
            "ingested_at": utils.now_iso(),
            "source_key": source_key,
            "type": first["metadata"].get("type", ""),
            "chunks_total": len(file_chunks),
            "qdrant_point_ids": [c["_point_id"] for c in file_chunks],
        }
        if first["metadata"].get("notion_last_edited"):
            registry["entries"][source_file]["notion_last_edited"] = first["metadata"]["notion_last_edited"]

    registry["last_sync"][source_key] = utils.now_iso()
    registry["last_sync"]["all"] = utils.now_iso()


# -----------------------------------------------------------------------------
# Orchestration per source
# -----------------------------------------------------------------------------

def process_source(source_key: str, source_cfg: dict, full_cfg: dict, registry: dict,
                    client: QdrantClient, embedder: GeminiEmbedder, enrichers_list: list,
                    dry_run: bool, force: bool, limit: int | None, logger) -> dict:
    logger.info("=" * 60)
    logger.info("SOURCE: %s (connector=%s, type=%s)", source_key, source_cfg["connector"], source_cfg.get("type", "?"))

    # Phase 1
    docs_to_ingest, skipped = detect_changes(source_key, source_cfg, full_cfg, registry, force, limit, logger)

    if not docs_to_ingest:
        return {"new": 0, "updated": 0, "skipped": len(skipped), "chunks": 0}

    # Phase 2
    all_chunks: list[dict] = []
    for doc in docs_to_ingest:
        chunks = chunk_doc(doc, source_cfg)
        logger.info("  %s → %d chunk(s)", doc["source_file"], len(chunks))
        all_chunks.extend(chunks)

    if dry_run:
        logger.info("DRY-RUN: would enrich + embed + upsert %d chunks", len(all_chunks))
        for chunk in all_chunks[:3]:
            preview = chunk["content"][:150].replace("\n", " ")
            logger.info("    sample[%d]: %s…", chunk["chunk_index"], preview)
        return {"new": len([d for d in docs_to_ingest if d.get("action") == "new"]),
                "updated": len([d for d in docs_to_ingest if d.get("action") == "update"]),
                "skipped": len(skipped),
                "chunks": len(all_chunks),
                "dry_run": True}

    # Phase 3
    logger.info("enriching %d chunks…", len(all_chunks))
    for i, chunk in enumerate(all_chunks, 1):
        enrich_chunk(chunk, enrichers_list)
        if i % 5 == 0:
            logger.info("  enriched %d/%d", i, len(all_chunks))

    # Phase 4
    logger.info("embedding %d chunks…", len(all_chunks))
    embedded = embed_chunks(all_chunks, embedder, logger)

    # Phase 5
    if embedded:
        collection = full_cfg["qdrant"]["collection"]
        batch_size = full_cfg["qdrant"].get("batch_size", 50)
        upsert_chunks(client, collection, embedded, registry, logger, batch_size)

    # Phase 6
    update_registry(embedded, source_key, registry)

    return {
        "new": len([d for d in docs_to_ingest if d.get("action") == "new"]),
        "updated": len([d for d in docs_to_ingest if d.get("action") == "update"]),
        "skipped": len(skipped),
        "chunks": len(embedded),
    }


# -----------------------------------------------------------------------------
# Commands
# -----------------------------------------------------------------------------

def cmd_sync(args, cfg, logger):
    utils.load_env()
    client = build_qdrant_client(cfg)
    embedder = GeminiEmbedder(cfg, logger)
    enrichers_list = build_enrichers(cfg, logger)

    registry = utils.load_registry()

    if args.source:
        sources_to_run = {args.source: cfg["sources"][args.source]}
    else:
        sources_to_run = dict(cfg["sources"])

    total = {"new": 0, "updated": 0, "skipped": 0, "chunks": 0}
    for source_key, source_cfg in sources_to_run.items():
        try:
            stats = process_source(
                source_key, source_cfg, cfg, registry, client, embedder, enrichers_list,
                dry_run=args.dry_run, force=args.force, limit=args.limit, logger=logger,
            )
            for k in ["new", "updated", "skipped", "chunks"]:
                total[k] += stats.get(k, 0)
        except Exception as e:
            logger.exception("[%s] failed: %s", source_key, e)

    if not args.dry_run:
        utils.save_registry(registry)

    logger.info("=" * 60)
    logger.info("TOTAL: new=%d updated=%d skipped=%d chunks=%d", total["new"], total["updated"], total["skipped"], total["chunks"])
    logger.info("registry: %s", "not written (dry-run)" if args.dry_run else "saved")
    return 0


def cmd_stats(args, cfg, logger):
    registry = utils.load_registry()
    entries = registry.get("entries", {})
    by_source: dict[str, int] = {}
    by_type: dict[str, int] = {}
    for e in entries.values():
        by_source[e.get("source_key", "?")] = by_source.get(e.get("source_key", "?"), 0) + 1
        by_type[e.get("type", "?")] = by_type.get(e.get("type", "?"), 0) + 1

    print(f"Registry entries: {len(entries)}")
    print(f"Last sync (all): {registry.get('last_sync', {}).get('all', '—')}")
    print()
    print("By source_key:")
    for k, v in sorted(by_source.items(), key=lambda x: -x[1]):
        print(f"  {k:<20} {v}")
    print()
    print("By type:")
    for k, v in sorted(by_type.items(), key=lambda x: -x[1]):
        print(f"  {k:<20} {v}")

    # Qdrant side
    utils.load_env()
    client = build_qdrant_client(cfg)
    info = client.get_collection(cfg["qdrant"]["collection"])
    print()
    print(f"Qdrant collection: {cfg['qdrant']['collection']}")
    print(f"  points : {info.points_count}")
    print(f"  status : {info.status}")
    return 0


def cmd_query(args, cfg, logger):
    utils.load_env()
    client = build_qdrant_client(cfg)
    embedder = GeminiEmbedder(cfg, logger)
    vec = embedder.embed_query(args.query)
    results = client.query_points(
        collection_name=cfg["qdrant"]["collection"],
        query=vec,
        limit=args.top,
        with_payload=True,
    ).points

    print(f"Query: {args.query}")
    print(f"Top {args.top} results:")
    print()
    for i, pt in enumerate(results, 1):
        p = pt.payload or {}
        print(f"[{i}] score={pt.score:.4f}  type={p.get('type', '?')}  source={p.get('source_file', '?')}")
        if p.get("summary"):
            print(f"    summary: {p['summary']}")
        snippet = (p.get("content_text") or "")[:200].replace("\n", " ")
        print(f"    text: {snippet}…")
        print()
    return 0


def cmd_verify(args, cfg, logger):
    utils.load_env()
    client = build_qdrant_client(cfg)
    registry = utils.load_registry()
    entries = registry.get("entries", {})

    info = client.get_collection(cfg["qdrant"]["collection"])
    expected_points = sum(e.get("chunks_total", 0) for e in entries.values())
    actual = info.points_count

    print(f"Registry entries  : {len(entries)}")
    print(f"Expected points   : {expected_points}")
    print(f"Qdrant points     : {actual}")
    if expected_points == actual:
        print("STATUS            : OK (registry and Qdrant agree)")
    else:
        print(f"STATUS            : DRIFT (diff={actual - expected_points})")
    return 0


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description="Qdrant N2 sync CLI")
    parser.add_argument("--all", action="store_true", help="Sync all sources from config.yaml")
    parser.add_argument("--source", help="Sync only this source key")
    parser.add_argument("--dry-run", action="store_true", help="Detect + chunk only, no enrich / embed / upsert")
    parser.add_argument("--force", action="store_true", help="Re-ingest even if content_hash matches")
    parser.add_argument("--limit", type=int, help="Limit the number of documents processed per source")
    parser.add_argument("--stats", action="store_true", help="Show registry + Qdrant stats")
    parser.add_argument("--query", help="Run a semantic query against the collection")
    parser.add_argument("--top", type=int, default=5, help="Number of query results (default 5)")
    parser.add_argument("--verify", action="store_true", help="Check consistency registry ↔ Qdrant")
    args = parser.parse_args()

    cfg = utils.load_config()
    logger = utils.setup_logging(cfg.get("logging", {}).get("level", "INFO"))

    if args.stats:
        return cmd_stats(args, cfg, logger)
    if args.query:
        return cmd_query(args, cfg, logger)
    if args.verify:
        return cmd_verify(args, cfg, logger)
    if args.all or args.source:
        return cmd_sync(args, cfg, logger)

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
