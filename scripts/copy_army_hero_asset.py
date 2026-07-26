#!/usr/bin/env python3
"""Copy a generated hero image from Cursor assets to wwwroot as 1536x1024 WEBP."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURSOR_ASSETS = (
    Path.home()
    / ".cursor/projects/Users-luke-gumbleton-Documents-Azure-Github-Star-Wars/assets"
)


def find_source(filename: str) -> Path | None:
    stem = filename.replace(".webp", "")
    for base in (CURSOR_ASSETS,):
        if not base.is_dir():
            continue
        for candidate in (
            base / filename,
            base / f"{stem}.png",
            base / filename.replace(".webp", ".png"),
        ):
            if candidate.is_file():
                return candidate
    return None


def install(filename: str, output: str, *, force: bool = False) -> bool:
    dest = ROOT / output
    src = find_source(filename)
    if src is None:
        return False

    if dest.is_file() and not force:
        return True

    dest.parent.mkdir(parents=True, exist_ok=True)
    if src.suffix.lower() == ".webp":
        from PIL import Image
        import shutil

        with Image.open(src) as img:
            if img.size == (1536, 1024):
                shutil.copy2(src, dest)
                return True

    from PIL import Image

    img = Image.open(src).convert("RGB")
    img = img.resize((1536, 1024), Image.Resampling.LANCZOS)
    img.save(dest, format="WEBP", quality=90, method=6)
    return True


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: copy_army_hero_asset.py <filename> <output>", file=sys.stderr)
        raise SystemExit(2)
    ok = install(sys.argv[1], sys.argv[2])
    raise SystemExit(0 if ok else 1)
