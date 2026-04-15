"""
sources/__init__.py – Interface commune des connecteurs de sources.

Chaque connecteur expose `iter_documents(source_cfg, global_cfg)` qui yield des
dicts {source_file, content, metadata}. Le connecteur ne calcule pas le hash ni
les chunks : c'est le rôle de sync.py.
"""

from __future__ import annotations

from typing import Iterable, Protocol

from . import filesystem as _fs
from . import notion as _notion
from . import transcripts as _tr
from . import outline as _outline


class SourceConnector(Protocol):
    def iter_documents(self, source_cfg: dict, global_cfg: dict) -> Iterable[dict]:
        ...


CONNECTORS = {
    "filesystem": _fs,
    "notion": _notion,
    "transcripts": _tr,
    "outline": _outline,
}


def get_connector(name: str):
    if name not in CONNECTORS:
        raise ValueError(f"Unknown connector: {name}")
    return CONNECTORS[name]
