#!/usr/bin/env python3
"""Verify referenced /images/ paths exist in Azure Blob Storage."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "Data"
PROFILES = ROOT / "wwwroot" / "data" / "profiles"
APPSettings = ROOT / "wwwroot" / "appsettings.json"

ROUTE_PATTERN = re.compile(r'Route\s*=\s*"([^"]+)"')
IMAGE_PATH_PATTERN = re.compile(r'"/images/[^"]+"|\'/images/[^\']+\'')
GALLERY_PATH_PATTERN = re.compile(r'"path"\s*:\s*"(/images/[^"]+)"')


def load_base_url() -> str:
    settings = json.loads(APPSettings.read_text(encoding="utf-8"))
    return settings["ImageBaseUrl"].rstrip("/")


def collect_paths() -> set[str]:
    paths: set[str] = set()
    scan_roots = [ROOT / "Data", ROOT / "Pages", ROOT / "Components", ROOT / "Models", ROOT / "wwwroot"]
    literal_pattern = re.compile(r'(/images/[^"\']+)')

    for scan_root in scan_roots:
        if not scan_root.exists():
            continue
        for file_path in scan_root.rglob("*"):
            if file_path.suffix.lower() not in {".cs", ".razor", ".json"}:
                continue
            if file_path.name == "CrossLinkImageResolver.cs":
                continue
            text = file_path.read_text(encoding="utf-8", errors="ignore")
            for match in literal_pattern.finditer(text):
                path = match.group(1)
                if "{" in path or "}" in path:
                    continue
                paths.add(path)

    for file_path in DATA.glob("*.cs"):
        if file_path.name == "CrossLinkImageResolver.cs":
            continue
        text = file_path.read_text(encoding="utf-8")
        for match in IMAGE_PATH_PATTERN.finditer(text):
            path = match.group(0).strip("\"'")
            if "{" in path or "}" in path:
                continue
            paths.add(path)
        if file_path.name == "GalaxyData.cs":
            for match in re.finditer(r'ImagePath\s*=\s*"([^"]+)"', text):
                paths.add(match.group(1))

    resolver = (DATA / "CrossLinkImageResolver.cs").read_text(encoding="utf-8")
    for match in re.finditer(r'=\s*"(/images/[^"]+)"', resolver):
        paths.add(match.group(1))

    for profile_path in PROFILES.rglob("*.json"):
        payload = profile_path.read_text(encoding="utf-8")
        for match in GALLERY_PATH_PATTERN.finditer(payload):
            paths.add(match.group(1))

    from parse_csharp_data import (
        all_directory_entries,
        load_characters,
        load_factions,
        load_planets,
    )

    category_image_patterns: dict[str, tuple[str, ...]] = {
        "jedi": ("/images/jedi/{slug}.webp", "/images/jedi/{slug}-scene.webp"),
        "sith": ("/images/sith/{slug}.webp", "/images/sith/{slug}-scene.webp"),
        "ships": ("/images/ships/{slug}.webp", "/images/ships/{slug}-scene.webp"),
        "species": ("/images/species/{slug}.webp", "/images/species/{slug}-scene.webp"),
        "bounty-hunters": (
            "/images/bounty-hunters/{slug}.webp",
            "/images/bounty-hunters/{slug}-scene.webp",
        ),
        "settlements": (
            "/images/settlements/{slug}.webp",
            "/images/settlements/{slug}-scene.webp",
        ),
        "force-powers": (
            "/images/force-powers/{slug}.webp",
            "/images/force-powers/{slug}-scene.webp",
        ),
        "droids": ("/images/droids/{slug}.webp", "/images/droids/{slug}-scene.webp"),
    }

    for category, patterns in category_image_patterns.items():
        for entry in all_directory_entries().get(category, []):
            slug = entry["slug"]
            for pattern in patterns:
                paths.add(pattern.format(slug=slug))

    for entry in load_characters():
        slug = entry["slug"]
        paths.add(f"/images/characters/{slug}.webp")
        paths.add(f"/images/characters/{slug}-scene.webp")

    for entry in load_factions():
        slug = entry["slug"]
        paths.add(f"/images/factions/{slug}.svg")
        paths.add(f"/images/factions/{slug}-scene.webp")

    for entry in load_planets():
        slug = entry["slug"]
        paths.add(f"/images/planets/{slug}-hero.webp")
        paths.add(f"/images/planets/{slug}-space.webp")
        if entry.get("imagepath"):
            paths.add(entry["imagepath"])

    def slugs_from(filename: str) -> list[str]:
        path = DATA / filename
        if not path.is_file():
            return []
        return re.findall(r'Slug = "([^"]+)"', path.read_text(encoding="utf-8"))

    for org_slug in slugs_from("OrganizationData.cs"):
        paths.add(f"/images/organizations/{org_slug}.webp")
        paths.add(f"/images/organizations/{org_slug}-scene.webp")

    for creature_slug in slugs_from("CreatureData.cs"):
        paths.add(f"/images/creatures/{creature_slug}.webp")
        paths.add(f"/images/creatures/{creature_slug}-scene.webp")

    for gov_slug in slugs_from("GovernmentData.cs"):
        paths.add(f"/images/governments/{gov_slug}-scene.webp")

    for chronicle_slug in slugs_from("ChroniclesData.cs"):
        paths.add(f"/images/chronicles/{chronicle_slug}-scene.webp")

    for topic_slug in slugs_from("TheForceTopicData.cs"):
        paths.add(f"/images/the-force/{topic_slug}-hero.webp")

    for form_slug in slugs_from("LightsaberFormData.cs"):
        paths.add(f"/images/the-force/lightsaber-forms/{form_slug}-hero.webp")

    military_text = (DATA / "MilitaryUnitData.cs").read_text(encoding="utf-8")
    for faction_slug in re.findall(r'Slug = "([^"]+)"', military_text):
        paths.add(f"/images/military-units/{faction_slug}-army-hero.webp")
        paths.add(f"/images/military-units/{faction_slug}-navy-hero.webp")
        paths.add(f"/images/military-units/{faction_slug}-faction-hero.webp")

    branch_map = {"Army": "army", "Navy": "navy"}
    catalog_path = DATA / "MilitaryUnitCatalog.cs"
    if catalog_path.is_file():
        catalog_text = catalog_path.read_text(encoding="utf-8")
        faction_slugs: set[str] = set()
        for match in re.finditer(
            r'Unit\("([^"]+)",\s*MilitaryUnitBranch\.(\w+),\s*"([^"]+)"',
            catalog_text,
        ):
            faction_slug, branch, unit_slug = match.groups()
            branch_slug = branch_map.get(branch, branch.lower())
            faction_slugs.add(faction_slug)
            paths.add(f"/images/military-units/{faction_slug}-{branch_slug}-{unit_slug}-hero.webp")
        for faction_slug in faction_slugs:
            paths.add(f"/images/military-units/{faction_slug}-army-hero.webp")
            paths.add(f"/images/military-units/{faction_slug}-navy-hero.webp")
            paths.add(f"/images/military-units/{faction_slug}-faction-hero.webp")

    vehicle_path = DATA / "VehicleData.cs"
    if vehicle_path.is_file():
        vehicle_text = vehicle_path.read_text(encoding="utf-8")
        type_map = {"Ground": "ground", "Air": "air"}
        blocks = re.findall(r"new\(\)\s*\{(.*?)\}", vehicle_text, re.DOTALL)
        for block in blocks:
            slug_match = re.search(r'Slug = "([^"]+)"', block)
            faction_match = re.search(r'FactionSlug = "([^"]+)"', block)
            type_match = re.search(r"Type = MilitaryVehicleType\.(\w+)", block)
            if not slug_match or not faction_match or not type_match:
                continue
            type_slug = type_map.get(type_match.group(1), type_match.group(1).lower())
            paths.add(
                f"/images/military-vehicles/{faction_match.group(1)}-{type_slug}-{slug_match.group(1)}-hero.webp"
            )

    battle_text = (DATA / "BattleData.cs").read_text(encoding="utf-8")
    for slug in re.findall(r'Battle\("[^"]+", "([^"]+)"', battle_text):
        paths.add(f"/images/wars-conflicts/battles/{slug}-hero.webp")

    war_text = (DATA / "WarConflictData.cs").read_text(encoding="utf-8")
    for slug in re.findall(r'Slug = "([^"]+)"', war_text):
        paths.add(f"/images/wars-conflicts/{slug}-hero.webp")
    paths.add("/images/wars-conflicts/wars-conflicts-directory-hero.webp")

    # Jedi Purge gallery scenes referenced in battle profile
    jedi_purge_gallery = [
        "jedi-purge-temple-assault.webp",
        "jedi-purge-order-66-felucia.webp",
        "jedi-purge-kashyyyk.webp",
        "jedi-purge-mustafar-duel.webp",
        "jedi-purge-younglings.webp",
        "jedi-purge-survivors.webp",
        "jedi-purge-inquisitors.webp",
    ]
    for filename in jedi_purge_gallery:
        paths.add(f"/images/wars-conflicts/battles/{filename}")

    return paths


def blob_rel(path: str) -> str:
    path = path.strip()
    if path.startswith("/images/"):
        return path[len("/images/") :]
    if path.startswith("images/"):
        return path[len("images/") :]
    return path.lstrip("/")


def head_exists(base_url: str, rel: str) -> bool:
    url = f"{base_url}/{rel}"
    result = subprocess.run(
        ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", url],
        capture_output=True,
        text=True,
        check=False,
    )
    return result.stdout.strip() == "200"


def main() -> int:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    base_url = load_base_url()
    paths = sorted(collect_paths())
    print(f"Checking {len(paths)} referenced image paths against {base_url}")

    missing: list[str] = []
    with ThreadPoolExecutor(max_workers=24) as pool:
        futures = {pool.submit(head_exists, base_url, blob_rel(path)): path for path in paths}
        for future in as_completed(futures):
            path = futures[future]
            if not future.result():
                missing.append(path)

    missing.sort()
    print(f"Missing: {len(missing)}")
    for path in missing[:40]:
        print(f"  {path}")
    if len(missing) > 40:
        print(f"  ... and {len(missing) - 40} more")

    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
