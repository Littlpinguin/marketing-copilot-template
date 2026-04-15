"""
enrichers/__init__.py – Tous les enrichers (summary, entities, claims, meeting).

Responsabilité : à partir d'un chunk de texte et de son type, retourner des
champs additionnels (summary, entities, claims, decisions, action_items) qui
seront stockés dans le payload Qdrant.

Chaque enricher peut échouer silencieusement (log WARN, retour dict vide). Le
chunk est ingéré avec ce qui est disponible.
"""

from __future__ import annotations

import json
import logging
import os
import re
import time
from typing import Any

import requests

GEMINI_GEN_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"


def _call_gemini(
    prompt: str,
    text: str,
    model: str,
    max_output_tokens: int,
    api_key: str,
    logger: logging.Logger,
    expect_json: bool = False,
) -> str | None:
    url = GEMINI_GEN_ENDPOINT.format(model=model)
    full_prompt = f"{prompt}\n\n---\n\n{text}"
    # Gemini 2.5 Flash uses part of maxOutputTokens for internal thinking. For
    # extraction tasks we don't need reasoning, so we set thinkingBudget=0 to
    # make the budget fully available to the actual output. We also double the
    # raw budget as a safety margin.
    payload: dict[str, Any] = {
        "contents": [{"parts": [{"text": full_prompt}]}],
        "generationConfig": {
            "maxOutputTokens": max_output_tokens * 4,
            "temperature": 0.2,
            "thinkingConfig": {"thinkingBudget": 0},
        },
    }
    if expect_json:
        payload["generationConfig"]["responseMimeType"] = "application/json"

    try:
        r = requests.post(url, params={"key": api_key}, json=payload, timeout=60)
        if r.status_code != 200:
            logger.warning("Gemini generate %d: %s", r.status_code, r.text[:300])
            return None
        data = r.json()
        candidates = data.get("candidates", [])
        if not candidates:
            logger.warning("Gemini response has no candidates: %s", str(data)[:200])
            return None
        candidate = candidates[0]
        finish_reason = candidate.get("finishReason")
        parts = candidate.get("content", {}).get("parts", [])
        if not parts:
            logger.warning("Gemini candidate has no parts (finishReason=%s): %s", finish_reason, str(candidate)[:200])
            return None
        result = parts[0].get("text", "").strip()
        if not result:
            logger.warning("Gemini returned empty text (finishReason=%s)", finish_reason)
        return result
    except requests.RequestException as e:
        logger.warning("Gemini generate exception: %s", e)
        return None


def _parse_json_maybe_fenced(text: str) -> dict | None:
    """Parse JSON from a string that may contain markdown fences or trailing garbage."""
    if not text:
        return None
    cleaned = text.strip()
    cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned)
    cleaned = re.sub(r"\s*```$", "", cleaned)
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", cleaned, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(0))
            except json.JSONDecodeError:
                return None
        return None


class Enricher:
    """Base class. Subclasses implement run(text, meta) → dict of payload fields."""

    def __init__(self, cfg: dict, logger: logging.Logger):
        self.cfg = cfg
        self.logger = logger
        self.enabled = cfg.get("enabled", True)
        self.fail_silent = cfg.get("fail_silent", True)

    def applies(self, doc_type: str) -> bool:
        applies_to = self.cfg.get("applies_to_types")
        if applies_to is None:
            return True
        return doc_type in applies_to

    def run(self, text: str, meta: dict) -> dict:
        raise NotImplementedError


class HashEnricher(Enricher):
    """Stores the content hash in the payload. Actual hashing is done upstream."""

    def run(self, text: str, meta: dict) -> dict:
        from utils import content_hash
        return {"content_hash": content_hash(text)}


class SummaryEnricher(Enricher):
    def run(self, text: str, meta: dict) -> dict:
        if not self.enabled:
            return {}
        try:
            result = _call_gemini(
                prompt=self.cfg["prompt"],
                text=text,
                model=self.cfg["model"],
                max_output_tokens=self.cfg["max_output_tokens"],
                api_key=os.environ["GOOGLE_AI_API_KEY"],
                logger=self.logger,
                expect_json=False,
            )
            if result:
                return {"summary": result.strip()}
        except Exception as e:
            if not self.fail_silent:
                raise
            self.logger.warning("SummaryEnricher failed: %s", e)
        return {}


