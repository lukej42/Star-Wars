#!/usr/bin/env python3
"""Generate cross-links.json for character, jedi, sith, and droid profile pages."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "Data"
PROFILES = ROOT / "wwwroot" / "data" / "profiles"
OUTPUT = ROOT / "wwwroot" / "data" / "cross-links.json"

ROUTE_PATTERN = re.compile(r'Route\s*=\s*"([^"]+)"')

MANUAL: dict[str, list[dict[str, str]]] = {
    "sith/darth-vader": [
        {"label": "Faction", "value": "Galactic Empire", "route": "factions/empire"},
        {"label": "Planet", "value": "Tatooine", "route": "planet/tatooine"},
        {"label": "Ship", "value": "Executor", "route": "ships/executor-class"},
        {"label": "Force power", "value": "Force Choke", "route": "force-powers/force-choke"},
        {"label": "Force power", "value": "Force Throw", "route": "force-powers/force-throw"},
        {"label": "Lightsaber form", "value": "Form V (Shien/Djem So)", "route": "the-force/lightsaber-forms/shien-djem-so"},
        {"label": "Battle", "value": "Battle of Yavin", "route": "wars-conflicts/battles/battle-of-yavin"},
        {"label": "Species", "value": "Human", "route": "species/human"},
    ],
    "characters/luke-skywalker": [
        {"label": "Faction", "value": "Rebel Alliance", "route": "factions/rebel-alliance"},
        {"label": "Planet", "value": "Tatooine", "route": "planet/tatooine"},
        {"label": "Ship", "value": "X-wing", "route": "ships/x-wing"},
        {"label": "Force power", "value": "Force Heal", "route": "force-powers/force-heal"},
        {"label": "Lightsaber form", "value": "Form V (Shien/Djem So)", "route": "the-force/lightsaber-forms/shien-djem-so"},
        {"label": "Battle", "value": "Battle of Yavin", "route": "wars-conflicts/battles/battle-of-yavin"},
        {"label": "Species", "value": "Human", "route": "species/human"},
    ],
    "jedi/yoda": [
        {"label": "Directory", "value": "Jedi Order", "route": "all-jedi"},
        {"label": "Planet", "value": "Dagobah", "route": "planet/dagobah"},
        {"label": "Force power", "value": "Force Lightning (reflected)", "route": "force-powers/force-lightning"},
        {"label": "Lightsaber form", "value": "Form IV (Ataru)", "route": "the-force/lightsaber-forms/ataru"},
        {"label": "Battle", "value": "First Battle of Geonosis", "route": "wars-conflicts/battles/first-battle-of-geonosis"},
    ],
}

AFFILIATION_ROUTES = {
    "galactic empire": ("Faction", "Galactic Empire", "factions/empire"),
    "imperial navy": ("Military unit", "Imperial Navy", "military-units/galactic-empire/imperial-navy"),
    "501st legion": ("Military unit", "501st Legion", "military-units/galactic-empire/501st-legion"),
    "death star command": ("Military unit", "Imperial Navy", "military-units/galactic-empire/imperial-navy"),
    "rebel alliance": ("Faction", "Rebel Alliance", "factions/rebel-alliance"),
    "alliance to restore the republic": ("Faction", "Rebel Alliance", "factions/rebel-alliance"),
    "jedi order": ("Directory", "Jedi Order", "all-jedi"),
    "jedi high council": ("Directory", "Jedi Order", "all-jedi"),
    "sith order": ("Directory", "Sith Order", "all-sith"),
    "confederacy of independent systems": ("Faction", "Confederacy", "factions/confederacy"),
    "separatist": ("Faction", "Confederacy", "factions/confederacy"),
    "cis": ("Faction", "Confederacy", "factions/confederacy"),
    "galactic republic": ("Faction", "Republic", "factions/republic"),
    "clone trooper corps": ("Military unit", "Clone Trooper Corps", "military-units/galactic-republic/clone-trooper-corps"),
    "first order": ("Faction", "First Order", "factions/first-order"),
    "resistance": ("Faction", "Resistance", "factions/resistance"),
    "new republic": ("Faction", "New Republic", "factions/new-republic"),
    "mandalorian": ("Faction", "Mandalorians", "factions/mandalorians"),
    "mandalorians": ("Faction", "Mandalorians", "factions/mandalorians"),
    "hutt cartel": ("Faction", "Hutts", "factions/hutts"),
    "hutt": ("Faction", "Hutts", "factions/hutts"),
    "trade federation": ("Faction", "Trade Federation", "factions/trade-federation"),
    "sith empire": ("Faction", "Sith Empire", "factions/sith-empire"),
    "bounty hunters guild": ("Directory", "Bounty Hunters", "all-bounty-hunters"),
}

PLANET_SLUGS = {
    "tatooine": "planet/tatooine",
    "coruscant": "planet/coruscant",
    "naboo": "planet/naboo",
    "mustafar": "planet/mustafar",
    "dagobah": "planet/dagobah",
    "hoth": "planet/hoth",
    "endor": "planet/endor",
    "kamino": "planet/kamino",
    "bespin": "bespin",
    "kashyyyk": "planet/kashyyyk",
}

BATTLE_PHRASES = {
    "battle of yavin": ("Battle of Yavin", "wars-conflicts/battles/battle-of-yavin"),
    "battle of hoth": ("Battle of Hoth", "wars-conflicts/battles/battle-of-hoth"),
    "battle of endor": ("Battle of Endor", "wars-conflicts/battles/battle-of-endor"),
    "battle of geonosis": ("First Battle of Geonosis", "wars-conflicts/battles/first-battle-of-geonosis"),
    "cloud city": ("Assault on Cloud City", "wars-conflicts/battles/assault-on-cloud-city"),
    "order 66": ("Clone Wars", "wars-conflicts/clone-wars"),
}

FORCE_POWER_PHRASES = {
    "force choke": ("Force Choke", "force-powers/force-choke"),
    "force lightning": ("Force Lightning", "force-powers/force-lightning"),
    "telekinesis": ("Force Throw", "force-powers/force-throw"),
    "force heal": ("Force Heal", "force-powers/force-heal"),
    "mind trick": ("Mind Trick", "force-powers/mind-trick"),
}


def load_valid_routes() -> set[str]:
    routes: set[str] = {
        "all-planets", "all-characters", "all-jedi", "all-sith", "all-ships",
        "all-species", "all-factions", "all-cities-settlements", "all-droids",
        "all-bounty-hunters", "all-military-units",
    }

    for file_path in DATA.glob("*.cs"):
        text = file_path.read_text(encoding="utf-8")
        routes.update(ROUTE_PATTERN.findall(text))

    return routes


VALID_ROUTES = load_valid_routes()


def add_link(links: list[dict[str, str]], seen: set[str], label: str, value: str, route: str) -> None:
    if route not in VALID_ROUTES or route in seen:
        return

    links.append({"label": label, "value": value, "route": route})
    seen.add(route)


def links_from_profile(category: str, slug: str, profile: dict) -> list[dict[str, str]]:
    key = f"{category}/{slug}"
    if key in MANUAL:
        links: list[dict[str, str]] = []
        seen: set[str] = set()
        for link in MANUAL[key]:
            add_link(links, seen, link["label"], link["value"], link["route"])
        return links

    links = []
    seen = set()

    for affiliation in profile.get("affiliations", []):
        normalized = affiliation.lower().strip()
        for needle, (label, value, route) in AFFILIATION_ROUTES.items():
            if needle in normalized:
                display = affiliation if value.lower() not in affiliation.lower() else value
                add_link(links, seen, label, display, route)

    text_blob = " ".join(
        [
            profile.get("overview", ""),
            profile.get("history", ""),
            " ".join(profile.get("notableEvents", [])),
        ]
    ).lower()

    for planet, route in PLANET_SLUGS.items():
        if planet in text_blob:
            add_link(links, seen, "Planet", planet.title(), route)

    for phrase, (value, route) in BATTLE_PHRASES.items():
        if phrase in text_blob:
            label = "Battle" if route.startswith("wars-conflicts/battles") else "Conflict"
            add_link(links, seen, label, value, route)

    for phrase, (value, route) in FORCE_POWER_PHRASES.items():
        if phrase in text_blob:
            add_link(links, seen, "Force power", value, route)

    if "human" in text_blob:
        add_link(links, seen, "Species", "Human", "species/human")

    return links[:10]


def main() -> None:
    entries: list[dict] = []

    for category in ("characters", "jedi", "sith", "droids"):
        category_dir = PROFILES / category
        if not category_dir.exists():
            continue

        for profile_path in sorted(category_dir.glob("*.json")):
            slug = profile_path.stem
            profile = json.loads(profile_path.read_text(encoding="utf-8"))
            links = links_from_profile(category, slug, profile)
            entries.append({"category": category, "slug": slug, "links": links})

    OUTPUT.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(entries)} cross-link entries to {OUTPUT}")


if __name__ == "__main__":
    main()
