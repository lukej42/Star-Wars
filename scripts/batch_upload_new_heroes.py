#!/usr/bin/env python3
"""Batch-convert generated hero assets to 1536x1024 webp and upload to Azure Blob Storage."""

from __future__ import annotations

import argparse
import io
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

WIDTH, HEIGHT = 1536, 1024
ASSETS = (
    Path.home()
    / ".cursor/projects/Users-luke-gumbleton-Documents-Azure-Github-Star-Wars/assets"
)


@dataclass(frozen=True)
class HeroSpec:
    slug: str
    category: str
    blob_names: tuple[str, ...]
    source_ext: str = ".png"


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


def find_source(slug: str, ext: str) -> Path | None:
    for candidate in (ASSETS / f"{slug}{ext}", ASSETS / f"{slug}.png", ASSETS / f"{slug}.webp"):
        if candidate.is_file():
            return candidate
    return None


def org_spec(slug: str) -> HeroSpec:
    return HeroSpec(
        slug=slug,
        category="organizations",
        blob_names=(f"organizations/{slug}.webp", f"organizations/{slug}-scene.webp"),
    )


def creature_spec(slug: str) -> HeroSpec:
    return HeroSpec(
        slug=slug,
        category="creatures",
        blob_names=(f"creatures/{slug}-scene.webp",),
    )


def vehicle_spec(faction: str, type_slug: str, slug: str) -> HeroSpec:
    name = f"{faction}-{type_slug}-{slug}"
    return HeroSpec(
        slug=name,
        category="military-vehicles",
        blob_names=(f"military-vehicles/{name}-hero.webp",),
    )


HERO_SPECS: list[HeroSpec] = [
    org_spec("organizations-directory-hero"),
    org_spec("techno-union"),
    org_spec("intergalactic-banking-clan"),
    org_spec("commerce-guild"),
    org_spec("corporate-alliance"),
    org_spec("retail-caucus"),
    org_spec("pyke-syndicate"),
    org_spec("black-sun"),
    org_spec("crimson-dawn"),
    org_spec("inquisitorius"),
    org_spec("mining-guild"),
    org_spec("smuggler-guilds"),
    org_spec("corporate-blocs"),
    org_spec("crime-families"),
    org_spec("spice-runners-guild"),
    org_spec("corellian-smuggler-guild"),
    org_spec("hutt-smuggling-rings"),
    org_spec("desilijic-kajidic"),
    org_spec("besadii-kajidic"),
    org_spec("black-sun-vigo-council"),
    org_spec("trade-federation-directorate"),
    org_spec("intergalactic-banking-holding"),
    creature_spec("creatures-directory-hero"),
    creature_spec("rancor"),
    creature_spec("wampa"),
    creature_spec("purrgil"),
    creature_spec("krayt-dragon"),
    creature_spec("zillo-beast"),
    creature_spec("exogorth"),
    creature_spec("tauntaun"),
    creature_spec("bantha"),
    creature_spec("loth-wolf"),
    creature_spec("mudhorn"),
    creature_spec("sarlacc"),
    creature_spec("nexu"),
    creature_spec("convor"),
    creature_spec("porg"),
    creature_spec("rathtar"),
    creature_spec("blurrg"),
    creature_spec("mynock"),
    creature_spec("colo-claw-fish"),
    creature_spec("varactyl"),
    creature_spec("krykna"),
    vehicle_spec("galactic-empire", "ground", "at-at"),
    vehicle_spec("galactic-empire", "ground", "at-st"),
    vehicle_spec("galactic-empire", "air", "tie-fighter"),
    vehicle_spec("galactic-republic", "ground", "at-te"),
    vehicle_spec("galactic-republic", "air", "laat"),
    vehicle_spec("confederacy-of-independent-systems", "ground", "mtt"),
    vehicle_spec("confederacy-of-independent-systems", "ground", "aat"),
    vehicle_spec("rebel-alliance", "air", "snowspeeder"),
    vehicle_spec("first-order", "ground", "at-m6"),
    vehicle_spec("confederacy-of-independent-systems", "air", "vulture-droid"),
    vehicle_spec("galactic-empire", "air", "tie-bomber"),
    vehicle_spec("galactic-empire", "ground", "at-act"),
    vehicle_spec("galactic-republic", "ground", "juggernaut"),
    vehicle_spec("rebel-alliance", "air", "u-wing"),
    vehicle_spec("first-order", "air", "tie-fo"),
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--account", default="ststarwars")
    parser.add_argument("--container", default="images")
    parser.add_argument("--slug", action="append", help="Upload only these slugs (repeatable)")
    args = parser.parse_args()

    try:
        from azure.storage.blob import BlobServiceClient
    except ImportError:
        print("Install azure-storage-blob: pip install azure-storage-blob", file=sys.stderr)
        return 1

    specs = HERO_SPECS
    if args.slug:
        wanted = set(args.slug)
        specs = [s for s in HERO_SPECS if s.slug in wanted]

    blob_service = BlobServiceClient.from_connection_string(get_connection_string(args.account))
    uploaded = 0
    failures: list[str] = []

    for spec in specs:
        source = find_source(spec.slug, spec.source_ext)
        if source is None:
            failures.append(f"{spec.slug}: source not found in {ASSETS}")
            continue
        try:
            payload = to_webp_bytes(source)
            for blob_name in spec.blob_names:
                upload(blob_service, args.container, blob_name, payload)
                uploaded += 1
                print(f"Uploaded {blob_name} ({len(payload):,} bytes) from {source.name}")
        except Exception as exc:  # noqa: BLE001
            failures.append(f"{spec.slug}: {exc}")

    print(f"\nTotal blobs uploaded: {uploaded}")
    if failures:
        print(f"Failures ({len(failures)}):", file=sys.stderr)
        for item in failures:
            print(f"  - {item}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
