"""
sources/outline.py – Connecteur pour une Knowledge Base Outline (https://www.getoutline.com).

Parcourt les collections configurées dans config.yaml (section
`sources.outline.collections`) via l'API REST Outline, pagine les documents,
et retourne chaque doc comme un candidat à l'ingestion.

Les documents archivés (archivedAt != null) et supprimés (deletedAt != null)
sont ignorés.

Endpoint principal : POST /api/documents.list qui retourne déjà le champ `text`
complet. Pas besoin d'un second documents.info.

Configuration attendue dans config.yaml :
  sources:
    outline:
      connector: outline
      collections:
        "Collection Name": "uuid-of-the-collection"
        "Another Collection": "uuid-..."
"""

from __future__ import annotations

import logging
import os
from typing import Iterable

import requests

logger = logging.getLogger("qdrant_sync")

DEFAULT_PAGE_SIZE = 25


def _headers() -> dict:
    return {
        "Authorization": f"Bearer {os.environ['OUTLINE_API_KEY']}",
        "Content-Type": "application/json",
    }


def _outline_url() -> str:
    return os.environ.get("OUTLINE_URL", "https://app.getoutline.com")


def _list_docs_in_collection(collection_id: str) -> Iterable[dict]:
    base = _outline_url()
    offset = 0
    limit = DEFAULT_PAGE_SIZE
    while True:
        payload = {
            "collectionId": collection_id,
            "limit": limit,
            "offset": offset,
        }
        r = requests.post(f"{base}/api/documents.list", headers=_headers(), json=payload, timeout=30)
        if r.status_code != 200:
            logger.error("Outline documents.list failed %d: %s", r.status_code, r.text[:300])
            return
        data = r.json()
        docs = data.get("data", [])
        for doc in docs:
            yield doc
        pagination = data.get("pagination", {})
        total = pagination.get("total", 0)
        offset += limit
        if offset >= total or not docs:
            return


def iter_documents(source_cfg: dict, global_cfg: dict) -> Iterable[dict]:
    source_key = source_cfg.get("_key", "outline")
    collections = source_cfg.get("collections", {})  # {collection_name: collection_id}

    if not collections:
        logger.warning("No collections configured for outline source")
        return

    for coll_name, coll_id in collections.items():
        logger.info("Outline: scanning collection '%s' (id=%s)", coll_name, coll_id)
        count = 0
        for doc in _list_docs_in_collection(coll_id):
            if doc.get("archivedAt") or doc.get("deletedAt"):
                continue

            doc_id = doc.get("id")
            title = (doc.get("title") or "").strip() or "(untitled)"
            text = (doc.get("text") or "").strip()

            if not text:
                logger.debug("Outline doc %s has empty text, skip", doc_id)
                continue

            full_text = f"# {title}\n\n{text}"

            metadata = {
                "type": source_cfg.get("type", "outline-doc"),
                "source_key": source_key,
                "source_file": f"outline://{doc_id}",
                "language": source_cfg.get("language", "both"),
                "channel": "internal",
                "author": "n2",
                "status": "published",
                "tags": [f"collection:{coll_name.lower().replace(' ', '-')}"],
                "date": doc.get("updatedAt") or doc.get("createdAt"),
                "outline_url": doc.get("url"),
                "outline_updated_at": doc.get("updatedAt"),
            }

            count += 1
            yield {
                "source_file": f"outline://{doc_id}",
                "content": full_text,
                "metadata": metadata,
            }
        logger.info("Outline: collection '%s' → %d documents", coll_name, count)
