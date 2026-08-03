#!/usr/bin/env python3
"""Generate compact vertical lightsaber GIFs in memory and upload directly to Azure Blob Storage."""

from __future__ import annotations

import argparse
import io
import math
import subprocess
import sys

COLORS: dict[str, tuple[int, int, int]] = {
    "blue": (72, 148, 255),
    "green": (0, 225, 96),
    "purple": (176, 96, 255),
    "red": (255, 56, 56),
    "yellow": (255, 224, 72),
    "white": (235, 245, 255),
}

# Per-color blade tuning (core highlight + glow strength).
COLOR_TUNING: dict[str, dict[str, object]] = {
    "green": {
        "core": (180, 255, 210),
        "glow_scale": 1.2,
        "pulse_floor": 0.78,
    },
}


def core_color(color: tuple[int, int, int], color_name: str) -> tuple[int, int, int]:
    tuning = COLOR_TUNING.get(color_name, {})
    if "core" in tuning:
        return tuning["core"]  # type: ignore[return-value]
    r, g, b = color
    return (min(255, r + 50), min(255, g + 50), min(255, b + 50))

WIDTH = 24
HEIGHT = 96
HILT_HEIGHT = 22
FRAMES = 16
DURATION_MS = 90


def get_connection_string(account: str) -> str:
    result = subprocess.run(
        ["az", "storage", "account", "show-connection-string", "--name", account, "-o", "tsv"],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def blend(alpha: float, rgb: tuple[int, int, int]) -> tuple[int, int, int, int]:
    return (rgb[0], rgb[1], rgb[2], max(0, min(255, int(255 * alpha))))


def draw_vertical_glow(
    draw,
    center_x: float,
    top: float,
    bottom: float,
    core_half: float,
    glow_half: float,
    color: tuple[int, int, int],
    core: tuple[int, int, int],
    pulse: float,
    glow_scale: float = 1.0,
) -> None:
    height = bottom - top
    steps = max(1, int(height))
    for step in range(steps):
        y = top + step
        t = step / max(steps - 1, 1)
        tip_fade = 0.55 + 0.45 * (1.0 - t)
        intensity = pulse * tip_fade

        glow_alpha = 0.22 * intensity * glow_scale
        draw.rectangle(
            (center_x - glow_half, y, center_x + glow_half, y + 1),
            fill=blend(glow_alpha, color),
        )
        mid_alpha = 0.45 * intensity * glow_scale
        draw.rectangle(
            (center_x - glow_half * 0.55, y, center_x + glow_half * 0.55, y + 1),
            fill=blend(mid_alpha, color),
        )
        core_alpha = 0.95 * intensity
        draw.rectangle(
            (center_x - core_half, y, center_x + core_half, y + 1),
            fill=blend(core_alpha, core),
        )


def render_frame(color: tuple[int, int, int], color_name: str, phase: float) -> "Image.Image":
    from PIL import Image, ImageDraw

    tuning = COLOR_TUNING.get(color_name, {})
    pulse_floor = float(tuning.get("pulse_floor", 0.72))
    glow_scale = float(tuning.get("glow_scale", 1.0))
    core = core_color(color, color_name)

    pulse = pulse_floor + (1.0 - pulse_floor) * (0.5 + 0.5 * math.sin(phase * math.pi * 2))
    flicker = 0.94 + 0.06 * math.sin(phase * math.pi * 4)
    pulse *= flicker

    img = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    center_x = WIDTH / 2
    hilt_top = HEIGHT - HILT_HEIGHT
    blade_bottom = hilt_top + 2
    blade_top = 4

    draw_vertical_glow(draw, center_x, blade_top, blade_bottom, 1.0, 5.5, color, core, pulse, glow_scale)

    # Emitter ring
    ring_y = hilt_top + 1
    draw.ellipse(
        (center_x - 4.5, ring_y - 1.5, center_x + 4.5, ring_y + 3.5),
        fill=(170, 175, 185, 230),
    )
    draw.ellipse(
        (center_x - 2.5, ring_y, center_x + 2.5, ring_y + 2.5),
        fill=blend(0.85 * pulse, color),
    )

    # Hilt body
    draw.rounded_rectangle(
        (center_x - 3.5, hilt_top + 3, center_x + 3.5, HEIGHT - 2),
        radius=2,
        fill=(42, 44, 50, 255),
    )
    draw.rectangle(
        (center_x - 4, hilt_top + 8, center_x + 4, hilt_top + 10),
        fill=(28, 30, 34, 255),
    )
    draw.rectangle(
        (center_x - 3, hilt_top + 14, center_x + 3, hilt_top + 15),
        fill=(90, 92, 98, 255),
    )
    draw.ellipse(
        (center_x - 2, HEIGHT - 6, center_x + 2, HEIGHT - 2),
        fill=(20, 22, 26, 255),
    )

    return img


def build_gif(color_name: str, rgb: tuple[int, int, int]) -> bytes:
    frames = [render_frame(rgb, color_name, index / FRAMES) for index in range(FRAMES)]
    buffer = io.BytesIO()
    frames[0].save(
        buffer,
        format="GIF",
        save_all=True,
        append_images=frames[1:],
        duration=DURATION_MS,
        loop=0,
        disposal=2,
        optimize=True,
    )
    return buffer.getvalue()


def upload_blob(blob_service, container: str, blob_name: str, payload: bytes) -> None:
    from azure.storage.blob import ContentSettings

    blob_client = blob_service.get_blob_client(container=container, blob=blob_name)
    blob_client.upload_blob(
        payload,
        overwrite=True,
        content_settings=ContentSettings(
            content_type="image/gif",
            cache_control="public, max-age=31536000, immutable",
        ),
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--account", default="ststarwars")
    parser.add_argument("--container", default="images")
    parser.add_argument("--prefix", default="lightsaber-glow")
    parser.add_argument("--only", choices=sorted(COLORS.keys()), help="Upload a single color")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    targets = {args.only: COLORS[args.only]} if args.only else COLORS

    try:
        from PIL import Image  # noqa: F401
    except ImportError:
        print("Install Pillow: pip install pillow", file=sys.stderr)
        return 1

    if args.dry_run:
        for color_name, rgb in targets.items():
            payload = build_gif(color_name, rgb)
            print(f"{color_name}.gif -> {len(payload):,} bytes ({WIDTH}x{HEIGHT})")
        return 0

    try:
        from azure.storage.blob import BlobServiceClient
    except ImportError:
        print("Install azure-storage-blob: pip install azure-storage-blob", file=sys.stderr)
        return 1

    connection_string = get_connection_string(args.account)
    blob_service = BlobServiceClient.from_connection_string(connection_string)

    for color_name, rgb in targets.items():
        payload = build_gif(color_name, rgb)
        blob_name = f"{args.prefix}/{color_name}.gif"
        upload_blob(blob_service, args.container, blob_name, payload)
        print(f"Uploaded {blob_name} ({len(payload):,} bytes, {WIDTH}x{HEIGHT})")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
