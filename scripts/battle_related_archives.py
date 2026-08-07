#!/usr/bin/env python3
"""Curated Related Archives for battle pages."""

from __future__ import annotations

import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

from battle_catalog_additions import NEW_BATTLES

BATTLE_OVERRIDES: dict[str, list[tuple[str, str, str]]] = {}

for entry in NEW_BATTLES:
    if entry.get("archives"):
        BATTLE_OVERRIDES[entry["slug"]] = list(entry["archives"])

BATTLE_OVERRIDES.update(
    {
        "first-battle-of-geonosis": [
            ("Jedi", "Anakin Skywalker", "jedi/anakin-skywalker"),
            ("Jedi", "Obi-Wan Kenobi", "jedi/obi-wan-kenobi"),
            ("Jedi", "Mace Windu", "jedi/mace-windu"),
            ("Planet", "Geonosis", "planet/geonosis"),
            ("Faction", "Confederacy of Independent Systems", "factions/confederacy"),
            ("Battle", "Second Battle of Geonosis", "wars-conflicts/battles/second-battle-of-geonosis"),
        ],
        "battle-of-coruscant": [
            ("Jedi", "Anakin Skywalker", "jedi/anakin-skywalker"),
            ("Jedi", "Obi-Wan Kenobi", "jedi/obi-wan-kenobi"),
            ("Character", "General Grievous", "characters/general-grievous"),
            ("Sith", "Count Dooku", "sith/darth-tyranus"),
            ("Planet", "Coruscant", "coruscant"),
            ("Battle", "Jedi Purge", "wars-conflicts/battles/jedi-purge"),
        ],
        "battle-of-utapau": [
            ("Jedi", "Obi-Wan Kenobi", "jedi/obi-wan-kenobi"),
            ("Character", "General Grievous", "characters/general-grievous"),
            ("Planet", "Utapau", "planet/utapau"),
            ("Battle", "Jedi Purge", "wars-conflicts/battles/jedi-purge"),
        ],
        "battle-of-kashyyyk": [
            ("Jedi", "Yoda", "jedi/yoda"),
            ("Planet", "Kashyyyk", "planet/kashyyyk"),
            ("Species", "Wookiee", "species/wookiee"),
            ("Battle", "Jedi Purge", "wars-conflicts/battles/jedi-purge"),
        ],
        "siege-of-mandalore": [
            ("Jedi", "Ahsoka Tano", "jedi/ahsoka-tano"),
            ("Character", "Bo-Katan Kryze", "characters/bo-katan-kryze"),
            ("Character", "Captain Rex", "characters/captain-rex"),
            ("Planet", "Mandalore", "planet/mandalore"),
            ("Battle", "Jedi Purge", "wars-conflicts/battles/jedi-purge"),
        ],
        "battle-of-mon-cala": [
            ("Jedi", "Anakin Skywalker", "jedi/anakin-skywalker"),
            ("Jedi", "Kit Fisto", "jedi/kit-fisto"),
            ("Planet", "Mon Cala", "planet/mon-cala"),
        ],
        "jedi-purge": [
            ("Sith", "Darth Sidious", "sith/darth-sidious"),
            ("Sith", "Darth Vader", "sith/darth-vader"),
            ("Battle", "Battle of Utapau", "wars-conflicts/battles/battle-of-utapau"),
            ("Battle", "Battle of Coruscant", "wars-conflicts/battles/battle-of-coruscant"),
            ("Planet", "Coruscant", "coruscant"),
            ("Faction", "Galactic Empire", "factions/empire"),
        ],
        "battle-of-yavin": [
            ("Jedi", "Luke Skywalker", "jedi/luke-skywalker"),
            ("Character", "Han Solo", "characters/han-solo"),
            ("Character", "Leia Organa", "characters/leia-organa"),
            ("Ship", "Death Star I", "ships/death-star-i"),
            ("Planet", "Yavin 4", "planet/yavin-4"),
            ("Battle", "Battle of Scarif", "wars-conflicts/battles/battle-of-scarif"),
        ],
        "battle-of-hoth": [
            ("Jedi", "Luke Skywalker", "jedi/luke-skywalker"),
            ("Character", "Han Solo", "characters/han-solo"),
            ("Character", "Leia Organa", "characters/leia-organa"),
            ("Planet", "Hoth", "hoth"),
            ("Battle", "Assault on Cloud City", "wars-conflicts/battles/assault-on-cloud-city"),
        ],
        "battle-of-endor": [
            ("Jedi", "Luke Skywalker", "jedi/luke-skywalker"),
            ("Character", "Han Solo", "characters/han-solo"),
            ("Character", "Leia Organa", "characters/leia-organa"),
            ("Planet", "Endor", "planet/endor"),
            ("Ship", "Death Star II", "ships/death-star-ii"),
        ],
        "battle-of-scarif": [
            ("Character", "Jyn Erso", "characters/jyn-erso"),
            ("Character", "Cassian Andor", "characters/cassian-andor"),
            ("Planet", "Scarif", "planet/scarif"),
            ("Battle", "Battle of Yavin", "wars-conflicts/battles/battle-of-yavin"),
        ],
        "battle-of-jakku": [
            ("Character", "Han Solo", "characters/han-solo"),
            ("Character", "Leia Organa", "characters/leia-organa"),
            ("Planet", "Jakku", "planet/jakku"),
            ("Battle", "Battle of Endor", "wars-conflicts/battles/battle-of-endor"),
        ],
        "assault-on-cloud-city": [
            ("Jedi", "Luke Skywalker", "jedi/luke-skywalker"),
            ("Character", "Han Solo", "characters/han-solo"),
            ("Character", "Lando Calrissian", "characters/lando-calrissian"),
            ("Planet", "Bespin", "bespin"),
            ("Battle", "Battle of Hoth", "wars-conflicts/battles/battle-of-hoth"),
        ],
        "battle-of-malachor-v": [
            ("Jedi", "Revan", "jedi/revan"),
            ("Sith", "Darth Malak", "sith/darth-malak"),
            ("Planet", "Malachor V", "planet/malachor-v"),
            ("Battle", "Final Confrontation at Malachor V", "wars-conflicts/battles/final-confrontation-at-malachor-v"),
        ],
        "battle-of-ossus": [
            ("Sith", "Exar Kun", "sith/exar-kun"),
            ("Planet", "Ossus", "planet/ossus"),
            ("Battle", "Sith Invasion of Ossus", "wars-conflicts/battles/sith-invasion-of-ossus"),
        ],
        "sacking-of-coruscant": [
            ("Sith", "Darth Malgus", "sith/darth-malgus"),
            ("Planet", "Coruscant", "coruscant"),
            ("Faction", "Sith Empire", "factions/sith-empire"),
        ],
        "battle-of-ruusan": [
            ("Sith", "Darth Bane", "sith/darth-bane"),
            ("Planet", "Ruusan", "planet/ruusan"),
            ("Battle", "Thought Bomb Detonation", "wars-conflicts/battles/thought-bomb-detonation"),
        ],
        "destruction-of-hosnian-prime": [
            ("Character", "Leia Organa", "characters/leia-organa"),
            ("Character", "Poe Dameron", "characters/poe-dameron"),
            ("Planet", "Hosnian Prime", "planet/hosnian-prime"),
            ("Battle", "Battle of Starkiller Base", "wars-conflicts/battles/battle-of-starkiller-base"),
        ],
        "battle-of-starkiller-base": [
            ("Character", "Han Solo", "characters/han-solo"),
            ("Character", "Finn", "characters/finn"),
            ("Character", "Poe Dameron", "characters/poe-dameron"),
            ("Planet", "Starkiller Base", "planet/starkiller-base"),
        ],
        "battle-of-crait": [
            ("Jedi", "Luke Skywalker", "jedi/luke-skywalker"),
            ("Character", "Leia Organa", "characters/leia-organa"),
            ("Planet", "Crait", "planet/crait"),
            ("Battle", "Attack on Ahch-To", "wars-conflicts/battles/attack-on-ahch-to"),
        ],
        "battle-of-exegol": [
            ("Character", "Rey", "characters/rey"),
            ("Character", "Finn", "characters/finn"),
            ("Character", "Poe Dameron", "characters/poe-dameron"),
            ("Planet", "Exegol", "planet/exegol"),
            ("Sith", "Darth Sidious", "sith/darth-sidious"),
        ],
    }
)

