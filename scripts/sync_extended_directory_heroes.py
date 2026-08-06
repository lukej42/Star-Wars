#!/usr/bin/env python3
"""Generate missing org/creature/vehicle hero banners and upload to Azure."""

from __future__ import annotations

import argparse
import hashlib
import io
import random
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "Data"
ASSETS = Path.home() / ".cursor/projects/Users-luke-gumbleton-Documents-Azure-Github-Star-Wars/assets"
WIDTH, HEIGHT = 1536, 1024
STRING_FIELD = re.compile(r'(\w+) = "(.*?)"')
TYPE_FIELD = re.compile(r"Type = MilitaryVehicleType\.(\w+)")


def parse_blocks(text: str) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    for block in re.findall(r"new\(\)\s*\{(.*?)\}", text, re.DOTALL):
        entry: dict[str, str] = {}
        for match in STRING_FIELD.finditer(block):
            entry[match.group(1)] = match.group(2)
        type_match = TYPE_FIELD.search(block)
        if type_match:
            entry["Type"] = type_match.group(1)
        if "Slug" in entry:
            entries.append(entry)
    return entries


def hex_to_rgb(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))


def rng_for_slug(slug: str) -> random.Random:
    seed = int(hashlib.sha256(slug.encode()).hexdigest()[:8], 16)
    return random.Random(seed)


def gradient_layer(
    width: int, height: int, top: tuple[int, int, int], bottom: tuple[int, int, int]
) -> Image.Image:
    layer = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(layer)
    for y in range(height):
        ratio = y / max(height - 1, 1)
        color = tuple(int(top[i] * (1 - ratio) + bottom[i] * ratio) for i in range(3))
        draw.line((0, y, width, y), fill=color)
    return layer


def star_layer(width: int, height: int, rng: random.Random, count: int = 180) -> Image.Image:
    layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    for _ in range(count):
        x = rng.randint(0, width - 1)
        y = rng.randint(0, int(height * 0.72))
        radius = rng.choice([1, 1, 2])
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
            value = dist**0.5
            pixels[x, y] = min(255, max(0, int((max(0, value - 0.35) / 0.9) * 170)))
    return mask


def draw_creature_silhouette(draw: ImageDraw.ImageDraw, habitat: str, color: tuple[int, int, int]) -> None:
    lowered = habitat.lower()
    if "desert" in lowered or "arid" in lowered:
        draw.polygon([(760, 620), (920, 520), (980, 640), (820, 720)], fill=color)
        draw.polygon([(860, 520), (900, 420), (940, 520)], fill=color)
    elif "arctic" in lowered or "tundra" in lowered:
        draw.ellipse((700, 480, 980, 760), fill=color)
        draw.ellipse((620, 560, 760, 700), fill=color)
    elif "ocean" in lowered or "aquatic" in lowered:
        draw.ellipse((680, 520, 1040, 700), fill=color)
        draw.polygon([(1040, 610), (1180, 580), (1040, 650)], fill=color)
    elif "space" in lowered or "vacuum" in lowered:
        draw.ellipse((620, 420, 1080, 760), fill=color)
        for x, y in ((700, 500), (820, 460), (940, 520)):
            draw.ellipse((x - 40, y - 40, x + 40, y + 40), fill=tuple(min(255, c + 40) for c in color))
    elif "swamp" in lowered or "wetland" in lowered:
        draw.ellipse((720, 540, 980, 760), fill=color)
        draw.line((850, 540, 850, 420), fill=color, width=18)
    else:
        draw.ellipse((700, 500, 980, 760), fill=color)
        draw.polygon([(760, 500), (820, 380), (880, 500)], fill=color)


