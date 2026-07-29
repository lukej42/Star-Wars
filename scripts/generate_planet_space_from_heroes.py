#!/usr/bin/env python3
"""Composite cinematic planet space backgrounds from hero banners + deep space.

Produces full-bleed 1536x1024 .webp backgrounds in the same resolution band as
Coruscant — using existing cinematic hero art for the planetary disc and a
generated starfield above the horizon.
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageOps

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from generate_cinematic_planet_space_backgrounds import (
    MIN_CINEMATIC_BYTES,
    atmosphere_glow,
    hex_to_rgb,
    nebula_layer,
    procedural_sphere,
    render_space as render_procedural,
    rng,
    slug_seed,
    starfield,
)
from parse_csharp_data import load_planets

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "wwwroot" / "images" / "planets"
SIZE = (1536, 1024)


def horizon_mask(width: int, height: int, horizon_y: int) -> Image.Image:
    mask = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(mask)
    draw.rectangle((0, horizon_y, width, height), fill=255)
    fade = int(height * 0.12)
    for y in range(max(0, horizon_y - fade), horizon_y):
        alpha = int(255 * (y - (horizon_y - fade)) / fade)
        draw.line([(0, y), (width, y)], fill=alpha)
    return mask.filter(ImageFilter.GaussianBlur(radius=6))


def render_from_hero(entry: dict[str, str], hero: Image.Image) -> Image.Image:
    width, height = SIZE
    seed = slug_seed(entry["slug"])
    accent = hex_to_rgb(entry.get("color", "#7eb8ff"))

    space = Image.new("RGB", SIZE, (2, 4, 12))
    composed = Image.alpha_composite(space.convert("RGBA"), nebula_layer(width, height, accent, seed))
    composed = Image.alpha_composite(composed, starfield(width, height, seed, count=520))

    hero_fit = ImageOps.fit(hero.convert("RGB"), (width, int(height * 0.92)), centering=(0.5, 1.0))
    horizon_y = int(height * 0.34)
    planet_layer = Image.new("RGBA", SIZE, (0, 0, 0, 0))
    planet_layer.paste(hero_fit, (0, horizon_y - int(height * 0.08)))
    mask = horizon_mask(width, height, horizon_y)
    composed = Image.composite(composed, planet_layer, mask)

    cx = width // 2
    cy = horizon_y + int(height * 0.22)
    radius = int(width * 0.52)
    composed = Image.alpha_composite(composed, atmosphere_glow(width, height, cx, cy, radius, accent))

    vignette = Image.new("L", SIZE, 0)
    vdraw = ImageDraw.Draw(vignette)
    vdraw.ellipse((-width // 4, -height // 5, width + width // 4, height + height // 3), fill=255)
    vignette = vignette.filter(ImageFilter.GaussianBlur(radius=100))
    dark = Image.new("RGB", SIZE, (0, 0, 0))
    return Image.composite(composed.convert("RGB"), dark, Image.eval(vignette, lambda p: 255 - p // 5))


def render_entry(entry: dict[str, str], force: bool = False) -> tuple[str, int]:
    slug = entry["slug"]
    out_path = OUT / f"{slug}-space.webp"
    if not force and out_path.exists() and out_path.stat().st_size >= MIN_CINEMATIC_BYTES:
        return "skipped", out_path.stat().st_size

    hero_path = OUT / f"{slug}-hero.webp"
    if hero_path.is_file() and hero_path.stat().st_size >= 500_000:
        image = render_from_hero(entry, Image.open(hero_path))
        mode = "hero"
    else:
        render_procedural(entry, force=True)
        return "procedural", out_path.stat().st_size if out_path.exists() else 0

    OUT.mkdir(parents=True, exist_ok=True)
    image.save(out_path, format="WEBP", quality=92, method=6)
    return mode, out_path.stat().st_size


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    stats: dict[str, int] = {"hero": 0, "procedural": 0, "skipped": 0}
    for entry in load_planets():
        mode, size = render_entry(entry, force=args.force)
        stats[mode if mode in stats else "skipped"] = stats.get(mode, 0) + 1
        if mode == "hero" and size < MIN_CINEMATIC_BYTES:
            stats["small"] = stats.get("small", 0) + 1

    print(
        f"hero={stats.get('hero', 0)}, procedural={stats.get('procedural', 0)}, "
        f"skipped={stats.get('skipped', 0)}, under_threshold={stats.get('small', 0)}"
    )


if __name__ == "__main__":
    main()
