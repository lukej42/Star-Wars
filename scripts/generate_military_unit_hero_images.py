#!/usr/bin/env python3
"""Generate cinematic military unit hero banners as WEBP files."""

from __future__ import annotations

import argparse
import hashlib
import random
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from military_unit_hero_prompts import hero_filename, load_military_units

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "wwwroot" / "images" / "military-units"
CURSOR_ASSETS = (
    Path.home()
    / ".cursor/projects/Users-luke-gumbleton-Documents-Azure-Github-Star-Wars/assets"
)
WIDTH, HEIGHT = 1536, 1024


def hex_to_rgb(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))


def rng_for_slug(slug: str) -> random.Random:
    seed = int(hashlib.sha256(slug.encode()).hexdigest()[:8], 16)
    return random.Random(seed)


def gradient_layer(width: int, height: int, top: tuple[int, int, int], bottom: tuple[int, int, int]) -> Image.Image:
    layer = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(layer)
    for y in range(height):
        ratio = y / max(height - 1, 1)
        color = tuple(int(top[i] * (1 - ratio) + bottom[i] * ratio) for i in range(3))
        draw.line((0, y, width, y), fill=color)
    return layer


def noise_layer(width: int, height: int, rng: random.Random, alpha: int = 28) -> Image.Image:
    gray = Image.new("L", (width, height))
    pixels = gray.load()
    for y in range(height):
        for x in range(width):
            pixels[x, y] = rng.randint(0, 255)
    return Image.merge("RGBA", (gray, gray, gray, Image.new("L", (width, height), alpha)))


def star_layer(width: int, height: int, rng: random.Random, count: int = 180) -> Image.Image:
    layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    for _ in range(count):
        x = rng.randint(0, width - 1)
        y = rng.randint(0, int(height * 0.72))
        radius = rng.choice([1, 1, 1, 2])
        brightness = rng.randint(150, 255)
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(brightness, brightness, brightness, 220))
    return layer


def vignette(width: int, height: int) -> Image.Image:
    mask = Image.new("L", (width, height))
    pixels = mask.load()
    cx, cy = width / 2, height / 2
    for y in range(height):
        for x in range(width):
            dist = ((x - cx) / (width * 0.55)) ** 2 + ((y - cy) / (height * 0.55)) ** 2
            value = dist ** 0.5
            pixels[x, y] = min(255, max(0, int((max(0, value - 0.35) / 0.9) * 170)))
    return mask


def draw_troop_line(draw: ImageDraw.ImageDraw, y: int, count: int, color: tuple[int, int, int], width: int) -> None:
    spacing = width // (count + 2)
    for index in range(count):
        x = spacing * (index + 1)
        draw.rectangle((x - 18, y - 48, x + 18, y), fill=color)
        draw.ellipse((x - 22, y - 78, x + 22, y - 34), fill=color)


