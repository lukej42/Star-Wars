#!/usr/bin/env python3
"""Build Related Archives cross-links for all Star Wars directory pages."""

from __future__ import annotations

import json
import re
from pathlib import Path

from parse_csharp_data import (
    all_directory_entries,
    load_characters,
    load_factions,
    load_planets,
)

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "Data"
PROFILES = ROOT / "wwwroot" / "data" / "profiles"
MAX_LINKS = 14

ROUTE_PATTERN = re.compile(r'Route\s*=\s*"([^"]+)"')
BATTLE_CALL = re.compile(r'Battle\("([^"]+)", "([^"]+)", "([^"]+)", "([^"]+)", "([^"]+)"\)')
UNIT_CALL = re.compile(
    r'Unit\("([^"]+)", MilitaryUnitBranch\.(Army|Navy), "([^"]+)", "([^"]+)", "([^"]+)", (null|"[^"]+"), "([^"]+)", "([^"]+)"(?:, ([^)]+))?\)'
)
FORM_BLOCK = re.compile(
    r'private static LightsaberFormContent (\w+) => new\(\s*.*?Practitioners:\s*\[(.*?)\]',
    re.DOTALL,
)
STRING_LITERAL = re.compile(r'"([^"]+)"')

BATTLE_PLANETS: dict[str, str] = {
    "first-battle-of-geonosis": "Geonosis",
    "battle-of-coruscant": "Coruscant",
    "battle-of-utapau": "Utapau",
    "battle-of-kashyyyk": "Kashyyyk",
    "siege-of-mandalore": "Mandalore",
    "battle-of-mon-cala": "Mon Cala",
    "battle-of-yavin": "Yavin 4",
    "battle-of-hoth": "Hoth",
    "battle-of-endor": "Endor",
    "battle-of-scarif": "Scarif",
    "battle-of-jakku": "Jakku",
    "assault-on-cloud-city": "Bespin",
    "battle-of-malachor-v": "Malachor V",
    "battle-of-dxun": "Dxun",
    "devastation-of-cathar": "Cathar",
    "battle-of-telos-iv": "Telos IV",
    "siege-of-tar-is": "Taris",
    "battle-of-althir": "Althir",
    "battle-of-ossus": "Ossus",
    "battle-of-coruscant-great-sith-war": "Coruscant",
    "battle-of-yavin-4-exar-kun": "Yavin 4",
    "battle-of-kemplex-nine": "Kemplex IX",
    "duel-on-ossus": "Ossus",
    "sith-invasion-of-ossus": "Ossus",
    "sacking-of-coruscant": "Coruscant",
    "battle-of-alderaan-great-galactic-war": "Alderaan",
    "recapture-of-korriban": "Korriban",
    "battle-of-ilum-great-galactic-war": "Ilum",
    "siege-of-balmorra": "Balmorra",
    "invasion-of-ord-mantell": "Ord Mantell",
    "battle-of-troiken": "Troiken",
    "battle-of-qika": "Qika",
    "battle-of-primus-goluud": "Primus Goluud",
    "coruscant-financial-crisis": "Coruscant",
    "battle-of-corbos": "Corbos",
    "battle-of-tython": "Tython",
    "battle-of-ruusan": "Ruusan",
    "seventh-battle-of-ruusan": "Ruusan",
    "thought-bomb-detonation": "Ruusan",
    "battle-of-jabiim-new-sith-wars": "Jabiim",
    "destruction-of-hosnian-prime": "Hosnian Prime",
    "battle-of-starkiller-base": "Starkiller Base",
    "battle-of-crait": "Crait",
    "battle-of-exegol": "Exegol",
    "battle-of-takodana": "Takodana",
    "battle-of-d-qar": "D'Qar",
    "battle-of-corellia": "Corellia",
    "battle-of-alderaan-great-war": "Alderaan",
    "battle-of-ilum-great-war": "Ilum",
    "battle-of-makeb": "Makeb",
    "siege-of-kaon": "Kaon",
    "fall-of-balmorra-great-war": "Balmorra",
}

