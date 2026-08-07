#!/usr/bin/env python3
"""Curated Related Archives data for Creatures & Fauna pages."""

from __future__ import annotations

# Hand-curated accurate links per creature slug
CREATURE_OVERRIDES: dict[str, list[tuple[str, str, str]]] = {
    "rancor": [
        ("Character", "Jabba the Hutt", "characters/jabba-the-hutt"),
        ("Jedi", "Luke Skywalker", "jedi/luke-skywalker"),
        ("Organization", "Desilijic Kajidic", "organizations/desilijic-kajidic"),
        ("Planet", "Tatooine", "tatooine"),
        ("Planet", "Dathomir", "planet/dathomir"),
        ("Creature", "Sarlacc", "creatures/sarlacc"),
    ],
    "wampa": [
        ("Jedi", "Luke Skywalker", "jedi/luke-skywalker"),
        ("Character", "Han Solo", "characters/han-solo"),
        ("Battle", "Battle of Hoth", "wars-conflicts/battles/battle-of-hoth"),
        ("Planet", "Hoth", "hoth"),
        ("Creature", "Tauntaun", "creatures/tauntaun"),
    ],
    "sarlacc": [
        ("Jedi", "Luke Skywalker", "jedi/luke-skywalker"),
        ("Character", "Han Solo", "characters/han-solo"),
        ("Character", "Leia Organa", "characters/leia-organa"),
        ("Character", "Boba Fett", "characters/boba-fett"),
        ("Character", "Jabba the Hutt", "characters/jabba-the-hutt"),
        ("Planet", "Tatooine", "tatooine"),
        ("Creature", "Rancor", "creatures/rancor"),
    ],
    "krayt-dragon": [
        ("Jedi", "Obi-Wan Kenobi", "jedi/obi-wan-kenobi"),
        ("Jedi", "Luke Skywalker", "jedi/luke-skywalker"),
        ("Species", "Tusken Raider", "species/tusken-raider"),
        ("Planet", "Tatooine", "tatooine"),
    ],
    "purrgil": [
        ("Jedi", "Ezra Bridger", "jedi/ezra-bridger"),
        ("The Force", "Force Philosophy", "the-force/force-philosophy"),
        ("Planet", "Lothal", "planet/lothal"),
    ],
    "loth-cat": [
        ("Jedi", "Ezra Bridger", "jedi/ezra-bridger"),
        ("Planet", "Lothal", "planet/lothal"),
        ("Creature", "Loth-Wolf", "creatures/loth-wolf"),
    ],
    "loth-wolf": [
        ("Jedi", "Ezra Bridger", "jedi/ezra-bridger"),
        ("The Force", "Force Philosophy", "the-force/force-philosophy"),
        ("The Force", "Force Creatures", "the-force/force-creatures"),
        ("Planet", "Lothal", "planet/lothal"),
    ],
    "convor": [
        ("Jedi", "Ahsoka Tano", "jedi/ahsoka-tano"),
        ("Planet", "Mortis", "planet/mortis"),
        ("Planet", "Lothal", "planet/lothal"),
    ],
    "zillo-beast": [
        ("Sith", "Darth Sidious", "sith/darth-sidious"),
        ("Jedi", "Anakin Skywalker", "jedi/anakin-skywalker"),
        ("Planet", "Malastare", "planet/malastare"),
        ("Planet", "Coruscant", "coruscant"),
    ],
    "nexu": [
        ("Character", "Padmé Amidala", "characters/padme-amidala"),
        ("Jedi", "Anakin Skywalker", "jedi/anakin-skywalker"),
        ("Jedi", "Obi-Wan Kenobi", "jedi/obi-wan-kenobi"),
        ("Battle", "First Battle of Geonosis", "wars-conflicts/battles/first-battle-of-geonosis"),
        ("Planet", "Geonosis", "planet/geonosis"),
        ("Creature", "Reek", "creatures/reek"),
        ("Creature", "Acklay", "creatures/acklay"),
    ],
    "reek": [
        ("Character", "Jango Fett", "characters/jango-fett"),
        ("Jedi", "Anakin Skywalker", "jedi/anakin-skywalker"),
        ("Battle", "First Battle of Geonosis", "wars-conflicts/battles/first-battle-of-geonosis"),
        ("Planet", "Geonosis", "planet/geonosis"),
    ],
    "acklay": [
        ("Jedi", "Obi-Wan Kenobi", "jedi/obi-wan-kenobi"),
        ("Jedi", "Anakin Skywalker", "jedi/anakin-skywalker"),
        ("Battle", "First Battle of Geonosis", "wars-conflicts/battles/first-battle-of-geonosis"),
        ("Planet", "Geonosis", "planet/geonosis"),
    ],
    "tauntaun": [
        ("Jedi", "Luke Skywalker", "jedi/luke-skywalker"),
        ("Character", "Han Solo", "characters/han-solo"),
        ("Battle", "Battle of Hoth", "wars-conflicts/battles/battle-of-hoth"),
        ("Planet", "Hoth", "hoth"),
        ("Creature", "Wampa", "creatures/wampa"),
    ],
    "dewback": [
        ("Faction", "Galactic Empire", "factions/empire"),
        ("Planet", "Tatooine", "tatooine"),
    ],
    "bantha": [
        ("Species", "Tusken Raider", "species/tusken-raider"),
        ("Planet", "Tatooine", "tatooine"),
    ],
    "rathtar": [
        ("Character", "Han Solo", "characters/han-solo"),
        ("Character", "Chewbacca", "characters/chewbacca"),
        ("Character", "Finn", "characters/finn"),
    ],
    "fyrnock": [
        ("Character", "Captain Rex", "characters/captain-rex"),
        ("Planet", "Anaxes", "planet/anaxes"),
    ],
    "krykna": [
        ("Character", "Thrawn", "characters/thrawn"),
        ("Character", "Hera Syndulla", "characters/hera-syndulla"),
        ("Jedi", "Ezra Bridger", "jedi/ezra-bridger"),
        ("Planet", "Atollon", "planet/atollon"),
    ],
    "mudhorn": [
        ("Character", "Din Djarin", "characters/din-djarin"),
        ("Jedi", "Grogu", "jedi/grogu"),
        ("Faction", "Mandalorians", "factions/mandalorians"),
    ],
    "blurrg": [
        ("Character", "Bo-Katan Kryze", "characters/bo-katan-kryze"),
        ("Character", "Cham Syndulla", "characters/cham-syndulla"),
        ("Planet", "Ryloth", "planet/ryloth"),
        ("Faction", "Mandalorians", "factions/mandalorians"),
    ],
    "varactyl": [
        ("Jedi", "Obi-Wan Kenobi", "jedi/obi-wan-kenobi"),
        ("Character", "General Grievous", "characters/general-grievous"),
        ("Battle", "Battle of Utapau", "wars-conflicts/battles/battle-of-utapau"),
        ("Planet", "Utapau", "planet/utapau"),
    ],
    "exogorth": [
        ("Character", "Han Solo", "characters/han-solo"),
        ("Character", "Leia Organa", "characters/leia-organa"),
        ("Character", "C-3PO", "characters/c-3po"),
        ("Planet", "Hoth", "hoth"),
        ("Ship", "Millennium Falcon", "ships/millennium-falcon"),
    ],
    "mynock": [
        ("Character", "Han Solo", "characters/han-solo"),
        ("Character", "Leia Organa", "characters/leia-organa"),
        ("Ship", "Millennium Falcon", "ships/millennium-falcon"),
        ("Planet", "Ord Mantell", "planet/ord-mantell"),
    ],
    "colo-claw-fish": [
        ("Character", "Jar Jar Binks", "characters/jar-jar-binks"),
        ("Jedi", "Obi-Wan Kenobi", "jedi/obi-wan-kenobi"),
        ("Planet", "Naboo", "naboo"),
        ("Military unit", "Gungan Grand Army", "military-units/other/army/gungan-grand-army"),
    ],
    "sando-aqua-monster": [
        ("Character", "Nute Gunray", "characters/nute-gunray"),
        ("Faction", "Trade Federation", "factions/trade-federation"),
        ("Planet", "Naboo", "naboo"),
        ("Military unit", "Gungan Grand Army", "military-units/other/army/gungan-grand-army"),
    ],
    "opee-sea-killer": [
        ("Character", "Jar Jar Binks", "characters/jar-jar-binks"),
        ("Planet", "Naboo", "naboo"),
        ("Military unit", "Gungan Grand Army", "military-units/other/army/gungan-grand-army"),
    ],
    "aiwha": [
        ("Planet", "Kamino", "planet/kamino"),
        ("Battle", "First Battle of Geonosis", "wars-conflicts/battles/first-battle-of-geonosis"),
    ],
    "bogling": [
        ("Planet", "Dagobah", "planet/dagobah"),
        ("Jedi", "Luke Skywalker", "jedi/luke-skywalker"),
    ],
    "steelpecker": [
        ("Character", "Rey", "characters/rey"),
        ("Character", "Unkar Plutt", "characters/unkar-plutt"),
        ("Planet", "Jakku", "planet/jakku"),
    ],
    "dark-side-spiders": [
        ("Jedi", "Ezra Bridger", "jedi/ezra-bridger"),
        ("The Force", "Light and Dark Side Conflict", "the-force/conflict-between-light-and-dark-side"),
        ("Planet", "Malachor", "planet/malachor"),
    ],
    "charhound": [
        ("The Force", "Force Creatures", "the-force/force-creatures"),
    ],
    "roggwart": [
        ("Character", "Jabba the Hutt", "characters/jabba-the-hutt"),
        ("Organization", "Desilijic Kajidic", "organizations/desilijic-kajidic"),
        ("Planet", "Tatooine", "tatooine"),
    ],
    "gundark": [
        ("Directory", "All Planets", "all-planets"),
    ],
    "wyyyschokk": [
        ("Character", "Chewbacca", "characters/chewbacca"),
        ("Planet", "Kashyyyk", "planet/kashyyyk"),
    ],
    "vornskr": [
        ("The Force", "Force Sense", "force-powers/force-sense"),
        ("Planet", "Myrkr", "planet/myrkr"),
    ],
    "tusk-cat": [
        ("Character", "Boss Nass", "characters/boss-nass"),
        ("Planet", "Naboo", "naboo"),
    ],
    "nuna": [
        ("Planet", "Naboo", "naboo"),
        ("Character", "Boss Nass", "characters/boss-nass"),
        ("Species", "Gungan", "species/gungan"),
    ],
    "falumpaset": [
        ("Character", "Boss Nass", "characters/boss-nass"),
        ("Character", "Jar Jar Binks", "characters/jar-jar-binks"),
        ("Military unit", "Gungan Grand Army", "military-units/other/army/gungan-grand-army"),
        ("Planet", "Naboo", "naboo"),
    ],
    "kaadu": [
        ("Character", "Jar Jar Binks", "characters/jar-jar-binks"),
        ("Character", "Boss Nass", "characters/boss-nass"),
        ("Military unit", "Gungan Grand Army", "military-units/other/army/gungan-grand-army"),
        ("Planet", "Naboo", "naboo"),
    ],
    "ronto": [
        ("Planet", "Tatooine", "tatooine"),
        ("Species", "Tusken Raider", "species/tusken-raider"),
        ("Creature", "Bantha", "creatures/bantha"),
    ],
    "happabore": [
        ("Character", "Unkar Plutt", "characters/unkar-plutt"),
        ("Planet", "Jakku", "planet/jakku"),
    ],
    "eopie": [
        ("Planet", "Tatooine", "tatooine"),
        ("Species", "Jawa", "species/jawa"),
    ],
    "dianoga": [
        ("Jedi", "Luke Skywalker", "jedi/luke-skywalker"),
        ("Character", "Han Solo", "characters/han-solo"),
        ("Character", "Leia Organa", "characters/leia-organa"),
        ("Ship", "Death Star I", "ships/death-star-i"),
        ("Battle", "Battle of Yavin", "wars-conflicts/battles/battle-of-yavin"),
    ],
    "kowakian-monkey-lizard": [
        ("Character", "Jabba the Hutt", "characters/jabba-the-hutt"),
        ("Organization", "Desilijic Kajidic", "organizations/desilijic-kajidic"),
        ("Planet", "Tatooine", "tatooine"),
    ],
    "porg": [
        ("Jedi", "Luke Skywalker", "jedi/luke-skywalker"),
        ("Character", "Chewbacca", "characters/chewbacca"),
        ("Character", "Rey", "characters/rey"),
        ("Planet", "Ahch-To", "planet/ahch-to"),
    ],
    "vulptex": [
        ("Jedi", "Luke Skywalker", "jedi/luke-skywalker"),
        ("Battle", "Battle of Crait", "wars-conflicts/battles/battle-of-crait"),
        ("Planet", "Crait", "planet/crait"),
    ],
    "tooka-cat": [
        ("Jedi", "Ezra Bridger", "jedi/ezra-bridger"),
        ("Character", "Sabine Wren", "characters/sabine-wren"),
        ("Planet", "Lothal", "planet/lothal"),
    ],
    "loth-bat": [
        ("Planet", "Lothal", "planet/lothal"),
        ("Creature", "Loth-Cat", "creatures/loth-cat"),
    ],
    "ice-spider": [
        ("The Force", "Kyber Crystals", "the-force/kyber-crystals"),
        ("Planet", "Ilum", "planet/ilum"),
    ],
}

HABITAT_LINKS: dict[str, list[tuple[str, str, str]]] = {
    "Dark Side & Exotic": [
        ("The Force", "Light and Dark Side Conflict", "the-force/conflict-between-light-and-dark-side"),
    ],
    "Space & Vacuum": [
        ("Directory", "All Ships", "all-ships"),
    ],
}

HOMEWORLD_ALIASES: dict[str, str] = {
    "unknown regions": "ilum",
    "asteroid fields": "hoth",
}
