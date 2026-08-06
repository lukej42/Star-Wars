#!/usr/bin/env python3
"""Install military vehicle hero banners and upload to Azure (overwrite procedural blobs)."""

from __future__ import annotations

import argparse
import io
import json
import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from military_vehicle_hero_prompts import (
    ASSETS,
    GOOD_SIZE_THRESHOLD,
    OUTPUT,
    asset_slug,
    find_best_source,
    hero_filename,
    parse_vehicles,
    vehicle_prompt,
)

WIDTH, HEIGHT = 1536, 1024


def get_connection_string(account: str) -> str:
    result = subprocess.run(
        ["az", "storage", "account", "show-connection-string", "--name", account, "-o", "tsv"],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def to_webp_bytes(source: Path) -> bytes:
    from PIL import Image

    img = Image.open(source).convert("RGB")
    if img.size != (WIDTH, HEIGHT):
        img = img.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
    buffer = io.BytesIO()
    img.save(buffer, format="WEBP", quality=90, method=6)
    return buffer.getvalue()


def upload(blob_service, container: str, blob_name: str, payload: bytes) -> None:
    from azure.storage.blob import ContentSettings

    blob_client = blob_service.get_blob_client(container=container, blob=blob_name)
    blob_client.upload_blob(
        payload,
        overwrite=True,
        content_settings=ContentSettings(
            content_type="image/webp",
            cache_control="public, max-age=31536000, immutable",
        ),
    )


def classify_vehicles() -> tuple[list[dict], list[dict]]:
    good: list[dict] = []
    need: list[dict] = []
    for vehicle in parse_vehicles():
        slug = asset_slug(vehicle)
        source = find_best_source(slug)
        size = source.stat().st_size if source else 0
        entry = {**vehicle, "asset_slug": slug, "source": str(source) if source else None, "source_size": size}
        if source and size >= GOOD_SIZE_THRESHOLD:
            good.append(entry)
        else:
            need.append(entry)
    return good, need


def export_manifest(path: Path, only_missing: bool = True) -> None:
    good, need = classify_vehicles()
    targets = need if only_missing else good + need
    items = [
        {
            "asset_slug": entry["asset_slug"],
            "filename": hero_filename(entry),
            "asset_file": entry["asset_slug"],
            "prompt": vehicle_prompt(
                entry["asset_slug"],
                entry["Name"],
                entry["VehicleClass"],
                entry["Description"],
            ),
        }
        for entry in targets
    ]
    path.write_text(json.dumps(items, indent=2), encoding="utf-8")


def install_and_upload(account: str, container: str, slug_filter: str | None) -> int:
    try:
        from azure.storage.blob import BlobServiceClient
    except ImportError:
        print("Install azure-storage-blob", file=sys.stderr)
        return 1

    blob_service = BlobServiceClient.from_connection_string(get_connection_string(account))
    OUTPUT.mkdir(parents=True, exist_ok=True)

    uploaded = 0
    missing: list[str] = []

    for vehicle in parse_vehicles():
        slug = asset_slug(vehicle)
        if slug_filter and slug != slug_filter:
            continue

        source = find_best_source(slug)
        if source is None or source.stat().st_size < GOOD_SIZE_THRESHOLD:
            missing.append(slug)
            continue

        filename = hero_filename(vehicle)
        payload = to_webp_bytes(source)
        dest = OUTPUT / filename
        dest.write_bytes(payload)

        blob_name = f"military-vehicles/{filename}"
        upload(blob_service, container, blob_name, payload)
        uploaded += 1
        print(f"  {slug} ({len(payload) // 1024} KB)")

    print(f"Uploaded {uploaded} vehicle heroes")
    if missing:
        print(f"Still missing quality assets ({len(missing)}):")
        for slug in missing:
            print(f"  {slug}")
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--export-manifest", type=Path, help="Write JSON manifest of vehicles needing regen")
    parser.add_argument("--status", action="store_true", help="Print good vs missing counts")
    parser.add_argument("--slug", help="Process only this asset slug")
    parser.add_argument("--account", default="ststarwars")
    parser.add_argument("--container", default="images")
    args = parser.parse_args()

    if args.status:
        good, need = classify_vehicles()
        print(f"Good: {len(good)}, Need regeneration: {len(need)}")
        for entry in need:
            print(f"  NEED {entry['asset_slug']}")
        return 0

    if args.export_manifest:
        export_manifest(args.export_manifest)
        print(f"Wrote {args.export_manifest}")
        return 0

    return install_and_upload(args.account, args.container, args.slug)


if __name__ == "__main__":
    raise SystemExit(main())
