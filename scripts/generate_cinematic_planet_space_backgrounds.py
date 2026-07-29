#!/usr/bin/env python3
"""Generate cinematic full-page planet space backgrounds in Coruscant-style .webp format.

For planets with hero banners, maps the hero texture onto a lit sphere in deep space.
For planets without heroes, synthesises a detailed world from catalogue colour and description.
Skips planets that already have a cinematic space background (>= MIN_SIZE bytes).
"""

from __future__ import annotations

import hashlib
import math
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageOps

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from parse_csharp_data import load_planets

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "wwwroot" / "images" / "planets"
SIZE = (1536, 1024)
MIN_CINEMATIC_BYTES = 500_000


def slug_seed(slug: str) -> int:
    return int(hashlib.md5(slug.encode()).hexdigest(), 16)


def hex_to_rgb(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return int(value[0:2], 16), int(value[2:4], 16), int(value[4:6], 16)


def rng(seed: int, index: int) -> float:
    return ((seed * (index + 1) * 1103515245 + 12345) % 2_147_483_648) / 2_147_483_648


def starfield(width: int, height: int, seed: int, count: int = 420) -> Image.Image:
    layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    for i in range(count):
        x = int(rng(seed, i * 3 + 1) * width)
        y = int(rng(seed, i * 3 + 2) * height)
        r = 1 if rng(seed, i * 3 + 3) > 0.82 else 2
        alpha = int(120 + rng(seed, i * 5) * 135)
        tint = (
            255,
            int(240 + rng(seed, i * 7) * 15),
            int(235 + rng(seed, i * 11) * 20),
            alpha,
        )
        draw.ellipse((x - r, y - r, x + r, y + r), fill=tint)
    return layer.filter(ImageFilter.GaussianBlur(radius=0.4))


def nebula_layer(width: int, height: int, accent: tuple[int, int, int], seed: int) -> Image.Image:
    layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    placements = (
        (int(width * 0.72), int(height * 0.18), int(width * 0.42), 38),
        (int(width * 0.18), int(height * 0.28), int(width * 0.28), 24),
        (int(width * 0.55), int(height * 0.55), int(width * 0.55), 18),
    )
    for cx, cy, radius, alpha in placements:
        jitter = int(rng(seed, cx + cy) * 80 - 40)
        draw.ellipse(
            (cx - radius + jitter, cy - radius, cx + radius + jitter, cy + radius),
            fill=(*accent, alpha),
        )
    return layer.filter(ImageFilter.GaussianBlur(radius=90))


def sample_hero_on_sphere(
    hero: Image.Image,
    width: int,
    height: int,
    cx: int,
    cy: int,
    radius: int,
    light: tuple[float, float, float] = (-0.45, -0.35, 0.82),
) -> Image.Image:
    hero_rgb = hero.convert("RGB")
    hero_rgb = ImageOps.fit(hero_rgb, (hero_rgb.width, hero_rgb.height // 2 + hero_rgb.height // 4))
    pixels = hero_rgb.load()
    hw, hh = hero_rgb.size
    sphere = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    spx = sphere.load()

    for y in range(max(0, cy - radius - 2), min(height, cy + radius + 2)):
        for x in range(max(0, cx - radius - 2), min(width, cx + radius + 2)):
            dx = x - cx
            dy = y - cy
            dist2 = dx * dx + dy * dy
            if dist2 > radius * radius:
                continue
            z = math.sqrt(radius * radius - dist2)
            nx, ny, nz = dx / radius, dy / radius, z / radius
            u = (math.atan2(nx, nz) / (2 * math.pi)) + 0.5
            v = 0.5 - (math.asin(max(-1.0, min(1.0, ny))) / math.pi)
            hx = min(hw - 1, max(0, int(u * hw)))
            hy = min(hh - 1, max(0, int(v * hh)))
            base = pixels[hx, hy]
            shade = max(
                0.12,
                nx * light[0] + ny * light[1] + nz * light[2],
            )
            limb = min(1.0, z / radius * 1.15)
            r = int(base[0] * shade * limb)
            g = int(base[1] * shade * limb)
            b = int(base[2] * shade * limb)
            alpha = int(255 * min(1.0, (z / radius) ** 0.65))
            spx[x, y] = (r, g, b, alpha)
    return sphere


def procedural_sphere(
    width: int,
    height: int,
    cx: int,
    cy: int,
    radius: int,
    accent: tuple[int, int, int],
    desc: str,
    seed: int,
) -> Image.Image:
    lowered = desc.lower()
    is_gas = any(word in lowered for word in ("gas", "giant", "tibanna", "cloud"))
    layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    if is_gas:
        draw.ellipse(
            (cx - radius, cy - int(radius * 0.55), cx + radius, cy + int(radius * 0.55)),
            fill=(*accent, 240),
        )
        draw.ellipse(
            (cx - int(radius * 0.75), cy - int(radius * 0.35), cx + int(radius * 0.4), cy + int(radius * 0.2)),
            fill=(255, 255, 255, 35),
        )
    else:
        draw.ellipse((cx - radius, cy - radius, cx + radius, cy + radius), fill=(*accent, 245))
        for i in range(8):
            bx = cx + int((rng(seed, i) - 0.5) * radius * 1.2)
            by = cy + int((rng(seed, i + 20) - 0.5) * radius * 0.9)
            br = int(radius * (0.08 + rng(seed, i + 40) * 0.12))
            tone = tuple(min(255, int(c * (0.55 + rng(seed, i + 60) * 0.35))) for c in accent)
            draw.ellipse((bx - br, by - br, bx + br, by + br), fill=(*tone, 90))
        draw.ellipse(
            (cx - int(radius * 0.55), cy - int(radius * 0.55), cx - int(radius * 0.05), cy - int(radius * 0.05)),
            fill=(255, 255, 255, 40),
        )
    return layer


def atmosphere_glow(
    width: int,
    height: int,
    cx: int,
    cy: int,
    radius: int,
    accent: tuple[int, int, int],
) -> Image.Image:
    layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    glow_r = int(radius * 1.08)
    draw.ellipse((cx - glow_r, cy - glow_r, cx + glow_r, cy + glow_r), outline=(*accent, 90), width=8)
    draw.ellipse((cx - glow_r, cy - glow_r, cx + glow_r, cy + glow_r), outline=(255, 255, 255, 55), width=3)
    return layer.filter(ImageFilter.GaussianBlur(radius=4))


def render_space(entry: dict[str, str], force: bool = False) -> tuple[Path, str]:
    slug = entry["slug"]
    out_path = OUT / f"{slug}-space.webp"
    if not force and out_path.exists() and out_path.stat().st_size >= MIN_CINEMATIC_BYTES:
        return out_path, "skipped"

    width, height = SIZE
    seed = slug_seed(slug)
    accent = hex_to_rgb(entry.get("color", "#7eb8ff"))
    base = Image.new("RGB", SIZE, (2, 4, 12))
    composed = Image.alpha_composite(base.convert("RGBA"), nebula_layer(width, height, accent, seed))
    composed = Image.alpha_composite(composed, starfield(width, height, seed))

    cx = int(width * 0.58)
    cy = int(height * 0.78)
    radius = int(min(width, height) * 0.36)
    hero_path = OUT / f"{slug}-hero.webp"
    if hero_path.is_file() and hero_path.stat().st_size >= 50_000:
        hero = Image.open(hero_path)
        sphere = sample_hero_on_sphere(hero, width, height, cx, cy, radius)
    else:
        sphere = procedural_sphere(width, height, cx, cy, radius, accent, entry.get("description", ""), seed)

    composed = Image.alpha_composite(composed, sphere)
    composed = Image.alpha_composite(composed, atmosphere_glow(width, height, cx, cy, radius, accent))

    vignette = Image.new("L", SIZE, 0)
    vdraw = ImageDraw.Draw(vignette)
    vdraw.ellipse((-width // 3, -height // 4, width + width // 3, height + height // 2), fill=255)
    vignette = vignette.filter(ImageFilter.GaussianBlur(radius=120))
    dark = Image.new("RGB", SIZE, (0, 0, 0))
    final = Image.composite(composed.convert("RGB"), dark, Image.eval(vignette, lambda p: 255 - p // 4))

    OUT.mkdir(parents=True, exist_ok=True)
    final.save(out_path, format="WEBP", quality=92, method=6)
    return out_path, "created"


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Generate cinematic planet space backgrounds")
    parser.add_argument("--force", action="store_true", help="Regenerate even if cinematic asset exists")
    parser.add_argument("--slug", action="append", help="Only process specific slug(s)")
    args = parser.parse_args()

    entries = load_planets()
    if args.slug:
        wanted = {s.lower() for s in args.slug}
        entries = [e for e in entries if e["slug"].lower() in wanted]

    created = skipped = 0
    for entry in entries:
        _, status = render_space(entry, force=args.force)
        if status == "created":
            created += 1
        else:
            skipped += 1
    print(f"Space backgrounds: created={created}, skipped={skipped}, total={len(entries)}")


if __name__ == "__main__":
    main()
