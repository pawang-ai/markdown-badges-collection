"""Load the YAML catalog into typed models."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from .models import Badge, Catalog, Category, DataError

_BADGE_REQUIRED = ("id", "name", "slug", "hex", "category")
_CATEGORY_REQUIRED = ("id", "name_en", "name_id")


def _require(entry: Any, keys: tuple[str, ...], where: str) -> None:
    if not isinstance(entry, dict):
        raise DataError(f"{where}: expected a mapping, got {type(entry).__name__}")
    missing = [k for k in keys if k not in entry]
    if missing:
        raise DataError(f"{where}: missing required key(s): {', '.join(missing)}")


def load_catalog(path: Path) -> Catalog:
    """Read ``path`` and return a :class:`Catalog`.

    Args:
        path: Location of ``badges.yml``.

    Raises:
        DataError: If the file is missing, not valid YAML, or lacks required keys.
    """
    try:
        raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise DataError(f"Catalog file not found: {path}") from exc
    except yaml.YAMLError as exc:
        raise DataError(f"Invalid YAML in {path}: {exc}") from exc

    if not isinstance(raw, dict) or "categories" not in raw or "badges" not in raw:
        raise DataError(f"{path}: top level must contain 'categories' and 'badges'")

    categories = []
    for i, entry in enumerate(raw["categories"]):
        _require(entry, _CATEGORY_REQUIRED, f"categories[{i}]")
        categories.append(Category(**{k: str(entry[k]) for k in _CATEGORY_REQUIRED}))

    badges = []
    for i, entry in enumerate(raw["badges"]):
        _require(entry, _BADGE_REQUIRED, f"badges[{i}]")
        data = {k: str(v) for k, v in entry.items() if v is not None}
        try:
            badges.append(Badge(**data))
        except TypeError as exc:
            raise DataError(f"badges[{i}] ({entry.get('id')}): {exc}") from exc

    return Catalog(tuple(categories), tuple(badges), root=path.parent.parent)
