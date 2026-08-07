#!/usr/bin/env python3
"""Upload Wars & Conflicts hero images from Cursor assets directly to Azure Blob Storage."""

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

from regenerate_wars_conflicts_heroes import export_manifest, load_battles, load_wars

ROOT = Path(__file__).resolve().parents[1]
ASSETS = Path.home() / ".cursor/projects/Users-luke-gumbleton-Documents-Azure-Github-Star-Wars/assets"
MANIFEST = SCRIPTS / "wars_conflicts_hero_manifest.json"
WIDTH, HEIGHT = 1536, 1024

JEDI_PURGE_GALLERY = [
    ("jedi-purge-temple-assault.webp", "wars-conflicts/battles/jedi-purge-temple-assault.webp"),
    ("jedi-purge-order-66-felucia.webp", "wars-conflicts/battles/jedi-purge-order-66-felucia.webp"),
    ("jedi-purge-kashyyyk.webp", "wars-conflicts/battles/jedi-purge-kashyyyk.webp"),
    ("jedi-purge-mustafar-duel.webp", "wars-conflicts/battles/jedi-purge-mustafar-duel.webp"),
    ("jedi-purge-younglings.webp", "wars-conflicts/battles/jedi-purge-younglings.webp"),
    ("jedi-purge-survivors.webp", "wars-conflicts/battles/jedi-purge-survivors.webp"),
    ("jedi-purge-inquisitors.webp", "wars-conflicts/battles/jedi-purge-inquisitors.webp"),
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


def upload_bytes(blob_service, container: str, blob_name: str, payload: bytes) -> None:
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


def blob_name_for_item(item: dict[str, str]) -> str:
    if item["category"] == "battle":
        return f"wars-conflicts/battles/{item['slug']}-hero.webp"
    return f"wars-conflicts/{item['slug']}-hero.webp"


def find_source(item: dict[str, str]) -> Path | None:
    slug = item["slug"]
    names: list[str] = [item["filename"]]
    if item["category"] == "battle":
        names.extend(
            [
                f"battles-{slug}-hero.webp",
                f"{slug}-hero.webp",
                f"battle-of-{slug}-hero.webp",
            ]
        )
    else:
        names.extend([f"wars-{slug}-hero.webp", f"{slug}-hero.webp"])

    for name in names:
        base = name.replace(".webp", "")
        for ext in (".webp", ".png", ".jpg", ".jpeg", ""):
            candidate = ASSETS / (base + ext if ext else name)
            if candidate.is_file():
                return candidate

    for candidate in sorted(ASSETS.glob(f"*{slug}*")):
        if candidate.suffix.lower() in {".webp", ".png", ".jpg", ".jpeg"} and "hero" in candidate.name.lower():
            return candidate
    return None


def find_gallery_source(filename: str) -> Path | None:
    for name in (filename, filename.replace(".webp", ".png")):
        candidate = ASSETS / name
        if candidate.is_file():
            return candidate
    stem = Path(filename).stem
    matches = [p for p in ASSETS.glob(f"{stem}*") if p.suffix.lower() in {".webp", ".png", ".jpg"}]
    return max(matches, key=lambda p: p.stat().st_mtime) if matches else None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--account", default="ststarwars")
    parser.add_argument("--container", default="images")
    parser.add_argument("--slug", action="append", help="Only upload these slugs")
    parser.add_argument("--include-gallery", action="store_true", default=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    export_manifest()
    items: list[dict[str, str]] = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if args.slug:
        wanted = set(args.slug)
        items = [item for item in items if item["slug"] in wanted]

    try:
        from azure.storage.blob import BlobServiceClient
    except ImportError:
        print("Install azure-storage-blob: pip install azure-storage-blob", file=sys.stderr)
        return 1

    if args.dry_run:
        missing = [item["slug"] for item in items if not find_source(item)]
        present = len(items) - len(missing)
        print(f"Would upload {present}/{len(items)} war/battle heroes")
        if missing:
            print(f"Missing assets ({len(missing)}):")
            for slug in missing[:30]:
                print(f"  {slug}")
        return 1 if missing else 0

    blob_service = BlobServiceClient.from_connection_string(get_connection_string(args.account))
    uploaded = 0
    missing: list[str] = []

    for item in items:
        source = find_source(item)
        blob = blob_name_for_item(item)
        if source is None:
            missing.append(item["slug"])
            continue
        payload = to_webp_bytes(source)
        upload_bytes(blob_service, args.container, blob, payload)
        uploaded += 1
        print(f"Uploaded {blob} ({len(payload):,} bytes) from {source.name}")

    if args.include_gallery and not args.slug:
        for filename, blob in JEDI_PURGE_GALLERY:
            source = find_gallery_source(filename)
            if source is None:
                print(f"WARN: gallery asset missing: {filename}", file=sys.stderr)
                continue
            payload = to_webp_bytes(source)
            upload_bytes(blob_service, args.container, blob, payload)
            uploaded += 1
            print(f"Uploaded {blob} from {source.name}")

    print(f"\nDone: {uploaded} blobs uploaded")
    if missing:
        print(f"Missing AI assets for {len(missing)} entries — generate before upload:")
        for slug in missing:
            print(f"  {slug}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
