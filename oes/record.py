"""A check is a named statement, its status, and whether it held here."""

from dataclasses import dataclass, field
from typing import Any

from .gates import STATUSES


@dataclass
class Check:
    layer: str
    name: str
    status: str
    passed: bool
    value: Any = None
    note: str = ""

    def __post_init__(self):
        if self.status not in STATUSES:
            raise ValueError(f"unknown status {self.status!r}")
        self.passed = bool(self.passed)

    def as_dict(self):
        v = self.value
        if hasattr(v, "tolist"):
            v = v.tolist()
        return {"layer": self.layer, "name": self.name, "status": self.status,
                "passed": self.passed, "value": _plain(v), "note": self.note}


def _plain(v):
    if isinstance(v, dict):
        return {str(k): _plain(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)):
        return [_plain(x) for x in v]
    if isinstance(v, (bool, int, float, str)) or v is None:
        return v
    try:
        return float(v)
    except (TypeError, ValueError):
        return str(v)


@dataclass
class Report:
    layer: str
    checks: list = field(default_factory=list)

    def add(self, name, status, passed, value=None, note=""):
        c = Check(self.layer, name, status, passed, value, note)
        self.checks.append(c)
        return c
