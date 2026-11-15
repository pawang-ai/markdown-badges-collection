from pathlib import Path

import pytest

from badgekit.loader import load_catalog
from badgekit.models import DataError


def test_load_catalog(repo: Path) -> None:
    catalog = load_catalog(repo / "data" / "badges.yml")
    assert [b.id for b in catalog.badges] == ["zig", "node-red"]
    assert catalog.category("lang").name("id") == "Bahasa"
    assert catalog.badges[0].source == "simple-icons"


def test_hex_stays_a_string(repo: Path) -> None:
    (repo / "data" / "badges.yml").write_text(
        "categories:\n  - {id: c, name_en: C, name_id: C}\n"
        'badges:\n  - {id: a, name: A, slug: a, hex: "000000", category: c}\n',
        encoding="utf-8",
    )
    assert load_catalog(repo / "data" / "badges.yml").badges[0].hex == "000000"


def test_missing_file(tmp_path: Path) -> None:
    with pytest.raises(DataError, match="not found"):
        load_catalog(tmp_path / "nope.yml")


def test_missing_required_key(repo: Path) -> None:
    (repo / "data" / "badges.yml").write_text(
        "categories: []\nbadges:\n  - {id: a, name: A}\n", encoding="utf-8"
    )
    with pytest.raises(DataError, match="missing required key"):
        load_catalog(repo / "data" / "badges.yml")


def test_invalid_yaml(repo: Path) -> None:
    (repo / "data" / "badges.yml").write_text("categories: [", encoding="utf-8")
    with pytest.raises(DataError, match="Invalid YAML"):
        load_catalog(repo / "data" / "badges.yml")


def test_unknown_field_is_reported(repo: Path) -> None:
    (repo / "data" / "badges.yml").write_text(
        "categories: []\nbadges:\n"
        "  - {id: a, name: A, slug: a, hex: '000000', category: c, bogus: 1}\n",
        encoding="utf-8",
    )
    with pytest.raises(DataError, match="bogus"):
        load_catalog(repo / "data" / "badges.yml")
