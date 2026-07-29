#!/usr/bin/env python3
"""Install government cinematic hero webp assets into wwwroot."""

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
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ASSETS = Path.home() / ".cursor/projects/Users-luke-gumbleton-Documents-Azure-Github-Star-Wars/assets"
MANIFEST = SCRIPTS / "government_hero_manifest.json"
GOVERNMENT_IMAGES = ROOT / "wwwroot" / "images" / "governments"


def load_manifest() -> list[dict]:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def save_webp(source: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if source.suffix.lower() == ".webp":
        shutil.copy2(source, dest)
        return
    if Image is None:
        raise RuntimeError("Pillow is required to convert non-webp sources")
    with Image.open(source) as img:
        rgb = img.convert("RGB")
        if rgb.size != (1536, 1024):
            rgb = rgb.resize((1536, 1024), Image.Resampling.LANCZOS)
        rgb.save(dest, format="WEBP", quality=90, method=6)


def install_slug(slug: str, source_dir: Path) -> bool:
    scene_name = f"{slug}-scene.webp"
    candidates = [
        source_dir / scene_name,
        source_dir / f"{slug}.webp",
        source_dir / f"{slug}-scene.png",
        source_dir / f"{slug}.png",
    ]
    src = next((path for path in candidates if path.is_file()), None)
    if src is None:
        return False

    scene_dest = GOVERNMENT_IMAGES / scene_name
    save_webp(src, scene_dest)
    save_webp(src, GOVERNMENT_IMAGES / f"{slug}.webp")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Install government hero webp assets")
    parser.add_argument("source", nargs="?", default=str(DEFAULT_ASSETS))
    args = parser.parse_args()
    source = Path(args.source)
    entries = load_manifest()
    installed = 0
    missing: list[str] = []
    for entry in entries:
        slug = entry["slug"]
        if install_slug(slug, source):
            installed += 1
        else:
            missing.append(slug)
    print(f"Installed {installed}/{len(entries)} government hero webp files from {source}")
    if missing:
        preview = ", ".join(missing[:10])
        suffix = "…" if len(missing) > 10 else ""
        print(f"Missing ({len(missing)}): {preview}{suffix}")


if __name__ == "__main__":
    main()
