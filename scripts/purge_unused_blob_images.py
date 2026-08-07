#!/usr/bin/env python3
"""Delete Azure Blob images that are not referenced anywhere in the Star Wars app."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

from verify_blob_images import blob_rel, collect_paths, load_base_url


def get_connection_string(account: str) -> str:
    result = subprocess.run(
        ["az", "storage", "account", "show-connection-string", "--name", account, "-o", "tsv"],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def list_blobs(blob_service, container: str) -> list[str]:
    container_client = blob_service.get_container_client(container)
    return [blob.name for blob in container_client.list_blobs()]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--account", default="ststarwars")
    parser.add_argument("--container", default="images")
    parser.add_argument("--prefix", default="", help="Only purge blobs under this prefix")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    referenced = {blob_rel(path) for path in collect_paths()}
    # Lightsaber glow GIFs and other runtime assets
    referenced.update(
        {
            "lightsaber-glow/blue.gif",
            "lightsaber-glow/green.gif",
            "lightsaber-glow/purple.gif",
            "lightsaber-glow/red.gif",
            "lightsaber-glow/white.gif",
            "lightsaber-glow/yellow.gif",
        }
    )

    try:
        from azure.storage.blob import BlobServiceClient
    except ImportError:
        print("Install azure-storage-blob", file=sys.stderr)
        return 1

    blob_service = BlobServiceClient.from_connection_string(get_connection_string(args.account))
    blobs = list_blobs(blob_service, args.container)
    if args.prefix:
        blobs = [name for name in blobs if name.startswith(args.prefix)]

    unused = sorted(name for name in blobs if name not in referenced)
    print(f"Referenced paths: {len(referenced)}")
    print(f"Blobs scanned: {len(blobs)}")
    print(f"Unused blobs: {len(unused)}")

    if args.dry_run:
        for name in unused[:50]:
            print(f"  would delete {name}")
        if len(unused) > 50:
            print(f"  ... and {len(unused) - 50} more")
        return 0

    deleted = 0
    for name in unused:
        blob_service.get_blob_client(args.container, name).delete_blob()
        deleted += 1
        if deleted % 100 == 0:
            print(f"  deleted {deleted}/{len(unused)}...")
    print(f"Deleted {deleted} unused blobs from {args.container}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