def _flatten_list_of_maybe_dicts(items: list, value_keys: tuple = ("value", "name", "entity", "text")) -> list[str]:
    """Convert a list that may contain strings OR dicts into a flat string list.
    For dicts, look for common value keys like 'value', 'name', etc."""
    out: list[str] = []
    for item in items:
        if isinstance(item, str):
            s = item.strip()
            if s:
                out.append(s)
        elif isinstance(item, dict):
            for k in value_keys:
                if k in item and isinstance(item[k], str):
                    s = item[k].strip()
                    if s:
                        out.append(s)
                    break
    return out


class EntitiesEnricher(Enricher):
    def run(self, text: str, meta: dict) -> dict:
        if not self.enabled:
            return {}
        try:
            raw = _call_gemini(
                prompt=self.cfg["prompt"],
                text=text,
                model=self.cfg["model"],
                max_output_tokens=self.cfg["max_output_tokens"],
                api_key=os.environ["GOOGLE_AI_API_KEY"],
                logger=self.logger,
                expect_json=True,
            )
            parsed = _parse_json_maybe_fenced(raw or "")
            if parsed and isinstance(parsed.get("entities"), list):
                entities = _flatten_list_of_maybe_dicts(parsed["entities"])
                return {"entities": entities}
        except Exception as e:
            if not self.fail_silent:
                raise
            self.logger.warning("EntitiesEnricher failed: %s", e)
        return {}


class ClaimsEnricher(Enricher):
    def run(self, text: str, meta: dict) -> dict:
        if not self.enabled:
            return {}
        try:
            raw = _call_gemini(
                prompt=self.cfg["prompt"],
                text=text,
                model=self.cfg["model"],
                max_output_tokens=self.cfg["max_output_tokens"],
                api_key=os.environ["GOOGLE_AI_API_KEY"],
                logger=self.logger,
                expect_json=True,
            )
            parsed = _parse_json_maybe_fenced(raw or "")
            if parsed and isinstance(parsed.get("claims"), list):
                claims = _flatten_list_of_maybe_dicts(parsed["claims"], value_keys=("text", "claim", "statement", "value"))
                return {"claims": claims}
        except Exception as e:
            if not self.fail_silent:
                raise
            self.logger.warning("ClaimsEnricher failed: %s", e)
        return {}


class MeetingEnricher(Enricher):
    def applies(self, doc_type: str) -> bool:
        return doc_type in self.cfg.get("applies_to_types", ["transcript"])

    def run(self, text: str, meta: dict) -> dict:
        if not self.enabled:
            return {}
        try:
            raw = _call_gemini(
                prompt=self.cfg["prompt"],
                text=text,
                model=self.cfg["model"],
                max_output_tokens=self.cfg["max_output_tokens"],
                api_key=os.environ["GOOGLE_AI_API_KEY"],
                logger=self.logger,
                expect_json=True,
            )
            parsed = _parse_json_maybe_fenced(raw or "")
            if not parsed:
                return {}
            result: dict[str, Any] = {}
            if isinstance(parsed.get("decisions"), list):
                result["decisions"] = [str(d).strip() for d in parsed["decisions"] if str(d).strip()]
            if isinstance(parsed.get("action_items"), list):
                items = []
                for ai in parsed["action_items"]:
                    if isinstance(ai, dict):
                        who = str(ai.get("who", "")).strip()
                        what = str(ai.get("what", "")).strip()
                        when = str(ai.get("when", "")).strip()
                        if what:
                            items.append(f"[{who}] {what}" + (f" ({when})" if when else ""))
                    elif isinstance(ai, str):
                        items.append(ai.strip())
                if items:
                    result["action_items"] = items
            return result
        except Exception as e:
            if not self.fail_silent:
                raise
            self.logger.warning("MeetingEnricher failed: %s", e)
        return {}


ENRICHER_CLASSES = {
    "hash": HashEnricher,
    "summary": SummaryEnricher,
    "entities": EntitiesEnricher,
    "claims": ClaimsEnricher,
    "meeting": MeetingEnricher,
}


def build_enrichers(full_cfg: dict, logger: logging.Logger) -> list[Enricher]:
    enriched = []
    enrichers_cfg = full_cfg.get("enrichers", {})
    # Order matters: hash, summary, entities, claims, meeting
    for key in ["hash", "summary", "entities", "claims", "meeting"]:
        sub = enrichers_cfg.get(key)
        if not sub:
            continue
        cls = ENRICHER_CLASSES[key]
        enriched.append(cls(sub, logger))
    return enriched
