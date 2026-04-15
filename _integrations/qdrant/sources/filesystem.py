"""
sources/filesystem.py – Connecteur pour fichiers locaux (markdown, HTML).

Scan un pattern glob, exclut selon config, retourne pour chaque fichier un doc
avec son contenu brut et les métadonnées de la source.
"""

from __future__ import annotations

import logging
import os
import re
from pathlib import Path
from typing import Iterable

HERE = Path(__file__).resolve().parent
PROJECT_ROOT = HERE.parent.parent.parent

logger = logging.getLogger("qdrant_sync")


def _strip_html(text: str) -> str:
    text = re.sub(r"<script[^>]*>.*?</script>", " ", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<style[^>]*>.*?</style>", " ", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def _read_file(path: Path) -> str:
    raw = path.read_text(encoding="utf-8", errors="replace")
    if path.suffix.lower() in {".html", ".htm"}:
        return _strip_html(raw)
    return raw


def _is_file_excluded(path: Path, source_cfg: dict, global_exclusions: dict) -> bool:
    from utils import is_excluded

    if is_excluded(path, global_exclusions):
        return True

    source_excluded_files = set(source_cfg.get("exclude_files", []))
    if path.name in source_excluded_files:
        return True

    for frag in source_cfg.get("exclude_patterns", []):
        # Crude glob fragment matching on the posix path
        cleaned = frag.replace("**/", "").replace("/**", "").replace("*", "")
        if cleaned and cleaned in path.as_posix():
            return True

    return False


def iter_documents(source_cfg: dict, global_cfg: dict) -> Iterable[dict]:
    pattern = source_cfg["pattern"]
    doc_type = source_cfg["type"]
    source_key = source_cfg.get("_key") or source_cfg.get("source_key") or "unknown"

    global_exclusions = global_cfg.get("global_exclusions", {})

    # Resolve pattern relative to project root
    paths = sorted(PROJECT_ROOT.glob(pattern))

    for path in paths:
        if not path.is_file():
            continue
        if _is_file_excluded(path, source_cfg, global_exclusions):
            logger.debug("Skip excluded: %s", path)
            continue

        try:
            content = _read_file(path)
        except Exception as e:
            logger.warning("Cannot read %s: %s", path, e)
            continue

        if not content.strip():
            logger.debug("Skip empty: %s", path)
            continue

        rel_path = path.relative_to(PROJECT_ROOT).as_posix()

        metadata = {
            "type": doc_type,
            "source_key": source_key,
            "source_file": rel_path,
            "language": source_cfg.get("language", "en"),
            "channel": source_cfg.get("channel", "internal"),
            "author": source_cfg.get("author", "n2"),
            "status": source_cfg.get("status", "published"),
        }

        yield {
            "source_file": rel_path,
            "content": content,
            "metadata": metadata,
        }
