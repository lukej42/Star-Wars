#!/usr/bin/env python3
"""Convert all PNG assets to lossless WebP and update text references."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXT_EXTENSIONS = {
    ".cs",
    ".css",
    ".html",
    ".js",
    ".json",
    ".md",
    ".py",
    ".razor",
    ".xml",
    ".yaml",
    ".yml",
}
SKIP_DIRS = {".git", "bin", "obj", "node_modules", ".cursor"}


def iter_text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() in TEXT_EXTENSIONS:
            files.append(path)
    return files


def convert_pngs(dry_run: bool = False) -> tuple[int, int, int]:
    try:
        from PIL import Image
    except ImportError as exc:
        raise SystemExit("Pillow is required: pip install pillow") from exc

    png_files = sorted(path for path in ROOT.rglob("*.png") if path.is_file())
    converted = 0
    skipped = 0
    bytes_before = 0
    bytes_after = 0

    for png_path in png_files:
        if any(part in SKIP_DIRS for part in png_path.parts):
            skipped += 1
            continue

        webp_path = png_path.with_suffix(".webp")
        bytes_before += png_path.stat().st_size

        if dry_run:
            converted += 1
            continue

        with Image.open(png_path) as image:
            if image.mode not in ("RGB", "RGBA"):
                image = image.convert("RGBA" if "A" in image.getbands() else "RGB")
            image.save(webp_path, "WEBP", lossless=True, method=6)

        bytes_after += webp_path.stat().st_size
        png_path.unlink()
        converted += 1

        if converted % 100 == 0:
            print(f"Converted {converted}/{len(png_files)}...", flush=True)

    saved = bytes_before - bytes_after
    print(
        f"PNG conversion: {converted} converted, {skipped} skipped, "
        f"{bytes_before / (1024 ** 3):.2f} GiB -> {bytes_after / (1024 ** 3):.2f} GiB "
        f"(saved {saved / (1024 ** 3):.2f} GiB)"
    )
    return converted, bytes_before, bytes_after


def update_references(dry_run: bool = False) -> int:
    updated_files = 0

    for path in iter_text_files():
        if path.name == "convert_png_to_webp.py":
            continue

        original = path.read_text(encoding="utf-8")
        if ".png" not in original:
            continue

        updated = original.replace(".png", ".webp")
        if updated == original:
            continue

        if not dry_run:
            path.write_text(updated, encoding="utf-8")
        updated_files += 1

    print(f"Reference update: {updated_files} text files {'would be ' if dry_run else ''}updated")
    return updated_files


def fix_favicon_mime() -> None:
    index_path = ROOT / "wwwroot" / "index.html"
    if not index_path.exists():
        return

    content = index_path.read_text(encoding="utf-8")
    updated = content.replace('type="image/png"', 'type="image/webp"')
    if updated != content:
        index_path.write_text(updated, encoding="utf-8")
        print("Updated favicon MIME type in wwwroot/index.html")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--references-only", action="store_true")
    parser.add_argument("--convert-only", action="store_true")
    args = parser.parse_args()

    if not args.references_only:
        convert_pngs(dry_run=args.dry_run)

    if not args.convert_only:
        update_references(dry_run=args.dry_run)
        if not args.dry_run:
            fix_favicon_mime()

    return 0


if __name__ == "__main__":
    sys.exit(main())