SETTLEMENT_SPECIES: dict[str, list[tuple[str, str]]] = {
    "mos-eisley": [("Human", "species/human"), ("Jawa", "species/jawa"), ("Tusken Raider", "species/tusken-raider")],
    "mos-espa": [("Human", "species/human"), ("Jawa", "species/jawa")],
    "anchorhead": [("Human", "species/human"), ("Jawa", "species/jawa")],
    "theed": [("Human", "species/human"), ("Gungan", "species/gungan")],
    "otoh-gunga": [("Gungan", "species/gungan")],
    "rwookrrorro": [("Wookiee", "species/wookiee")],
    "dac-city": [("Mon Calamari", "species/mon-calamari")],
    "tipoca-city": [("Kaminoan", "species/kaminoan")],
    "sundari": [("Mandalorian", "species/mandalorian")],
    "kaas-city": [("Sith (Pureblood)", "species/sith-pureblood")],
    "jedha-city": [("Human", "species/human")],
    "mandalore-capital": [("Mandalorian", "species/mandalorian")],
    "cloud-city": [("Human", "species/human"), ("Ugnaught", "species/ugnaught")],
    "coruscant-underworld": [("Human", "species/human")],
    "senate-district": [("Human", "species/human")],
}

AFFILIATION_ROUTES: dict[str, tuple[str, str, str]] = {
    "galactic empire": ("Faction", "Galactic Empire", "factions/empire"),
    "imperial navy": ("Military unit", "Imperial Navy", "military-units/galactic-empire/navy"),
    "imperial army": ("Military unit", "Imperial Army", "military-units/galactic-empire/army"),
    "501st legion": ("Military unit", "501st Legion", "military-units/galactic-empire/army/501st-legion"),
    "stormtrooper": ("Military unit", "Stormtrooper Corps", "military-units/galactic-empire/army/stormtrooper-corps"),
    "rebel alliance": ("Faction", "Rebel Alliance", "factions/rebel-alliance"),
    "alliance to restore the republic": ("Faction", "Rebel Alliance", "factions/rebel-alliance"),
    "jedi order": ("Directory", "Jedi Order", "all-jedi"),
    "jedi high council": ("Directory", "Jedi Order", "all-jedi"),
    "sith order": ("Directory", "Sith Order", "all-sith"),
    "confederacy": ("Faction", "Confederacy", "factions/confederacy"),
    "separatist": ("Faction", "Confederacy", "factions/confederacy"),
    "cis": ("Faction", "Confederacy", "factions/confederacy"),
    "galactic republic": ("Faction", "Republic", "factions/republic"),
    "clone trooper": ("Military unit", "Clone Trooper Corps", "military-units/galactic-republic/army/clone-trooper-corps"),
    "first order": ("Faction", "First Order", "factions/first-order"),
    "resistance": ("Faction", "Resistance", "factions/resistance"),
    "new republic": ("Faction", "New Republic", "factions/new-republic"),
    "mandalorian": ("Faction", "Mandalorians", "factions/mandalorians"),
    "hutt cartel": ("Faction", "Hutts", "factions/hutts"),
    "trade federation": ("Faction", "Trade Federation", "factions/trade-federation"),
    "bounty hunters guild": ("Directory", "Bounty Hunters", "all-bounty-hunters"),
    "bounty hunters' guild": ("Directory", "Bounty Hunters", "all-bounty-hunters"),
}

FORCE_POWER_ALIASES: dict[str, tuple[str, str]] = {
    "force push": ("Force Push", "force-powers/force-push"),
    "force pull": ("Force Pull", "force-powers/force-pull"),
    "force choke": ("Force Choke", "force-powers/force-choke"),
    "force lightning": ("Force Lightning", "force-powers/force-lightning"),
    "force throw": ("Force Throw", "force-powers/force-throw"),
    "telekinesis": ("Force Throw", "force-powers/force-throw"),
    "force heal": ("Force Heal", "force-powers/force-heal"),
    "mind trick": ("Mind Trick", "force-powers/mind-trick"),
    "battle meditation": ("Battle Meditation", "force-powers/battle-meditation"),
    "force speed": ("Force Speed", "force-powers/force-speed"),
    "force jump": ("Force Jump", "force-powers/force-jump"),
    "force sense": ("Force Sense", "force-powers/force-sense"),
    "force rage": ("Force Rage", "force-powers/force-rage"),
    "force drain": ("Force Drain", "force-powers/force-drain"),
}

