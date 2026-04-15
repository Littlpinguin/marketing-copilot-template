#!/usr/bin/env python3
"""
init_collection.py – Création idempotente de la collection Qdrant n2-knowledge.

Lecture du schéma depuis config.yaml. Si la collection existe déjà avec la bonne
dimension + distance, ce script ne fait rien. Sinon il la crée et configure les
index payload.

Usage :
    python3 init_collection.py                # crée si absente, compare si présente
    python3 init_collection.py --recreate     # DROP + CREATE (destructif, confirmation)
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import yaml
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.http import models as rest

HERE = Path(__file__).resolve().parent
PROJECT_ROOT = HERE.parent.parent

# Payload fields we want indexed for efficient filtering.
# Types must match runbook.md section "Schéma de payload".
INDEXED_FIELDS: list[tuple[str, rest.PayloadSchemaType]] = [
    ("type", rest.PayloadSchemaType.KEYWORD),
    ("source_key", rest.PayloadSchemaType.KEYWORD),
    ("source_file", rest.PayloadSchemaType.KEYWORD),
    ("content_hash", rest.PayloadSchemaType.KEYWORD),
    ("language", rest.PayloadSchemaType.KEYWORD),
    ("author", rest.PayloadSchemaType.KEYWORD),
    ("pillar", rest.PayloadSchemaType.KEYWORD),
    ("channel", rest.PayloadSchemaType.KEYWORD),
    ("status", rest.PayloadSchemaType.KEYWORD),
    ("persona_target", rest.PayloadSchemaType.KEYWORD),
    ("tags", rest.PayloadSchemaType.KEYWORD),
    ("entities", rest.PayloadSchemaType.KEYWORD),
    ("date", rest.PayloadSchemaType.DATETIME),
]


def load_config() -> dict:
    with open(HERE / "config.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_client() -> QdrantClient:
    load_dotenv(PROJECT_ROOT / ".env")
    url = os.environ["QDRANT_URL"]
    api_key = os.environ["QDRANT_API_KEY"]
    return QdrantClient(url=url, api_key=api_key, timeout=30)


def ensure_collection(client: QdrantClient, cfg: dict, recreate: bool = False) -> None:
    coll = cfg["qdrant"]["collection"]
    dim = cfg["qdrant"]["vector_size"]
    distance_name = cfg["qdrant"]["distance"]
    distance = {
        "Cosine": rest.Distance.COSINE,
        "Euclid": rest.Distance.EUCLID,
        "Dot": rest.Distance.DOT,
    }[distance_name]

    existing = {c.name for c in client.get_collections().collections}

    if coll in existing:
        info = client.get_collection(coll)
        current_dim = info.config.params.vectors.size
        current_dist = info.config.params.vectors.distance

        if not recreate:
            if current_dim == dim and current_dist == distance:
                print(f"OK  collection '{coll}' already exists (dim={dim}, distance={distance_name})")
            else:
                print(
                    f"WARN collection '{coll}' exists with DIFFERENT schema "
                    f"(dim={current_dim}, distance={current_dist}). "
                    f"Expected dim={dim}, distance={distance_name}. "
                    f"Use --recreate to drop and recreate.",
                    file=sys.stderr,
                )
                sys.exit(1)
        else:
            print(f"DROP collection '{coll}' (--recreate)")
            client.delete_collection(coll)
            existing.discard(coll)

    if coll not in existing:
        print(f"CREATE collection '{coll}' (dim={dim}, distance={distance_name})")
        client.create_collection(
            collection_name=coll,
            vectors_config=rest.VectorParams(size=dim, distance=distance),
        )

    for field, schema_type in INDEXED_FIELDS:
        try:
            client.create_payload_index(
                collection_name=coll,
                field_name=field,
                field_schema=schema_type,
            )
            print(f"INDEX payload field '{field}' ({schema_type.value})")
        except Exception as e:
            # Index already exists or field not yet present: non-fatal
            msg = str(e).lower()
            if "already exists" in msg or "exists" in msg:
                print(f"SKIP index '{field}' (already exists)")
            else:
                print(f"WARN  index '{field}' failed: {e}", file=sys.stderr)

    final = client.get_collection(coll)
    print()
    print(f"Collection summary:")
    print(f"  name   : {coll}")
    print(f"  dim    : {final.config.params.vectors.size}")
    print(f"  points : {final.points_count}")
    print(f"  status : {final.status}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize or verify the N2 Qdrant collection.")
    parser.add_argument(
        "--recreate",
        action="store_true",
        help="Drop and recreate the collection (destructive). Will ask for confirmation.",
    )
    args = parser.parse_args()

    if args.recreate:
        reply = input("DESTRUCTIVE: this will drop the collection and lose all indexed data. Type 'yes' to continue: ")
        if reply.strip().lower() != "yes":
            print("Aborted.")
            return 1

    cfg = load_config()
    client = get_client()
    ensure_collection(client, cfg, recreate=args.recreate)
    return 0


if __name__ == "__main__":
    sys.exit(main())
