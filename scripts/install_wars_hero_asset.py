#!/usr/bin/env python3
"""Install generated hero PNGs into Cursor assets as WEBP for wars upload pipeline."""

from __future__ import annotations

import argparse
import io
import json
import sys
from pathlib import Path

from PIL import Image

SCRIPTS = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[1]
ASSETS = Path.home() / ".cursor/projects/Users-luke-gumbleton-Documents-Azure-Github-Star-Wars/assets"
MANIFEST = SCRIPTS / "wars_conflicts_hero_manifest.json"
WIDTH, HEIGHT = 1536, 1024

SEARCH_DIRS = [
    ROOT,
    ROOT / "assets",
    ASSETS,
]


def to_webp(source: Path, dest: Path) -> None:
    img = Image.open(source).convert("RGB")
    if img.size != (WIDTH, HEIGHT):
        img = img.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
    dest.parent.mkdir(parents=True, exist_ok=True)
    img.save(dest, format="WEBP", quality=90, method=6)


def find_source(slug: str) -> Path | None:
    patterns = [
        f"{slug}-hero.png",
        f"{slug}-hero.webp",
        f"battle-of-{slug}-hero.png",
    ]
    for directory in SEARCH_DIRS:
        for pattern in patterns:
            candidate = directory / pattern
            if candidate.is_file():
                return candidate
        for candidate in directory.glob(f"*{slug}*hero*"):
            if candidate.suffix.lower() in {".png", ".webp", ".jpg"}:
                return candidate
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, help="Explicit source image path")
    parser.add_argument("--slug", required=True)
    args = parser.parse_args()

    items = json.loads(MANIFEST.read_text(encoding="utf-8"))
    item = next((i for i in items if i["slug"] == args.slug), None)
    if item is None:
        print(f"Unknown slug: {args.slug}", file=sys.stderr)
        return 1

    source = args.source or find_source(args.slug)
    if source is None:
        print(f"No source image found for {args.slug}", file=sys.stderr)
        return 1

    dest = ASSETS / item["filename"]
    to_webp(source, dest)
    print(f"Installed {dest} from {source}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
