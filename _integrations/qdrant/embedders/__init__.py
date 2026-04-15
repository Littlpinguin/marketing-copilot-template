"""
embedders/__init__.py – Embedding Gemini.

Responsabilité : transformer un texte en vecteur de la bonne dimension.
Gère retry, rate limit, et task_type (RETRIEVAL_DOCUMENT pour ingestion,
RETRIEVAL_QUERY pour recherche).
"""

from __future__ import annotations

import logging
import os
import time

import requests

GEMINI_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/{model}:embedContent"


class GeminiEmbedder:
    def __init__(self, cfg: dict, logger: logging.Logger | None = None):
        embedder_cfg = cfg["embedder"]
        self.model = embedder_cfg["model"]
        self.output_dim = embedder_cfg["output_dimensions"]
        self.task_ingest = embedder_cfg["task_type_ingest"]
        self.task_query = embedder_cfg["task_type_query"]

        self.max_attempts = embedder_cfg["retry"]["max_attempts"]
        self.backoff = embedder_cfg["retry"]["backoff_seconds"]
        self.sleep_between = embedder_cfg["rate_limit"]["sleep_between_calls_sec"]

        self.api_key = os.environ["GOOGLE_AI_API_KEY"]
        self.logger = logger or logging.getLogger("qdrant_sync")
        self._last_call = 0.0

    def _throttle(self) -> None:
        elapsed = time.time() - self._last_call
        if elapsed < self.sleep_between:
            time.sleep(self.sleep_between - elapsed)
        self._last_call = time.time()

    def embed(self, text: str, task_type: str | None = None) -> list[float]:
        """Embed a single text. Returns a vector of output_dim floats."""
        if not text or not text.strip():
            raise ValueError("Cannot embed empty text")

        task = task_type or self.task_ingest
        url = GEMINI_ENDPOINT.format(model=self.model)
        params = {"key": self.api_key}
        payload = {
            "content": {"parts": [{"text": text}]},
            "taskType": task,
            "outputDimensionality": self.output_dim,
        }

        last_error: Exception | None = None
        for attempt in range(self.max_attempts):
            self._throttle()
            try:
                response = requests.post(url, params=params, json=payload, timeout=60)
                if response.status_code == 200:
                    data = response.json()
                    values = data.get("embedding", {}).get("values", [])
                    if len(values) != self.output_dim:
                        raise RuntimeError(
                            f"Unexpected embedding dimension: got {len(values)}, expected {self.output_dim}"
                        )
                    return values
                elif response.status_code == 429:
                    sleep_for = self.backoff[min(attempt, len(self.backoff) - 1)]
                    self.logger.warning("Gemini rate limit hit, sleeping %ss (attempt %d)", sleep_for, attempt + 1)
                    time.sleep(sleep_for)
                else:
                    last_error = RuntimeError(f"Gemini error {response.status_code}: {response.text[:200]}")
                    self.logger.warning("Gemini embed attempt %d failed: %s", attempt + 1, last_error)
                    time.sleep(self.backoff[min(attempt, len(self.backoff) - 1)])
            except requests.RequestException as e:
                last_error = e
                self.logger.warning("Gemini request exception attempt %d: %s", attempt + 1, e)
                time.sleep(self.backoff[min(attempt, len(self.backoff) - 1)])

        raise RuntimeError(f"Gemini embed failed after {self.max_attempts} attempts: {last_error}")

    def embed_query(self, text: str) -> list[float]:
        return self.embed(text, task_type=self.task_query)
