#!/usr/bin/env python3
"""Install military faction hero banners to wwwroot and upload to Azure."""

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

from military_faction_hero_prompts import faction_hero_filename, faction_prompt

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "wwwroot" / "images" / "military-units"
ASSETS = Path.home() / ".cursor/projects/Users-luke-gumbleton-Documents-Azure-Github-Star-Wars/assets"
WIDTH, HEIGHT = 1536, 1024

FACTIONS = [
    ("Confederacy of Independent Systems", "confederacy-of-independent-systems"),
    ("First Order", "first-order"),
    ("Galactic Empire", "galactic-empire"),
    ("Galactic Republic", "galactic-republic"),
    ("Mandalorian", "mandalorian"),
    ("New Republic", "new-republic"),
    ("Other", "other"),
    ("Rebel Alliance", "rebel-alliance"),
    ("Resistance", "resistance"),
    ("Sith Empire", "sith-empire"),
    ("Old Republic", "old-republic"),
]


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


def find_source(slug: str) -> Path | None:
    stem = f"military-faction-{slug}"
    for base in (ASSETS, ROOT / "assets" / "military-units"):
        for name in (stem, slug):
            for ext in (".png", ".webp", ".jpg", ".jpeg"):
                candidate = base / f"{name}{ext}"
                if candidate.is_file():
                    return candidate
    return None


def export_manifest(path: Path) -> None:
    items = [
        {
            "slug": slug,
            "filename": faction_hero_filename(slug),
            "asset_slug": f"military-faction-{slug}",
            "output": str((OUTPUT / faction_hero_filename(slug)).relative_to(ROOT)),
            "prompt": faction_prompt(slug, name),
        }
        for name, slug in FACTIONS
    ]
    path.write_text(json.dumps(items, indent=2), encoding="utf-8")


def install_and_upload(account: str, container: str, slug_filter: str | None) -> int:
    try:
        from azure.storage.blob import BlobServiceClient
    except ImportError:
        print("Install azure-storage-blob", file=sys.stderr)
        return 1

    conn = get_connection_string(account)
    blob_service = BlobServiceClient.from_connection_string(conn)
    OUTPUT.mkdir(parents=True, exist_ok=True)

    installed = 0
    uploaded = 0
    missing: list[str] = []

    for name, slug in FACTIONS:
        if slug_filter and slug != slug_filter:
            continue

        filename = faction_hero_filename(slug)
        dest = OUTPUT / filename
        source = find_source(slug)
        if source is None:
            missing.append(slug)
            continue

        payload = to_webp_bytes(source)
        dest.write_bytes(payload)
        installed += 1

        blob_name = f"military-units/{filename}"
        upload(blob_service, container, blob_name, payload)
        uploaded += 1
        print(f"  {slug} -> {blob_name} ({len(payload) // 1024} KB)")

    print(f"Installed {installed}, uploaded {uploaded}")
    if missing:
        print("Missing source assets:")
        for slug in missing:
            print(f"  military-faction-{slug}.png")
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--export-manifest", type=Path, help="Write generation manifest JSON")
    parser.add_argument("--slug", help="Process only this faction slug")
    parser.add_argument("--account", default="ststarwars")
    parser.add_argument("--container", default="images")
    args = parser.parse_args()

    if args.export_manifest:
        export_manifest(args.export_manifest)
        print(f"Wrote {args.export_manifest}")
        return 0

    return install_and_upload(args.account, args.container, args.slug)


if __name__ == "__main__":
    raise SystemExit(main())