FORM_SLUGS = {
    "ShiiCho": "shii-cho",
    "Makashi": "makashi",
    "Soresu": "soresu",
    "Ataru": "ataru",
    "ShienDjemSo": "shien-djem-so",
    "Niman": "niman",
    "JuyoVaapad": "juyo-vaapad",
}

CAPITAL_OVERRIDES: dict[str, str] = {
    "republic": "Coruscant",
    "confederacy": "Raxus Secundus",
    "empire": "Coruscant",
    "rebel-alliance": "Dantooine",
    "new-republic": "Chandrila",
    "hutts": "Nal Hutta",
    "trade-federation": "Neimoidia",
    "first-order": "Starkiller Base",
    "resistance": "D'Qar",
    "mandalorians": "Mandalore",
    "sith-empire": "Dromund Kaas",
}


class CrossLinkIndexes:
    def __init__(self) -> None:
        self.valid_routes: set[str] = set()
        self.planets: list[dict[str, str]] = []
        self.planet_by_norm: dict[str, dict[str, str]] = {}
        self.species: list[dict[str, str]] = []
        self.species_by_norm: dict[str, dict[str, str]] = {}
        self.factions: list[dict[str, str]] = []
        self.ships: list[dict[str, str]] = []
        self.ship_by_norm: dict[str, dict[str, str]] = {}
        self.people: list[tuple[str, dict[str, str]]] = []
        self.people_by_norm: dict[str, tuple[str, dict[str, str]]] = {}
        self.settlements: list[dict[str, str]] = []
        self.settlements_by_planet: dict[str, list[dict[str, str]]] = {}
        self.powers: list[dict[str, str]] = []
        self.power_by_norm: dict[str, dict[str, str]] = {}
        self.forms: list[dict[str, str]] = []
        self.form_practitioners: dict[str, list[str]] = {}
        self.battles: list[dict[str, str]] = []
        self.battles_by_war: dict[str, list[dict[str, str]]] = {}
        self.battles_by_planet: dict[str, list[dict[str, str]]] = {}
        self.wars: list[dict[str, str]] = []
        self.military_units: list[dict[str, str]] = []
        self.profiles: dict[str, dict[str, dict]] = {}
        self.species_members: dict[str, list[tuple[str, dict[str, str]]]] = {}
        self.power_users: dict[str, list[tuple[str, dict[str, str]]]] = {}
        self.form_users: dict[str, list[tuple[str, dict[str, str]]]] = {}

    def load(self) -> None:
        self.valid_routes = self._load_valid_routes()
        self.planets = load_planets()
        self.species = all_directory_entries()["species"]
        self.factions = load_factions()
        self.ships = all_directory_entries()["ships"]
        self.settlements = all_directory_entries()["settlements"]
        self.powers = all_directory_entries()["force-powers"]
        self.forms = self._load_forms()
        self.form_practitioners = self._load_form_practitioners()
        self.battles = self._load_battles()
        self.wars = self._load_wars()
        self.military_units = self._load_military_units()

        for battle in self.battles:
            self.valid_routes.add(battle["route"])
        for war in self.wars:
            self.valid_routes.add(war["route"])
        for unit in self.military_units:
            self.valid_routes.add(unit["route"])

        for planet in self.planets:
            self.planet_by_norm[self._norm(planet["name"])] = planet
            self.planet_by_norm[self._norm(planet["slug"].replace("-", " "))] = planet

        for sp in self.species:
            self.species_by_norm[self._norm(sp["name"])] = sp

        for ship in self.ships:
            self.ship_by_norm[self._norm(ship["name"])] = ship
            self.ship_by_norm[self._norm(ship["slug"].replace("-", " "))] = ship

        for power in self.powers:
            self.power_by_norm[self._norm(power["name"])] = power

        for category in (
            "characters",
            "jedi",
            "sith",
            "bounty-hunters",
            "droids",
            "ships",
            "settlements",
            "species",
            "planets",
            "factions",
            "force-powers",
        ):
            self.profiles[category] = self._load_profiles(category)

        chars = load_characters()
        for entry in chars:
            self.people.append(("characters", entry))
            self._index_person(entry, "characters")
        for category in ("jedi", "sith", "bounty-hunters"):
            for entry in all_directory_entries()[category]:
                self.people.append((category, entry))
                self._index_person(entry, category)

        for settlement in self.settlements:
            planet_norm = self._norm(settlement.get("planet", ""))
            self.settlements_by_planet.setdefault(planet_norm, []).append(settlement)

        for battle in self.battles:
            self.battles_by_war.setdefault(battle["warSlug"], []).append(battle)
            planet_name = BATTLE_PLANETS.get(battle["slug"])
            if planet_name:
                self.battles_by_planet.setdefault(self._norm(planet_name), []).append(battle)

        self._build_reverse_indexes()

    def _norm(self, value: str) -> str:
        value = value.lower().replace("'", "").replace("'", "")
        value = re.sub(r"[^a-z0-9\s-]", " ", value)
        return re.sub(r"\s+", " ", value).strip()

    def _load_valid_routes(self) -> set[str]:
        routes: set[str] = {
            "all-planets",
            "all-characters",
            "all-jedi",
            "all-sith",
            "all-ships",
            "all-species",
            "all-factions",
            "all-cities-settlements",
            "all-droids",
            "all-bounty-hunters",
            "all-military-units",
            "all-force-powers",
            "all-light-side-powers",
            "all-dark-side-powers",
            "galaxy-map",
            "timelines",
            "the-force",
            "wars-conflicts",
        }
        for file_path in DATA.glob("*.cs"):
            routes.update(ROUTE_PATTERN.findall(file_path.read_text(encoding="utf-8")))
        return routes

    def _load_profiles(self, category: str) -> dict[str, dict]:
        folder = PROFILES / category
        if not folder.is_dir():
            return {}
        return {path.stem: json.loads(path.read_text(encoding="utf-8")) for path in folder.glob("*.json")}

    def _load_battles(self) -> list[dict[str, str]]:
        text = (DATA / "BattleData.cs").read_text(encoding="utf-8")
        battles: list[dict[str, str]] = []
        for match in BATTLE_CALL.finditer(text):
            war_slug, slug, name, era, color = match.groups()
            battles.append(
                {
                    "warSlug": war_slug,
                    "slug": slug,
                    "name": name,
                    "era": era,
                    "color": color,
                    "route": f"wars-conflicts/battles/{slug}",
                }
            )
        return battles

    def _load_wars(self) -> list[dict[str, str]]:
        text = (DATA / "WarConflictData.cs").read_text(encoding="utf-8")
        wars: list[dict[str, str]] = []
        for match in re.finditer(
            r'Name\s*=\s*"([^"]+)".*?Slug\s*=\s*"([^"]+)".*?Route\s*=\s*"([^"]+)"',
            text,
            re.DOTALL,
        ):
            name, slug, route = match.groups()
            wars.append({"name": name, "slug": slug, "route": route})
        return wars

    def _load_forms(self) -> list[dict[str, str]]:
        text = (DATA / "LightsaberFormData.cs").read_text(encoding="utf-8")
        forms: list[dict[str, str]] = []
        for match in re.finditer(
            r'Name\s*=\s*"([^"]+)".*?Slug\s*=\s*"([^"]+)".*?Route\s*=\s*"([^"]+)"',
            text,
            re.DOTALL,
        ):
            name, slug, route = match.groups()
            forms.append({"name": name, "slug": slug, "route": route})
        return forms

    def _load_form_practitioners(self) -> dict[str, list[str]]:
        text = (DATA / "LightsaberFormContentData.cs").read_text(encoding="utf-8")
        result: dict[str, list[str]] = {}
        for match in FORM_BLOCK.finditer(text):
            block_name, practitioners_raw = match.groups()
            slug = FORM_SLUGS.get(block_name)
            if not slug:
                continue
            names = STRING_LITERAL.findall(practitioners_raw)
            result[slug] = names
        return result

    def _load_military_units(self) -> list[dict[str, str]]:
        catalog = DATA / "MilitaryUnitCatalog.cs"
        if not catalog.is_file():
            return []
        text = catalog.read_text(encoding="utf-8")
        units: list[dict[str, str]] = []
        for match in UNIT_CALL.finditer(text):
            faction, branch, slug, name, *_rest = match.groups()
            branch_slug = branch.lower()
            units.append(
                {
                    "factionSlug": faction,
                    "branch": branch,
                    "slug": slug,
                    "name": name,
                    "route": f"military-units/{faction}/{branch_slug}/{slug}",
                }
            )
        return units

    def _index_person(self, entry: dict[str, str], category: str) -> None:
        norms = {self._norm(entry["name"])}
        parts = entry["name"].split()
        if len(parts) >= 2:
            norms.add(self._norm(parts[-1]))
        if category == "sith" and entry["name"].lower().startswith("darth "):
            norms.add(self._norm(entry["name"][6:]))
        for norm in norms:
            self.people_by_norm.setdefault(norm, (category, entry))

    def _build_reverse_indexes(self) -> None:
        for category, entry in self.people:
            profile = self.profiles.get(category, {}).get(entry["slug"], {})
            text = self._profile_text(profile, entry)
            species = self._detect_species(text, entry)
            if species:
                self.species_members.setdefault(species["slug"], []).append((category, entry))
            for power in self._match_force_powers(text):
                self.power_users.setdefault(power["slug"], []).append((category, entry))
            for form in self._match_forms(text):
                self.form_users.setdefault(form["slug"], []).append((category, entry))

        for form_slug, practitioners in self.form_practitioners.items():
            for practitioner in practitioners:
                person = self._match_practitioner(practitioner)
                if person:
                    self.form_users.setdefault(form_slug, []).append(person)

    def _profile_text(self, profile: dict, entry: dict[str, str] | None = None) -> str:
        chunks = [
            profile.get("overview", ""),
            profile.get("history", ""),
            profile.get("significance", ""),
            " ".join(profile.get("notableEvents", [])),
            " ".join(profile.get("affiliations", [])),
        ]
        if entry:
            chunks.extend(
                [
                    entry.get("description", ""),
                    entry.get("role", ""),
                    entry.get("rank", ""),
                    entry.get("title", ""),
                    entry.get("specialty", ""),
                    entry.get("homeworld", ""),
                    entry.get("class", ""),
                ]
            )
        return self._norm(" ".join(chunks))

    def _detect_species(self, text: str, entry: dict[str, str]) -> dict[str, str] | None:
        desc = entry.get("description", "")
        for sp in sorted(self.species, key=lambda s: len(s["name"]), reverse=True):
            name_norm = self._norm(sp["name"])
            if name_norm in text or name_norm in self._norm(desc):
                return sp
        if "human" in text or " human " in f" {text} ":
            return self.species_by_norm.get("human")
        return None

    def _match_planets(self, text: str) -> list[dict[str, str]]:
        found: list[dict[str, str]] = []
        seen: set[str] = set()
        for planet in sorted(self.planets, key=lambda p: len(p["name"]), reverse=True):
            norm = self._norm(planet["name"])
            if norm and norm in text and planet["route"] not in seen:
                found.append(planet)
                seen.add(planet["route"])
        return found

    def _match_species(self, text: str) -> list[dict[str, str]]:
        found: list[dict[str, str]] = []
        seen: set[str] = set()
        for sp in sorted(self.species, key=lambda s: len(s["name"]), reverse=True):
            norm = self._norm(sp["name"])
            if norm in text and sp["route"] not in seen:
                found.append(sp)
                seen.add(sp["route"])
        return found

    def _match_ships(self, text: str) -> list[dict[str, str]]:
        found: list[dict[str, str]] = []
        seen: set[str] = set()
        for ship in sorted(self.ships, key=lambda s: len(s["name"]), reverse=True):
            norm = self._norm(ship["name"])
            if norm in text and ship["route"] not in seen:
                found.append(ship)
                seen.add(ship["route"])
        return found

    def _match_force_powers(self, text: str) -> list[dict[str, str]]:
        found: list[dict[str, str]] = []
        seen: set[str] = set()
        for phrase, (_label, route) in sorted(FORCE_POWER_ALIASES.items(), key=lambda x: -len(x[0])):
            if phrase in text and route not in seen:
                slug = route.split("/")[-1]
                power = self.power_by_norm.get(self._norm(slug.replace("-", " ")))
                if power:
                    found.append(power)
                    seen.add(route)
        for power in sorted(self.powers, key=lambda p: len(p["name"]), reverse=True):
            norm = self._norm(power["name"])
            if norm in text and power["route"] not in seen:
                found.append(power)
                seen.add(power["route"])
        return found

    def _match_forms(self, text: str) -> list[dict[str, str]]:
        found: list[dict[str, str]] = []
        seen: set[str] = set()
        aliases = {
            "form i": "shii-cho",
            "shii cho": "shii-cho",
            "form ii": "makashi",
            "form iii": "soresu",
            "form iv": "ataru",
            "form v": "shien-djem-so",
            "djem so": "shien-djem-so",
            "shien": "shien-djem-so",
            "form vi": "niman",
            "form vii": "juyo-vaapad",
            "juyo": "juyo-vaapad",
            "vaapad": "juyo-vaapad",
        }
        for phrase, slug in aliases.items():
            if phrase in text:
                form = next((f for f in self.forms if f["slug"] == slug), None)
                if form and form["route"] not in seen:
                    found.append(form)
                    seen.add(form["route"])
        return found

    def _match_battles(self, text: str) -> list[dict[str, str]]:
        found: list[dict[str, str]] = []
        seen: set[str] = set()
        for battle in sorted(self.battles, key=lambda b: len(b["name"]), reverse=True):
            if self._norm(battle["name"]) in text and battle["route"] not in seen:
                found.append(battle)
                seen.add(battle["route"])
        return found

    def _match_practitioner(self, practitioner: str) -> tuple[str, dict[str, str]] | None:
        cleaned = re.sub(r"\([^)]*\)", "", practitioner)
        cleaned = cleaned.split("/")[0].strip()
        norm = self._norm(cleaned)
        if norm in self.people_by_norm:
            return self.people_by_norm[norm]
        for key, value in self.people_by_norm.items():
            if key in norm or norm in key:
                return value
        return None

    def _planet_for_name(self, name: str) -> dict[str, str] | None:
        return self.planet_by_norm.get(self._norm(name))

    def add_link(
        self,
        links: list[dict[str, str]],
        seen: set[str],
        label: str,
        value: str,
        route: str,
    ) -> None:
        if route not in self.valid_routes or route in seen:
            return
        links.append({"label": label, "value": value, "route": route})
        seen.add(route)

    def add_affiliations(self, links: list[dict[str, str]], seen: set[str], profile: dict) -> None:
        text = self._norm(" ".join(profile.get("affiliations", [])))
        for needle, (label, value, route) in AFFILIATION_ROUTES.items():
            if needle in text:
                self.add_link(links, seen, label, value, route)

    def links_for_profile_category(
        self,
        category: str,
        slug: str,
        entry: dict[str, str],
        *,
        homeworld: str = "",
        extra_planet: str = "",
    ) -> list[dict[str, str]]:
        profile = self.profiles.get(category, {}).get(slug, {})
        text = self._profile_text(profile, entry)
        links: list[dict[str, str]] = []
        seen: set[str] = set()

        self.add_affiliations(links, seen, profile)

        species = self._detect_species(text, entry)
        if species:
            self.add_link(links, seen, "Species", species["name"], species["route"])

        for planet in self._match_planets(text):
            self.add_link(links, seen, "Planet", planet["name"], planet["route"])

        if homeworld:
            for part in re.split(r"[;/,]", homeworld):
                planet = self._planet_for_name(part.strip())
                if planet:
                    self.add_link(links, seen, "Homeworld", planet["name"], planet["route"])

        if extra_planet:
            planet = self._planet_for_name(extra_planet)
            if planet:
                self.add_link(links, seen, "Planet", planet["name"], planet["route"])

        for ship in self._match_ships(text):
            self.add_link(links, seen, "Ship", ship["name"], ship["route"])

        for battle in self._match_battles(text):
            self.add_link(links, seen, "Battle", battle["name"], battle["route"])

        for power in self._match_force_powers(text):
            self.add_link(links, seen, "Force power", power["name"], power["route"])

        for form in self._match_forms(text):
            self.add_link(links, seen, "Lightsaber form", form["name"], form["route"])

        if category == "jedi":
            self.add_link(links, seen, "Directory", "Jedi Order", "all-jedi")
        elif category == "sith":
            self.add_link(links, seen, "Directory", "Sith Order", "all-sith")
        elif category == "bounty-hunters":
            self.add_link(links, seen, "Directory", "Bounty Hunters", "all-bounty-hunters")

        return links[:MAX_LINKS]

    def build_all_entries(self) -> list[dict]:
        entries: list[dict] = []

        for entry in load_characters():
            links = self.links_for_profile_category("characters", entry["slug"], entry)
            entries.append({"category": "characters", "slug": entry["slug"], "links": links})

        for category in ("jedi", "sith", "bounty-hunters", "droids"):
            for entry in all_directory_entries()[category]:
                homeworld = entry.get("homeworld", "")
                links = self.links_for_profile_category(
                    category, entry["slug"], entry, homeworld=homeworld
                )
                entries.append({"category": category, "slug": entry["slug"], "links": links})

        for ship in self.ships:
            profile = self.profiles.get("ships", {}).get(ship["slug"], {})
            text = self._profile_text(profile, ship)
            links: list[dict[str, str]] = []
            seen: set[str] = set()
            self.add_affiliations(links, seen, profile)
            for battle in self._match_battles(text):
                self.add_link(links, seen, "Battle", battle["name"], battle["route"])
            for person_cat, person in self.people:
                person_text = self._profile_text(
                    self.profiles.get(person_cat, {}).get(person["slug"], {}), person
                )
                if self._norm(ship["name"]) in person_text or self._norm(ship["slug"]) in person_text:
                    label = person_cat.rstrip("s").replace("-", " ").title()
                    self.add_link(links, seen, label, person["name"], person["route"])
            entries.append({"category": "ships", "slug": ship["slug"], "links": links[:MAX_LINKS]})

        for settlement in self.settlements:
            profile = self.profiles.get("settlements", {}).get(settlement["slug"], {})
            links: list[dict[str, str]] = []
            seen: set[str] = set()
            planet = self._planet_for_name(settlement.get("planet", ""))
            if planet:
                self.add_link(links, seen, "Planet", planet["name"], planet["route"])
            if settlement["slug"] in SETTLEMENT_SPECIES:
                for sp_name, sp_route in SETTLEMENT_SPECIES[settlement["slug"]]:
                    self.add_link(links, seen, "Species", sp_name, sp_route)
            elif planet:
                for sp in self.species:
                    if self._norm(sp.get("homeworld", "")) == self._norm(planet["name"]):
                        self.add_link(links, seen, "Species", sp["name"], sp["route"])
                        if sum(1 for link in links if link["label"] == "Species") >= 3:
                            break
            self.add_affiliations(links, seen, profile)
            entries.append({"category": "settlements", "slug": settlement["slug"], "links": links[:MAX_LINKS]})

        for sp in self.species:
            links: list[dict[str, str]] = []
            seen: set[str] = set()
            planet = self._planet_for_name(sp.get("homeworld", ""))
            if planet:
                self.add_link(links, seen, "Homeworld", planet["name"], planet["route"])
            for category, person in self.species_members.get(sp["slug"], [])[:8]:
                label = category.rstrip("s").replace("-", " ").title()
                self.add_link(links, seen, label, person["name"], person["route"])
            entries.append({"category": "species", "slug": sp["slug"], "links": links[:MAX_LINKS]})

        for planet in self.planets:
            profile = self.profiles.get("planets", {}).get(planet["slug"], {})
            links: list[dict[str, str]] = []
            seen: set[str] = set()
            for settlement in self.settlements_by_planet.get(self._norm(planet["name"]), [])[:6]:
                self.add_link(links, seen, "Settlement", settlement["name"], settlement["route"])
            for battle in self.battles_by_planet.get(self._norm(planet["name"]), []):
                self.add_link(links, seen, "Battle", battle["name"], battle["route"])
            for sp in self.species:
                if self._norm(sp.get("homeworld", "")) == self._norm(planet["name"]):
                    self.add_link(links, seen, "Species", sp["name"], sp["route"])
            text = self._profile_text(profile, planet)
            for category, person in self.people:
                if self._norm(planet["name"]) in self._profile_text(
                    self.profiles.get(category, {}).get(person["slug"], {}), person
                ):
                    label = category.rstrip("s").replace("-", " ").title()
                    self.add_link(links, seen, label, person["name"], person["route"])
            entries.append({"category": "planets", "slug": planet["slug"], "links": links[:MAX_LINKS]})

        for faction in self.factions:
            profile = self.profiles.get("factions", {}).get(faction["slug"], {})
            links: list[dict[str, str]] = []
            seen: set[str] = set()
            capital_name = CAPITAL_OVERRIDES.get(faction["slug"]) or faction.get("capital", "")
            capital_name = capital_name.split("(")[0].split("/")[0].strip()
            planet = self._planet_for_name(capital_name)
            if planet:
                self.add_link(links, seen, "Capital", planet["name"], planet["route"])
            self.add_affiliations(links, seen, profile)
            entries.append({"category": "factions", "slug": faction["slug"], "links": links[:MAX_LINKS]})

        for power in self.powers:
            links: list[dict[str, str]] = []
            seen: set[str] = set()
            side_label = "Jedi" if power.get("side") == "light" else "Sith"
            for category, person in self.power_users.get(power["slug"], []):
                if category not in ("jedi", "sith"):
                    continue
                self.add_link(links, seen, side_label, person["name"], person["route"])
            for category, person in self.power_users.get(power["slug"], []):
                if category == "characters":
                    self.add_link(links, seen, "Character", person["name"], person["route"])
            entries.append({"category": "force-powers", "slug": power["slug"], "links": links[:MAX_LINKS]})

        for form in self.forms:
            links: list[dict[str, str]] = []
            seen: set[str] = set()
            for category, person in self.form_users.get(form["slug"], []):
                label = "Jedi" if category == "jedi" else "Sith" if category == "sith" else "Character"
                self.add_link(links, seen, label, person["name"], person["route"])
            entries.append({"category": "lightsaber-forms", "slug": form["slug"], "links": links[:MAX_LINKS]})

        for battle in self.battles:
            links: list[dict[str, str]] = []
            seen: set[str] = set()
            war = next((w for w in self.wars if w["slug"] == battle["warSlug"]), None)
            if war:
                self.add_link(links, seen, "Conflict", war["name"], war["route"])
            planet_name = BATTLE_PLANETS.get(battle["slug"])
            if planet_name:
                planet = self._planet_for_name(planet_name)
                if planet:
                    self.add_link(links, seen, "Planet", planet["name"], planet["route"])
            entries.append({"category": "battles", "slug": battle["slug"], "links": links[:MAX_LINKS]})

        for unit in self.military_units:
            links: list[dict[str, str]] = []
            seen: set[str] = set()
            faction_route = f"military-units/{unit['factionSlug']}"
            if faction_route in self.valid_routes:
                self.add_link(links, seen, "Faction", unit["factionSlug"].replace("-", " ").title(), faction_route)
            branch_route = f"military-units/{unit['factionSlug']}/{unit['branch'].lower()}"
            if branch_route in self.valid_routes:
                label = "All Army Units" if unit["branch"] == "Army" else "All Navy Units"
                self.add_link(links, seen, "Branch", label, branch_route)
            entries.append({"category": "military-units", "slug": f"{unit['factionSlug']}/{unit['slug']}", "links": links[:MAX_LINKS]})

        return entries


def build_cross_link_entries() -> list[dict]:
    indexes = CrossLinkIndexes()
    indexes.load()
    return indexes.build_all_entries()
