#!/usr/bin/env python3
"""
mcp_server.py – Serveur MCP custom pour la base Qdrant N2.

Pourquoi custom et pas mcp-server-qdrant officiel ?
Le serveur officiel utilise fastembed (MiniLM) pour embedder les requêtes. Or
notre base a été indexée avec Gemini embedding-001 (3072 dims). Les espaces
vectoriels sont incompatibles : une requête fastembed sur des points Gemini
produit des scores aléatoires.

Ce serveur wrap notre GeminiEmbedder existant pour garantir la cohérence du
pipeline (même modèle à l'ingestion et à la requête, avec task_type asymétrique
RETRIEVAL_DOCUMENT / RETRIEVAL_QUERY).

Outils exposés :
  - qdrant_search(query, top, filter_type, filter_source_key)  : recherche sémantique
  - qdrant_stats()                                              : état de la base
  - qdrant_find_similar(text, top, exclude_source_file)         : anti-répétition (pour brand-check)

Usage dans .mcp.json :
  {
    "mcpServers": {
      "qdrant-n2": {
        "command": "python3",
        "args": ["_integrations/qdrant/mcp_server.py"]
      }
    }
  }
"""

from __future__ import annotations

import logging
import os
import sys
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from qdrant_client import QdrantClient
from qdrant_client.http import models as rest

import utils
from embedders import GeminiEmbedder

# Silence noisy loggers
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("qdrant_mcp")

# Load env from project root (.env)
PROJECT_ROOT = HERE.parent.parent
load_dotenv(PROJECT_ROOT / ".env")

# Load config and initialize clients once at startup
_cfg = utils.load_config()
_embedder = GeminiEmbedder(_cfg, logger=logger)
_client = QdrantClient(
    url=os.environ["QDRANT_URL"],
    api_key=os.environ["QDRANT_API_KEY"],
    timeout=60,
)
_collection = _cfg["qdrant"]["collection"]

# Initialize MCP server
mcp = FastMCP("qdrant-n2")


def _format_hit(pt: Any) -> dict:
    """Normalize a Qdrant scored point into a compact dict."""
    p = pt.payload or {}
    return {
        "score": round(float(pt.score), 4),
        "source_file": p.get("source_file"),
        "type": p.get("type"),
        "channel": p.get("channel"),
        "author": p.get("author"),
        "date": p.get("date"),
        "summary": p.get("summary"),
        "entities": (p.get("entities") or [])[:15],
        "claims": (p.get("claims") or [])[:5],
        "content_preview": (p.get("content_text") or "")[:500],
        "chunk_index": p.get("chunk_index"),
    }


def _build_filter(filter_type: str | None, filter_source_key: str | None, filter_channel: str | None, exclude_source_file: str | None) -> rest.Filter | None:
    must: list = []
    must_not: list = []
    if filter_type:
        must.append(rest.FieldCondition(key="type", match=rest.MatchValue(value=filter_type)))
    if filter_source_key:
        must.append(rest.FieldCondition(key="source_key", match=rest.MatchValue(value=filter_source_key)))
    if filter_channel:
        must.append(rest.FieldCondition(key="channel", match=rest.MatchValue(value=filter_channel)))
    if exclude_source_file:
        must_not.append(rest.FieldCondition(key="source_file", match=rest.MatchValue(value=exclude_source_file)))
    if not must and not must_not:
        return None
    return rest.Filter(must=must or None, must_not=must_not or None)


@mcp.tool()
def qdrant_search(
    query: str,
    top: int = 5,
    filter_type: str | None = None,
    filter_source_key: str | None = None,
    filter_channel: str | None = None,
) -> list[dict]:
    """
    Recherche sémantique dans la base N2 (newsletters, posts, emails, brand, transcripts, notion).

    Args:
        query: Question ou sujet en langage naturel (FR ou EN).
        top: Nombre de résultats à retourner (défaut 5, max 20).
        filter_type: Filtre par type de contenu. Valeurs : 'newsletter', 'promo',
            'sales-email', 'linkedin-post', 'blog-post', 'brand-doc', 'transcript',
            'landing-page', 'discord-post', 'whatsapp-post'.
        filter_source_key: Filtre par source. Valeurs : 'newsletters', 'promos',
            'sales_outreach', 'linkedin', 'brand', 'notion', 'transcripts',
            'landing_pages', 'outline'.
        filter_channel: Filtre par canal. Valeurs : 'newsletter', 'email',
            'linkedin', 'discord', 'whatsapp', 'blog', 'website', 'internal'.

    Returns:
        Liste de hits, chacun avec score, source_file, type, summary, entities, content_preview.
    """
    top = max(1, min(20, top))
    vec = _embedder.embed_query(query)
    filt = _build_filter(filter_type, filter_source_key, filter_channel, None)
    results = _client.query_points(
        collection_name=_collection,
        query=vec,
        limit=top,
        with_payload=True,
        query_filter=filt,
    ).points
    return [_format_hit(pt) for pt in results]


@mcp.tool()
def qdrant_find_similar(
    text: str,
    top: int = 5,
    exclude_source_file: str | None = None,
    threshold: float = 0.0,
) -> list[dict]:
    """
    Recherche de contenu similaire au texte fourni. Utilisé pour l'anti-répétition :
    avant de publier un draft, vérifier si N2 a déjà publié quelque chose de très
    proche (score > 0.85 = alerte répétition probable).

    Args:
        text: Le draft ou extrait à vérifier.
        top: Nombre de voisins à retourner (défaut 5).
        exclude_source_file: Chemin du fichier source à exclure des résultats
            (utile quand on vérifie un draft qui est déjà indexé).
        threshold: Score minimum pour inclure un résultat (défaut 0 = tous).

    Returns:
        Liste de voisins sémantiques ordonnés par score décroissant.
    """
    top = max(1, min(20, top))
    vec = _embedder.embed_query(text)
    filt = _build_filter(None, None, None, exclude_source_file)
    results = _client.query_points(
        collection_name=_collection,
        query=vec,
        limit=top,
        with_payload=True,
        query_filter=filt,
    ).points
    hits = [_format_hit(pt) for pt in results]
    return [h for h in hits if h["score"] >= threshold]


@mcp.tool()
def qdrant_stats() -> dict:
    """
    État global de la base Qdrant N2.

    Returns:
        Dict avec nombre de points, status, taille par type de contenu.
    """
    info = _client.get_collection(_collection)
    registry = utils.load_registry()
    entries = registry.get("entries", {})

    by_source: dict[str, int] = {}
    by_type: dict[str, int] = {}
    for e in entries.values():
        by_source[e.get("source_key", "?")] = by_source.get(e.get("source_key", "?"), 0) + 1
        by_type[e.get("type", "?")] = by_type.get(e.get("type", "?"), 0) + 1

    return {
        "collection": _collection,
        "points_count": info.points_count,
        "status": str(info.status),
        "registry_entries": len(entries),
        "by_source_key": by_source,
        "by_type": by_type,
        "last_sync": registry.get("last_sync", {}),
    }


if __name__ == "__main__":
    mcp.run()
