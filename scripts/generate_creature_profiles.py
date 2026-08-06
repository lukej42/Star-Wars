#!/usr/bin/env python3
"""Generate rich creature profile JSON for all Creatures & Fauna entries."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "Data" / "CreatureData.cs"
OUTPUT = ROOT / "wwwroot" / "data" / "profiles" / "creatures"

STRING_FIELD = re.compile(r'(\w+) = "(.*?)"')

PLANET_ROUTES = {
    "hoth": "hoth",
    "tatooine": "tatooine",
    "naboo": "naboo",
    "dathomir": "planet/dathomir",
    "coruscant": "coruscant",
    "dagobah": "dagobah",
    "mustafar": "mustafar",
    "kashyyyk": "planet/kashyyyk",
    "geonosis": "planet/geonosis",
    "lothal": "planet/lothal",
    "kamino": "planet/kamino",
    "utapau": "planet/utapau",
    "jakku": "jakku",
    "crait": "planet/crait",
    "ahch-to": "planet/ahch-to",
    "malachor": "planet/malachor",
    "atollon": "planet/atollon",
    "ilum": "planet/ilum",
    "ryloth": "planet/ryloth",
    "arvala-7": "planet/arvala-7",
    "malastare": "planet/malastare",
    "myrkr": "planet/myrkr",
    "kowak": "planet/kowak",
    "vodran": "planet/vodran",
    "anaxes": "planet/anaxes",
    "cholganna": "planet/cholganna",
    "ylesia": "planet/ylesia",
    "gundar": "planet/gundar",
    "vendaxa": "planet/vendaxa",
    "ord mantell": "planet/ord-mantell",
    "elphrona": "planet/elphrona",
}

FILMS = {
    "core": [
        "Star Wars: Episode I — The Phantom Menace",
        "Star Wars: Episode II — Attack of the Clones",
        "Star Wars: Episode III — Revenge of the Sith",
        "Star Wars: Episode IV — A New Hope",
        "Star Wars: Episode V — The Empire Strikes Back",
        "Star Wars: Episode VI — Return of the Jedi",
        "Star Wars: Episode VII — The Force Awakens",
        "Star Wars: Episode VIII — The Last Jedi",
    ],
}

SERIES = [
    "Star Wars: The Clone Wars",
    "Star Wars Rebels",
    "Star Wars: The Bad Batch",
    "Star Wars: The Mandalorian",
    "Star Wars: Tales of the Jedi",
]


def parse_creatures() -> list[dict[str, str]]:
    text = DATA.read_text(encoding="utf-8")
    entries: list[dict[str, str]] = []
    for block in re.findall(r"new\(\)\s*\{(.*?)\}", text, re.DOTALL):
        entry: dict[str, str] = {}
        for match in STRING_FIELD.finditer(block):
            entry[match.group(1)] = match.group(2)
        if "Slug" in entry:
            entries.append(entry)
    return entries


def planet_link(name: str) -> dict[str, str]:
    key = name.lower().strip()
    route = PLANET_ROUTES.get(key, f"planet/{key.replace(' ', '-')}")
    return {"label": "Planet", "value": name, "route": route}


def character_link(name: str, route: str) -> dict[str, str]:
    return {"label": "Character", "value": name, "route": route}


def scene_gallery(slug: str, name: str) -> list[dict[str, str]]:
    return [{"path": f"/images/creatures/{slug}-scene.webp", "caption": f"Cinematic habitat portrait — {name}"}]


def extra_gallery(slug: str, filename: str, caption: str) -> dict[str, str]:
    return {"path": f"/images/creatures/{filename}", "caption": caption}


# Hand-authored iconic profiles with character story sections
ICONIC: dict[str, dict] = {}


def _iconic_wampa() -> dict:
    return {
        "overview": (
            "The wampa is Hoth's apex ice predator — a white-furred carnivore standing up to three meters tall "
            "that ambushes prey from snow caves and drags victims back to lairs carved into glacier walls. "
            "Their heat-sensitive vision, crushing strength, and tolerance for Hoth's lethal nights make them "
            "among the most dangerous fauna in the Anoat sector. Rebel scouts at Echo Base learned to fear "
            "wampa territory almost as much as Imperial probe droids."
        ),
        "history": (
            "Wampas evolved on Hoth's sixth moon in isolation, developing thick fur, layered fat reserves, and "
            "claws capable of shredding tauntaun hide. They hunt by scent and thermal signature, often leaving "
            "only bloodstains on the wind-swept ice plains. Tusken-style cave networks across the glacier "
            "ranges house family groups that compete fiercely for territory during the brief seasonal thaw.\n\n"
            "**Luke Skywalker and the Hoth wampa.** During a routine patrol near Echo Base, Luke Skywalker "
            "mounted a tauntaun to investigate a meteor impact that turned out to be an Imperial probe droid. "
            "When a blizzard separated him from base, he dismounted to investigate a dead tauntaun — and a wampa "
            "struck without warning. The creature knocked Luke unconscious, lashed him to the ceiling of its ice "
            "cave with frozen residue, and killed his mount for food.\n\n"
            "Luke awoke dangling above the wampa's kill, his face frostbitten and his lightsaber out of reach on "
            "the snow floor. Using the Force to summon the weapon, he freed himself and severed the beast's arm "
            "in a desperate fight before stumbling into the Hoth night. Han Solo eventually found him near death "
            "and sheltered him inside a tauntaun's warm carcass — one of the Rebellion's most iconic survival "
            "moments and the first clear demonstration that Hoth's wildlife could kill as surely as the Empire.\n\n"
            "Echo Base security afterward marked wampa caves on tactical maps and restricted solo patrols. "
            "Imperial records later noted wampa pelts traded on black markets, though hunting the creatures "
            "remains extraordinarily dangerous."
        ),
        "significance": (
            "The wampa attack opens *The Empire Strikes Back* with immediate physical peril unrelated to the Empire — "
            "reminding viewers that the galaxy's worlds are alive with threats of their own.\n\n"
            "Luke's Force-pull of his lightsaber in the cave became a defining hero moment and a template for "
            "later Force telekinesis showcases across films and series.\n\n"
            "Ecologically, wampas anchor Hoth's food chain alongside tauntauns and ice spiders, making the planet "
            "uninhabitable without serious infrastructure — a fact the Rebellion accepted for the sake of secrecy."
        ),
        "notableEvents": [
            "Luke Skywalker attacked and captured by a wampa during an Echo Base patrol",
            "Luke escaped the wampa cave using Force telekinesis to retrieve his lightsaber",
            "Han Solo found Luke and sheltered him inside a tauntaun carcass",
            "Wampa caves mapped near Rebel perimeter defenses at Echo Base",
            "Wampa remains documented in New Republic xenobiology surveys",
        ],
        "majorCharacters": [
            character_link("Luke Skywalker", "characters/luke-skywalker"),
            character_link("Han Solo", "characters/han-solo"),
            character_link("Leia Organa", "characters/leia-organa"),
        ],
        "planets": [planet_link("Hoth")],
        "majorEvents": [
            {"text": "Battle of Hoth — Echo Base evacuation", "route": "wars-conflicts/battles/battle-of-hoth"},
            {"text": "Luke Skywalker begins Jedi training on Dagobah", "route": "characters/luke-skywalker"},
        ],
        "films": ["Star Wars: Episode V — The Empire Strikes Back"],
        "series": ["Star Wars Galaxy of Creatures", "Star Wars: Forces of Destiny"],
        "affiliations": ["Hoth ecosystem", "Echo Base perimeter hazards", "Outer Rim xenobiology"],
        "timeline": [
            {"era": "Pre-Rebellion", "event": "Wampas documented by Hoth mining surveys"},
            {"era": "3 ABY", "event": "Luke Skywalker attacked during Echo Base patrol"},
            {"era": "3 ABY", "event": "Battle of Hoth forces base evacuation"},
            {"era": "New Republic", "event": "Wampa conservation debates on protected-world lists"},
        ],
        "gallery": scene_gallery("wampa", "Wampa") + [
            extra_gallery("wampa", "wampa-luke-skywalker-fight.webp", "Luke Skywalker fights off a wampa in the ice caves of Hoth"),
        ],
    }


def _iconic_tauntaun() -> dict:
    return {
        "overview": (
            "Tauntauns are reptomammals native to Hoth — warm-blooded enough to survive brief surface exposure "
            "but vulnerable to nighttime freezes that can kill them within minutes. Their musk, layered fur, and "
            "sure-footed gait on ice made them indispensable mount animals for the Rebel Alliance at Echo Base, "
            "where snowspeeders could not reach every patrol route."
        ),
        "history": (
            "Tauntauns evolved as herd animals on Hoth's equatorial ice shelves, grazing on lichens and subterranean "
            "moss exposed by geothermal vents. They communicate through honks and scent marking, forming packs that "
            "migrate toward warmth when night temperatures plummet. Domestication proved difficult; only experienced "
            "handlers like Rebel beastmasters could keep them calm in base corrals.\n\n"
            "**The Rebel Alliance on Hoth.** When the Alliance established Echo Base inside the ice caves of Hoth, "
            "tauntauns replaced speeders for short-range patrols in sectors where repulsorlift engines fouled in "
            "extreme cold. Riders wrapped themselves in thermal gear and used the creatures' natural homing instinct "
            "to return before sunset — because, as Han Solo famously warned, tauntauns \"smell bad on the outside\" "
            "but die if left exposed after dusk.\n\n"
            "Luke Skywalker rode a tauntaun on the patrol that ended in a wampa attack; the mount was killed and "
            "eaten by the predator. Later, when Luke went missing in the blizzard, Han Solo took another tauntaun "
            "into the night to search for him — an act of loyalty that pushed the animal past its limits. When the "
            "tauntaun collapsed and died from exposure, Han used his lightsaber to open the carcass and placed the "
            "delirious Luke inside for warmth until rescue could arrive.\n\n"
            "That sacrifice became one of the saga's most enduring images: a frozen plain, two friends, and a "
            "tauntaun whose body saved the Rebellion's greatest hope. Echo Base personnel afterward treated "
            "tauntauns with renewed respect, expanding heated stables and rotating patrol schedules to protect "
            "the herds that protected them."
        ),
        "significance": (
            "Tauntauns embody the Rebellion's improvisational spirit — using local fauna when high technology fails.\n\n"
            "Han Solo's tauntaun rescue sequence defines his character as fiercely loyal beneath cynical wit.\n\n"
            "The creatures remain synonymous with Hoth in merchandising, theme parks, and fan culture as the "
            "galaxy's most beloved — if malodorous — steeds."
        ),
        "notableEvents": [
            "Rebel Alliance domesticated tauntauns for Echo Base patrol routes",
            "Luke Skywalker's tauntaun killed by a wampa during a patrol",
            "Han Solo rode a tauntaun into a Hoth blizzard to rescue Luke",
            "Han sheltered Luke inside a tauntaun carcass after the mount died from cold",
            "Tauntaun herds evacuated or lost during the Battle of Hoth",
        ],
        "majorCharacters": [
            character_link("Han Solo", "characters/han-solo"),
            character_link("Luke Skywalker", "characters/luke-skywalker"),
            character_link("Leia Organa", "characters/leia-organa"),
        ],
        "planets": [planet_link("Hoth")],
        "majorEvents": [
            {"text": "Battle of Hoth", "route": "wars-conflicts/battles/battle-of-hoth"},
        ],
        "films": ["Star Wars: Episode V — The Empire Strikes Back"],
        "series": ["Star Wars Galaxy of Creatures", "Star Wars: Forces of Destiny"],
        "affiliations": ["Echo Base patrol corps", "Rebel Alliance logistics", "Hoth native fauna"],
        "timeline": [
            {"era": "3 ABY", "event": "Rebel Alliance begins tauntaun patrol program at Echo Base"},
            {"era": "3 ABY", "event": "Luke's patrol tauntaun killed by a wampa"},
            {"era": "3 ABY", "event": "Han Solo's tauntaun dies saving Luke in the blizzard"},
            {"era": "3 ABY", "event": "Battle of Hoth ends Echo Base operations"},
        ],
        "gallery": scene_gallery("tauntaun", "Tauntaun") + [
            extra_gallery("tauntaun", "tauntaun-han-solo-riding.webp", "Han Solo rides a tauntaun across the frozen plains of Hoth"),
        ],
    }


def _iconic_kaadu() -> dict:
    return {
        "overview": (
            "Kaadu are fast amphibious reptiles native to Naboo's swamps and grasslands — the primary cavalry "
            "mounts of the Gungan Grand Army. Their broad feet paddle through wetlands as easily as they gallop "
            "across the Great Grass Plains, carrying warriors wielding booma catapults and atlatls into battle."
        ),
        "history": (
            "Kaadu evolved in Naboo's equatorial marsh basins, developing waterproof hides, powerful hind legs, "
            "and social flocking behavior. Gungans domesticated them centuries before human settlement, treating "
            "kaadu as partners rather than mere beasts — ceremonial armor and saddle rigs reflect clan status.\n\n"
            "**Gungan cavalry and Jar Jar Binks.** When the Trade Federation invaded Naboo, Boss Nass united the "
            "Gungan Grand Army to draw battle droid forces away from Theed while Queen Amidala retook the capital. "
            "Kaadu cavalry formed the army's mobile spearhead, thundering across the Great Grass Plains in one "
            "of the saga's most colorful battles.\n\n"
            "Jar Jar Binks — exiled for clumsiness but eager to prove himself — rode a kaadu alongside General "
            "Ceel and the militiagung, charging Federation lines despite his notorious lack of grace. His mount "
            "bucked and swerved through blaster fire while Jar Jar accidentally launched boomas that sometimes "
            "helped and sometimes hindered the assault. The image of Gungan warriors on kaadu backs, banners "
            "flying and energy balls arcing toward droid formations, became Naboo liberation iconography.\n\n"
            "After the battle, kaadu remained central to Gungan culture — patrol units, festival races, and "
            "diplomatic processions all featured the mounts. The Naboo and Gungans' shared victory cemented "
            "kaadu as symbols of alliance between surface and underwater peoples."
        ),
        "significance": (
            "Kaadu cavalry visually distinguishes Gungan warfare from every other army in the saga — organic, "
            "colorful, and deeply tied to Naboo's ecology.\n\n"
            "Jar Jar's kaadu charge, however awkward, represents the theme that unlikely heroes matter in "
            "galactic history.\n\n"
            "The mounts connect Naboo's swamp and plains biomes into a single cultural identity."
        ),
        "notableEvents": [
            "Gungan Grand Army deployed kaadu cavalry at the Battle of the Great Grass Plains",
            "Jar Jar Binks rode a kaadu during the assault on Trade Federation forces",
            "Kaadu units drew droid armies away from Theed during the liberation of Naboo",
            "Post-war Gungan patrols continued kaadu-mounted security in the swamps",
        ],
        "majorCharacters": [
            character_link("Jar Jar Binks", "characters/jar-jar-binks"),
            character_link("Boss Nass", "characters/boss-nass"),
            character_link("Padmé Amidala", "characters/padme-amidala"),
        ],
        "planets": [planet_link("Naboo")],
        "majorEvents": [
            {"text": "Battle of Naboo — Great Grass Plains", "route": "wars-conflicts/battles/battle-of-naboo"},
        ],
        "films": ["Star Wars: Episode I — The Phantom Menace"],
        "series": ["Star Wars: The Clone Wars (Gungan episodes)"],
        "affiliations": ["Gungan Grand Army", "Naboo planetary defense", "Otoh Gunga cavalry traditions"],
        "timeline": [
            {"era": "Pre-Invasion", "event": "Gungans domesticated kaadu for cavalry and transport"},
            {"era": "32 BBY", "event": "Kaadu charge at the Battle of the Great Grass Plains"},
            {"era": "Clone Wars", "event": "Gungan kaadu units defended Naboo from Separatist incursions"},
            {"era": "Imperial Era", "event": "Kaadu festivals maintained under occupation as quiet resistance"},
        ],
        "gallery": scene_gallery("kaadu", "Kaadu") + [
            extra_gallery("kaadu", "kaadu-jar-jar-binks-riding.webp", "Jar Jar Binks leads Gungan kaadu cavalry at the Battle of Naboo"),
        ],
    }


def _iconic_rancor() -> dict:
    return {
        "overview": (
            "Rancors are towering carnivores native to Dathomir and other Outer Rim worlds — prized by Hutt "
            "crime lords as pit beasts for execution and entertainment. Their thick hides, crushing jaws, and "
            "surprising speed in enclosed spaces make them living weapons that require entire teams to transport "
            "and maintain."
        ),
        "history": (
            "Wild rancors nest in canyon warrens and jungle caves, raising young in communal broods until "
            "adolescents compete for dominance. Hutts import rancors through smuggler networks, often drugging "
            "them for transport and keeping them half-starved to maximize arena aggression. Dathomir's "
            "Nightsisters historically respected rancors as kin rather than pets.\n\n"
            "**Luke Skywalker in Jabba's palace.** When Luke Skywalker, Leia Organa, and Chewbacca infiltrated "
            "Jabba the Hutt's palace on Tatooine to rescue Han Solo from carbonite, Jabba sentenced Luke and "
            "a Weequay guard to death in the rancor pit beneath the throne room. The trapdoor dropped them into "
            "a bone-strewn chamber where Jabba's prized bull rancor — a beast that had eaten many victims — "
            "emerged from its shadowed alcove.\n\n"
            "Luke initially dodged the rancor's crushing claws, but conventional weapons proved useless against "
            "its armored hide. As the gate began to close and the creature cornered him, Luke leaped onto a "
            "boulder, summoned a discarded skull, and crushed the gate-control mechanism — dropping a heavy portcullis "
            "spike directly onto the rancor's neck, killing it instantly. The crowd above fell silent; Jabba, "
            "furious at the loss of his pet, condemned Luke, Han, and Chewie to the Sarlacc instead.\n\n"
            "The rancor keeper Malakili wept for the beast, revealing that even Jabba's monsters could inspire "
            "genuine affection. Luke's victory demonstrated that Jedi resourcefulness could defeat brute force "
            "without a lightsaber drawn — a prelude to the sail barge battle above the Great Pit of Carkoon."
        ),
        "significance": (
            "The rancor pit sequence is Return of the Jedi's first action set piece — grounding the rescue "
            "mission in visceral danger before the larger Sarlacc set piece.\n\n"
            "Rancors became franchise icons through games, comics, and The Book of Boba Fett's exploration "
            "of Malakili and rancor culture.\n\n"
            "Ecologically, rancors illustrate how apex predators become commodified in Hutt criminal economies."
        ),
        "notableEvents": [
            "Luke Skywalker killed Jabba's rancor in the palace pit beneath Tatooine",
            "Malakili the rancor keeper mourned the beast after its death",
            "Jabba sentenced surviving heroes to the Sarlacc following the rancor's defeat",
            "Wild rancors documented on Dathomir, Felucia, and Ottethan",
            "Boba Fett later encountered rancor-related culture on Tatooine",
        ],
        "majorCharacters": [
            character_link("Luke Skywalker", "characters/luke-skywalker"),
            character_link("Jabba the Hutt", "characters/jabba-the-hutt"),
            character_link("Leia Organa", "characters/leia-organa"),
            character_link("Han Solo", "characters/han-solo"),
        ],
        "planets": [planet_link("Tatooine"), planet_link("Dathomir")],
        "majorEvents": [
            {"text": "Rescue of Han Solo from Jabba's palace", "route": "characters/han-solo"},
            {"text": "Great Pit of Carkoon skiff battle", "route": "creatures/sarlacc"},
        ],
        "films": ["Star Wars: Episode VI — Return of the Jedi"],
        "series": ["Star Wars: The Book of Boba Fett", "Star Wars Galaxy of Creatures"],
        "affiliations": ["Hutt palace arenas", "Dathomir wildlife", "Desilijic Kajidic entertainment"],
        "timeline": [
            {"era": "Imperial Era", "event": "Jabba maintained a rancor pit beneath his Tatooine palace"},
            {"era": "4 ABY", "event": "Luke Skywalker killed Jabba's rancor during the rescue mission"},
            {"era": "4 ABY", "event": "Heroes condemned to Sarlacc after rancor defeat"},
            {"era": "New Republic", "event": "Rancor trafficking outlawed on multiple Rim worlds"},
        ],
        "gallery": scene_gallery("rancor", "Rancor") + [
            extra_gallery("rancor", "rancor-luke-skywalker-fight.webp", "Luke Skywalker battles the rancor in Jabba the Hutt's palace pit"),
        ],
    }


def _iconic_sarlacc() -> dict:
    return {
        "overview": (
            "The Sarlacc is a colossal subterranean predator whose Great Pit of Carkoon on Tatooine became "
            "synonymous with Hutt execution rituals. Victims digested over centuries in the creature's belly "
            "suffer a fate Jabba the Hutt described as worse than death — conscious agony in darkness while "
            "the Sarlacc slowly absorbs their life force."
        ),
        "history": (
            "Sarlaccs begin as spores drifting through Tatooine's upper atmosphere before rooting in desert "
            "crust and excavating pits over millennia. Tentacles ring the mouth to snare prey while the main "
            "body extends kilometers underground. Only one Great Pit of Carkoon is confirmed active in modern "
            "records, though legends speak of others buried beneath the Dune Sea.\n\n"
            "**Return of the Jedi — the skiff battle.** After Luke Skywalker killed Jabba's rancor, the Hutt "
            "ordered prisoners transported to the Great Pit of Carkoon on a desert skiff convoy. Luke, Han Solo "
            "(still recovering from hibernation sickness), Chewbacca, and Lando Calrissian (disguised as a guard) "
            "rode the lead skiff toward the pit's maw while Jabba's sail barge hosted spectators above.\n\n"
            "From the skiff's rail, prisoners could see the Sarlacc's tentacles writhing in the sand bowl below — "
            "a yawning maw that had consumed countless bounty hunters and debtors. Jabba demanded they witness "
            "their friends' execution. Instead, Luke — having concealed his new lightsaber in R2-D2 — caught the "
            "weapon mid-air, cut through guards, and sparked the battle that destroyed Jabba's barge and freed "
            "Leia, who had strangled the Hutt with her own chain.\n\n"
            "Boba Fett famously tumbled into the pit during the fight; Mandalorian armor and Sarlacc biology "
            "later became the subject of legend when he escaped decades afterward. Han Solo, half-blind and "
            "uncertain which direction to shoot, nonetheless helped hold the skiff long enough for Luke to "
            "prevail — completing the rescue arc that began in Cloud City.\n\n"
            "The Sarlacc pit remains a pilgrimage site for smugglers and historians, though the creature's "
            "post-Boba status is debated in classified Mandalorian records."
        ),
        "significance": (
            "The Great Pit of Carkoon anchors Return of the Jedi's opening act — reuniting the heroes and "
            "destroying the saga's most iconic crime lord.\n\n"
            "Boba Fett's survival and escape, explored in The Mandalorian and The Book of Boba Fett, turned "
            "the Sarlacc from a death sentence into a decades-long crucible.\n\n"
            "The creature represents Tatooine's harsh mythology: the desert consumes everyone eventually."
        ),
        "notableEvents": [
            "Jabba the Hutt sentenced Luke, Han, and Chewie to execution at the Great Pit of Carkoon",
            "Skiff battle above the Sarlacc during the rescue of Han Solo",
            "Boba Fett fell into the Sarlacc during the fight (later escaped)",
            "Jabba's sail barge destroyed; Leia Organa killed Jabba",
            "Luke Skywalker and allies escaped aboard the party barge",
        ],
        "majorCharacters": [
            character_link("Luke Skywalker", "characters/luke-skywalker"),
            character_link("Han Solo", "characters/han-solo"),
            character_link("Leia Organa", "characters/leia-organa"),
            character_link("Boba Fett", "bounty-hunters/boba-fett"),
            character_link("Jabba the Hutt", "characters/jabba-the-hutt"),
            character_link("Lando Calrissian", "characters/lando-calrissian"),
        ],
        "planets": [planet_link("Tatooine")],
        "majorEvents": [
            {"text": "Rescue mission at Jabba's palace", "route": "characters/han-solo"},
            {"text": "Luke Skywalker vs. the rancor", "route": "creatures/rancor"},
        ],
        "films": ["Star Wars: Episode VI — Return of the Jedi"],
        "series": ["Star Wars: The Book of Boba Fett", "Star Wars: The Mandalorian"],
        "affiliations": ["Hutt execution rituals", "Tatooine Dune Sea ecology", "Bounty hunter legend"],
        "timeline": [
            {"era": "Ancient", "event": "Great Pit of Carkoon Sarlacc established over millennia"},
            {"era": "Imperial Era", "event": "Jabba used the pit for executions and spectacle"},
            {"era": "4 ABY", "event": "Skiff battle and Jabba's death at Carkoon"},
            {"era": "4 ABY–9 ABY", "event": "Boba Fett survived digestion inside the Sarlacc"},
        ],
        "gallery": scene_gallery("sarlacc", "Sarlacc") + [
            extra_gallery("sarlacc", "sarlacc-return-of-the-jedi-skiff.webp", "Rebel heroes on a skiff above the Great Pit of Carkoon"),
        ],
    }


ICONIC.update({
    "wampa": _iconic_wampa(),
    "tauntaun": _iconic_tauntaun(),
    "kaadu": _iconic_kaadu(),
    "rancor": _iconic_rancor(),
    "sarlacc": _iconic_sarlacc(),
})

CHARACTER_STORIES: dict[str, str] = {
    "nexu": "**Geonosis arena.** Nexu were unleashed against Padmé Amidala, Anakin Skywalker, and Obi-Wan Kenobi in the Petranaki arena during the First Battle of Geonosis — their quilled backs and leaping strikes nearly killed the Senator before Jedi intervention.",
    "reek": "**Geonosis arena.** A drugged reek gored Jango Fett during the same execution attempt; Anakin Skywalker later rode the beast against arena predators in one of his first wartime improvisations.",
    "acklay": "**Geonosis arena.** Acklay crustacean predators joined nexu and reeks in the arena sand — their piercing forelimbs tested Jedi reflexes at the opening battle of the Clone Wars.",
    "varactyl": "**Utapau chase.** Obi-Wan Kenobi rode the varactyl Boga across sinkhole ledges while hunting General Grievous — one of the saga's most celebrated mount sequences.",
    "exogorth": "**Asteroid field.** Han Solo piloted the Millennium Falcon into a space slug's maw in the Hoth asteroid belt, escaping only by flying out before the jaws closed.",
    "dianoga": "**Death Star trash compactor.** A dianoga pulled Luke Skywalker underwater in the Death Star's garbage chamber before the walls began closing — one of A New Hope's claustrophobic horror beats.",
    "mudhorn": "**Arvala-7.** Din Djarin fought a mudhorn to protect Grogu during his first quest — the beast's armored skull nearly killed them both before the Child used the Force.",
    "purrgil": "**Hyperspace migration.** Ezra Bridger communed with purrgil in the Unknown Regions, using their natural routes to inspire the Rebels' path to Lothal and later to exile with the pod.",
    "loth-wolf": "**Lothal vergence.** Loth-wolves guided Ezra Bridger through the World Between Worlds, embodying the planet's Living Force during the Liberation of Lothal.",
    "convor": "**Morai and Ahsoka.** Convor birds — especially Morai — shadowed Ahsoka Tano as symbols of the Daughter of Mortis and the light side across the galaxy.",
    "zillo-beast": "**Coruscant rampage.** Palpatine imported a Zillo Beast from Malastare; when it rampaged through the capital, clone forces and Jedi contained it before the Emperor ordered its death for cloning research.",
    "rathtar": "**Eravana haul.** Han Solo's rathtar cargo aboard the Eravana broke loose and devoured gangsters before the Falcon escaped — a chaotic introduction in The Force Awakens.",
    "kowakian-monkey-lizard": "**Jabba's court.** Salacious B. Crumb and other Kowakian monkey-lizards cackled from Jabba's throne, tormenting prisoners and amusing the Hutt crime lord.",
    "porg": "**Ahch-To exile.** Porgs overran the Jedi temple islands where Luke Skywalker lived in exile; Chewbacca roasted one for dinner while Rey befriended the colony.",
    "vulptex": "**Battle of Crait.** Crystal vulptexes led Resistance survivors through salt-crystal caverns during the evacuation after the Battle of Crait.",
    "krykna": "**Atollon siege.** Krykna spider nests forced Phoenix Squadron to abandon Chopper Base when Thrawn's fleet blockaded Atollon.",
    "bantha": "**Tusken culture.** Banthas form sacred bonds with Tusken Raider clans — every warrior's mount is mourned like family upon death.",
    "krayt-dragon": "**Tatooine apex.** Krayt dragons rule the Dune Sea; Obi-Wan Kenobi mimicked a dragon's call to terrify Tusken Raiders away from a young Luke Skywalker.",
    "fyrnock": "**Fort Anaxes.** Clone Wars garrisons on Anaxes learned to seal blast doors before nightfall when fyrnock packs swarmed under artificial light thresholds.",
    "falumpaset": "**Gungan siege engines.** Falumpasets served as living artillery platforms during the Battle of Naboo, carrying heavy booma launchers across the grass plains.",
    "dark-side-spiders": "**Malachor temple.** Dark side spiders haunted the Sith temple on Malachor where Ezra Bridger first wielded the Sith holocron.",
    "ice-spider": "**Ilum harvesting.** Ice spiders nested in Ilum's crystal caves near Jedi kyber harvesting expeditions during the Clone Wars.",
    "steelpecker": "**Jakku scavenging.** Steelpeckers stripped Star Destroyer ribs on Jakku, nesting in the graveyard fleet that defined Rey's childhood.",
    "vornskr": "**Force tracking.** Talon Karrde's vornskrs hunted Jedi by Force scent during the Thrawn campaigns in Legends-adjacent lore adapted for modern guides.",
    "blurrg": "**Ryloth cavalry.** Twi'lek freedom fighters and Mandalorian clans rode blurrg mounts across frontier battlefields.",
    "sando-aqua-monster": "**Naboo depths.** Sando aqua monsters dwarfed Trade Federation submersibles during the planetary invasion — leviathans of the core lakes.",
    "opee-sea-killer": "**Naboo abyss.** Opee sea killers ambushed underwater craft with extensible tongue-lures in the teal depths beneath Gungan shields.",
    "colo-claw-fish": "**Naboo oceans.** Colo claw fish patrolled bioluminescent trenches where Jedi and Gungan scouts tested bongo submersibles.",
    "aiwha": "**Kamino storms.** Aiwha cetaceans skimmed Kamino's endless oceans beneath the platform cities where clone troopers were bred.",
    "gundark": "**Jungle terror.** Gundarks were proverbial for rage — 'You're as reckless as a gundark' became a common Core Worlds insult.",
    "wyyyschokk": "**Kashyyyk canopy.** Wyyyschokk tree spiders threatened Wookiee climbers and Clone Wars patrols in the high forest.",
    "roggwart": "**Hutt guards.** Roggwarts chained as palace guard beasts lunged from murky pools in Hutt fortresses across the Outer Rim.",
    "charhound": "**Elphrona wastes.** Charhounds tracked prey across volcanic plains with ember-glow eyes adapted to extreme heat.",
    "dewback": "**Imperial patrols.** Sandtroopers rode dewbacks at dawn on Tatooine when repulsorlift engines overheated in the double-sun heat.",
    "eopie": "**Jawa trade.** Jawas used eopies to haul scavenged droid parts across the Dune Sea between sandcrawler camps.",
    "ronto": "**Desert caravans.** Rontos hauled cargo between Mos Eisley and moisture farms — stubborn but dependable Tatooine transport.",
    "happabore": "**Jakku draught.** Happabores pulled salvage sleds across Jakku's flats for Unkar Plutt's operation and other scavenger bosses.",
    "nuna": "**Naboo farms.** Nuna birds were farmed across Naboo for meat and sport — their waddling herds dotted the pastoral countryside.",
    "tusk-cat": "**Naboo plains.** Tusk cats stalked Naboo's grasslands and appeared in Gungan ceremonial hunts alongside kaadu riders.",
    "loth-cat": "**Lothal grasslands.** Loth-cats hunted rodents near Lothal settlements; some exhibited Force sensitivity tied to the planet's vergence.",
    "loth-bat": "**Lothal nights.** Loth-bats filled the grasslands after dusk, roosting in cliff colonies near Imperial mining sites.",
    "tooka-cat": "**Galactic pets.** Tooka cats were sold as pets across the galaxy; Lothal's tooka dolls became symbols of childhood under occupation.",
    "bogling": "**Swamp scavengers.** Boglings nested in rotting marsh timber on Dagobah-like worlds, startling travelers with chirping calls.",
    "mynock": "**Power parasites.** Mynocks chewed starship power cables in asteroid caves — the Falcon's infestation forced repairs from Ord Mantell to Bespin.",
}


MAJOR_CHARACTERS: dict[str, list[dict[str, str]]] = {
    "nexu": [
        character_link("Padmé Amidala", "characters/padme-amidala"),
        character_link("Anakin Skywalker", "characters/anakin-skywalker"),
        character_link("Obi-Wan Kenobi", "characters/obi-wan-kenobi"),
    ],
    "reek": [
        character_link("Anakin Skywalker", "characters/anakin-skywalker"),
        character_link("Jango Fett", "bounty-hunters/jango-fett"),
    ],
    "acklay": [
        character_link("Obi-Wan Kenobi", "characters/obi-wan-kenobi"),
        character_link("Anakin Skywalker", "characters/anakin-skywalker"),
    ],
    "varactyl": [
        character_link("Obi-Wan Kenobi", "characters/obi-wan-kenobi"),
        character_link("General Grievous", "characters/general-grievous"),
    ],
    "exogorth": [character_link("Han Solo", "characters/han-solo"), character_link("Leia Organa", "characters/leia-organa")],
    "dianoga": [character_link("Luke Skywalker", "characters/luke-skywalker"), character_link("Han Solo", "characters/han-solo")],
    "mudhorn": [character_link("Din Djarin", "characters/din-djarin"), character_link("Grogu", "characters/grogu")],
    "purrgil": [character_link("Ezra Bridger", "characters/ezra-bridger")],
    "loth-wolf": [character_link("Ezra Bridger", "characters/ezra-bridger")],
    "convor": [character_link("Ahsoka Tano", "characters/ahsoka-tano")],
    "zillo-beast": [character_link("Palpatine", "characters/sheev-palpatine"), character_link("Anakin Skywalker", "characters/anakin-skywalker")],
    "rathtar": [character_link("Han Solo", "characters/han-solo")],
    "kowakian-monkey-lizard": [character_link("Jabba the Hutt", "characters/jabba-the-hutt")],
    "porg": [character_link("Luke Skywalker", "characters/luke-skywalker"), character_link("Chewbacca", "characters/chewbacca")],
    "vulptex": [character_link("Luke Skywalker", "characters/luke-skywalker")],
    "krayt-dragon": [character_link("Obi-Wan Kenobi", "characters/obi-wan-kenobi"), character_link("Luke Skywalker", "characters/luke-skywalker")],
    "falumpaset": [character_link("Boss Nass", "characters/boss-nass")],
    "bantha": [character_link("Tusken Raider", "species/tusken-raider")],
}


def build_standard_profile(creature: dict[str, str]) -> dict:
    name = creature["Name"]
    slug = creature["Slug"]
    habitat = creature["Habitat"]
    homeworld = creature["Homeworld"]
    desc = creature["Description"]

    char_story = CHARACTER_STORIES.get(slug, "")
    history_extra = f"\n\n{char_story}" if char_story else ""

    overview = (
        f"The {name} is a distinctive species of the {habitat.lower()} biome, native to {homeworld}. "
        f"{desc} Across the saga films, live-action series, and animated chronicles, {name.lower()} "
        f"specimens appear in ecological surveys, military campaigns, and frontier settlements — "
        f"embodying the biological diversity that makes the Star Wars galaxy feel lived-in and ancient."
    )

    history = (
        f"Xenobiologists classify {name.lower()} populations across {homeworld} within the broader "
        f"{habitat.lower()} ecological band. Their anatomy reflects millions of years of adaptation to "
        f"local climate, predator pressure, and food-chain position — whether as apex hunter, domestic "
        f"mount, scavenger, or symbiotic partner to sentient cultures.\n\n"
        f"Galactic records document {name.lower()} interactions with explorers, militaries, and "
        f"indigenous peoples from the Old Republic through the First Order era. Traders, hunters, and "
        f"documentarians filed holo-surveys that now populate the Archives of the New Republic "
        f"Xenobiology Division.\n\n"
        f"In campaign histories, {name.lower()} often appear at the margins of major battles — as "
        f"obstacles, allies, mounts, or environmental hazards that shaped tactical decisions. "
        f"Soldiers learned quickly that underestimating local fauna could be as fatal as blaster fire."
        f"{history_extra}\n\n"
        f"Conservationists debate protection status for {name.lower()} on worlds undergoing "
        f"industrialization. The Empire rarely cared; the New Republic sometimes does — especially "
        f"where species hold cultural significance for indigenous populations."
    )

    significance = (
        f"{name} enriches the {habitat.lower()} identity of {homeworld} within Star Wars worldbuilding — "
        f"grounding fantastical settings in believable ecology.\n\n"
        f"Creatures like the {name.lower()} remind audiences that the galaxy is not empty backdrop "
        f"but a network of ecosystems interacting with politics, war, and Force tradition.\n\n"
        f"For roleplayers, scouts, and lore enthusiasts, {name.lower()} entries connect planetary "
        f"surveys to character stories across nine saga films and dozens of series."
    )

    notable = [
        f"Documented on {homeworld} in {habitat.lower()} surveys",
        f"Referenced in galactic bestiary holocrons and scout manuals",
        desc.split(";")[0].strip() if ";" in desc else desc[:120],
        f"Catalogued in New Republic xenobiology archives",
        f"Featured in creature guides spanning films and series",
        f"Habitat classification: {habitat}",
    ]

    timeline = [
        {"era": "Old Republic", "event": f"Early surveys catalogued {name.lower()} on {homeworld}"},
        {"era": "Clone Wars", "event": f"Military campaigns recorded {name.lower()} encounters"},
        {"era": "Imperial Era", "event": f"Imperial resource extraction threatened {name.lower()} habitats"},
        {"era": "New Republic", "event": f"Conservation debates resumed for {name.lower()} populations"},
    ]

    planets = []
    if homeworld.lower() not in {"various", "unknown regions", "asteroid fields", "unknown"}:
        for part in homeworld.split(","):
            planets.append(planet_link(part.strip()))

    profile = {
        "overview": overview,
        "history": history,
        "significance": significance,
        "notableEvents": notable,
        "affiliations": [habitat, homeworld, "Galactic xenobiology records"],
        "timeline": timeline,
        "planets": planets,
        "films": ["Star Wars saga films (various appearances)"],
        "series": SERIES[:3],
        "gallery": scene_gallery(slug, name),
    }
    if slug in MAJOR_CHARACTERS:
        profile["majorCharacters"] = MAJOR_CHARACTERS[slug]
    return profile


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    creatures = parse_creatures()
    for creature in creatures:
        slug = creature["Slug"]
        profile = ICONIC.get(slug) or build_standard_profile(creature)
        path = OUTPUT / f"{slug}.json"
        path.write_text(json.dumps(profile, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Wrote {path.name}")
    print(f"Generated {len(creatures)} creature profiles")


if __name__ == "__main__":
    main()