WAR_ARCHIVES: dict[str, list[tuple[str, str, str]]] = {
    "clone-wars": [
        ("Faction", "Galactic Republic", "factions/republic"),
        ("Faction", "Confederacy of Independent Systems", "factions/confederacy"),
        ("Chronicle", "Fall of the Republic", "chronicles/galactic-history/fall-of-the-republic"),
    ],
    "galactic-civil-war": [
        ("Faction", "Rebel Alliance", "factions/rebel-alliance"),
        ("Faction", "Galactic Empire", "factions/empire"),
    ],
    "mandalorian-wars": [
        ("Faction", "Mandalorians", "factions/mandalorians"),
        ("Jedi", "Revan", "jedi/revan"),
    ],
    "great-sith-war": [
        ("Sith", "Exar Kun", "sith/exar-kun"),
        ("The Force", "Conflict Between Light and Dark", "the-force/conflict-between-light-and-dark-side"),
        ("Planet", "Korriban", "korriban"),
    ],
    "great-galactic-war": [
        ("Faction", "Sith Empire", "factions/sith-empire"),
        ("Planet", "Coruscant", "coruscant"),
        ("Battle", "Sacking of Coruscant", "wars-conflicts/battles/sacking-of-coruscant"),
    ],
    "stark-hyperspace-war": [
        ("Faction", "Trade Federation", "factions/trade-federation"),
        ("Planet", "Coruscant", "coruscant"),
    ],
    "hundred-year-darkness": [
        ("Planet", "Korriban", "korriban"),
        ("The Force", "Ancient Force Orders", "the-force/ancient-force-orders"),
    ],
    "new-sith-wars": [
        ("Sith", "Darth Bane", "sith/darth-bane"),
        ("Planet", "Ruusan", "planet/ruusan"),
    ],
    "cold-war": [
        ("Faction", "Resistance", "factions/resistance"),
        ("Faction", "First Order", "factions/first-order"),
    ],
    "great-war": [
        ("Faction", "Sith Empire", "factions/sith-empire"),
        ("Planet", "Corellia", "planet/corellia"),
    ],
}
