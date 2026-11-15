"""Validate catalog integrity: duplicates, colors, categories and logo availability."""

from __future__ import annotations

import json
import logging
import urllib.request
from collections import Counter
from pathlib import Path

from .models import HEX_RE, ID_RE, LOGO_COLORS, SOURCES, Catalog

logger = logging.getLogger(__name__)


def load_simple_icons_slugs(location: str) -> set[str]:
    """Load the set of slugs from a Simple Icons ``simple-icons.json``.

    Args:
        location: A local file path or an ``https://`` URL.

    Raises:
        OSError: If the file cannot be read or the URL cannot be fetched.
    """
    if location.startswith("https://"):
        with urllib.request.urlopen(location, timeout=30) as resp:  # noqa: S310
            data = json.load(resp)
    else:
        data = json.loads(Path(location).read_text(encoding="utf-8"))
    return {item["slug"] for item in data}


def validate(catalog: Catalog, simple_icons: set[str] | None = None) -> list[str]:
    """Return a list of human-readable problems (empty if the catalog is valid)."""
    errors: list[str] = []
    category_ids = {c.id for c in catalog.categories}

    for label, values in (
        ("id", [b.id for b in catalog.badges]),
        ("name", [b.name.lower() for b in catalog.badges]),
        ("category id", [c.id for c in catalog.categories]),
    ):
        errors += [f"duplicate {label}: {v}" for v, n in Counter(values).items() if n > 1]

    slugs = Counter(b.slug for b in catalog.badges if b.source == "simple-icons")
    errors += [f"duplicate simple-icons slug: {s}" for s, n in slugs.items() if n > 1]

    for b in catalog.badges:
        where = f"[{b.id}]"
        if not ID_RE.match(b.id):
            errors.append(f"{where} id must be lowercase letters, digits and hyphens")
        if not HEX_RE.match(b.hex):
            errors.append(f"{where} hex must be 6 hex digits without '#', got {b.hex!r}")
        if b.logo_color not in LOGO_COLORS:
            errors.append(f"{where} logo_color must be one of {sorted(LOGO_COLORS)}")
        if b.category not in category_ids:
            errors.append(f"{where} unknown category {b.category!r}")
        if b.source not in SOURCES:
            errors.append(f"{where} source must be one of {sorted(SOURCES)}")
        elif b.source == "custom":
            if not b.logo_file:
                errors.append(f"{where} custom badges require logo_file")
            elif not (catalog.root / b.logo_file).is_file():
                errors.append(f"{where} logo_file not found: {b.logo_file}")
        elif simple_icons is not None and b.slug not in simple_icons:
            errors.append(f"{where} slug {b.slug!r} not found in Simple Icons")
    return errors
