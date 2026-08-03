#!/usr/bin/env python3
"""Convert hero PNG from Cursor assets and upload to Azure Blob Storage."""

from __future__ import annotations

import argparse
import io
import subprocess
import sys
from pathlib import Path

WIDTH, HEIGHT = 1536, 1024
ASSETS = (
    Path.home()
    / ".cursor/projects/Users-luke-gumbleton-Documents-Azure-Github-Star-Wars/assets"
)


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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slug", help="Entity slug, e.g. yoda")
    parser.add_argument("--category", default="jedi")
    parser.add_argument("--account", default="ststarwars")
    parser.add_argument("--container", default="images")
    parser.add_argument("--source", help="Override source file path")
    args = parser.parse_args()

    source = Path(args.source) if args.source else ASSETS / f"{args.slug}.png"
    if not source.is_file():
        for ext in (".webp", ".png", ".jpg", ".jpeg"):
            candidate = ASSETS / f"{args.slug}{ext}"
            if candidate.is_file():
                source = candidate
                break

    if not source.is_file():
        print(f"Source not found for slug {args.slug}", file=sys.stderr)
        return 1

    try:
        from azure.storage.blob import BlobServiceClient
    except ImportError:
        print("Install azure-storage-blob", file=sys.stderr)
        return 1

    payload = to_webp_bytes(source)
    blob_service = BlobServiceClient.from_connection_string(get_connection_string(args.account))

    blobs = [
        f"{args.category}/{args.slug}.webp",
        f"{args.category}/{args.slug}-scene.webp",
    ]
    for blob_name in blobs:
        upload(blob_service, args.container, blob_name, payload)
        print(f"Uploaded {blob_name} ({len(payload):,} bytes) from {source.name}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
