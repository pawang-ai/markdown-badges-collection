"""Shared fixtures: a tiny repository layout in a temp directory."""

from __future__ import annotations

from pathlib import Path

import pytest

CATALOG = """\
categories:
  - {id: lang, name_en: "Languages", name_id: "Bahasa"}
  - {id: empty, name_en: "Empty", name_id: "Kosong"}
badges:
  - {id: zig, name: "Zig", slug: zig, hex: "F7A41D", logo_color: black, category: lang}
  - {id: node-red, name: "Node-RED", slug: nodered, hex: "8F0000", logo_color: white,
     category: lang}
"""

README = """\
# t
<!-- STATS:START -->
<!-- STATS:END -->
<!-- TOC:START -->
<!-- TOC:END -->
<!-- BADGES:START -->
<!-- BADGES:END -->
"""


@pytest.fixture()
def repo(tmp_path: Path) -> Path:
    """Create a minimal repo with a catalog and both README files."""
    (tmp_path / "data").mkdir()
    (tmp_path / "data" / "badges.yml").write_text(CATALOG, encoding="utf-8")
    (tmp_path / "README.md").write_text(README, encoding="utf-8")
    (tmp_path / "README.id.md").write_text(README, encoding="utf-8")
    return tmp_path
