# Changelog

All notable changes to this project are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses [Semantic Versioning](https://semver.org).

## [Unreleased]

### Added

- "Pawang Lencana" theme: design tokens in `docs/theme.css` with light and dark modes (WCAG AA contrast measured). Follows the system setting and can be forced with `data-theme`.
- Workbench site (`docs/index.html`, plain HTML/CSS/JS, no build step): category shelves, a README tray with copy-all, remove, clear with undo, reordering by drag or arrow keys, a badge style picker with live preview, a light/dark toggle, EN/ID switch, a `/` search shortcut and a mobile bottom sheet.
- SEO, AEO and GEO foundations for the site: keyword-aligned title and description, Open Graph and Twitter cards, `FAQPage` JSON-LD, `sitemap.xml`, `og-image.png`, a "Why this collection" section and a `noscript` fallback.
- Five FAQ entries (40-60 words each) on the site and in both READMEs.

### Changed

- Site rebuilt around the Workbench layout; hero copy follows the new tone of voice.
- Dark-mode drag-handle color raised to meet 3:1 non-text contrast (was 2.87:1 on the canvas, 2.46:1 on the panel).

## [0.1.0] - 2026-11-16

### Added

- Initial catalog of 191 badges in 12 categories, stored in `data/badges.yml`.
- `badgekit` CLI (`build`, `check`, `validate`, `stats`) that generates `README.md`, `README.id.md`, `docs/badges.json` and `docs/llms.txt`.
- Bilingual (English and Bahasa Indonesia) README and CONTRIBUTING.
- Searchable GitHub Pages site with category and badge-style filters.
- CI (lint, tests, Simple Icons slug validation), Pages deploy and release workflows, Dependabot, issue forms and PR template.

[Unreleased]: https://github.com/pawang-ai/markdown-badges-collection/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/pawang-ai/markdown-badges-collection/releases/tag/v0.1.0
