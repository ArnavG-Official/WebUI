from __future__ import annotations
from typing import Any


def flatten(items: Any) -> list[Any]:
    result: list[Any] = []
    if isinstance(items, (list, tuple)):
        for item in items:
            result.extend(flatten(item))
        return result
    if items is None:
        return []
    return [items]


def is_text(value: Any) -> bool:
    return isinstance(value, (str, int, float))


def stringify(value: Any) -> str:
    if value is None:
        return ""
    if hasattr(value, "render"):
        return str(value)
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def normalize_attr_name(name: str) -> str:
    if name.endswith("_"):
        return name[:-1]
    return name