def draw_vehicle_silhouette(draw: ImageDraw.ImageDraw, vehicle_type: str, vehicle_class: str, color: tuple[int, int, int]) -> None:
    lowered = f"{vehicle_type} {vehicle_class}".lower()
    if vehicle_type == "Air" or any(word in lowered for word in ("starfighter", "gunship", "bomber", "fighter")):
        for index in range(4):
            x = 220 + index * 260
            y = 280 + (index % 2) * 40
            draw.polygon([(x, y + 20), (x + 90, y), (x + 130, y + 20), (x + 90, y + 40)], fill=color)
            draw.polygon([(x + 40, y + 10), (x + 40, y - 30), (x + 70, y + 10)], fill=color)
    elif "walker" in lowered or "transport" in lowered:
        for offset in (260, 620, 980):
            draw.rectangle((offset, 430, offset + 120, 500), fill=color)
            draw.rectangle((offset + 35, 360, offset + 85, 430), fill=color)
    elif "artillery" in lowered or "tank" in lowered:
        draw.rectangle((420, 520, 980, 620), fill=color)
        draw.rectangle((760, 420, 920, 520), fill=color)
    else:
        draw.rectangle((360, 520, 1120, 640), fill=color)
        draw.rectangle((520, 420, 760, 520), fill=color)


def render_banner(
    slug: str,
    color_hex: str,
    scene: str,
    habitat: str = "",
    vehicle_type: str = "",
    vehicle_class: str = "",
) -> Image.Image:
    accent = hex_to_rgb(color_hex)
    dark = tuple(max(0, int(channel * 0.18)) for channel in accent)
    mid = tuple(max(0, int(channel * 0.45)) for channel in accent)
    glow = tuple(min(255, int(channel * 1.15)) for channel in accent)
    rng = rng_for_slug(slug)

    base = gradient_layer(WIDTH, HEIGHT, (max(dark[0], 8), max(dark[1], 10), max(dark[2], 18)), mid)
    horizon = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    horizon_draw = ImageDraw.Draw(horizon)
    horizon_y = int(HEIGHT * 0.62)
    horizon_draw.rectangle((0, horizon_y, WIDTH, HEIGHT), fill=(*tuple(max(0, c - 30) for c in mid), 255))
    horizon_draw.rectangle((0, horizon_y - 40, WIDTH, horizon_y), fill=(*glow, 120))
    composed = Image.alpha_composite(base.convert("RGBA"), horizon)

    scene_layer = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(scene_layer)
    silhouette = tuple(max(0, c - 80) for c in dark)
    if scene == "creature":
        draw_creature_silhouette(draw, habitat, silhouette)
    else:
        draw_vehicle_silhouette(draw, vehicle_type, vehicle_class, silhouette)

    composed = Image.alpha_composite(composed, scene_layer.filter(ImageFilter.GaussianBlur(0.6)))
    composed = Image.alpha_composite(composed, star_layer(WIDTH, HEIGHT, rng))
    light = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    light_draw = ImageDraw.Draw(light)
    light_draw.ellipse((WIDTH * 0.55, -120, WIDTH * 1.15, HEIGHT * 0.55), fill=(*glow, 70))
    composed = Image.alpha_composite(composed, light.filter(ImageFilter.GaussianBlur(24)))

    vign = vignette(WIDTH, HEIGHT)
    final = Image.new("RGB", (WIDTH, HEIGHT), (0, 0, 0))
    final.paste(composed.convert("RGB"), mask=Image.eval(vign, lambda px: 255 - px))
    return Image.blend(composed.convert("RGB"), final, 0.35)


@dataclass(frozen=True)
class UploadTarget:
    asset_slug: str
    blob_names: tuple[str, ...]
    color: str
    scene: str
    habitat: str = ""
    vehicle_type: str = ""
    vehicle_class: str = ""


def build_targets() -> list[UploadTarget]:
    targets: list[UploadTarget] = []

    for org in parse_blocks((DATA / "OrganizationData.cs").read_text(encoding="utf-8")):
        slug = org["Slug"]
        targets.append(
            UploadTarget(
                asset_slug=slug,
                blob_names=(f"organizations/{slug}.webp", f"organizations/{slug}-scene.webp"),
                color=org.get("Color", "#6366f1"),
                scene="organization",
            )
        )

    targets.append(
        UploadTarget(
            asset_slug="organizations-directory-hero",
            blob_names=("organizations/organizations-directory-hero.webp",),
            color="#6366f1",
            scene="organization",
        )
    )

    for creature in parse_blocks((DATA / "CreatureData.cs").read_text(encoding="utf-8")):
        slug = creature["Slug"]
        targets.append(
            UploadTarget(
                asset_slug=slug,
                blob_names=(f"creatures/{slug}-scene.webp",),
                color=creature.get("Color", "#64748b"),
                scene="creature",
                habitat=creature.get("Habitat", ""),
            )
        )

    targets.append(
        UploadTarget(
            asset_slug="creatures-directory-hero",
            blob_names=("creatures/creatures-directory-hero.webp",),
            color="#059669",
            scene="creature",
            habitat="Jungle & Forest",
        )
    )

    for vehicle in parse_blocks((DATA / "VehicleData.cs").read_text(encoding="utf-8")):
        faction = vehicle["FactionSlug"]
        slug = vehicle["Slug"]
        type_slug = "ground" if vehicle.get("Type") == "Ground" else "air"
        asset_slug = f"{faction}-{type_slug}-{slug}"
        targets.append(
            UploadTarget(
                asset_slug=asset_slug,
                blob_names=(f"military-vehicles/{asset_slug}-hero.webp",),
                color=vehicle.get("Color", "#4a90d9"),
                scene="vehicle",
                vehicle_type=vehicle.get("Type", "Ground"),
                vehicle_class=vehicle.get("VehicleClass", ""),
            )
        )

    return targets


