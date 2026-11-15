# Contributing / Kontribusi

**English** · [Bahasa Indonesia](#kontribusi-bahasa-indonesia)

## Contributing (English)

Thanks for helping! Most contributions are one line in `data/badges.yml`.

### Adding a badge

1. Confirm the logo exists on [simpleicons.org](https://simpleicons.org) and note its **slug** and **hex**.
2. Add one line under the right category comment in `data/badges.yml`:

   ```yaml
   - {id: apachekafka, name: "Apache Kafka", slug: apachekafka, hex: "231F20", logo_color: white, category: database}
   ```

3. `logo_color` is `white` on dark colors and `black` on light colors (check the preview).
4. Regenerate and verify:

   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -e ".[dev]"
   badgekit build
   badgekit check --simple-icons https://cdn.jsdelivr.net/npm/simple-icons/data/simple-icons.json
   ruff check . && black --check . && pytest
   ```

5. Commit `data/badges.yml` together with the regenerated `README.md`, `README.id.md` and `docs/` files.

### Badge criteria

- The product is a real, widely used technology, tool or service.
- `name` is the official product name; `hex` is the official brand color from Simple Icons.
- No duplicates: `badgekit validate` rejects repeated ids, names and slugs.
- Logos missing from Simple Icons can be added with `source: custom` and a `logo_file` under `assets/logos/` (SVG you have the right to use).

### Workflow and commits

We use [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow): branch from `main`, open a pull request, and squash-merge after CI passes. Commit messages follow [Conventional Commits](https://www.conventionalcommits.org), for example `feat(badges): add Apache Kafka` or `fix(render): escape underscores in labels`.

Never edit `README.md`, `README.id.md`, `docs/badges.json` or `docs/llms.txt` outside the marked sections; the generator owns them. Be kind: see the [Code of Conduct](CODE_OF_CONDUCT.md).

## Kontribusi (Bahasa Indonesia)

Terima kasih sudah membantu! Sebagian besar kontribusi cukup satu baris di `data/badges.yml`.

### Menambah badge

1. Pastikan logonya ada di [simpleicons.org](https://simpleicons.org), lalu catat **slug** dan **hex**-nya.
2. Tambahkan satu baris di bawah komentar kategori yang tepat di `data/badges.yml` (contoh format ada di bagian English di atas).
3. `logo_color` diisi `white` untuk warna gelap dan `black` untuk warna terang (cek di preview).
4. Regenerasi dan verifikasi dengan perintah yang sama seperti di atas (`badgekit build`, `badgekit check`, `ruff`, `black`, `pytest`).
5. Commit `data/badges.yml` bersama file hasil generate: `README.md`, `README.id.md`, dan `docs/`.

### Kriteria badge

- Produknya teknologi, tool, atau layanan nyata yang banyak dipakai.
- `name` adalah nama resmi produk; `hex` adalah warna brand resmi dari Simple Icons.
- Tidak boleh duplikat: `badgekit validate` menolak id, nama, dan slug yang berulang.
- Logo yang tidak ada di Simple Icons bisa ditambahkan dengan `source: custom` dan `logo_file` di `assets/logos/` (SVG yang kamu berhak pakai).

### Alur kerja dan commit

Kami memakai [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow): buat branch dari `main`, buka pull request, lalu squash-merge setelah CI lulus. Pesan commit mengikuti [Conventional Commits](https://www.conventionalcommits.org), misalnya `feat(badges): add Apache Kafka`.

Jangan mengedit `README.md`, `README.id.md`, `docs/badges.json`, atau `docs/llms.txt` di luar bagian yang bertanda; generator yang mengelolanya. Bersikaplah baik: lihat [Code of Conduct](CODE_OF_CONDUCT.md).
