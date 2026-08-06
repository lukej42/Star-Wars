#!/usr/bin/env python3
"""Append Related Archives cross-links for organizations, creatures, and military vehicles."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from parse_csharp_data import load_category, load_planets, normalize

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "wwwroot" / "data" / "cross-links.json"

VEHICLE_TYPE = re.compile(r"Type = MilitaryVehicleType\.(\w+)")

FACTION_LABELS: dict[str, tuple[str, str, str]] = {
    "confederacy": ("Faction", "Confederacy of Independent Systems", "factions/confederacy"),
    "empire": ("Faction", "Galactic Empire", "factions/empire"),
    "galactic-republic": ("Faction", "Galactic Republic", "factions/republic"),
    "confederacy-of-independent-systems": (
        "Faction",
        "Confederacy of Independent Systems",
        "factions/confederacy",
    ),
    "galactic-empire": ("Faction", "Galactic Empire", "factions/empire"),
    "rebel-alliance": ("Faction", "Rebel Alliance", "factions/rebel-alliance"),
    "first-order": ("Faction", "First Order", "factions/first-order"),
    "resistance": ("Faction", "Resistance", "factions/resistance"),
    "mandalorian": ("Faction", "Mandalorians", "factions/mandalorians"),
    "sith-empire": ("Faction", "Sith Empire", "factions/sith-empire"),
}

ORG_LINKS: dict[str, list[tuple[str, str, str]]] = {
    "techno-union": [
        ("Battle", "First Battle of Geonosis", "wars-conflicts/battles/first-battle-of-geonosis"),
        ("Planet", "Muunilinst", "planet/muunilinst"),
    ],
    "intergalactic-banking-clan": [
        ("Battle", "Battle of Muunilinst", "wars-conflicts/battles/battle-of-muunilinst"),
        ("Planet", "Muunilinst", "planet/muunilinst"),
    ],
    "commerce-guild": [
        ("Planet", "Castell", "planet/castell"),
        ("Battle", "First Battle of Geonosis", "wars-conflicts/battles/first-battle-of-geonosis"),
    ],
    "corporate-alliance": [
        ("Battle", "First Battle of Geonosis", "wars-conflicts/battles/first-battle-of-geonosis"),
    ],
    "retail-caucus": [
        ("Battle", "First Battle of Geonosis", "wars-conflicts/battles/first-battle-of-geonosis"),
    ],
    "pyke-syndicate": [
        ("Military unit", "Pyke Syndicate Forces", "military-units/other/army/pyke-syndicate-forces"),
        ("Planet", "Oba Diah", "planet/oba-diah"),
        ("Settlement", "Kessel", "settlements/kessel"),
        ("Bounty hunter", "Cad Bane", "bounty-hunters/cad-bane"),
    ],
    "black-sun": [
        ("Settlement", "Nar Shaddaa", "settlements/nar-shaddaa"),
        ("Planet", "Mustafar", "planet/mustafar"),
        ("Bounty hunter", "Boba Fett", "bounty-hunters/boba-fett"),
    ],
    "crimson-dawn": [
        ("Planet", "Corellia", "planet/corellia"),
        ("Character", "Qi'ra", "characters/qira"),
    ],
    "inquisitorius": [
        ("Directory", "Sith Order", "all-sith"),
        ("Force power", "Force Lightning", "force-powers/force-lightning"),
    ],
    "mining-guild": [
        ("Faction", "Galactic Empire", "factions/empire"),
    ],
    "smuggler-guilds": [
        ("Directory", "Bounty Hunters", "all-bounty-hunters"),
        ("Settlement", "Nar Shaddaa", "settlements/nar-shaddaa"),
    ],
    "corporate-blocs": [
        ("Faction", "Trade Federation", "factions/trade-federation"),
    ],
    "crime-families": [
        ("Faction", "Hutts", "factions/hutts"),
        ("Planet", "Nal Hutta", "planet/nal-hutta"),
    ],
    "spice-runners-guild": [
        ("Organization", "Smuggler Guilds", "organizations/smuggler-guilds"),
        ("Settlement", "Kessel", "settlements/kessel"),
    ],
    "corellian-smuggler-guild": [
        ("Organization", "Smuggler Guilds", "organizations/smuggler-guilds"),
        ("Planet", "Corellia", "planet/corellia"),
    ],
    "hutt-smuggling-rings": [
        ("Organization", "Smuggler Guilds", "organizations/smuggler-guilds"),
        ("Faction", "Hutts", "factions/hutts"),
    ],
    "desilijic-kajidic": [
        ("Organization", "Crime Families", "organizations/crime-families"),
        ("Planet", "Tatooine", "planet/tatooine"),
        ("Character", "Jabba the Hutt", "characters/jabba-the-hutt"),
    ],
    "besadii-kajidic": [
        ("Organization", "Crime Families", "organizations/crime-families"),
        ("Planet", "Nal Hutta", "planet/nal-hutta"),
    ],
    "black-sun-vigo-council": [
        ("Organization", "Crime Families", "organizations/crime-families"),
        ("Organization", "Black Sun", "organizations/black-sun"),
    ],
    "trade-federation-directorate": [
        ("Organization", "Corporate Blocs", "organizations/corporate-blocs"),
        ("Faction", "Trade Federation", "factions/trade-federation"),
    ],
    "intergalactic-banking-holding": [
        ("Organization", "Corporate Blocs", "organizations/corporate-blocs"),
        ("Organization", "InterGalactic Banking Clan", "organizations/intergalactic-banking-clan"),
    ],
}

CREATURE_LINKS: dict[str, list[tuple[str, str, str]]] = {
    "rancor": [
        ("Character", "Jabba the Hutt", "characters/jabba-the-hutt"),
        ("Organization", "Desilijic Kajidic", "organizations/desilijic-kajidic"),
    ],
    "wampa": [
        ("Battle", "Battle of Hoth", "wars-conflicts/battles/battle-of-hoth"),
        ("Character", "Luke Skywalker", "characters/luke-skywalker"),
    ],
    "sarlacc": [
        ("Character", "Boba Fett", "bounty-hunters/boba-fett"),
        ("Character", "Han Solo", "characters/han-solo"),
    ],
    "krayt-dragon": [
        ("Character", "Obi-Wan Kenobi", "characters/obi-wan-kenobi"),
    ],
    "purrgil": [
        ("Character", "Ezra Bridger", "characters/ezra-bridger"),
        ("The Force", "World Between Worlds", "the-force/world-between-worlds"),
    ],
    "loth-wolf": [
        ("Character", "Ezra Bridger", "characters/ezra-bridger"),
        ("The Force", "The Living Force", "the-force/the-living-force"),
    ],
    "convor": [
        ("Character", "Ahsoka Tano", "characters/ahsoka-tano"),
        ("The Force", "Mortis Gods", "the-force/mortis-gods"),
    ],
    "zillo-beast": [
        ("Character", "Palpatine", "characters/sheev-palpatine"),
        ("Planet", "Coruscant", "planet/coruscant"),
    ],
    "nexu": [
        ("Battle", "First Battle of Geonosis", "wars-conflicts/battles/first-battle-of-geonosis"),
    ],
    "reek": [
        ("Battle", "First Battle of Geonosis", "wars-conflicts/battles/first-battle-of-geonosis"),
        ("Character", "Anakin Skywalker", "characters/anakin-skywalker"),
    ],
    "acklay": [
        ("Battle", "First Battle of Geonosis", "wars-conflicts/battles/first-battle-of-geonosis"),
    ],
    "tauntaun": [
        ("Battle", "Battle of Hoth", "wars-conflicts/battles/battle-of-hoth"),
    ],
    "dewback": [
        ("Faction", "Galactic Empire", "factions/empire"),
    ],
    "bantha": [
        ("Species", "Tusken Raider", "species/tusken-raider"),
    ],
    "rathtar": [
        ("Character", "Han Solo", "characters/han-solo"),
    ],
    "mudhorn": [
        ("Character", "Din Djarin", "characters/din-djarin"),
        ("Character", "Grogu", "characters/grogu"),
    ],
    "varactyl": [
        ("Character", "Obi-Wan Kenobi", "characters/obi-wan-kenobi"),
        ("Character", "General Grievous", "characters/general-grievous"),
    ],
    "exogorth": [
        ("Character", "Han Solo", "characters/han-solo"),
        ("Planet", "Hoth", "planet/hoth"),
    ],
    "dark-side-spiders": [
        ("The Force", "Dark Side of the Force", "the-force/dark-side-of-the-force"),
        ("Planet", "Malachor", "planet/malachor"),
    ],
    "vornskr": [
        ("The Force", "Force Sense", "force-powers/force-sense"),
    ],
    "falumpaset": [
        ("Battle", "Battle of Naboo", "wars-conflicts/battles/battle-of-naboo"),
    ],
    "kaadu": [
        ("Battle", "Battle of Naboo", "wars-conflicts/battles/battle-of-naboo"),
    ],
    "dianoga": [
        ("Ship", "Death Star", "ships/death-star"),
    ],
    "kowakian-monkey-lizard": [
        ("Character", "Jabba the Hutt", "characters/jabba-the-hutt"),
    ],
    "porg": [
        ("Character", "Luke Skywalker", "characters/luke-skywalker"),
        ("Planet", "Ahch-To", "planet/ahch-to"),
    ],
    "vulptex": [
        ("Battle", "Battle of Crait", "wars-conflicts/battles/battle-of-crait"),
    ],
    "ice-spider": [
        ("The Force", "Kyber Crystals", "the-force/kyber-crystals"),
    ],
}

VEHICLE_BATTLE_LINKS: dict[str, tuple[str, str, str]] = {
    "at-te": ("Battle", "First Battle of Geonosis", "wars-conflicts/battles/first-battle-of-geonosis"),
    "at-rt": ("Battle", "First Battle of Geonosis", "wars-conflicts/battles/first-battle-of-geonosis"),
    "laat-i": ("Battle", "First Battle of Geonosis", "wars-conflicts/battles/first-battle-of-geonosis"),
    "mtt": ("Battle", "Battle of Naboo", "wars-conflicts/battles/battle-of-naboo"),
    "aat": ("Battle", "Battle of Felucia", "wars-conflicts/battles/battle-of-felucia"),
    "vulture-droid": ("Battle", "Battle of Coruscant", "wars-conflicts/battles/battle-of-coruscant"),
    "at-at": ("Battle", "Battle of Hoth", "wars-conflicts/battles/battle-of-hoth"),
    "at-st": ("Battle", "Battle of Endor", "wars-conflicts/battles/battle-of-endor"),
    "tie-fighter": ("Battle", "Battle of Yavin", "wars-conflicts/battles/battle-of-yavin"),
    "snowspeeder": ("Battle", "Battle of Hoth", "wars-conflicts/battles/battle-of-hoth"),
    "x-wing": ("Battle", "Battle of Yavin", "wars-conflicts/battles/battle-of-yavin"),
    "u-wing": ("Battle", "Battle of Scarif", "wars-conflicts/battles/battle-of-scarif"),
    "at-m6": ("Battle", "Battle of Crait", "wars-conflicts/battles/battle-of-crait"),
    "v-4x-d-ski-speeder": ("Battle", "Battle of Crait", "wars-conflicts/battles/battle-of-crait"),
    "t-70-x-wing": ("Battle", "Battle of Starkiller Base", "wars-conflicts/battles/battle-of-starkiller-base"),
    "resistance-bomber": ("Battle", "Battle of D'Qar", "wars-conflicts/battles/battle-of-d-qar"),
    "komrk-fighter-transport": ("Character", "Bo-Katan Kryze", "characters/bo-katan-kryze"),
}


def link(label: str, value: str, route: str) -> dict[str, str]:
    return {"label": label, "value": value, "route": route}


def dedupe_links(links: list[dict[str, str]]) -> list[dict[str, str]]:
    seen: set[str] = set()
    out: list[dict[str, str]] = []
    for item in links:
        route = item["route"]
        if route in seen:
            continue
        seen.add(route)
        out.append(item)
    return out


def planet_route(name: str, planets: list[dict[str, str]]) -> tuple[str, str] | None:
    normalized = name.lower().strip()
    aliases = {
        "unknown regions": "ilum",
        "asteroid fields": "hoth",
        "various": "tatooine",
    }
    slug_hint = aliases.get(normalized, normalized.replace(" ", "-"))
    for planet in planets:
        if planet["slug"] == slug_hint or planet["name"].lower() == normalized:
            return planet["name"], planet["route"]
    for planet in planets:
        if normalized in planet["name"].lower() or planet["name"].lower() in normalized:
            return planet["name"], planet["route"]
    return None


def load_organizations() -> list[dict[str, str]]:
    return [normalize(entry) for entry in load_category("OrganizationData.cs")]


def load_creatures() -> list[dict[str, str]]:
    return [normalize(entry) for entry in load_category("CreatureData.cs")]


def load_vehicles() -> list[dict[str, str]]:
    text = (ROOT / "Data" / "VehicleData.cs").read_text(encoding="utf-8")
    vehicles: list[dict[str, str]] = []
    for block in re.findall(r"new\(\)\s*\{(.*?)\}", text, re.DOTALL):
        entry: dict[str, str] = {}
        for match in re.finditer(r'(\w+) = "(.*?)"', block):
            key = match.group(1)
            entry[key[0].lower() + key[1:]] = match.group(2)
        type_match = VEHICLE_TYPE.search(block)
        if type_match and "slug" in entry:
            entry["type"] = type_match.group(1).lower()
            vehicles.append(entry)
    return vehicles


def military_unit_name(faction_slug: str) -> str:
    names = {
        "galactic-republic": "Galactic Republic Military Units",
        "confederacy-of-independent-systems": "Confederacy Military Units",
        "galactic-empire": "Imperial Military Units",
        "rebel-alliance": "Rebel Alliance Military Units",
        "first-order": "First Order Military Units",
        "resistance": "Resistance Military Units",
        "mandalorian": "Mandalorian Military Units",
        "sith-empire": "Sith Empire Military Units",
    }
    return names.get(faction_slug, "Military Units")


def build_organization_links(org: dict[str, str]) -> list[dict[str, str]]:
    slug = org["slug"]
    links = [link(*item) for item in ORG_LINKS.get(slug, [])]

    parent_faction = org.get("parentFactionSlug")
    if parent_faction and parent_faction in FACTION_LABELS:
        label, value, route = FACTION_LABELS[parent_faction]
        links.insert(0, link(label, value, route))

    parent_org = org.get("parentOrganizationSlug")
    if parent_org:
        parent = next((item for item in load_organizations() if item["slug"] == parent_org), None)
        if parent:
            links.append(link("Organization", parent["name"], parent["route"]))

    return dedupe_links(links)


def build_creature_links(creature: dict[str, str], planets: list[dict[str, str]]) -> list[dict[str, str]]:
    slug = creature["slug"]
    links = [link(*item) for item in CREATURE_LINKS.get(slug, [])]

    homeworld = creature.get("homeworld", "")
    if homeworld and homeworld.lower() not in {"unknown", "various"}:
        resolved = planet_route(homeworld, planets)
        if resolved:
            name, route = resolved
            links.insert(0, link("Planet", name, route))

    habitat = creature.get("habitat", "")
    if "Dark Side" in habitat:
        links.append(link("The Force", "Dark Side of the Force", "the-force/dark-side-of-the-force"))
    if habitat == "Space & Vacuum":
        links.append(link("Directory", "All Ships", "all-ships"))

    return dedupe_links(links)


def build_vehicle_links(vehicle: dict[str, str]) -> tuple[list[dict[str, str]], str]:
    faction_slug = vehicle["factionSlug"]
    type_slug = "ground" if vehicle["type"] == "ground" else "air"
    slug = vehicle["slug"]
    cross_slug = f"{faction_slug}/{type_slug}/{slug}"

    links: list[dict[str, str]] = [
        link("Military unit", military_unit_name(faction_slug), f"military-units/{faction_slug}")
    ]

    if faction_slug in FACTION_LABELS:
        _, value, route = FACTION_LABELS[faction_slug]
        links.append(link("Faction", value, route))

    battle = VEHICLE_BATTLE_LINKS.get(slug)
    if battle:
        links.append(link(*battle))

    return dedupe_links(links), cross_slug


def merge_entries(existing: list[dict], category: str, slug: str, new_links: list[dict[str, str]]) -> None:
    for entry in existing:
        if entry["category"] == category and entry["slug"] == slug:
            entry["links"] = dedupe_links(entry.get("links", []) + new_links)
            return
    existing.append({"category": category, "slug": slug, "links": new_links})


def main() -> None:
    planets = load_planets()
    organizations = load_organizations()
    creatures = load_creatures()
    vehicles = load_vehicles()

    entries = json.loads(OUTPUT.read_text(encoding="utf-8"))

    for org in organizations:
        merge_entries(entries, "organizations", org["slug"], build_organization_links(org))

    for creature in creatures:
        merge_entries(entries, "creatures", creature["slug"], build_creature_links(creature, planets))

    for vehicle in vehicles:
        vehicle_links, cross_slug = build_vehicle_links(vehicle)
        merge_entries(entries, "military-vehicles", cross_slug, vehicle_links)

    OUTPUT.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Appended extended cross-links to {OUTPUT}")
    print(f"  organizations: {len(organizations)}")
    print(f"  creatures: {len(creatures)}")
    print(f"  military-vehicles: {len(vehicles)}")
    print(f"  total entries: {len(entries)}")


if __name__ == "__main__":
    main()
