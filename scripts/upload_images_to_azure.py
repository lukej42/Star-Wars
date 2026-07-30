#!/usr/bin/env python3
"""Upload wwwroot/images to Azure Blob Storage (ststarwars/images container)."""

from __future__ import annotations

import argparse
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "wwwroot" / "images"

CONTENT_TYPES = {
    ".webp": "image/webp",
    ".svg": "image/svg+xml",
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
}

SKIP_NAMES = {".DS_Store", ".keep"}


def get_connection_string(account: str) -> str:
    result = subprocess.run(
        ["az", "storage", "account", "show-connection-string", "--name", account, "-o", "tsv"],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def collect_files() -> list[Path]:
    return sorted(
        path
        for path in SOURCE.rglob("*")
        if path.is_file() and path.name not in SKIP_NAMES
    )


def upload_file(blob_service, container: str, path: Path) -> tuple[str, int]:
    from azure.storage.blob import ContentSettings

    rel = path.relative_to(SOURCE).as_posix()
    content_type = CONTENT_TYPES.get(path.suffix.lower(), "application/octet-stream")
    blob_client = blob_service.get_blob_client(container=container, blob=rel)
    with path.open("rb") as handle:
        blob_client.upload_blob(
            handle,
            overwrite=True,
            content_settings=ContentSettings(
                content_type=content_type,
                cache_control="public, max-age=31536000, immutable",
            ),
        )
    return rel, path.stat().st_size


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--account", default="ststarwars")
    parser.add_argument("--container", default="images")
    parser.add_argument("--workers", type=int, default=16)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    files = collect_files()
    total_bytes = sum(path.stat().st_size for path in files)
    print(f"Found {len(files)} files ({total_bytes / 1024 / 1024 / 1024:.2f} GB)")

    if args.dry_run:
        return 0

    try:
        from azure.storage.blob import BlobServiceClient
    except ImportError:
        print("Install azure-storage-blob: pip install azure-storage-blob", file=sys.stderr)
        return 1

    connection_string = get_connection_string(args.account)
    blob_service = BlobServiceClient.from_connection_string(connection_string)

    uploaded = 0
    failed: list[str] = []

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {
            pool.submit(upload_file, blob_service, args.container, path): path for path in files
        }
        for index, future in enumerate(as_completed(futures), start=1):
            path = futures[future]
            try:
                rel, _size = future.result()
                uploaded += 1
                if index % 250 == 0 or index == len(files):
                    print(f"  {index}/{len(files)} uploaded (latest: {rel})")
            except Exception as exc:  # noqa: BLE001
                failed.append(f"{path.relative_to(SOURCE)}: {exc}")

    print(f"Done: {uploaded}/{len(files)} uploaded")
    if failed:
        print(f"Failed: {len(failed)}", file=sys.stderr)
        for line in failed[:20]:
            print(f"  {line}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
