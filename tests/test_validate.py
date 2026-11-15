import dataclasses
from pathlib import Path

from badgekit.loader import load_catalog
from badgekit.models import Catalog
from badgekit.validate import load_simple_icons_slugs, validate


def _catalog(repo: Path, **changes: object) -> Catalog:
    catalog = load_catalog(repo / "data" / "badges.yml")
    badges = list(catalog.badges)
    badges[0] = dataclasses.replace(badges[0], **changes)
    return dataclasses.replace(catalog, badges=tuple(badges))


def test_valid_catalog(repo: Path) -> None:
    catalog = load_catalog(repo / "data" / "badges.yml")
    assert validate(catalog, {"zig", "nodered"}) == []


def test_duplicate_id_and_name(repo: Path) -> None:
    catalog = load_catalog(repo / "data" / "badges.yml")
    dup = dataclasses.replace(catalog, badges=catalog.badges + (catalog.badges[0],))
    errors = validate(dup)
    assert any("duplicate id: zig" in e for e in errors)
    assert any("duplicate name: zig" in e for e in errors)


def test_bad_hex_color_and_category(repo: Path) -> None:
    errors = validate(_catalog(repo, hex="#FFF", logo_color="red", category="nope"))
    assert any("hex must be" in e for e in errors)
    assert any("logo_color" in e for e in errors)
    assert any("unknown category" in e for e in errors)


def test_unknown_slug(repo: Path) -> None:
    catalog = load_catalog(repo / "data" / "badges.yml")
    assert any("not found in Simple Icons" in e for e in validate(catalog, {"nodered"}))


def test_custom_requires_existing_logo(repo: Path) -> None:
    assert any("require logo_file" in e for e in validate(_catalog(repo, source="custom")))
    errors = validate(_catalog(repo, source="custom", logo_file="assets/logos/missing.svg"))
    assert any("logo_file not found" in e for e in errors)


def test_load_simple_icons_slugs(tmp_path: Path) -> None:
    path = tmp_path / "si.json"
    path.write_text('[{"slug": "a"}, {"slug": "b"}]', encoding="utf-8")
    assert load_simple_icons_slugs(str(path)) == {"a", "b"}
