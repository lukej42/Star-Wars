#!/usr/bin/env python3
"""Generate Force and Wars hero WEBP banners (AI assets + procedural fallback)."""

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

from force_wars_hero_prompts import HeroEntry, all_hero_entries

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


def draw_fleet(draw: ImageDraw.ImageDraw, color: tuple[int, int, int]) -> None:
    for index, scale in enumerate((1.0, 0.75, 0.55)):
        ship_w = int(220 * scale)
        ship_h = int(70 * scale)
        x = 180 + index * 260
        y = 220 + index * 40
        draw.polygon([(x, y + ship_h // 2), (x + ship_w, y + ship_h), (x + ship_w + 80, y + ship_h // 2), (x + ship_w, y)], fill=color)


def draw_battlefield(draw: ImageDraw.ImageDraw, width: int, color: tuple[int, int, int]) -> None:
    draw.rectangle((0, int(HEIGHT * 0.62), width, HEIGHT), fill=color)
    for index in range(6):
        x = 120 + index * 220
        draw.polygon([(x, 520), (x + 80, 470), (x + 160, 520), (x + 80, 560)], fill=tuple(min(255, c + 20) for c in color))


def scene_kind(entry: HeroEntry) -> str:
    if entry.category in {"war", "battle"}:
        return "battle"
    if entry.category == "lightsaber-form" or "lightsaber" in entry.slug:
        return "blade"
    if any(word in entry.slug for word in ("navy", "fleet", "war")):
        return "fleet"
    return "force"


def render_entry(entry: HeroEntry) -> None:
    accent = hex_to_rgb(entry.color)
    dark = tuple(max(0, int(channel * 0.18)) for channel in accent)
    mid = tuple(max(0, int(channel * 0.45)) for channel in accent)
    glow = tuple(min(255, int(channel * 1.15)) for channel in accent)
    rng = rng_for_slug(f"{entry.category}-{entry.slug}")

    base = gradient_layer(WIDTH, HEIGHT, (max(dark[0], 8), max(dark[1], 10), max(dark[2], 18)), mid)
    horizon = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    horizon_draw = ImageDraw.Draw(horizon)
    horizon_y = int(HEIGHT * 0.62)
    horizon_draw.rectangle((0, horizon_y, WIDTH, HEIGHT), fill=(*tuple(max(0, c - 30) for c in mid), 255))
    horizon_draw.rectangle((0, horizon_y - 40, WIDTH, horizon_y), fill=(*glow, 120))
    composed = Image.alpha_composite(base.convert("RGBA"), horizon)

    scene = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(scene)
    silhouette = tuple(max(0, c - 80) for c in dark)
    kind = scene_kind(entry)
    if kind == "fleet":
        draw_fleet(draw, silhouette)
    elif kind == "battle":
        draw_battlefield(draw, WIDTH, silhouette)
    elif kind == "blade":
        draw.line((280, 620, 1180, 280), fill=(*glow, 220), width=14)
        draw.line((320, 580, 1120, 320), fill=(255, 255, 255, 180), width=4)
    else:
        draw.ellipse((640, 260, 900, 520), fill=(*glow, 90))
        draw.rectangle((710, 380, 830, 430), fill=(255, 255, 255, 120))

    composed = Image.alpha_composite(composed, scene.filter(ImageFilter.GaussianBlur(0.6)))
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

    entry.output.parent.mkdir(parents=True, exist_ok=True)
    final.save(entry.output, format="WEBP", quality=88, method=6)


def asset_name(entry: HeroEntry) -> str:
    if entry.category == "battle":
        return f"battles-{entry.slug}-hero.webp"
    if entry.category == "lightsaber-form":
        return f"lightsaber-forms-{entry.slug}-hero.webp"
    if entry.category == "war":
        return f"wars-{entry.slug}-hero.webp"
    return f"the-force-{entry.slug}-hero.webp"


def find_cursor_asset(entry: HeroEntry) -> Path | None:
    if not CURSOR_ASSETS.is_dir():
        return None
    candidates = [
        CURSOR_ASSETS / entry.output.name,
        CURSOR_ASSETS / asset_name(entry),
        CURSOR_ASSETS / f"{entry.slug}-hero.webp",
        CURSOR_ASSETS / f"{entry.slug}-hero.png",
    ]
    return next((path for path in candidates if path.is_file()), None)


def copy_cursor_assets(entries: list[HeroEntry], force: bool) -> int:
    if not CURSOR_ASSETS.is_dir():
        return 0
    copied = 0
    for entry in entries:
        candidates = [
            CURSOR_ASSETS / entry.output.name,
            CURSOR_ASSETS / asset_name(entry),
        ]
        src = next((path for path in candidates if path.is_file()), None)
        if src is None:
            continue
        if entry.output.exists() and entry.output.stat().st_mtime >= src.stat().st_mtime and not force:
            continue
        entry.output.parent.mkdir(parents=True, exist_ok=True)
        entry.output.write_bytes(src.read_bytes())
        copied += 1
    return copied


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Force and Wars hero images")
    parser.add_argument("--force", action="store_true", help="Regenerate even if file exists")
    parser.add_argument("--skip-ai-copy", action="store_true")
    parser.add_argument(
        "--procedural-fallback",
        action="store_true",
        help="Allow procedural placeholders for missing Force/Wars heroes",
    )
    args = parser.parse_args()

    entries = all_hero_entries()
    if not args.skip_ai_copy:
        copied = copy_cursor_assets(entries, args.force)
        print(f"Copied {copied} Cursor-generated hero assets")

    if not args.procedural_fallback:
        wars_entries = [e for e in entries if e.category in {"war", "battle"}]
        missing_wars = [e for e in wars_entries if not find_cursor_asset(e)]
        if missing_wars:
            print(
                f"ERROR: {len(missing_wars)} Wars & Conflicts heroes missing AI assets. "
                "Generate with wars_conflicts_hero_manifest.json — never use --procedural-fallback for wars.",
                file=sys.stderr,
            )
            for entry in missing_wars[:10]:
                print(f"  missing: {entry.slug}", file=sys.stderr)
            return 1
        print(f"Wars & Conflicts AI heroes: {len(wars_entries)}/{len(wars_entries)} present")
        force_entries = [e for e in entries if e.category not in {"war", "battle"}]
        generated = 0
        for entry in force_entries:
            if entry.output.exists() and not args.force:
                continue
            render_entry(entry)
            generated += 1
        if generated:
            print(f"Generated {generated} procedural Force heroes")
        return

    generated = 0
    for entry in entries:
        if entry.output.exists() and not args.force:
            continue
        render_entry(entry)
        generated += 1

    present = sum(1 for entry in entries if entry.output.is_file())
    print(f"Generated {generated} procedural heroes ({present}/{len(entries)} total present)")


if __name__ == "__main__":
    main()
