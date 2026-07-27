#!/usr/bin/env python3
"""Generate space and hero WEBP assets for planets using PIL (procedural cinematic style)."""

from __future__ import annotations

import hashlib
import math
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "Data" / "GalaxyData.cs"
OUT = ROOT / "wwwroot" / "images" / "planets"
SPACE_SIZE = (1920, 1080)
HERO_SIZE = (1536, 1024)


def parse_planets() -> list[dict[str, str]]:
    text = DATA.read_text(encoding="utf-8")
    entries = []
    for block in re.findall(r"new\(\)\s*\{(.*?)\}", text, re.DOTALL):
        name = re.search(r'Name = "(.*?)"', block)
        slug = re.search(r'Slug = "(.*?)"', block)
        color = re.search(r'Color = "(.*?)"', block)
        desc = re.search(r'Description = "(.*?)"', block)
        if name and slug:
            entries.append(
                {
                    "name": name.group(1),
                    "slug": slug.group(1),
                    "color": color.group(1) if color else "#7eb8ff",
                    "desc": desc.group(1) if desc else "",
                }
            )
    return entries


def hex_to_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def seed(slug: str) -> int:
    return int(hashlib.md5(slug.encode()).hexdigest(), 16)


def draw_stars(draw: ImageDraw.ImageDraw, w: int, h: int, s: int, count: int = 140) -> None:
    for i in range(count):
        x = (s * (i + 17) * 37) % w
        y = (s * (i + 23) * 53) % h
        r = 1 + ((s + i) % 3)
        opacity = 80 + ((s + i * 3) % 120)
        draw.ellipse((x - r, y - r, x + r, y + r), fill=(255, 255, 255, opacity))


def space_image(entry: dict[str, str]) -> Image.Image:
    w, h = SPACE_SIZE
    img = Image.new("RGBA", (w, h), (2, 4, 10, 255))
    draw = ImageDraw.Draw(img, "RGBA")
    s = seed(entry["slug"])
    r, g, b = hex_to_rgb(entry["color"])
    draw_stars(draw, w, h, s)

    # Nebula glow
    for cx, cy, rad, alpha in (
        (1500, 180, 320, 35),
        (300, 260, 240, 25),
        (960, 540, 500, 20),
    ):
        glow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        gdraw = ImageDraw.Draw(glow)
        gdraw.ellipse((cx - rad, cy - rad, cx + rad, cy + rad), fill=(r, g, b, alpha))
        glow = glow.filter(ImageFilter.GaussianBlur(radius=60))
        img = Image.alpha_composite(img, glow)

    # Planet body
    px, py = 1180, 620
    pr = 280 if "gas" in entry["desc"].lower() else 220
    body = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    bdraw = ImageDraw.Draw(body)
    bdraw.ellipse((px - pr, py - pr, px + pr, py + pr), fill=(r, g, b, 240))
    highlight = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    hdraw = ImageDraw.Draw(highlight)
    hdraw.ellipse((px - pr + 40, py - pr + 30, px + pr - 80, py + pr - 80), fill=(255, 255, 255, 60))
    body = Image.alpha_composite(body, highlight)
    body = body.filter(ImageFilter.GaussianBlur(radius=1))
    img = Image.alpha_composite(img, body)
    return img.convert("RGB")


def hero_image(entry: dict[str, str]) -> Image.Image:
    w, h = HERO_SIZE
    r, g, b = hex_to_rgb(entry["color"])
    s = seed(entry["slug"])
    img = Image.new("RGB", (w, h), (8, 12, 24))
    draw = ImageDraw.Draw(img)

    # Sky gradient
    for y in range(h):
        t = y / h
        cr = int(8 + (r * 0.35) * (1 - t))
        cg = int(12 + (g * 0.35) * (1 - t))
        cb = int(24 + (b * 0.45) * (1 - t))
        draw.line([(0, y), (w, y)], fill=(cr, cg, cb))

    # Distant mountains / horizon
    base_y = int(h * 0.62)
    points = []
    for x in range(0, w + 40, 40):
        noise = ((s + x * 13) % 90) - 45
        points.append((x, base_y + noise))
    points += [(w, h), (0, h)]
    draw.polygon(points, fill=(max(r - 40, 0), max(g - 40, 0), max(b - 40, 0)))

    # Foreground terrain
    fg_points = []
    for x in range(0, w + 30, 30):
        noise = ((s + x * 29) % 60) - 20
        fg_points.append((x, base_y + 40 + noise))
    fg_points += [(w, h), (0, h)]
    draw.polygon(fg_points, fill=(max(r - 70, 0), max(g - 70, 0), max(b - 70, 0)))

    # Atmospheric glow
    glow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow)
    gdraw.ellipse((w // 4, h // 6, 3 * w // 4, h // 2), fill=(r, g, b, 40))
    glow = glow.filter(ImageFilter.GaussianBlur(radius=80))
    img = Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB")

    # Subtle vignette
    vignette = Image.new("L", (w, h), 0)
    vdraw = ImageDraw.Draw(vignette)
    vdraw.ellipse((-w // 4, -h // 4, 5 * w // 4, 5 * h // 4), fill=255)
    vignette = vignette.filter(ImageFilter.GaussianBlur(radius=120))
    dark = Image.new("RGB", (w, h), (0, 0, 0))
    img = Image.composite(img, dark, Image.eval(vignette, lambda p: 255 - p // 3))
    return img


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    created_space = created_hero = 0
    for entry in parse_planets():
        slug = entry["slug"]
        space_path = OUT / f"{slug}-space.webp"
        hero_path = OUT / f"{slug}-hero.webp"
        if not space_path.exists() or space_path.stat().st_size < 5000:
            space_image(entry).save(space_path, "WEBP", quality=90, method=6)
            created_space += 1
        if not hero_path.exists() or hero_path.stat().st_size < 5000:
            hero_image(entry).save(hero_path, "WEBP", quality=90, method=6)
            created_hero += 1
    print(f"Generated space={created_space} hero={created_hero} (total planets={len(parse_planets())})")


if __name__ == "__main__":
    main()
