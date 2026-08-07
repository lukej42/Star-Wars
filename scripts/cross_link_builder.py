#!/usr/bin/env python3
"""Build Related Archives cross-links for all Star Wars directory pages."""

from __future__ import annotations

import json
import re
from pathlib import Path

from chronicle_entity_links import (
    add_chronicle_links,
    chronicle_links_for_war,
    finalize_links,
    match_chronicle_slugs,
)
from entity_associations import factions_for_entity, inference_text, is_generic_profile
from related_archive_overrides import RELATED_ARCHIVE_OVERRIDES
from ship_related_archives import (
    ERA_PLANET_HINTS,
    SHIP_ALIASES,
    SHIP_BATTLE_LINKS,
    SHIP_COLOR_FACTION,
    SHIP_OVERRIDES,
    person_label,
)
from creature_related_archives import CREATURE_OVERRIDES, HABITAT_LINKS, HOMEWORLD_ALIASES
from battle_related_archives import BATTLE_OVERRIDES, WAR_ARCHIVES
from organization_related_archives import FACTION_LABELS as ORG_FACTION_LABELS, ORG_OVERRIDES
from parse_csharp_data import (
    all_directory_entries,
    load_category,
    load_characters,
    load_factions,
    load_planets,
    normalize,
)

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "Data"
PROFILES = ROOT / "wwwroot" / "data" / "profiles"
MAX_LINKS = 24
SETTLEMENT_SPECIES: dict[str, list[tuple[str, str]]] = {}
CHRONICLE_MAX_LINKS = 32

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
    "assault-on-cloud-city": "Bespin",
    "assault-on-dantooine-enclave": "Dantooine",
    "assault-on-ossus-library": "Ossus",
    "assault-on-starkiller-base-trench": "Starkiller Base",
    "attack-on-ahch-to": "Ahch To",
    "battle-of-ajan-kloss": "Ajan Kloss",
    "battle-of-alderaan-great-galactic-war": "Alderaan",
    "battle-of-alderaan-great-war": "Alderaan",
    "battle-of-althir": "Althir",
    "battle-of-anaxes": "Anaxes",
    "battle-of-atollon": "Atollon",
    "battle-of-boz-pity": "Boz Pity",
    "battle-of-cato-neimoidia": "Cato Neimoidia",
    "battle-of-christophsis": "Christophsis",
    "battle-of-corbos": "Corbos",
    "battle-of-corellia": "Corellia",
    "battle-of-coruscant": "Coruscant",
    "battle-of-coruscant-great-sith-war": "Coruscant",
    "battle-of-crait": "Crait",
    "battle-of-cyax-system": "Ossus",
    "battle-of-d-qar": "D'Qar",
    "battle-of-dantooine-great-war": "Dantooine",
    "battle-of-dromund-kaas-great-war": "Dromund Kaas",
    "battle-of-dxun": "Dxun",
    "battle-of-endor": "Endor",
    "battle-of-exegol": "Exegol",
    "battle-of-felucia": "Felucia",
    "battle-of-foerost": "Foerost",
    "battle-of-hoth": "Hoth",
    "battle-of-hoth-great-war": "Hoth",
    "battle-of-ilum-great-galactic-war": "Ilum",
    "battle-of-ilum-great-war": "Ilum",
    "battle-of-jabiim-new-sith-wars": "Jabiim",
    "battle-of-jagelland": "Althir",
    "battle-of-jakku": "Jakku",
    "battle-of-kashyyyk": "Kashyyyk",
    "battle-of-kef-bir": "Kef Bir",
    "battle-of-kemplex-nine": "Kemplex IX",
    "battle-of-kessel": "Kessel",
    "battle-of-kijimi": "Kijimi",
    "battle-of-korriban-ancient": "Korriban",
    "battle-of-makeb": "Makeb",
    "battle-of-malachor-v": "Malachor V",
    "battle-of-malastare": "Malastare",
    "battle-of-manaan-great-galactic-war": "Manaan",
    "battle-of-manaan-great-war": "Manaan",
    "battle-of-mimban": "Mimban",
    "battle-of-mon-cala": "Mon Cala",
    "battle-of-mygeeto": "Mygeeto",
    "battle-of-nal-hutta-great-war": "Nal Hutta",
    "battle-of-onderon-mandalorian-wars": "Onderon",
    "battle-of-ord-mantell-cold-war": "Ord Mantell",
    "battle-of-ord-mantell-great-war": "Ord Mantell",
    "battle-of-ossus": "Ossus",
    "battle-of-pasaana": "Pasaana",
    "battle-of-primus-goluud": "Primus Goluud",
    "battle-of-qika": "Qika",
    "battle-of-quell": "Quell",
    "battle-of-quesh-great-galactic-war": "Quesh",
    "battle-of-ringo-vinda": "Ringo Vinda",
    "battle-of-ruusan": "Ruusan",
    "battle-of-ryloth": "Ryloth",
    "battle-of-saleucami": "Saleucami",
    "battle-of-scarif": "Scarif",
    "battle-of-serroco": "Serroco",
    "battle-of-starkiller-base": "Starkiller Base",
    "battle-of-sullust": "Sullust",
    "battle-of-takodana": "Takodana",
    "battle-of-taris-great-war": "Taris",
    "battle-of-telos-iv": "Telos IV",
    "battle-of-troiken": "Troiken",
    "battle-of-tython": "Tython",
    "battle-of-tython-great-galactic-war": "Tython",
    "battle-of-umbara": "Umbara",
    "battle-of-utapau": "Utapau",
    "battle-of-vanquo": "Vanquo",
    "battle-of-voss": "Voss",
    "battle-of-voss-great-war": "Voss",
    "battle-of-yavin": "Yavin 4",
    "battle-of-yavin-4-exar-kun": "Yavin 4",
    "battle-of-ziost-great-war": "Ziost",
    "battle-on-eadu": "Eadu",
    "blockade-of-thyferra": "Thyferra",
    "coruscant-financial-crisis": "Coruscant",
    "dark-jedi-uprising-on-coruscant": "Coruscant",
    "defense-of-kamino": "Kamino",
    "defense-of-naboo-galactic-civil-war": "Naboo",
    "destruction-of-hosnian-prime": "Hosnian Prime",
    "devastation-of-cathar": "Cathar",
    "duel-on-ossus": "Ossus",
    "duel-on-yavin-4-great-sith-war": "Yavin 4",
    "exile-to-korriban": "Korriban",
    "fall-of-balmorra-great-war": "Balmorra",
    "fifth-battle-of-ruusan": "Ruusan",
    "final-confrontation-at-malachor-v": "Malachor V",
    "first-battle-of-geonosis": "Geonosis",
    "first-battle-of-ruusan": "Ruusan",
    "founding-of-the-sith-empire": "Korriban",
    "fourth-battle-of-ruusan": "Ruusan",
    "invasion-of-korriban-great-sith-war": "Korriban",
    "invasion-of-ord-mantell": "Ord Mantell",
    "jedi-intervention-at-coruscant": "Bordal",
    "jedi-purge": "Coruscant",
    "krath-coup-of-empress-teta": "Empress Teta",
    "liberation-of-sullust": "Sullust",
    "mandalorian-siege-of-taris": "Taris",
    "naval-battle-over-troiken": "Troiken",
    "raid-on-cathar-survivors": "Cathar",
    "recapture-of-korriban": "Korriban",
    "rise-of-darth-bane": "Ruusan",
    "sacking-of-coruscant": "Coruscant",
    "second-battle-of-geonosis": "Geonosis",
    "second-battle-of-ruusan": "Ruusan",
    "seventh-battle-of-ruusan": "Ruusan",
    "siege-of-balmorra": "Balmorra",
    "siege-of-formos": "Formos",
    "siege-of-kaon": "Kaon",
    "siege-of-kaon-great-war": "Kaon",
    "siege-of-lothal": "Lothal",
    "siege-of-mandalore": "Mandalore",
    "siege-of-maz-kanatas-castle": "Takodana",
    "siege-of-nal-hutta-great-galactic-war": "Nal Hutta",
    "siege-of-rhen-var": "Rhen Var",
    "siege-of-tar-is": "Taris",
    "sith-assault-on-dromund-kaas": "Dromund Kaas",
    "sith-bombardment-of-ambria": "Ambria",
    "sith-invasion-of-ossus": "Ossus",
    "sith-invasion-of-taris": "Taris",
    "sith-lord-skirmish-on-tython": "Tython",
    "sith-temple-construction-on-korriban": "Korriban",
    "sith-victory-at-ziost": "Ziost",
    "sixth-battle-of-ruusan": "Ruusan",
    "skirmish-on-jedha": "Jedha",
    "stark-hyperspace-ambush-at-taanab": "Taanab",
    "third-battle-of-ruusan": "Ruusan",
    "thought-bomb-detonation": "Ruusan",
}AFFILIATION_ROUTES: dict[str, tuple[str, str, str]] = {
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

PLANET_ALIASES: dict[str, str] = {
    "raxus secundus": "raxus",
    "neimoidia": "neimoidia",
    "cato neimoidia": "cato-neimoidia",
    "trade federation homeworld": "neimoidia",
    "starkiller base": "starkiller-base",
    "telos iv": "telos",
    "nal hutta moon": "nal-hutta",
    "imperial center": "coruscant",
    "galactic city": "coruscant",
    "yavin prime": "yavin-4",
    "mon cala dac": "mon-cala",
    "d qar": "d-qar",
    "dqar": "d-qar",
    "hosnian prime capital": "hosnian-prime",
    "hosnian system": "hosnian-prime",
    "moraband korriban": "moraband",
    "sith homeworld": "moraband",
    "unknown world": "lehon",
    "rakata prime": "rakata-prime",
    "lehon unknown world": "lehon",
    "ord mantell": "ord-mantell",
    "concord dawn": "concord-dawn",
    "plazir 17": "plazir-17",
    "narkina 5": "narkina-5",
    "stygeon prime": "stygeon-prime",
    "kemplex 9": "kemplex-nine",
    "kemplex ix": "kemplex-nine",
    "primus goluud": "primus-goluud",
    "barab i": "barab-i",
    "clakdor vii": "clakdor-vii",
    "colla iv": "colla-iv",
    "glee anselm": "glee-anselm",
    "l huguenok": "lhuguenok",
    "lah mu": "lahmu",
    "oba diah": "oba-diah",
    "orto plutonia": "orto-plutonia",
    "rhen var": "rhen-var",
    "telos iv restoration": "telos",
    "yag dhul": "yagdhul",
    "yar togna": "yar-togna",
    "cadomai prime": "cadomai-prime",
    "uvena prime": "uvena-prime",
    "maridun": "maridun",
    "kalakar six": "dromund-kalakar",
    "dromund kalakar": "dromund-kalakar",
    "jaguada moon": "jaguada-moon",
    "jaguadas moon": "jaguada-moon",
    "dromund fels": "dromund-fels",
    "dromund ixin": "dromund-ixin",
    "dromund tyne": "dromund-tyne",
    "ch hodos": "ch-hodos",
    "chhodos": "ch-hodos",
    "krayiss 2": "krayiss-ii",
    "khar delba": "khar-delba",
    "khar shian": "khar-shian",
    "ashas ree": "ashas-ree",
    "korriban outpost": "korriban-outpost",
}

FACTION_PLANETS: dict[str, list[tuple[str, str]]] = {
    "republic": [
        ("Capital", "Coruscant"),
        ("World", "Alderaan"),
        ("World", "Naboo"),
        ("World", "Corellia"),
        ("World", "Kuat"),
    ],
    "confederacy": [
        ("Capital", "Raxus Secundus"),
        ("World", "Geonosis"),
        ("World", "Raxus"),
        ("World", "Cato Neimoidia"),
        ("World", "Neimoidia"),
        ("World", "Mustafar"),
        ("World", "Serenno"),
    ],
    "empire": [
        ("Capital", "Coruscant"),
        ("World", "Mustafar"),
        ("World", "Scarif"),
        ("World", "Kuat"),
        ("World", "Fondor"),
        ("World", "Eadu"),
        ("World", "Wobani"),
    ],
    "rebel-alliance": [
        ("Base", "Dantooine"),
        ("Base", "Yavin 4"),
        ("Base", "Hoth"),
        ("World", "Scarif"),
        ("World", "Chandrila"),
        ("World", "Alderaan"),
        ("World", "Endor"),
        ("World", "Atollon"),
        ("World", "Lothal"),
    ],
    "new-republic": [
        ("Capital", "Chandrila"),
        ("Capital", "Hosnian Prime"),
        ("World", "Coruscant"),
        ("World", "Chandrila"),
        ("World", "Hosnian Prime"),
        ("World", "Bilbringi"),
        ("World", "Mon Cala"),
        ("World", "Naboo"),
    ],
    "hutts": [
        ("Capital", "Nal Hutta"),
        ("World", "Nal Hutta"),
        ("World", "Tatooine"),
        ("World", "Nar Shaddaa"),
        ("World", "Klatooine"),
    ],
    "trade-federation": [
        ("Capital", "Neimoidia"),
        ("World", "Neimoidia"),
        ("World", "Cato Neimoidia"),
    ],
    "first-order": [
        ("Capital", "Starkiller Base"),
        ("World", "Starkiller Base"),
        ("World", "Ilum"),
        ("World", "Jakku"),
        ("World", "Exegol"),
    ],
    "resistance": [
        ("Base", "D'Qar"),
        ("Base", "Crait"),
        ("Base", "Ajan Kloss"),
        ("World", "Takodana"),
        ("World", "D'Qar"),
        ("World", "Crait"),
    ],
    "mandalorians": [
        ("Capital", "Mandalore"),
        ("World", "Mandalore"),
        ("World", "Concord Dawn"),
        ("World", "Kalevala"),
        ("World", "Krownest"),
    ],
    "sith-empire": [
        ("Capital", "Dromund Kaas"),
        ("World", "Dromund Kaas"),
        ("World", "Korriban"),
        ("World", "Ziost"),
        ("World", "Moraband"),
        ("World", "Nathema"),
        ("World", "Rhelg"),
        ("World", "Ch'hodos"),
        ("World", "Krayiss II"),
        ("World", "Khar Delba"),
        ("World", "Khar Shian"),
        ("World", "Jaguada"),
        ("World", "Ashas Ree"),
        ("World", "Athiss"),
        ("World", "Begeren"),
        ("World", "Bosthirda"),
        ("World", "Dromund Fels"),
        ("World", "Dromund Ixin"),
        ("World", "Dromund Kalakar"),
        ("World", "Dromund Tyne"),
        ("World", "Kalsunor"),
        ("World", "Korriz"),
        ("World", "Nfolgai"),
        ("World", "Thule"),
        ("World", "Byss"),
        ("World", "Malachor V"),
    ],
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
        self.organizations: list[dict[str, str]] = []
        self.creatures: list[dict[str, str]] = []
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
        self.people_by_homeworld: dict[str, list[tuple[str, dict[str, str]]]] = {}
        self.factions_by_planet: dict[str, list[dict[str, str]]] = {}
        self.people_by_faction: dict[str, list[tuple[str, dict[str, str]]]] = {}

    def load(self) -> None:
        self.valid_routes = self._load_valid_routes()
        self.planets = load_planets()
        self.species = all_directory_entries()["species"]
        self.factions = load_factions()
        self.ships = all_directory_entries()["ships"]
        self.organizations = [normalize(entry) for entry in load_category("OrganizationData.cs")]
        self.creatures = [normalize(entry) for entry in load_category("CreatureData.cs")]
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

        for alias, slug in PLANET_ALIASES.items():
            planet = next((p for p in self.planets if p["slug"] == slug), None)
            if planet:
                self.planet_by_norm[self._norm(alias)] = planet

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
            "organizations",
            "creatures",
            "battles",
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
            planet = self._planet_for_name(settlement.get("planet", ""))
            if planet:
                self.settlements_by_planet.setdefault(planet["slug"], []).append(settlement)

        for battle in self.battles:
            self.battles_by_war.setdefault(battle["warSlug"], []).append(battle)
            planet_name = BATTLE_PLANETS.get(battle["slug"])
            if planet_name:
                planet = self._planet_for_name(planet_name)
                if planet:
                    self.battles_by_planet.setdefault(planet["slug"], []).append(battle)

        self._build_reverse_indexes()

    def _norm(self, value: str) -> str:
        value = value.lower()
        value = re.sub(r"'s\b", "", value)
        value = value.replace("'", "").replace("'", "")
        value = value.replace("-", " ")
        value = re.sub(r"[^a-z0-9\s]", " ", value)
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
                self._register_power_user(power["slug"], category, entry)
            for form in self._match_forms(text):
                self.form_users.setdefault(form["slug"], []).append((category, entry))
            homeworld = entry.get("homeworld", "")
            for part in re.split(r"[;/,]", homeworld):
                planet = self._planet_for_name(part.strip())
                if planet:
                    self.people_by_homeworld.setdefault(planet["slug"], []).append((category, entry))
            for planet in self._match_planets(text):
                self.people_by_homeworld.setdefault(planet["slug"], []).append((category, entry))

        for form_slug, practitioners in self.form_practitioners.items():
            for practitioner in practitioners:
                person = self._match_practitioner(practitioner)
                if person:
                    self.form_users.setdefault(form_slug, []).append(person)

        for power in self.powers:
            text = self._norm(power.get("description", ""))
            for category, person in self._match_people_in_text(text):
                self._register_power_user(power["slug"], category, person)

        for faction_slug, planet_names in FACTION_PLANETS.items():
            for _label, planet_name in planet_names:
                planet = self._planet_for_name(planet_name)
                if planet:
                    faction = next((f for f in self.factions if f["slug"] == faction_slug), None)
                    if faction:
                        self.factions_by_planet.setdefault(planet["slug"], []).append(faction)

    def _profile_text(self, profile: dict, entry: dict[str, str] | None = None) -> str:
        if entry and is_generic_profile(profile):
            return inference_text(profile, entry)
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
        padded = f" {text} "
        desc_padded = f" {self._norm(desc)} "
        for sp in sorted(self.species, key=lambda s: len(s["name"]), reverse=True):
            name_norm = self._norm(sp["name"])
            if not name_norm:
                continue
            needle = f" {name_norm} "
            if needle in padded or needle in desc_padded:
                return sp
        if " human " in padded or " human " in desc_padded:
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

    def _match_planets_bounded(self, text: str) -> list[dict[str, str]]:
        padded = f" {self._norm(text)} "
        found: list[dict[str, str]] = []
        seen: set[str] = set()
        for planet in sorted(self.planets, key=lambda p: len(p["name"]), reverse=True):
            norm = self._norm(planet["name"])
            if norm and f" {norm} " in padded and planet["route"] not in seen:
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

    def _register_power_user(self, power_slug: str, category: str, person: dict[str, str]) -> None:
        bucket = self.power_users.setdefault(power_slug, [])
        if any(existing["route"] == person["route"] for _, existing in bucket):
            return
        bucket.append((category, person))

    def _match_people_in_text(self, text: str) -> list[tuple[str, dict[str, str]]]:
        padded = f" {text} "
        found: list[tuple[str, dict[str, str]]] = []
        seen: set[str] = set()
        for category, person in sorted(self.people, key=lambda item: len(item[1]["name"]), reverse=True):
            norm_name = self._norm(person["name"])
            if not norm_name:
                continue
            matched = f" {norm_name} " in padded or f" {norm_name} s " in padded
            if not matched:
                parts = norm_name.split()
                if len(parts) >= 2:
                    matched = (
                        f" {parts[0]} {parts[1]} " in padded
                        or f" {' '.join(parts[:2])} " in padded
                        or f" {' '.join(parts)} " in padded
                    )
                elif len(parts) == 1 and len(parts[0]) >= 3:
                    matched = f" {parts[0]} " in padded
            if not matched and norm_name.startswith("darth ") and len(norm_name) > 6:
                matched = f" {norm_name[6:]} " in padded
            if matched and person["route"] not in seen:
                found.append((category, person))
                seen.add(person["route"])
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
        if not name:
            return None
        norm = self._norm(name)
        planet = self.planet_by_norm.get(norm)
        if planet:
            return planet
        alias_slug = PLANET_ALIASES.get(norm)
        if alias_slug:
            return next((p for p in self.planets if p["slug"] == alias_slug), None)
        for planet in sorted(self.planets, key=lambda p: len(p["name"]), reverse=True):
            pnorm = self._norm(planet["name"])
            if pnorm and (pnorm in norm or norm in pnorm):
                return planet
        return None

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
        if is_generic_profile(profile):
            return
        text = self._norm(" ".join(profile.get("affiliations", [])))
        for needle, (label, value, route) in AFFILIATION_ROUTES.items():
            if label == "Faction":
                continue
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
        war_slugs: list[str] | None = None,
        ship_era: str = "",
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

        chronicle_eras = match_chronicle_slugs(
            category,
            slug,
            entry,
            profile,
            war_slugs=war_slugs,
            ship_era=ship_era,
        )
        for label, value, route in factions_for_entity(
            category,
            slug,
            entry,
            profile,
            chronicle_eras=chronicle_eras,
        ):
            self.add_link(links, seen, label, value, route)
            if label == "Faction" and route.startswith("factions/"):
                faction_slug = route.split("/", 1)[1]
                members = self.people_by_faction.setdefault(faction_slug, [])
                if not any(m[1]["slug"] == slug and m[0] == category for m in members):
                    members.append((category, entry))

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

        add_chronicle_links(
            self,
            links,
            seen,
            category,
            slug,
            entry,
            profile,
            war_slugs=war_slugs,
            ship_era=ship_era,
        )

        for label, value, route in RELATED_ARCHIVE_OVERRIDES.get((category, slug), []):
            self.add_link(links, seen, label, value, route)

        return finalize_links(links)

    def links_for_ship(self, ship: dict[str, str]) -> list[dict[str, str]]:
        slug = ship["slug"]
        profile = self.profiles.get("ships", {}).get(slug, {})
        text = self._profile_text(profile, ship)
        description = ship.get("description", "")
        combined = f"{text} {description}".lower()
        links: list[dict[str, str]] = []
        seen: set[str] = set()

        for label, value, route in SHIP_OVERRIDES.get(slug, []):
            self.add_link(links, seen, label, value, route)

        color = ship.get("color", "")
        if color in SHIP_COLOR_FACTION:
            label, value, route = SHIP_COLOR_FACTION[color]
            self.add_link(links, seen, label, value, route)

        battle = SHIP_BATTLE_LINKS.get(slug)
        if battle:
            self.add_link(links, seen, *battle)

        for battle in self._match_battles(combined):
            self.add_link(links, seen, "Battle", battle["name"], battle["route"])

        for _keyword, label, value, route in ERA_PLANET_HINTS:
            if re.search(rf"\b{re.escape(_keyword)}\b", combined):
                self.add_link(links, seen, label, value, route)

        for planet in self._match_planets_bounded(combined):
            self.add_link(links, seen, "Planet", planet["name"], planet["route"])

        search_terms = {
            self._norm(ship["name"]),
            self._norm(ship["slug"].replace("-", " ")),
        }
        for alias in SHIP_ALIASES.get(slug, []):
            search_terms.add(self._norm(alias))

        for person_cat, person in self.people:
            person_text = self._profile_text(
                self.profiles.get(person_cat, {}).get(person["slug"], {}), person
            )
            person_norm = self._norm(person_text)
            if any(term and len(term) > 3 and term in person_norm for term in search_terms):
                self.add_link(links, seen, person_label(person_cat), person["name"], person["route"])

        for person_cat, person in self._match_people_in_text(combined):
            self.add_link(links, seen, person_label(person_cat), person["name"], person["route"])

        self.add_affiliations(links, seen, profile)

        for label, value, route in RELATED_ARCHIVE_OVERRIDES.get(("ships", slug), []):
            self.add_link(links, seen, label, value, route)

        return finalize_links(links)[:MAX_LINKS]

    def links_for_organization(self, org: dict[str, str]) -> list[dict[str, str]]:
        slug = org["slug"]
        profile = self.profiles.get("organizations", {}).get(slug, {})
        text = self._profile_text(profile, org)
        description = org.get("description", "")
        combined = f"{text} {description}".lower()
        links: list[dict[str, str]] = []
        seen: set[str] = set()

        for label, value, route in ORG_OVERRIDES.get(slug, []):
            self.add_link(links, seen, label, value, route)

        parent_faction = org.get("parentFactionSlug")
        if parent_faction and parent_faction in ORG_FACTION_LABELS:
            self.add_link(links, seen, *ORG_FACTION_LABELS[parent_faction])

        parent_org = org.get("parentOrganizationSlug")
        if parent_org:
            parent = next((item for item in self.organizations if item["slug"] == parent_org), None)
            if parent:
                self.add_link(links, seen, "Organization", parent["name"], parent["route"])

        for key, default_label in (
            ("majorCharacters", "Character"),
            ("planets", "Planet"),
            ("keyFactions", "Faction"),
            ("ships", "Ship"),
        ):
            for item in profile.get(key, []):
                label = item.get("label") or default_label
                self.add_link(links, seen, label, item["value"], item["route"])

        for key in ("headOfState", "headOfGovernment"):
            item = profile.get(key)
            if isinstance(item, dict) and item.get("route"):
                route = item["route"]
                label = "Jedi" if route.startswith("jedi/") else (
                    "Sith" if route.startswith("sith/") else "Character"
                )
                self.add_link(links, seen, label, item["value"], route)

        for battle in self._match_battles(combined):
            self.add_link(links, seen, "Battle", battle["name"], battle["route"])

        for planet in self._match_planets_bounded(combined):
            self.add_link(links, seen, "Planet", planet["name"], planet["route"])

        for person_cat, person in self._match_people_in_text(combined):
            self.add_link(links, seen, person_label(person_cat), person["name"], person["route"])

        self.add_affiliations(links, seen, profile)

        for label, value, route in RELATED_ARCHIVE_OVERRIDES.get(("organizations", slug), []):
            self.add_link(links, seen, label, value, route)

        return finalize_links(links)[:MAX_LINKS]

    def links_for_creature(self, creature: dict[str, str]) -> list[dict[str, str]]:
        slug = creature["slug"]
        profile = self.profiles.get("creatures", {}).get(slug, {})
        text = self._profile_text(profile, creature)
        description = creature.get("description", "")
        combined = f"{text} {description}".lower()
        links: list[dict[str, str]] = []
        seen: set[str] = set()

        for label, value, route in CREATURE_OVERRIDES.get(slug, []):
            self.add_link(links, seen, label, value, route)

        homeworld = creature.get("homeworld", "")
        if homeworld:
            for part in re.split(r"[,;/]", homeworld):
                planet = self._planet_for_name(part.strip())
                if not planet:
                    alias = HOMEWORLD_ALIASES.get(part.strip().lower())
                    if alias:
                        planet = next((p for p in self.planets if p["slug"] == alias), None)
                if planet:
                    self.add_link(links, seen, "Planet", planet["name"], planet["route"])

        habitat = creature.get("habitat", "")
        for label, value, route in HABITAT_LINKS.get(habitat, []):
            self.add_link(links, seen, label, value, route)

        for key, default_label in (
            ("majorCharacters", "Character"),
            ("planets", "Planet"),
            ("keyFactions", "Faction"),
        ):
            for item in profile.get(key, []):
                label = item.get("label") or default_label
                self.add_link(links, seen, label, item["value"], item["route"])

        for event in profile.get("majorEvents", []):
            if isinstance(event, dict) and event.get("route"):
                label = "Battle" if "battle" in event["route"] else "Event"
                self.add_link(links, seen, label, event.get("text", event["route"]), event["route"])

        for battle in self._match_battles(combined):
            self.add_link(links, seen, "Battle", battle["name"], battle["route"])

        self.add_affiliations(links, seen, profile)

        for label, value, route in RELATED_ARCHIVE_OVERRIDES.get(("creatures", slug), []):
            self.add_link(links, seen, label, value, route)

        return finalize_links(links)[:MAX_LINKS]

    def links_for_battle(self, battle: dict[str, str]) -> list[dict[str, str]]:
        slug = battle["slug"]
        profile = self.profiles.get("battles", {}).get(slug, {})
        links: list[dict[str, str]] = []
        seen: set[str] = set()

        war = next((w for w in self.wars if w["slug"] == battle["warSlug"]), None)
        if war:
            self.add_link(links, seen, "Conflict", war["name"], war["route"])

        for label, value, route in BATTLE_OVERRIDES.get(slug, []):
            self.add_link(links, seen, label, value, route)

        for label, value, route in WAR_ARCHIVES.get(battle["warSlug"], []):
            self.add_link(links, seen, label, value, route)

        planet_name = BATTLE_PLANETS.get(slug)
        if planet_name:
            planet = self._planet_for_name(planet_name)
            if planet:
                self.add_link(links, seen, "Planet", planet["name"], planet["route"])

        for key, default_label in (
            ("majorCharacters", "Character"),
            ("keyFactions", "Faction"),
            ("planets", "Planet"),
        ):
            for item in profile.get(key, []):
                label = item.get("label") or default_label
                self.add_link(links, seen, label, item["value"], item["route"])

        for event in profile.get("majorEvents", []):
            if isinstance(event, dict) and event.get("route"):
                self.add_link(links, seen, "Battle", event.get("text", event["route"]), event["route"])

        for label, value, route in RELATED_ARCHIVE_OVERRIDES.get(("battles", slug), []):
            self.add_link(links, seen, label, value, route)

        return finalize_links(links)[:MAX_LINKS]

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
            links = self.links_for_ship(ship)
            entries.append({"category": "ships", "slug": ship["slug"], "links": links})

        for org in self.organizations:
            links = self.links_for_organization(org)
            entries.append({"category": "organizations", "slug": org["slug"], "links": links})

        for creature in self.creatures:
            links = self.links_for_creature(creature)
            entries.append({"category": "creatures", "slug": creature["slug"], "links": links})

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
            for category, person in self.species_members.get(sp["slug"], [])[:12]:
                label = category.rstrip("s").replace("-", " ").title()
                self.add_link(links, seen, label, person["name"], person["route"])
            entries.append({"category": "species", "slug": sp["slug"], "links": links[:MAX_LINKS]})

        for planet in self.planets:
            profile = self.profiles.get("planets", {}).get(planet["slug"], {})
            links: list[dict[str, str]] = []
            seen: set[str] = set()
            for settlement in self.settlements_by_planet.get(planet["slug"], [])[:8]:
                self.add_link(links, seen, "Settlement", settlement["name"], settlement["route"])
            for battle in self.battles_by_planet.get(planet["slug"], []):
                self.add_link(links, seen, "Battle", battle["name"], battle["route"])
            for sp in self.species:
                hw = sp.get("homeworld", "")
                if self._planet_for_name(hw) and self._planet_for_name(hw)["slug"] == planet["slug"]:
                    self.add_link(links, seen, "Species", sp["name"], sp["route"])
            for category, person in self.people_by_homeworld.get(planet["slug"], [])[:10]:
                label = category.rstrip("s").replace("-", " ").title()
                self.add_link(links, seen, label, person["name"], person["route"])
            for faction in self.factions_by_planet.get(planet["slug"], []):
                self.add_link(links, seen, "Faction", faction["name"], faction["route"])
            text = self._profile_text(profile, planet)
            for category, person in self.people:
                person_text = self._profile_text(
                    self.profiles.get(category, {}).get(person["slug"], {}), person
                )
                if self._norm(planet["name"]) in person_text or self._norm(planet["slug"]) in person_text:
                    label = category.rstrip("s").replace("-", " ").title()
                    self.add_link(links, seen, label, person["name"], person["route"])
            self.add_affiliations(links, seen, profile)
            war_slugs = [
                battle["warSlug"]
                for battle in self.battles_by_planet.get(planet["slug"], [])
            ]
            add_chronicle_links(
                self,
                links,
                seen,
                "planets",
                planet["slug"],
                planet,
                profile,
                war_slugs=war_slugs,
            )
            entries.append({"category": "planets", "slug": planet["slug"], "links": finalize_links(links)})

        for faction in self.factions:
            profile = self.profiles.get("factions", {}).get(faction["slug"], {})
            links: list[dict[str, str]] = []
            seen: set[str] = set()
            for label, planet_name in FACTION_PLANETS.get(faction["slug"], []):
                planet = self._planet_for_name(planet_name)
                if planet:
                    self.add_link(links, seen, label, planet["name"], planet["route"])
            capital_raw = CAPITAL_OVERRIDES.get(faction["slug"]) or faction.get("capital", "")
            for part in re.split(r"[,;/]| and | then ", capital_raw):
                cleaned = part.strip().split("(")[0].strip()
                if not cleaned or cleaned.lower() in {"mobile", "corporate fleet"}:
                    continue
                planet = self._planet_for_name(cleaned)
                if planet:
                    self.add_link(links, seen, "Capital", planet["name"], planet["route"])
            self.add_affiliations(links, seen, profile)
            for category, person in self.people_by_faction.get(faction["slug"], [])[:16]:
                label = category.rstrip("s").replace("-", " ").title()
                self.add_link(links, seen, label, person["name"], person["route"])
            entries.append({"category": "factions", "slug": faction["slug"], "links": links[:MAX_LINKS]})

        for power in self.powers:
            links: list[dict[str, str]] = []
            seen: set[str] = set()
            label_map = {
                "jedi": "Jedi",
                "sith": "Sith",
                "characters": "Character",
                "bounty-hunters": "Bounty Hunter",
            }
            for category, person in self.power_users.get(power["slug"], []):
                label = label_map.get(category)
                if label:
                    self.add_link(links, seen, label, person["name"], person["route"])
            entries.append({"category": "force-powers", "slug": power["slug"], "links": links[:MAX_LINKS]})

        for side in ("light", "dark"):
            links: list[dict[str, str]] = []
            seen: set[str] = set()
            label_map = {
                "jedi": "Jedi",
                "sith": "Sith",
                "characters": "Character",
                "bounty-hunters": "Bounty Hunter",
            }
            for power in self.powers:
                if power.get("side") != side:
                    continue
                for category, person in self.power_users.get(power["slug"], []):
                    label = label_map.get(category)
                    if label:
                        self.add_link(links, seen, label, person["name"], person["route"])
            entries.append(
                {
                    "category": "force-power-index",
                    "slug": f"{side}-side",
                    "links": links[:MAX_LINKS],
                }
            )

        for form in self.forms:
            links: list[dict[str, str]] = []
            seen: set[str] = set()
            for category, person in self.form_users.get(form["slug"], []):
                label = "Jedi" if category == "jedi" else "Sith" if category == "sith" else "Character"
                self.add_link(links, seen, label, person["name"], person["route"])
            entries.append({"category": "lightsaber-forms", "slug": form["slug"], "links": links[:MAX_LINKS]})

        for battle in self.battles:
            links = self.links_for_battle(battle)
            entries.append({"category": "battles", "slug": battle["slug"], "links": links})

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

        for war in self.wars:
            links: list[dict[str, str]] = []
            seen: set[str] = set()
            for label, value, route in chronicle_links_for_war(war["slug"]):
                self.add_link(links, seen, label, value, route)
            for battle in self.battles_by_war.get(war["slug"], [])[:12]:
                self.add_link(links, seen, "Battle", battle["name"], battle["route"])
            entries.append({"category": "wars-conflicts", "slug": war["slug"], "links": finalize_links(links)})

        from chronicle_era_links import CHRONICLE_ERA_LINKS

        for slug, era_links in CHRONICLE_ERA_LINKS.items():
            links: list[dict[str, str]] = []
            seen: set[str] = set()
            for label, value, route in era_links:
                self.add_link(links, seen, label, value, route)
            entries.append({"category": "chronicles", "slug": slug, "links": links[:CHRONICLE_MAX_LINKS]})

        return entries


def inherit_chronicle_links(entries: list[dict]) -> None:
    """Copy Galactic History and faction links from sibling directory entries that share a slug."""
    by_key = {(entry["category"], entry["slug"]): entry for entry in entries}
    character_slugs = {entry["slug"] for entry in entries if entry["category"] == "characters"}
    source_categories = ["jedi", "sith", "bounty-hunters", "droids"]

    for slug in character_slugs:
        target = by_key.get(("characters", slug))
        if not target:
            continue

        if not any(link["label"] == "Chronicle" for link in target["links"]):
            for source_category in source_categories:
                source = by_key.get((source_category, slug))
                if not source:
                    continue
                chronicles = [link for link in source["links"] if link["label"] == "Chronicle"]
                if chronicles:
                    target["links"] = finalize_links(target["links"] + chronicles)
                    break

        if not any(link["label"] == "Faction" for link in target["links"]):
            for source_category in source_categories:
                source = by_key.get((source_category, slug))
                if not source:
                    continue
                factions = [link for link in source["links"] if link["label"] == "Faction"]
                if factions:
                    target["links"] = finalize_links(target["links"] + factions)
                    break


def build_cross_link_entries() -> list[dict]:
    indexes = CrossLinkIndexes()
    indexes.load()
    entries = indexes.build_all_entries()
    inherit_chronicle_links(entries)
    return entries
