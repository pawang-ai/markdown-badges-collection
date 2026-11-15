"""Data models for the badge catalog."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

HEX_RE = re.compile(r"^[0-9A-Fa-f]{6}$")
ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
LOGO_COLORS = frozenset({"white", "black"})
SOURCES = frozenset({"simple-icons", "custom"})


class DataError(ValueError):
    """Raised when the catalog file is malformed."""


@dataclass(frozen=True)
class Category:
    """A badge category, with display names in each supported language."""

    id: str
    name_en: str
    name_id: str

    def name(self, lang: str) -> str:
        """Return the category name for ``lang`` (``"en"`` or ``"id"``)."""
        return self.name_id if lang == "id" else self.name_en


@dataclass(frozen=True)
class Badge:
    """A single Shields.io badge definition."""

    id: str
    name: str
    slug: str
    hex: str
    category: str
    logo_color: str = "white"
    source: str = "simple-icons"
    logo_file: str | None = None


@dataclass(frozen=True)
class Catalog:
    """The full catalog: ordered categories and badges."""

    categories: tuple[Category, ...]
    badges: tuple[Badge, ...]
    root: Path = field(default_factory=Path)

    def category(self, category_id: str) -> Category | None:
        """Look up a category by id."""
        return next((c for c in self.categories if c.id == category_id), None)

    def badges_in(self, category_id: str) -> list[Badge]:
        """Return badges of a category sorted case-insensitively by name."""
        items = [b for b in self.badges if b.category == category_id]
        return sorted(items, key=lambda b: b.name.lower())