def find_source(slug: str) -> Path | None:
    for candidate in (ASSETS / f"{slug}.png", ASSETS / f"{slug}.webp"):
        if candidate.is_file():
            return candidate
    return None


def ensure_asset(target: UploadTarget, force: bool, allow_procedural: bool) -> Path:
    source = find_source(target.asset_slug)
    if source is not None:
        return source

    generated = ASSETS / f"{target.asset_slug}.png"
    if generated.is_file() and not force:
        return generated

    if not allow_procedural:
        raise FileNotFoundError(f"No AI asset for {target.asset_slug}; use GenerateImage or pass --allow-procedural")

    ASSETS.mkdir(parents=True, exist_ok=True)
    image = render_banner(
        target.asset_slug,
        target.color,
        target.scene,
        habitat=target.habitat,
        vehicle_type=target.vehicle_type,
        vehicle_class=target.vehicle_class,
    )
    image.save(generated, format="PNG")
    return generated


def to_webp_bytes(source: Path) -> bytes:
    img = Image.open(source).convert("RGB")
    if img.size != (WIDTH, HEIGHT):
        img = img.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
    buffer = io.BytesIO()
    img.save(buffer, format="WEBP", quality=90, method=6)
    return buffer.getvalue()


def get_connection_string(account: str) -> str:
    result = subprocess.run(
        ["az", "storage", "account", "show-connection-string", "--name", account, "-o", "tsv"],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--account", default="ststarwars")
    parser.add_argument("--container", default="images")
    parser.add_argument("--generate-only", action="store_true")
    parser.add_argument("--force-generate", action="store_true")
    parser.add_argument(
        "--allow-procedural",
        action="store_true",
        help="Generate gradient placeholder PNGs when AI source assets are missing",
    )
    parser.add_argument("--slug", action="append", help="Upload only these asset slugs (repeatable)")
    args = parser.parse_args()

    targets = build_targets()
    if args.slug:
        wanted = set(args.slug)
        targets = [target for target in targets if target.asset_slug in wanted]
        if not targets:
            print(f"No targets matched slugs: {', '.join(sorted(wanted))}", file=sys.stderr)
            return 1
    generated = 0
    for target in targets:
        before = find_source(target.asset_slug)
        source = ensure_asset(target, args.force_generate, args.allow_procedural)
        if before is None:
            generated += 1
            print(f"Generated {source.name}")

    print(f"Prepared assets for {len(targets)} targets ({generated} newly generated)")

    if args.generate_only:
        return 0

    try:
        from azure.storage.blob import BlobServiceClient, ContentSettings
    except ImportError:
        print("Install azure-storage-blob", file=sys.stderr)
        return 1

    blob_service = BlobServiceClient.from_connection_string(get_connection_string(args.account))
    uploaded = 0
    for target in targets:
        source = ensure_asset(target, False, args.allow_procedural)
        payload = to_webp_bytes(source)
        for blob_name in target.blob_names:
            blob_client = blob_service.get_blob_client(container=args.container, blob=blob_name)
            blob_client.upload_blob(
                payload,
                overwrite=True,
                content_settings=ContentSettings(
                    content_type="image/webp",
                    cache_control="public, max-age=31536000, immutable",
                ),
            )
            uploaded += 1
            print(f"Uploaded {blob_name}")

    print(f"Uploaded {uploaded} blobs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
