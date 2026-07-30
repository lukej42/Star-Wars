#!/usr/bin/env python3
"""Install a planet hero or space regen batch from Cursor assets into wwwroot."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    Image = None  # type: ignore[misc, assignment]

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
DEFAULT_ASSETS = Path.home() / ".cursor/projects/Users-luke-gumbleton-Documents-Azure-Github-Star-Wars/assets"
MIN_BYTES = 100_000


def save_webp(source: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if source.suffix.lower() == ".webp":
        # Preserve full-quality AI-generated webp without re-encoding
        shutil.copy2(source, dest)
        return
    if Image is None:
        raise RuntimeError("Pillow required to convert non-webp sources")
    with Image.open(source) as img:
        rgb = img.convert("RGB")
        if rgb.size != (1536, 1024):
            rgb = rgb.resize((1536, 1024), Image.Resampling.LANCZOS)
        rgb.save(dest, format="WEBP", quality=92, method=6)


def find_source(slug: str, kind: str, source_dir: Path) -> Path | None:
    names = [
        f"{slug}-{kind}.webp",
        f"{slug}.webp",
        f"{slug}-{kind}.png",
        f"{slug}.png",
    ]
    for name in names:
        path = source_dir / name
        if path.is_file():
            return path
    return None


def main() -> None:
    parser = argparse.ArgumentParser(description="Install planet regen batch assets")
    parser.add_argument("batch", type=Path, help="Batch JSON path")
    parser.add_argument("--kind", choices=("hero", "space"), default="hero")
    parser.add_argument("--source", default=str(DEFAULT_ASSETS))
    args = parser.parse_args()

    source_dir = Path(args.source)
    entries = json.loads(args.batch.read_text(encoding="utf-8"))
    installed = 0
    missing: list[str] = []
    small: list[str] = []

    for entry in entries:
        slug = entry["slug"]
        src = find_source(slug, args.kind, source_dir)
        if src is None:
            missing.append(slug)
            continue
        dest = ROOT / entry["output"]
        save_webp(src, dest)
        size = dest.stat().st_size
        if size < MIN_BYTES:
            small.append(f"{slug}({size})")
        installed += 1

    print(f"Installed {installed}/{len(entries)} from {args.batch.name}")
    if missing:
        print(f"Missing ({len(missing)}): {', '.join(missing[:8])}{'…' if len(missing) > 8 else ''}")
    if small:
        print(f"Small ({len(small)}): {', '.join(small[:5])}{'…' if len(small) > 5 else ''}")


if __name__ == "__main__":
    main()