def draw_fleet(draw: ImageDraw.ImageDraw, width: int, height: int, color: tuple[int, int, int]) -> None:
    for index, scale in enumerate((1.0, 0.75, 0.55)):
        ship_w = int(220 * scale)
        ship_h = int(70 * scale)
        x = 180 + index * 260
        y = 220 + index * 40
        draw.polygon(
            [
                (x, y + ship_h // 2),
                (x + ship_w, y + ship_h),
                (x + ship_w + 80, y + ship_h // 2),
                (x + ship_w, y),
            ],
            fill=color,
        )
        draw.rectangle((x + 40, y + ship_h, x + ship_w - 20, y + ship_h + int(30 * scale)), fill=color)


def draw_walkers(draw: ImageDraw.ImageDraw, width: int, height: int, color: tuple[int, int, int]) -> None:
    for offset in (260, 620, 980):
        draw.rectangle((offset, 430, offset + 120, 500), fill=color)
        draw.rectangle((offset + 35, 360, offset + 85, 430), fill=color)
        for leg_x in (offset + 20, offset + 90):
            draw.line((leg_x, 500, leg_x - 20, 590), fill=color, width=8)
            draw.line((leg_x, 500, leg_x + 20, 590), fill=color, width=8)


def draw_droids(draw: ImageDraw.ImageDraw, width: int, height: int, color: tuple[int, int, int]) -> None:
    for index in range(8):
        x = 140 + index * 150
        draw.rectangle((x, 470, x + 36, 560), fill=color)
        draw.ellipse((x - 8, 430, x + 44, 470), fill=color)


def draw_fighters(draw: ImageDraw.ImageDraw, width: int, height: int, color: tuple[int, int, int]) -> None:
    for index in range(5):
        x = 180 + index * 240
        y = 250 + (index % 2) * 40
        draw.polygon([(x, y + 20), (x + 90, y), (x + 130, y + 20), (x + 90, y + 40)], fill=color)
        draw.polygon([(x + 40, y + 10), (x + 40, y - 30), (x + 70, y + 10)], fill=color)
        draw.polygon([(x + 40, y + 30), (x + 40, y + 70), (x + 70, y + 30)], fill=color)


def scene_template(unit_type: str, slug: str) -> str:
    lowered = f"{unit_type} {slug}".lower()
    if any(word in lowered for word in ("navy", "fleet", "bomber", "starfighter", "squadron")):
        return "fleet"
    if any(word in lowered for word in ("walker", "army", "garrison", "ground")):
        return "walkers"
    if "droid" in lowered:
        return "droids"
    if any(word in lowered for word in ("starfighter", "wing", "rapier", "rogue")):
        return "fighters"
    return "troops"


def render_unit(entry: dict[str, str], force: bool = False) -> Path:
    filename = hero_filename(entry)
    output_path = OUTPUT / filename
    if output_path.exists() and not force:
        return output_path

    accent = hex_to_rgb(entry["color"])
    dark = tuple(max(0, int(channel * 0.18)) for channel in accent)
    mid = tuple(max(0, int(channel * 0.45)) for channel in accent)
    glow = tuple(min(255, int(channel * 1.15)) for channel in accent)
    slug_key = f"{entry['factionSlug']}-{entry['slug']}"
    rng = rng_for_slug(slug_key)

    base = gradient_layer(WIDTH, HEIGHT, (max(dark[0], 8), max(dark[1], 10), max(dark[2], 18)), (mid[0], mid[1], mid[2]))
    horizon = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    horizon_draw = ImageDraw.Draw(horizon)
    horizon_y = int(HEIGHT * 0.62)
    horizon_draw.rectangle((0, horizon_y, WIDTH, HEIGHT), fill=(*tuple(max(0, c - 30) for c in mid), 255))
    horizon_draw.rectangle((0, horizon_y - 40, WIDTH, horizon_y), fill=(*glow, 120))
    base = Image.alpha_composite(base.convert("RGBA"), horizon)

    scene = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(scene)
    silhouette = tuple(max(0, c - 80) for c in dark)
    template = scene_template(entry["unitType"], entry["slug"])
    if template == "fleet":
        draw_fleet(draw, WIDTH, HEIGHT, silhouette)
    elif template == "walkers":
        draw_walkers(draw, WIDTH, HEIGHT, silhouette)
    elif template == "droids":
        draw_droids(draw, WIDTH, HEIGHT, silhouette)
    elif template == "fighters":
        draw_fighters(draw, WIDTH, HEIGHT, silhouette)
    else:
        draw_troop_line(draw, int(HEIGHT * 0.72), 10, silhouette, WIDTH)

    scene = scene.filter(ImageFilter.GaussianBlur(0.6))
    composed = Image.alpha_composite(base, scene)
    composed = Image.alpha_composite(composed, star_layer(WIDTH, HEIGHT, rng))
    composed = Image.alpha_composite(composed, noise_layer(WIDTH, HEIGHT, rng))

    light = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    light_draw = ImageDraw.Draw(light)
    light_draw.ellipse((WIDTH * 0.55, -120, WIDTH * 1.15, HEIGHT * 0.55), fill=(*glow, 70))
    composed = Image.alpha_composite(composed, light.filter(ImageFilter.GaussianBlur(24)))

    vign = vignette(WIDTH, HEIGHT)
    final = Image.new("RGB", (WIDTH, HEIGHT), (0, 0, 0))
    final.paste(composed.convert("RGB"), mask=Image.eval(vign, lambda px: 255 - px))
    final = Image.blend(composed.convert("RGB"), final, 0.35)

    OUTPUT.mkdir(parents=True, exist_ok=True)
    final.save(output_path, format="WEBP", quality=88, method=6)
    return output_path


def copy_cursor_assets() -> int:
    if not CURSOR_ASSETS.is_dir():
        return 0
    copied = 0
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for asset in CURSOR_ASSETS.glob("*-hero.webp"):
        dest = OUTPUT / asset.name
        if not dest.exists() or asset.stat().st_mtime > dest.stat().st_mtime:
            dest.write_bytes(asset.read_bytes())
            copied += 1
    return copied


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate military unit hero WEBP banners")
    parser.add_argument("--force", action="store_true", help="Regenerate even if file exists")
    parser.add_argument("--skip-ai-copy", action="store_true", help="Do not copy Cursor-generated assets first")
    args = parser.parse_args()

    if not args.skip_ai_copy:
        copied = copy_cursor_assets()
        print(f"Copied {copied} Cursor-generated hero assets")

    generated = 0
    for entry in load_military_units():
        path = OUTPUT / hero_filename(entry)
        if path.exists() and not args.force:
            continue
        render_unit(entry, force=True)
        generated += 1

    total = len(load_military_units())
    present = sum(1 for entry in load_military_units() if (OUTPUT / hero_filename(entry)).is_file())
    print(f"Generated {generated} procedural heroes ({present}/{total} total present)")


if __name__ == "__main__":
    main()
