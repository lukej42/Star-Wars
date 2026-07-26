#!/usr/bin/env python3
"""Copy generated hero image from Cursor assets to output path as WEBP 1536x1024 q90."""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
CURSOR_ASSETS = (
    Path.home()
    / ".cursor/projects/Users-luke-gumbleton-Documents-Azure-Github-Star-Wars/assets"
)
WIDTH, HEIGHT = 1536, 1024


def find_asset(filename: str) -> Path | None:
    stem = Path(filename).stem
    for ext in (".webp", ".png", ".jpg", ".jpeg"):
        candidate = CURSOR_ASSETS / f"{stem}{ext}"
        if candidate.exists():
            return candidate
        candidate = CURSOR_ASSETS / filename
        if candidate.exists():
            return candidate
    # Fallback: newest file matching stem
    matches = list(CURSOR_ASSETS.glob(f"{stem}*"))
    if matches:
        return max(matches, key=lambda p: p.stat().st_mtime)
    return None


def copy_to_output(filename: str, output_rel: str) -> str:
    src = find_asset(filename)
    if src is None:
        return f"FAIL: asset not found for {filename}"

    out = ROOT / output_rel
    out.parent.mkdir(parents=True, exist_ok=True)

    if src.suffix.lower() == ".webp":
        with Image.open(src) as img:
            if img.size == (WIDTH, HEIGHT):
                import shutil

                shutil.copy2(src, out)
                return f"OK: {output_rel}"

    img = Image.open(src).convert("RGB")
    if img.size != (WIDTH, HEIGHT):
        img = img.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
    img.save(out, "WEBP", quality=90, method=6)
    return f"OK: {output_rel}"


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: copy_hero_asset.py <filename> <output_rel>")
        sys.exit(1)
    result = copy_to_output(sys.argv[1], sys.argv[2])
    print(result)
    sys.exit(0 if result.startswith("OK") else 1)
