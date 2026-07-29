#!/usr/bin/env python3
"""Hand-authored extended profiles for Galactic History chronicle eras."""

from __future__ import annotations


def L(
    label: str,
    value: str,
    route: str,
    *,
    emphasized: bool = False,
    emphasis_tone: str = "",
) -> dict[str, str | bool]:
    item: dict[str, str | bool] = {"label": label, "value": value, "route": route}
    if emphasized:
        item["emphasized"] = True
    if emphasis_tone:
        item["emphasisTone"] = emphasis_tone
    return item


SITH_EMPIRE_PLANETS: list[tuple[str, str]] = [
    ("Dromund Kaas", "planet/dromund-kaas"),
    ("Korriban", "korriban"),
    ("Ziost", "planet/ziost"),
    ("Moraband", "planet/moraband"),
    ("Nathema", "planet/nathema"),
    ("Yavin 4", "planet/yavin-4"),
    ("Ossus", "planet/ossus"),
    ("Malachor V", "planet/malachor-v"),
    ("Byss", "planet/byss"),
    ("Thule", "planet/thule"),
    ("Rhelg", "planet/rhelg"),
    ("Ch'hodos", "planet/ch-hodos"),
    ("Krayiss II", "planet/krayiss-ii"),
    ("Khar Delba", "planet/khar-delba"),
    ("Khar Shian", "planet/khar-shian"),
    ("Jaguada", "planet/jaguada"),
    ("Ashas Ree", "planet/ashas-ree"),
    ("Athiss", "planet/atthiss"),
    ("Begeren", "planet/begeren"),
    ("Bosthirda", "planet/bosthirda"),
    ("Dromund Fels", "planet/dromund-fels"),
    ("Dromund Ixin", "planet/dromund-ixin"),
    ("Dromund Kalakar", "planet/dromund-kalakar"),
    ("Dromund Tyne", "planet/dromund-tyne"),
    ("Kalsunor", "planet/kalsunor"),
    ("Korriz", "planet/korriz"),
    ("Nfolgai", "planet/nfolgai"),
]


def E(text: str, route: str = "") -> dict[str, str]:
    return {"text": text, "route": route}


def G(slug: str, caption: str) -> dict[str, str]:
    return {"path": f"/images/chronicles/{slug}-scene.webp", "caption": caption}


def GL(
    value: str,
    route: str = "",
    *,
    emphasized: bool = False,
    emphasis_tone: str = "",
) -> dict[str, str | bool]:
    item: dict[str, str | bool] = {"value": value, "route": route}
    if emphasized:
        item["emphasized"] = True
    if emphasis_tone:
        item["emphasisTone"] = emphasis_tone
    return item


def get_chronicle_profiles() -> dict[str, dict]:
    return {
        "dawn-of-the-jedi": {
            "dateRange": "c. 36,453 BBY – c. 25,000 BBY",
            "government": GL("Je'daii Order", "governments/jedaii-order"),
            "headOfState": GL("Je'daii Temple Masters", "governments/jedaii-order"),
            "overview": (
                "The Dawn of the Jedi era marks the deepest recorded stratum of Force tradition in "
                "galactic history — a time before the Republic, before the Sith Empire, and before "
                "the words 'Jedi' and 'Sith' had hardened into opposing orders. On [Tython](planet/tython), "
                "Force-sensitive settlers discovered that the energy binding all life could be "
                "studied, balanced, and channeled through discipline rather than superstition."
            ),
            "history": (
                "Galactic civilization in this epoch was shaped less by unified government than by "
                "the Tho Yor — mysterious pyramidal vessels that gathered Force-sensitive beings "
                "from across the galaxy and deposited them on Tython. There, amid nine distinct "
                "Temples aligned to the planet's moons and Force nexuses, the Je'daii Order arose. "
                "They named the light side Ashla and the dark side Bogan, teaching that imbalance "
                "between the two invited catastrophe — a philosophy that would echo in the later "
                "[Jedi Code](the-force/jedi-code) and its shadow counterpart, the [Sith Code](the-force/sith-code).\n\n"
                "Je'daii society was itinerant and rigorous. Adepts traveled between Temples — "
                "Mahra Kesh for alchemy, Anil Kesh for science, Kaleth for philosophy — and were "
                "exiled to Tython's moon Ashla or Bogan when they fell too far toward one pole of "
                "the Force. This institutional balance was not pacifism; Je'daii masters wielded "
                "swords, staves, and early forms of what would become lightsaber combat when "
                "metal-forging and Adegan crystal lore matured on worlds like Ilum.\n\n"
                "The Rakata Infinite Empire cast a long shadow across pre-Republic space. Using "
                "Force-powered hyperdrive technology and enslaving countless species, the Rakata "
                "built Star Forge-scale monuments and seeded worlds with their architecture. Their "
                "empire's collapse — brought on by a plague that severed their Force sensitivity — "
                "left hyperspace routes fractured and worlds like Lehon (Rakata Prime) abandoned, "
                "but their legacy of dark-side superweapons haunted later ages.\n\n"
                "The schism that ended the Je'daii golden age began when a faction led by "
                "Ajunta Pall and other Dark Jedi rejected exile and embraced Bogan as a path to "
                "power rather than a warning. Cast out after the Hundred-Year Darkness, these "
                "exiles conquered the Sith species on Korriban and interbred with them, forging "
                "the first Sith Lords. Their departure from Tython did not destroy Je'daii culture "
                "overnight, but it permanently split the galaxy's Force traditions into competing "
                "bloodlines of light and darkness.\n\n"
                "By roughly 25,000 BBY, the Je'daii had evolved into the Jedi Order as historians "
                "later understood it — monastic, temple-centered, and increasingly aligned with "
                "the emerging Galactic Republic's democratic ideals. Ossus became a great library "
                "world; Tython itself would be abandoned and revisited across millennia whenever "
                "the Order sought its forgotten roots.\n\n"
                "Legends sources such as *Star Wars: Dawn of the Jedi* and the *Je'daii* comic "
                "series flesh out characters like Xesh, Daegen Lok, and Shae Koda, while modern "
                "canon references in *The Acolyte* and High Republic materials treat Tython and "
                "the balance philosophy as living precedents for every later debate about "
                "attachment, prophecy, and the danger of suppressing the dark side rather than "
                "understanding it."
            ),
            "significance": (
                "Every subsequent Force tradition in Star Wars is, in some sense, a footnote to "
                "decisions made on Tython. The Je'daii's insistence on balance explains why later "
                "Jedi feared emotional attachment, why Sith define freedom through passion, and "
                "why the galaxy keeps rediscovering the same lesson: unchecked power — light or "
                "dark — reshapes civilization at catastrophic scale.\n\n"
                "The era also anchors the franchise's deepest timeline, connecting Rakatan "
                "hyperdrive lore, Sith species mythology, and the Republic founding narrative "
                "into a single archaeological layer fans and in-universe scholars mine for "
                "precedent whenever a new crisis threatens galactic order.\n\n"
                "For roleplaying games and reference works, the Dawn of the Jedi provides a "
                "sandbox unburdened by film continuity — a place to explore what the Force "
                "might have been before lightsabers, before the Rule of Two, and before Palpatine "
                "proved how fragile democracy could be."
            ),
            "majorEvents": [
                E(
                    "Tho Yor gather Force-sensitives on Tython; Je'daii Order founded",
                ),
                E(
                    "Rakata Infinite Empire dominates known space before plague-induced collapse",
                ),
                E(
                    "Hundred-Year Darkness — Dark Jedi schism and exile from Tython",
                    "wars-conflicts/hundred-year-darkness",
                ),
                E(
                    "Exiled Dark Jedi conquer Korriban and become the first Sith Lords",
                ),
                E(
                    "Je'daii transition toward the early Jedi Order; Republic founding era begins",
                ),
            ],
            "keyFactions": [],
            "majorCharacters": [
                L("Sith", "Ajunta Pall", "sith/ajunta-pall"),
            ],
            "planets": [
                L("Planet", "Tython", "planet/tython"),
                L("Planet", "Korriban", "korriban"),
                L("Planet", "Ossus", "planet/ossus"),
            ],
            "ships": [],
            "films": [],
            "series": ["Star Wars: The Acolyte (references to ancient Force traditions)"],
            "games": [
                "Star Wars: The Old Republic (ancient history codex entries)",
            ],
            "books": [
                "Star Wars: Dawn of the Jedi — Into the Void (Legends novel)",
                "Star Wars: Dawn of the Jedi — Force Storm (Legends comic series)",
            ],
            "timeline": [
                {"era": "c. 36,453 BBY", "event": "Tho Yor arrive on Tython; Je'daii Order established"},
                {"era": "c. 30,000 BBY", "event": "Rakata Infinite Empire reaches its zenith"},
                {"era": "c. 25,793 BBY", "event": "Hundred-Year Darkness begins"},
                {"era": "c. 25,000 BBY", "event": "Exiles found Sith culture on Korriban"},
                {"era": "c. 25,000 BBY", "event": "Galactic Republic founding era opens"},
            ],
            "gallery": [
                G("dawn-of-the-jedi", "Je'daii Temples on Tython beneath the planet's twin moons"),
            ],
        },
        "old-sith-empire": {
            "dateRange": "c. 6,900 BBY – 5,000 BBY",
            "government": GL("Dark Council", "governments/dark-council"),
            "headOfState": GL(
                "Sith Emperor",
                "sith/darth-vitiate",
                emphasized=True,
                emphasis_tone="sith",
            ),
            "overview": (
                "The Old Sith Empire was the first galactic dominion built explicitly on the dark "
                "side — a theocratic war-state born from exiled Dark Jedi and the native Sith "
                "species of Korriban. Its Golden Age saw Sith sorcery, alchemy, and mass-produced "
                "war fleets challenge the young Republic across the stars until hubris and "
                "internal rivalry shattered Sith unity forever."
            ),
            "history": (
                "After the Hundred-Year Darkness, Ajunta Pall and his followers landed on Korriban "
                "and were worshipped by the red-skinned Sith as gods. Over generations the "
                "exiles intermarried with the Sith species, creating a hybrid culture that "
                "worshipped the dark side as divine will. Korriban became a necropolis of "
                "tombs; Ziost, the ancient capital, pulsed with Sithspawn experiments and "
                "ritual sacrifice.\n\n"
                "Marka Ragnos's reign epitomized the Sith Golden Age — centuries of expansion "
                "into the Stygian Caldera while the Republic remained unaware of the threat "
                "brewing beyond the Rim. When Ragnos died, Naga Sadow and Ludo Kressh fought "
                "a succession war that weakened the empire at the worst possible moment. "
                "Sadow's discovery of hyperspace routes to the Republic Core precipitated "
                "the Great Hyperspace War — an invasion that reached as far as Coruscant before "
                "Republic and Jedi forces rallied.\n\n"
                "The Republic's counterattack devastated Sadow's fleets and bombarded Sith "
                "worlds. Sadow fled to Yavin 4, where he placed himself in suspended animation "
                "inside a temple complex that would later entomb Exar Kun. The Sith Empire "
                "on Korriban collapsed; survivors fled into the Unknown Regions aboard "
                "generation ships, seeding the exile culture that would eventually produce "
                "Darth Vitiate's Sith Empire in Legends continuity.\n\n"
                "Centuries later, Freedon Nadd — a fallen Jedi — recovered Sadow's teachings "
                "and conquered Onderon, embedding Sith worship in that world's monarchy. His "
                "spirit would corrupt Exar Kun, who raided Ossus's Great Jedi Library, "
                "forged a Sith amulet, and launched the Great Sith War alongside the "
                "Krath cult and Mandalorian Crusaders. Kun's Brotherhood of the Sith "
                "burned across the galaxy until the combined Jedi Order, led by Nomi Sunrider "
                "and Odan-Urr, trapped his spirit on Yavin 4.\n\n"
                "The Stark Hyperspace War — a corporate banking crisis manipulated by Sith "
                "agents — demonstrated that economic warfare could destabilize the Republic "
                "without open fleet battles. Though shorter than the Great Sith War, it "
                "revealed how deeply Sith influence could penetrate Core politics.\n\n"
                "By 5,000 BBY the Old Sith Empire as a territorial state was gone, but its "
                "cultural DNA persisted: holocrons buried on desert worlds, Sith swords in "
                "private collections, and the enduring myth that the dark side could build "
                "empires faster than the light could legislate them away."
            ),
            "significance": (
                "The Old Sith Empire established the template for every later dark-side "
                "hegemony — from Exar Kun's Brotherhood to Palpatine's Galactic Empire. "
                "Its fall taught the Jedi that victory over Sith armies did not extinguish "
                "Sith ideology; it merely drove it underground.\n\n"
                "Naga Sadow's invasion and Exar Kun's war are the earliest galactic-scale "
                "conflicts in the timeline, proving that the Republic was never inherently "
                "safe — only temporarily unthreatened. The mass exodus of Sith into the "
                "Unknown Regions also foreshadows the First Order's later emergence from "
                "Imperial exile.\n\n"
                "For fans of Legends material, this era is the backbone of the *Tales of the "
                "Jedi* animated stories, *Knights of the Old Republic* flashback lore, and "
                "countless reference works on Sith alchemy and holocron tradition."
            ),
            "majorEvents": [
                E(
                    "Marka Ragnos's Golden Age consolidates Sith dominion in the Outer Rim",
                ),
                E(
                    "Great Hyperspace War — Naga Sadow invades the Republic Core",
                    "wars-conflicts/great-sith-war",
                ),
                E(
                    "Republic counterattack shatters the Sith Empire; survivors flee to the Unknown Regions",
                ),
                E(
                    "Great Sith War — Exar Kun and Ulic Qel-Droma devastate the Republic",
                    "wars-conflicts/great-sith-war",
                ),
                E(
                    "Stark Hyperspace War — Sith-manipulated financial crisis strikes the Core",
                    "wars-conflicts/stark-hyperspace-war",
                ),
            ],
            "keyFactions": [],
            "majorCharacters": [
                L("Sith Emperor", "Darth Vitiate", "sith/darth-vitiate", emphasized=True, emphasis_tone="sith"),
                L("Sith", "Naga Sadow", "sith/naga-sadow"),
                L("Sith", "Exar Kun", "sith/exar-kun"),
                L("Sith", "Marka Ragnos", "sith/marka-ragnos"),
                L("Sith", "Ludo Kressh", "sith/ludo-kressh"),
                L("Sith", "Freedon Nadd", "sith/freedon-nadd"),
                L("Sith", "Ajunta Pall", "sith/ajunta-pall"),
            ],
            "planets": [L("Planet", name, route) for name, route in SITH_EMPIRE_PLANETS],
            "ships": [
                L("Ship", "Sith Interceptor", "ships/sith-interceptor"),
            ],
            "films": [],
            "series": ["Star Wars: Tales of the Jedi (Legends / reference)"],
            "games": [
                "Star Wars: Knights of the Old Republic",
                "Star Wars: Knights of the Old Republic II — The Sith Lords",
            ],
            "books": [
                "Tales of the Jedi comic series (Legends)",
                "The Sith War (Legends comic arc)",
            ],
            "timeline": [
                {"era": "c. 6,900 BBY", "event": "Sith Golden Age under Marka Ragnos"},
                {"era": "5,000 BBY", "event": "Great Hyperspace War devastates Sith space"},
                {"era": "3,996 BBY", "event": "Exar Kun declares himself Dark Lord of the Sith"},
                {"era": "3,996–3,994 BBY", "event": "Great Sith War ravages the Republic"},
                {"era": "c. 44 BBY", "event": "Stark Hyperspace War (Legends dating)"},
            ],
            "gallery": [
                G("old-sith-empire", "Sith war fleets mass above Korriban during the Golden Age"),
            ],
        },
        "old-republic": {
            "dateRange": "c. 25,000 BBY – c. 1,000 BBY",
            "government": GL("Galactic Senate", "governments/galactic-senate"),
            "headOfState": GL("Supreme Chancellor", "governments/galactic-senate"),
            "overview": (
                "The Old Republic era spans more than twenty-four millennia of democratic "
                "experiment — from the unification of the Core Worlds through countless Jedi–Sith "
                "conflicts, Mandalorian crusades, and the final New Sith Wars that ended with "
                "Darth Bane's Rule of Two and the Ruusan Reformations. For most of this period "
                "the Republic was the default condition of civilized space, guarded by a Jedi "
                "Order that evolved from frontier knights into galactic peacekeepers."
            ),
            "history": (
                "The founding of the Galactic Republic united disparate Core systems under a "
                "single Senate and judiciary, with the Jedi Order serving as voluntary "
                "mediators rather than rulers. Early expansion along newly charted hyperspace "
                "lanes brought member worlds from the Colonies into the Mid Rim, but the "
                "process was never bloodless — corporate exploitation, slavery in the Outer Rim, "
                "and periodic Sith resurgences tested the Republic's ideals from the beginning.\n\n"
                "The Mandalorian Wars of 3,964–3,960 BBY exposed a fatal flaw in Jedi doctrine. "
                "When the warrior clans of Mandalore the Ultimate swept through the Outer Rim, "
                "the Jedi Council refused to intervene — but Revan and Malak defied the Order, "
                "leading rogue knights to victory at terrible moral cost. Revan's fall to the "
                "dark side, Malak's destruction of Taris, and the Star Forge crisis on Lehon "
                "became cautionary tales cited for centuries whenever Jedi debated preemptive war.\n\n"
                "The Great Galactic War (3,681–3,653 BBY) and subsequent Cold War pitted a "
                "restored Sith Empire — hidden since the Hyperspace War — against a Republic "
                "already scarred by Mandalorian and Jedi civil conflicts. Battles on Coruscant "
                "itself, the sacking of the Jedi Temple, and the treachery of Sith politics "
                "defined the *Star Wars: The Old Republic* era. The [Sith Code](the-force/sith-code) "
                "and [Jedi Code](the-force/jedi-code) were not abstract texts here; they were "
                "marching orders for armies numbering in the billions.\n\n"
                "Between these galactic wars, the Republic endured brushfire conflicts, "
                "corporate privatization of security forces, and the slow drift of Rim worlds "
                "toward separatist sentiment. The Jedi rebuilt temples, trained padawans on "
                "Coruscant, and maintained the Great Library on Ossus until its destruction "
                "during Exar Kun's campaign — later replaced by archives on Telos and the "
                "Jedi Temple itself.\n\n"
                "The New Sith Wars (c. 2,000–1,000 BBY) — also called the Sith Wars or "
                "Brotherhood of Darkness era — reduced vast regions of the galaxy to "
                "battlefields. Sith Lords multiplied under Kaan's Brotherhood, abandoning "
                "Bane's eventual philosophy of secrecy for open warfare. The final campaign "
                "on Ruusan consumed both armies in a thought bomb's annihilation, leaving "
                "Darth Bane the sole surviving Sith Lord. His Rule of Two — master and "
                "apprentice, hidden until the moment of galactic conquest — reshaped Sith "
                "strategy for the next thousand years.\n\n"
                "The Ruusan Reformations (~1,000 BBY) demilitarized the Republic, reorganized "
                "the Jedi as peacekeepers rather than generals, and began the millennium of "
                "relative stability that Palpatine would exploit. Yoda, already centuries old, "
                "trained generations of Jedi in this new era — an unbroken chain leading "
                "directly to the prequel trilogy's tragedy."
            ),
            "significance": (
                "The Old Republic is the galaxy's longest experiment in democratic governance "
                "at interstellar scale. Its successes — trade, diplomacy, cultural exchange — "
                "and failures — inequality, militarization, Sith infiltration — explain every "
                "political argument in the Skywalker saga.\n\n"
                "Revan, Malak, Bane, and the Ruusan Reformations are hinge points that connect "
                "Legends games and novels to film canon. Without Bane's Rule of Two, Palpatine "
                "and Vader's dyad makes no sense; without the Mandalorian Wars, Revan's mask "
                "and the Jedi Council's caution in the Clone Wars lose their historical weight.\n\n"
                "The era also grounds the Jedi Order's identity: guardians who learned, again "
                "and again, that refusing to fight could be as catastrophic as fighting without "
                "restraint."
            ),
            "majorEvents": [
                E(
                    "Galactic Republic founded; Core Worlds unified under the Senate",
                ),
                E(
                    "Mandalorian Wars — Revan and Malak defy the Jedi Council",
                    "wars-conflicts/mandalorian-wars",
                ),
                E(
                    "Great Galactic War — restored Sith Empire invades the Republic",
                    "wars-conflicts/great-galactic-war",
                ),
                E(
                    "New Sith Wars — Brotherhood of Darkness ravages the galaxy",
                    "wars-conflicts/new-sith-wars",
                ),
                E(
                    "Ruusan Reformations — Darth Bane's Rule of Two begins; Jedi reformed",
                ),
            ],
            "keyFactions": [
                L("Faction", "Galactic Republic", "factions/republic"),
            ],
            "majorCharacters": [
                L("Jedi", "Yoda", "jedi/yoda", emphasized=True, emphasis_tone="jedi"),
                L("Jedi", "Bastila Shan", "jedi/bastila-shan"),
                L("Jedi", "Jolee Bindo", "jedi/jolee-bindo"),
                L("Jedi", "Meetra Surik", "jedi/meetra-surik"),
                L("Jedi", "Satele Shan", "jedi/satele-shan"),
                L("Jedi", "Revan", "jedi/revan"),
                L("Republic", "Carth Onasi", "characters/carth-onasi"),
                L("Sith", "Darth Revan", "sith/darth-revan"),
                L("Sith", "Darth Malak", "sith/darth-malak"),
                L("Sith", "Sith Emperor", "sith/darth-vitiate"),
                L("Sith", "Darth Malgus", "sith/darth-malgus"),
                L("Sith", "Darth Nihilus", "sith/darth-nihilus"),
                L("Sith", "Darth Sion", "sith/darth-sion"),
                L("Sith", "Darth Traya", "sith/darth-traya"),
                L("Sith", "Ulic Qel-Droma", "sith/ulic-qel-droma"),
                L("Sith", "Darth Bane", "sith/darth-bane"),
                L("Sith", "Darth Zannah", "sith/darth-zannah"),
            ],
            "planets": [
                L("Planet", "Coruscant", "coruscant"),
                L("Planet", "Ruusan", "planet/ruusan"),
                L("Planet", "Dxun", "planet/dxun"),
                L("Planet", "Malachor V", "planet/malachor-v"),
                L("Planet", "Telos", "planet/telos"),
            ],
            "ships": [
                L("Ship", "Hammerhead Corvette", "ships/hammerhead-corvette"),
            ],
            "films": [],
            "series": [],
            "games": [
                "Star Wars: Knights of the Old Republic",
                "Star Wars: Knights of the Old Republic II — The Sith Lords",
                "Star Wars: The Old Republic",
            ],
            "books": [
                "Darth Bane: Path of Destruction (Legends novel)",
                "The Old Republic novel series",
                "Revan (Legends novel)",
            ],
            "timeline": [
                {"era": "c. 25,000 BBY", "event": "Galactic Republic founded"},
                {"era": "3,964 BBY", "event": "Mandalorian Wars begin in the Outer Rim"},
                {"era": "3,681 BBY", "event": "Great Galactic War opens with Sith invasion"},
                {"era": "c. 2,000 BBY", "event": "New Sith Wars erupt across multiple sectors"},
                {"era": "~1,000 BBY", "event": "Ruusan cataclysm; Bane establishes Rule of Two"},
            ],
            "gallery": [
                G("old-republic", "Hammerhead corvettes and Jedi starfighters over Ruusan"),
            ],
        },
        "high-republic": {
            "dateRange": "c. 500 BBY – c. 100 BBY",
            "government": GL("Galactic Senate", "governments/galactic-senate"),
            "headOfState": GL("Supreme Chancellor Lina Soh", "governments/galactic-senate"),
            "overview": (
                "The High Republic was a zenith of Jedi idealism and Republic expansion — an age "
                "when the Order served openly as heroes of the frontier, Starlight Beacons guided "
                "hyperspace lanes, and Chancellor Lina Soh's Great Hyperspace Rush promised "
                "prosperity from the Core to the Rim. It ended not in one decisive battle but in "
                "the slow revelation that optimism without vigilance could breed horrors like "
                "the Nihil, the Drengir, and the Nameless."
            ),
            "history": (
                "Centuries before the Trade Federation blockaded Naboo, the Republic entered "
                "what modern historians call the High Republic — a period of confident "
                "expansion unmatched in later eras. The Jedi were public figures: marshals, "
                "diplomats, and symbols of justice who worked alongside the Senate rather "
                "than hiding in a Coruscant temple. Chancellor Soh championed the Starlight "
                "Beacon program — massive space stations that served as navigational "
                "lighthouses, trade hubs, and diplomatic embassies in the Outer Rim.\n\n"
                "Jedi Masters like Avar Kriss, Stellan Gios, and Elzar Mann embodied the "
                "era's spirit. Kriss's Force network — a choral binding of Jedi wills — "
                "demonstrated cooperative light-side technique at galactic scale. The "
                "[Jedi Code](the-force/jedi-code) was lived openly: protect, serve, and "
                "trust in the Force without the paranoia that would later define the prequel "
                "Council. Padawans traveled Rim worlds as celebrated helpers, not secretive monks.\n\n"
                "The Great Hyperspace Rush opened new routes and settlements, but it also "
                "outpaced governance. Colonists on worlds like Elphrona and Sedri Minor faced "
                "pirates, slavers, and environmental catastrophe without adequate Republic "
                "defense. The Jedi stretched thin — a strategic vulnerability the Nihil "
                "marauders exploited with cruel precision.\n\n"
                "Marchion Ro, heir to an ancient Force-hating tradition, united the Nihil "
                "under stormlike raids that weaponized hyperspace anomalies. The destruction "
                "of Starlight Beacon and the Legacy Run disaster — a passenger liner torn "
                "apart in hyperspace — shattered the era's complacency. Parallel threats "
                "emerged: the Drengir, plant-like dark-side entities awakened from "
                "imprisonment, and the Nameless — creatures that consumed Force users and "
                "could not be sensed through the Force at all.\n\n"
                "By the time Yoda ascended to the Jedi Council's senior ranks (~100 BBY), "
                "the High Republic's open idealism had already faded. The Order retreated "
                "into caution, attachment restrictions hardened, and frontier expansion slowed. "
                "The seeds of the Clone Wars — centralized emergency powers, corporate "
                "military influence, and Jedi politicization — were planted in the backlash "
                "to High Republic hubris.\n\n"
                "Canon novels, comics, and the *Young Jedi Adventures* series document this "
                "era in detail, while Legends material offers no direct counterpart — making "
                "the High Republic Lucasfilm's primary sandbox for exploring Jedi history "
                "between the Old Republic wars and the prequel trilogy."
            ),
            "significance": (
                "The High Republic reframes the Jedi as beloved rather than suspicious — "
                "a necessary context for understanding why the galaxy mourned their fall "
                "during Order 66 and why Luke Skywalker's restoration carried such symbolic "
                "weight.\n\n"
                "It connects ancient threats (Nameless, Drengir) to modern storytelling, "
                "suggesting that the dark side evolves in forms lightsabers alone cannot "
                "solve. The era's failure modes — overextension, celebrity culture among "
                "Jedi, and Rim neglect — mirror the late Republic's flaws in miniature.\n\n"
                "For readers and viewers, the High Republic proves that Star Wars history "
                "is not a straight decline from golden age to Empire; it is a cycle of "
                "hope, catastrophe, and cautious rebuilding that repeats across millennia."
            ),
            "majorEvents": [
                E(
                    "Chancellor Lina Soh launches the Great Hyperspace Rush and Starlight Beacon program",
                ),
                E(
                    "Legacy Run disaster exposes hyperspace routing vulnerabilities in the Outer Rim",
                ),
                E(
                    "Nihil marauders destroy Starlight Beacon; Marchion Ro's campaign begins",
                ),
                E(
                    "Drengir and Nameless crises force Jedi to confront limits of conventional Force doctrine",
                ),
                E(
                    "High Republic era closes as Jedi adopt increasingly cautious, insular policies",
                ),
            ],
            "keyFactions": [
                L("Faction", "Galactic Republic", "factions/republic"),
            ],
            "majorCharacters": [
                L("Jedi", "Yoda", "jedi/yoda"),
            ],
            "planets": [
                L("Planet", "Coruscant", "coruscant"),
                L("Planet", "Naboo", "naboo"),
                L("Planet", "Dathomir", "planet/dathomir"),
                L("Planet", "Carida", "planet/carida"),
            ],
            "ships": [
                L("Ship", "Consular-class Cruiser", "ships/consular-class"),
                L("Ship", "Venator-class Star Destroyer", "ships/venator-class"),
            ],
            "films": [],
            "series": [
                "Star Wars: Young Jedi Adventures",
                "Star Wars: The Acolyte",
            ],
            "games": [],
            "books": [
                "Light of the Jedi (Charles Soule)",
                "The Rising Storm (Cavan Scott)",
                "The Fallen Star (Claudia Gray)",
                "Star Wars: The High Republic comic series",
            ],
            "timeline": [
                {"era": "c. 500 BBY", "event": "High Republic expansion era begins"},
                {"era": "c. 232 BBY", "event": "Starlight Beacon operational in Eiram system"},
                {"era": "232 BBY", "event": "Legacy Run catastrophe in Hetzal system"},
                {"era": "231 BBY", "event": "Starlight Beacon destroyed by the Nihil"},
                {"era": "c. 100 BBY", "event": "Era winds down; Jedi Council grows more cautious"},
            ],
            "gallery": [
                G("high-republic", "Starlight Beacon illuminates a frontier sector of the Outer Rim"),
            ],
        },
        "fall-of-the-republic": {
            "dateRange": "32 BBY – 19 BBY",
            "government": GL("Galactic Senate", "governments/galactic-senate"),
            "headOfState": GL(
                "Supreme Chancellor Palpatine",
                "sith/darth-sidious",
                emphasized=True,
                emphasis_tone="sith",
            ),
            "overview": (
                "The Fall of the Republic covers the final thirteen years of democratic rule — "
                "from the Naboo crisis through the Clone Wars to Order 66 and the Great Jedi "
                "Purge. It is the era when Darth Sidious, hidden in plain sight as Supreme "
                "Chancellor Palpatine, engineered the very war that would give him absolute "
                "power and destroy the Jedi Order in a single night."
            ),
            "history": (
                "The Trade Federation's blockade of Naboo in 32 BBY exposed the Republic Senate "
                "as gridlocked and corrupt. Queen Amidala's plea for intervention failed until "
                "Chancellor Valorum fell and Senator Palpatine of Naboo ascended to the "
                "chancellorship — the first move in a Sith grand strategy a millennium in "
                "the making. Qui-Gon Jinn's discovery of Anakin Skywalker on Tatooine and "
                "Darth Maul's emergence revealed that the Sith had returned, but the Jedi "
                "Council's skepticism toward Anakin would prove as fateful as Palpatine's "
                "smile.\n\n"
                "A decade of separatist agitation followed. Count Dooku — secretly Darth Tyranus "
                "— formed the Confederacy of Independent Systems, backed by the Trade Federation, "
                "Banking Clan, Techno Union, and Corporate Alliance. Corporate droid armies "
                "massed on Geonosis while the Senate debated. The [Jedi Code](the-force/jedi-code) "
                "forbade attachment, yet the Order became entangled in politics as never before, "
                "leading armies and serving as generals in a conflict Darth Sidious controlled "
                "from both sides.\n\n"
                "The Clone Wars (22–19 BBY) scarred every sector. Battles on Christophsis, "
                "Ryloth, Umbara, and Mandalore killed billions. Anakin Skywalker, Obi-Wan Kenobi, "
                "and Ahsoka Tano became symbols of Republic heroism even as war crimes accumulated "
                "on both sides. General Grievous led Separatist droid fleets; Asajj Ventress and "
                "Savage Opress tested the Sith apprenticeship under Tyranus. The [Sith Code](the-force/sith-code) "
                "demanded betrayal — and Sidious eventually ordered Tyranus's death to "
                "advance Anakin's fall.\n\n"
                "Palpatine accumulated emergency powers with each crisis: the kidnapping on "
                "Coruscant, the Zillo Beast incident, and the bombing of the Jedi Temple hangar. "
                "The Jedi Council's distrust of the Chancellor — and Anakin's fear of losing "
                "Padmé — created the emotional wedge Sidious needed. When Mace Windu confronted "
                "Palpatine in his office, Anakin chose betrayal, and the duel left the Chancellor "
                "scarred but victorious.\n\n"
                "Order 66 (19 BBY) activated inhibitor chips in every clone trooper. Jedi across "
                "the galaxy were murdered by the soldiers they had trusted — on Felucia, Kashyyyk, "
                "Mygeeto, and Utapau where Obi-Wan killed Grievous even as the directive "
                "executed. Anakin, now Darth Vader, slaughtered younglings in the Temple; "
                "Yoda and Obi-Wan alone survived to flee into exile. The Senate applauded "
                "as Palpatine declared the Galactic Empire.\n\n"
                "In thirteen years the Republic died not from external conquest but from "
                "engineered crisis, militarization, and the Jedi Order's inability to see "
                "that their role as generals had already compromised the ideals they "
                "swore to defend."
            ),
            "significance": (
                "The Fall of the Republic is the moral engine of the entire Skywalker saga — "
                "the moment democracy chooses security over liberty and pays for it across "
                "generations. Every prequel story arc converges here: Anakin's prophecy, "
                "Padmé's faith in reform, Dooku's aristocratic rebellion, and Palpatine's "
                "patience.\n\n"
                "The Clone Wars redefine the Jedi from monks to soldiers, explaining the "
                "cynicism of the Original Trilogy's survivors and the New Republic's later "
                "reluctance to maintain standing armies. Order 66 remains the franchise's "
                "most haunting set piece — a reminder that institutional trust can be "
                "weaponized in an instant.\n\n"
                "For chronology enthusiasts, this era anchors the galactic calendar's "
                "modern dating system and connects film, *The Clone Wars*, *Bad Batch*, "
                "and countless novels into a single tragic arc."
            ),
            "majorEvents": [
                E(
                    "Trade Federation blockades Naboo; Palpatine elected Supreme Chancellor",
                ),
                E(
                    "First Battle of Geonosis opens the Clone Wars",
                    "wars-conflicts/clone-wars",
                ),
                E(
                    "Clone Wars ravage the galaxy; Jedi serve as generals",
                    "wars-conflicts/clone-wars",
                ),
                E(
                    "Order 66 — clone troopers execute Jedi across the galaxy",
                ),
                E(
                    "Palpatine declares the Galactic Empire; Jedi Purge begins",
                ),
            ],
            "keyFactions": [
                L("Faction", "Galactic Republic", "factions/republic"),
                L("Faction", "Confederacy of Independent Systems", "factions/confederacy"),
            ],
            "majorCharacters": [
                L("Jedi", "Obi-Wan Kenobi", "jedi/obi-wan-kenobi"),
                L("Jedi", "Anakin Skywalker", "jedi/anakin-skywalker"),
                L("Jedi", "Yoda", "jedi/yoda"),
                L("Jedi", "Ahsoka Tano", "jedi/ahsoka-tano"),
                L("Sith", "Darth Sidious", "sith/darth-sidious"),
                L("Sith", "Darth Maul", "sith/darth-maul"),
                L("Character", "General Grievous", "characters/general-grievous"),
            ],
            "planets": [
                L("Planet", "Coruscant", "coruscant"),
                L("Planet", "Geonosis", "planet/geonosis"),
                L("Planet", "Utapau", "planet/utapau"),
                L("Planet", "Mustafar", "mustafar"),
                L("Planet", "Kashyyyk", "planet/kashyyyk"),
            ],
            "ships": [
                L("Ship", "Venator-class Star Destroyer", "ships/venator-class"),
                L("Ship", "X-wing (prototype lineage)", "ships/x-wing"),
            ],
            "films": [
                "Star Wars: Episode I — The Phantom Menace",
                "Star Wars: Episode II — Attack of the Clones",
                "Star Wars: Episode III — Revenge of the Sith",
            ],
            "series": [
                "Star Wars: The Clone Wars",
                "Star Wars: Tales of the Jedi",
            ],
            "games": [
                "Star Wars: Battlefront II (2005)",
                "Star Wars Jedi: Fallen Order (flashback sequences)",
            ],
            "books": [
                "Master & Apprentice (Claudia Gray)",
                "Dark Disciple (Christie Golden)",
                "Revenge of the Sith novelization (Matthew Stover)",
            ],
            "timeline": [
                {"era": "32 BBY", "event": "Naboo crisis; Palpatine becomes Chancellor"},
                {"era": "22 BBY", "event": "First Battle of Geonosis; Clone Wars begin"},
                {"era": "19 BBY", "event": "Battle of Coruscant; Dooku killed"},
                {"era": "19 BBY", "event": "Order 66 executed; Jedi Temple falls"},
                {"era": "19 BBY", "event": "Empire proclaimed in the Senate chamber"},
            ],
            "gallery": [
                G("fall-of-the-republic", "Clone troopers and Jedi generals during the Battle of Geonosis"),
            ],
        },
        "reign-of-the-empire": {
            "dateRange": "19 BBY – 4 BBY",
            "government": GL("Imperial Ruling Council", "governments/imperial-ruling-council"),
            "headOfState": GL(
                "Galactic Emperor",
                "sith/darth-sidious",
                emphasized=True,
                emphasis_tone="sith",
            ),
            "overview": (
                "The Reign of the Empire — often called the Dark Times — spans two decades of "
                "authoritarian rule under Emperor Palpatine and Darth Vader. The Imperial "
                "military pacified the galaxy with Star Destroyers and TIE swarms, the "
                "Inquisitorius hunted surviving Jedi, and the Death Star project consumed "
                "resources on a genocidal scale. Yet even in this iron grip, rebel cells "
                "and hidden Force users kept resistance alive in the shadows."
            ),
            "history": (
                "Palpatine's proclamation on Coruscant reorganized the Republic into the "
                "First Galactic Empire with thunderous applause — a legislative suicide "
                "masked as salvation. The [Sith Code](the-force/sith-code) at last governed "
                "galactic law: power concentrated in two rulers, fear as policy, and passion "
                "channeled into domination. Darth Vader, encased in black armor, became the "
                "Emperor's fist — hunting Jedi survivors and crushing Separatist holdouts "
                "while the Imperial Security Bureau monitored civilian dissent.\n\n"
                "The Jedi Purge continued systematically. Inquisitors — fallen Jedi turned "
                "dark-side hunters — tracked Force-sensitive children and refugees. Kanan "
                "Jarrus (Caleb Dume) and Ezra Bridger on Lothal represented the Order's "
                "flickering embers, while Cal Kestis evaded capture in *Jedi: Fallen Order*. "
                "Temples on Ilum were strip-mined for kyber crystals; Jedha's holy city "
                "became a conduit for the Death Star's superlaser research.\n\n"
                "Imperial governance relied on Moffs, regional governors, and the "
                "military-industrial complex. The Imperial I-class Star Destroyer became "
                "the symbol of occupation; TIE fighters swarmed from hangar bays on "
                "countless worlds. Grand Moff Tarkin pioneered the doctrine of rule "
                "through fear — culminating in the Death Star, a mobile battle station "
                "capable of destroying planets. Alderaan's annihilation would later prove "
                "his doctrine correct in the worst possible way.\n\n"
                "Outer Rim worlds bore the heaviest burden. Lothal's factories fueled "
                "Imperial expansion; Kashyyyk's Wookiees were enslaved; Geonosis's population "
                "was sterilized to hide the Death Star's origins. The Empire sold order "
                "while extracting wealth — a pattern Rim worlds would remember when the "
                "Rebel Alliance called for recruits.\n\n"
                "Malachor's Sith temple and Yoda's exile on Dagobah anchored the Force "
                "side of this era. Ahsoka Tano, no longer a Jedi, confronted Vader at "
                "Malachor; Ezra Bridger communed with Loth-wolves and purrgil; the "
                "[Jedi Code](the-force/jedi-code) survived only in whispers and broken "
                "holocrons. The Ghost crew's operations on Lothal demonstrated that "
                "localized rebellion could bleed an empire even before a formal alliance formed.\n\n"
                "By 4 BBY, cells from Lothal to Mustafar were coordinating under Mon Mothma's "
                "network. The Death Star neared completion. The Empire looked unassailable — "
                "but its overreach, reliance on fear, and Vader's divided loyalty contained "
                "the seeds of its destruction."
            ),
            "significance": (
                "The Imperial era defines Star Wars's political dystopia — the cautionary "
                "tale of how democracies die and how ordinary people resist anyway. It "
                "explains why survivors like Obi-Wan and Yoda hid rather than fought openly, "
                "and why the Rebel Alliance needed years to coalesce.\n\n"
                "The Inquisitorius, Death Star construction, and Rim exploitation connect "
                "film canon to *Rebels*, *Andor*, *Obi-Wan Kenobi*, and the *Jedi* game "
                "series into a coherent picture of totalitarian everyday life.\n\n"
                "Without these twenty years, the Original Trilogy's victories would lack "
                "context — the Empire is not merely evil, it is the logical endpoint of "
                "Palpatine's Republic-era strategy."
            ),
            "majorEvents": [
                E(
                    "Proclamation of the Galactic Empire; Jedi Purge intensifies",
                ),
                E(
                    "Inquisitorius established to hunt Force-sensitive survivors",
                ),
                E(
                    "Death Star construction begins; kyber crystals harvested on Jedha and Ilum",
                ),
                E(
                    "Lothal resistance and growing rebel cells challenge Imperial occupation",
                ),
                E(
                    "Formal Rebel Alliance coalesces as Imperial oppression peaks",
                ),
            ],
            "keyFactions": [
                L("Faction", "Galactic Empire", "factions/empire"),
            ],
            "majorCharacters": [
                L("Sith", "Darth Vader", "sith/darth-vader"),
                L("Sith", "Darth Sidious", "sith/darth-sidious"),
                L("Jedi", "Kanan Jarrus", "jedi/kanan-jarrus"),
                L("Jedi", "Ezra Bridger", "jedi/ezra-bridger"),
            ],
            "planets": [
                L("Planet", "Coruscant", "coruscant"),
                L("Planet", "Lothal", "planet/lothal"),
                L("Planet", "Malachor", "planet/malachor"),
                L("Planet", "Ilum", "planet/ilum"),
                L("Planet", "Jedha", "planet/jedha"),
            ],
            "ships": [
                L("Ship", "Imperial I-class Star Destroyer", "ships/imperial-i-class"),
                L("Ship", "TIE Fighter", "ships/tie-fighter"),
                L("Ship", "Executor-class Star Dreadnought", "ships/executor-class"),
            ],
            "films": [
                "Rogue One: A Star Wars Story",
                "Star Wars: Episode III — Revenge of the Sith (opening)",
            ],
            "series": [
                "Star Wars Rebels",
                "Star Wars: The Bad Batch",
                "Star Wars: Obi-Wan Kenobi",
                "Star Wars: Andor",
            ],
            "games": [
                "Star Wars Jedi: Fallen Order",
                "Star Wars Jedi: Survivor",
                "Star Wars: Squadrons",
            ],
            "books": [
                "Lords of the Sith (Paul S. Kemp)",
                "Tarkin (James Luceno)",
                "Catalyst: A Rogue One Novel (James Luceno)",
            ],
            "timeline": [
                {"era": "19 BBY", "event": "Empire proclaimed; Great Jedi Purge begins"},
                {"era": "14 BBY", "event": "Inquisitorius hunts survivors; Cal Kestis emerges"},
                {"era": "5 BBY", "event": "Spectres crew forms on Lothal"},
                {"era": "4 BBY", "event": "Rebel cells begin formal coordination"},
                {"era": "0 BBY", "event": "Death Star nearing operational status"},
            ],
            "gallery": [
                G("reign-of-the-empire", "Imperial Star Destroyers patrol a subjugated Outer Rim world"),
            ],
        },
        "age-of-rebellion": {
            "dateRange": "4 BBY – 4 ABY",
            "government": GL("Alliance Civil Government", "governments/alliance-civil-government"),
            "headOfState": GL("Chancellor Mon Mothma", "characters/mon-mothma"),
            "overview": (
                "The Age of Rebellion covers the Galactic Civil War — from the first formal "
                "strikes against the Empire to the decisive victory at Endor. The Rebel Alliance "
                "transformed scattered cells into a coalition capable of destroying Death Stars, "
                "while Luke Skywalker's journey restored the Jedi legacy and revealed that "
                "even Darth Vader could be redeemed."
            ),
            "history": (
                "The Rebel Alliance coalesced around Mon Mothma, Bail Organa, and Saw Gerrera's "
                "networks — a multi-species coalition united by the memory of the Republic and "
                "horror at Imperial atrocities. Early victories on Lothal and Atollon were costly; "
                "the Empire responded with blockades, ISB infiltration, and the Death Star — "
                "a weapon that made conventional rebellion seem suicidal.\n\n"
                "The theft of the Death Star plans on Scarif (0 BBY) and their transmission to "
                "Leia Organa's Tantive IV set the Original Trilogy in motion. Luke Skywalker, "
                "raised on Tatooine, joined Obi-Wan Kenobi and learned the basics of the Force "
                "before the mentor fell to Darth Vader aboard the Death Star. The Battle of "
                "Yavin — where Luke fired the proton torpedoes that destroyed the battle station "
                "— became year zero for galactic dating and proof that hope could defeat terror.\n\n"
                "The [Jedi Code](the-force/jedi-code) lived again in Luke's training on "
                "Dagobah under Yoda, while the [Sith Code](the-force/sith-code) bound Vader "
                "to Palpatine through pain and duty. Han Solo, Leia, Chewbacca, and the "
                "droids R2-D2 and C-3PO formed the Alliance's irregular heart — smugglers "
                "and diplomats who could strike where formal fleets could not.\n\n"
                "The Empire struck back at Hoth, scattering the Alliance and forcing Luke to "
                "confront Vader at Cloud City on Bespin. The revelation — 'I am your father' — "
                "fractured the rebellion's greatest hope even as Lando Calrissian and Chewbacca "
                "raced to rescue Han from Jabba the Hutt. The second Death Star, under "
                "construction over Endor, became Palpatine's trap.\n\n"
                "The Galactic Civil War reached its climax in 4 ABY. The Battle of Endor "
                "combined a ground assault on the shield generator, a fleet action against "
                "the Executor-class Super Star Destroyer, and Luke's refusal to kill his father "
                "— a choice that allowed Anakin Skywalker to destroy the Emperor and fulfill "
                "the prophecy. The Empire's leadership was decapitated; celebrations erupted "
                "from Coruscant to Naboo even as Imperial holdouts prepared for guerrilla war.\n\n"
                "This era is the mythic core of Star Wars — farmboys and princesses against "
                "armored tyranny, the Force as spiritual counterweight to superweapons, and "
                "the proof that rebellion is not terrorism when the state itself is the crime."
            ),
            "significance": (
                "The Age of Rebellion is the franchise's founding narrative — the template "
                "for every subsequent story about resistance, redemption, and the cost of "
                "freedom. The galactic calendar itself dates from the Battle of Yavin.\n\n"
                "Luke and Leia's discovery of their heritage connects the prequel tragedy "
                "to Original Trilogy hope, while Han's arc from cynic to believer models "
                "the civilian's role in political struggle.\n\n"
                "Endor's victory did not end war — Jakku and Imperial remnants would follow "
                "— but it proved that Sith dominion could be broken, setting the stage for "
                "the New Republic and the eventual rise of the First Order."
            ),
            "majorEvents": [
                E(
                    "Rebel Alliance steals Death Star plans at Scarif",
                ),
                E(
                    "Battle of Yavin destroys the first Death Star",
                    "wars-conflicts/galactic-civil-war",
                ),
                E(
                    "Battle of Hoth; Alliance scatters from Echo Base",
                    "wars-conflicts/galactic-civil-war",
                ),
                E(
                    "Battle of Endor — Emperor Palpatine killed; second Death Star destroyed",
                    "wars-conflicts/galactic-civil-war",
                ),
            ],
            "keyFactions": [
                L("Faction", "Rebel Alliance", "factions/rebel-alliance"),
                L("Faction", "Galactic Empire", "factions/empire"),
            ],
            "majorCharacters": [
                L("Jedi", "Luke Skywalker", "jedi/luke-skywalker"),
                L("Jedi", "Obi-Wan Kenobi", "jedi/obi-wan-kenobi"),
                L("Jedi", "Yoda", "jedi/yoda"),
                L("Character", "Leia Organa", "characters/leia-organa"),
                L("Character", "Han Solo", "characters/han-solo"),
                L("Sith", "Darth Vader", "sith/darth-vader"),
            ],
            "planets": [
                L("Planet", "Yavin 4", "planet/yavin-4"),
                L("Planet", "Hoth", "hoth"),
                L("Planet", "Endor", "planet/endor"),
                L("Planet", "Bespin", "bespin"),
                L("Planet", "Scarif", "planet/scarif"),
                L("Planet", "Dagobah", "planet/dagobah"),
            ],
            "ships": [
                L("Ship", "Millennium Falcon", "ships/millennium-falcon"),
                L("Ship", "X-wing Starfighter", "ships/x-wing"),
                L("Ship", "Executor-class Star Dreadnought", "ships/executor-class"),
            ],
            "films": [
                "Rogue One: A Star Wars Story",
                "Star Wars: Episode IV — A New Hope",
                "Star Wars: Episode V — The Empire Strikes Back",
                "Star Wars: Episode VI — Return of the Jedi",
            ],
            "series": [
                "Star Wars Rebels (closing arcs)",
            ],
            "games": [
                "Star Wars: Battlefront (2015)",
                "Star Wars: Squadrons",
            ],
            "books": [
                "Lost Stars (Claudia Gray)",
                "Battlefront: Twilight Company (Alexander Freed)",
            ],
            "timeline": [
                {"era": "0 BBY", "event": "Death Star plans stolen; Battle of Yavin"},
                {"era": "3 ABY", "event": "Battle of Hoth; duel on Cloud City"},
                {"era": "4 ABY", "event": "Rescue of Han Solo from Jabba's palace"},
                {"era": "4 ABY", "event": "Battle of Endor; Emperor and Vader die"},
            ],
            "gallery": [
                G("age-of-rebellion", "Rebel starfighters attack the Death Star over Yavin"),
            ],
        },
        "new-republic": {
            "dateRange": "4 ABY – 34 ABY",
            "government": GL("New Republic Senate", "governments/new-republic-senate"),
            "headOfState": GL("Chancellor of the New Republic", "characters/mon-mothma"),
            "overview": (
                "The New Republic era spans three decades of restored democracy after Endor — "
                "a fragile peace built on demilitarization, war-crimes tribunals, and Senate "
                "politics that never fully healed the galaxy's wounds. Imperial remnants fought "
                "on Jakku and beyond, while hidden forces in the Unknown Regions rebuilt the "
                "Imperial Navy into the First Order that would shatter this restored Republic."
            ),
            "history": (
                "Mon Mothma's provisional government on Chandrila promised a Republic without "
                "the Old Order's militarism. The Galactic Senate reconvened; member worlds "
                "debated disarmament treaties while Grand Admiral Thrawn's campaigns (in Legends) "
                "and canon Imperial holdouts tested the new state's resolve. The Battle of "
                "Jakku (5 ABY) — where the Empire's last major fleet crashed into Jakku's "
                "sands — formalized capitulation and the signing of the Galactic Concordance.\n\n"
                "Luke Skywalker searched for Jedi lore across the galaxy, recovering texts "
                "from Ossus, Christophsis, and other forgotten sites before founding a training "
                "academy on Ossus and later locations. Leia Organa served as senator and "
                " diplomat, warning that Imperial sympathizers remained embedded in Core "
                "worlds. Han Solo and Chewbacca worked to liberate Kashyyyk while the "
                "New Republic Defense Fleet was deliberately kept small — a political "
                "choice that would prove catastrophic.\n\n"
                "The Centrist and Populist factions in the Senate replayed old Core–Rim "
                "tensions. Corporate zones flourished; the Outer Rim Trade Coalition lobbied "
                "against regulation. Ben Solo's birth offered hope — the son of heroes — "
                "but Snoke's influence and the dark side's pull toward legacy would corrupt "
                "Luke's academy years later. In the Unknown Regions, Imperial exiles under "
                "leaders like Rae Sloane and eventually Snoke rebuilt fleets in secret.\n\n"
                "The Resistance formed as Leia's private militia when the New Republic "
                "government refused to acknowledge the First Order threat. Starkiller Base's "
                "construction on Ilum — the planet stripped of its kyber — went undetected "
                "until too late. Hosnian Prime's destruction (34 ABY) annihilated the Senate "
                "and fleet in a single shot, ending the New Republic as a governing force "
                "almost overnight.\n\n"
                "Between Endor and Hosnian, this era encompasses *The Mandalorian*, *Ahsoka*, "
                "and *The Book of Boba Fett* — stories of bounty hunters, Grogu's training, "
                "and the slow fade of Jedi restoration amid galactic complacency. The "
                "[Jedi Code](the-force/jedi-code) survived in Luke's texts but failed to "
                "prevent his academy tragedy — a wound Rey would later inherit.\n\n"
                "The New Republic's story is therefore one of victory squandered: democracy "
                "returned, but the institutions that might have defended it were deliberately "
                "weakened, and the enemy was allowed to regrow in the shadows Palpatine had "
                "always favored."
            ),
            "significance": (
                "The New Republic explains the Sequel Trilogy's political vacuum — why Leia "
                "commands a Resistance instead of a superpower, and why the galaxy can forget "
                "the Jedi between Luke's exile and Rey's emergence.\n\n"
                "It connects the Original Trilogy's triumph to modern series storytelling, "
                "showing that destroying a Death Star does not automatically rebuild "
                "civilization. Jakku's wreckage and Hosnian's ashes bookend the era as "
                "monuments to incomplete peace.\n\n"
                "For historians in-universe and fans out-of-universe, the New Republic is "
                "the cautionary epilogue to rebellion — proof that winning the war is "
                "easier than winning the peace."
            ),
            "majorEvents": [
                E(
                    "Battle of Endor decapitates Imperial leadership; New Republic proclaimed",
                ),
                E(
                    "Battle of Jakku — Imperial fleet defeated; Galactic Concordance signed",
                ),
                E(
                    "Luke Skywalker establishes Jedi training academy; searches for lost lore",
                ),
                E(
                    "First Order consolidates in the Unknown Regions; Resistance formed",
                ),
                E(
                    "Destruction of Hosnian system ends New Republic governance",
                ),
            ],
            "keyFactions": [
                L("Faction", "New Republic", "factions/new-republic"),
            ],
            "majorCharacters": [
                L("Jedi", "Luke Skywalker", "jedi/luke-skywalker"),
                L("Character", "Leia Organa", "characters/leia-organa"),
                L("Character", "Han Solo", "characters/han-solo"),
                L("Jedi", "Grogu", "jedi/grogu"),
            ],
            "planets": [
                L("Planet", "Jakku", "planet/jakku"),
                L("Planet", "Coruscant", "coruscant"),
                L("Planet", "Hosnian Prime", "planet/hosnian-prime"),
                L("Planet", "Takodana", "planet/takodana"),
                L("Planet", "Ahch-To", "planet/ahch-to"),
            ],
            "ships": [
                L("Ship", "MC80 Star Cruiser", "ships/mc80-cruiser"),
                L("Ship", "X-wing Starfighter", "ships/x-wing"),
            ],
            "films": [
                "Star Wars: Episode VII — The Force Awakens (Hosnian cataclysm)",
            ],
            "series": [
                "The Mandalorian",
                "The Book of Boba Fett",
                "Ahsoka",
            ],
            "games": [
                "Star Wars: Battlefront II (2017) — Resurrection campaign",
            ],
            "books": [
                "Bloodline (Claudia Gray)",
                "Aftermath trilogy (Chuck Wendig)",
                "The Last Jedi: Expanded Edition (Jason Fry)",
            ],
            "timeline": [
                {"era": "4 ABY", "event": "Empire falls at Endor; New Republic founded"},
                {"era": "5 ABY", "event": "Battle of Jakku; Imperial capitulation"},
                {"era": "c. 15 ABY", "event": "Luke searches for Jedi artifacts"},
                {"era": "28 ABY", "event": "Luke's academy destroyed; Ben Solo falls"},
                {"era": "34 ABY", "event": "Hosnian system destroyed by Starkiller Base"},
            ],
            "gallery": [
                G("new-republic", "New Republic star cruisers above a restored Core world"),
            ],
        },
        "rise-of-the-first-order": {
            "dateRange": "34 ABY – 35 ABY",
            "government": GL("First Order Supreme Council", "governments/first-order-supreme-council"),
            "headOfState": GL("Supreme Leader", "governments/first-order-supreme-council"),
            "overview": (
                "The Rise of the First Order covers the Sequel Trilogy's central conflict — "
                "a compressed but galaxy-shaking war in which the First Order emerged from "
                "Imperial exile, destroyed the New Republic capital with Starkiller Base, "
                "and drove the Resistance to its last stands on Crait and Exegol. It is the "
                "era when Rey, Finn, and Poe Dameron carried the legacy of the Jedi and "
                "Rebellion against a resurgent dark-side empire."
            ),
            "history": (
                "The First Order rose from the Unknown Regions — a militarized successor to "
                "the Galactic Empire built on child conscription, fanatical loyalty, and "
                "technology refined in secret for three decades. Supreme Leader Snoke manipulated "
                "Kylo Ren (Ben Solo) as a dark-side heir while General Hux commanded "
                "Resurgent-class Star Destroyers and TIE fighter wings that matched Imperial "
                "scale. The New Republic's demilitarization left no fleet capable of "
                "containing the threat until Starkiller Base fired.\n\n"
                "The destruction of the Hosnian system (34 ABY) killed the Senate, the "
                "Republic fleet, and billions of civilians in minutes — a demonstration "
                "of power that echoed the Death Star but on a multi-planetary scale. "
                "Starkiller Base, built into the planet Ilum, drained a star to fire "
                "through hyperspace. The Resistance's counterattack, led by Han Solo, "
                "Chewbacca, and Finn, destroyed the weapon but cost Han his life at "
                "Kylo Ren's hand inside the oscillator trench.\n\n"
                "Rey — a scavenger from Jakku — discovered Luke Skywalker's lightsaber, "
                "trained under Leia and later Luke on Ahch-To, and confronted the pull "
                "of the dark side in Force visions and dyad bond with Kylo. The "
                "[Jedi Code](the-force/jedi-code) and [Sith Code](the-force/sith-code) "
                "collided in her lineage reveal: she was Palpatine's granddaughter, "
                "yet chose the light. Luke's Force projection at Crait bought the "
                "Resistance escape; he became one with the Force on Ahch-To.\n\n"
                "The Cold War between First Order and Resistance escalated into open "
                "battle across Takodana, D'Qar, and Crait — white salt plains stained "
                "by red dust from First Order walkers. Snoke's death at Rey's hand "
                " (via Kylo's betrayal) reshuffled the dark-side hierarchy before "
                "Palpatine's return on Exegol revealed the Sith Eternal's hidden fleet.\n\n"
                "The Battle of Exegol (35 ABY) rallied citizens' fleets from across "
                "the galaxy — Corellian freighters, Mon Cal cruisers, and X-wings "
                "answering Lando Calrissian's call. Rey, empowered by the voices of "
                "past Jedi, destroyed Palpatine permanently; Finn and Jannah led a "
                "ground assault on the Sith fleet's navigation tower. The First Order "
                "and Final Order collapsed together, ending Sidious's millennia-long "
                "design.\n\n"
                "Though brief on the calendar, this era reshaped galactic politics "
                "irreversibly — the New Republic was gone, the Resistance ascendant, "
                "and the Jedi path open to a new generation willing to choose their "
                "own legacy."
            ),
            "significance": (
                "The Rise of the First Order closes the Skywalker saga's loop — Palpatine's "
                "return and final defeat, the redemption of Ben Solo, and Rey's affirmation "
                "that lineage does not dictate destiny.\n\n"
                "Starkiller Base and Hosnian's fall demonstrate that demilitarization without "
                "vigilance invites catastrophe, echoing the Old Republic's final century. "
                "The dyad between Rey and Ben revisits the Force's balance theme from the "
                "Je'daii through the Rule of Two.\n\n"
                "For modern Star Wars storytelling, this era bridges film, *Resistance*, "
                "novels, and theme-park continuity — the living present of the franchise "
                "timeline."
            ),
            "majorEvents": [
                E(
                    "Starkiller Base destroys the Hosnian system; New Republic falls",
                ),
                E(
                    "Resistance destroys Starkiller Base; Han Solo killed by Kylo Ren",
                ),
                E(
                    "Cold War escalates into open war between First Order and Resistance",
                    "wars-conflicts/cold-war",
                ),
                E(
                    "Battle of Crait; Luke Skywalker becomes one with the Force",
                ),
                E(
                    "Battle of Exegol — Palpatine and Final Order defeated",
                ),
            ],
            "keyFactions": [
                L("Faction", "First Order", "factions/first-order"),
            ],
            "majorCharacters": [
                L("Character", "Rey", "characters/rey"),
                L("Character", "Finn", "characters/finn"),
                L("Sith", "Darth Sidious", "sith/darth-sidious"),
            ],
            "planets": [
                L("Planet", "Starkiller Base", "planet/starkiller-base"),
                L("Planet", "Crait", "planet/crait"),
                L("Planet", "Exegol", "planet/exegol"),
                L("Planet", "D'Qar", "planet/d-qar"),
                L("Planet", "Hosnian Prime", "planet/hosnian-prime"),
            ],
            "ships": [
                L("Ship", "Resurgent-class Star Destroyer", "ships/resurgent-class"),
                L("Ship", "TIE Fighter", "ships/tie-fighter"),
            ],
            "films": [
                "Star Wars: Episode VII — The Force Awakens",
                "Star Wars: Episode VIII — The Last Jedi",
                "Star Wars: Episode IX — The Rise of Skywalker",
            ],
            "series": [
                "Star Wars Resistance",
            ],
            "games": [
                "Star Wars: Battlefront II (2017)",
            ],
            "books": [
                "The Force Awakens novelization (Alan Dean Foster)",
                "The Last Jedi: Expanded Edition (Jason Fry)",
                "The Rise of Skywalker: Expanded Edition (Rae Carson)",
            ],
            "timeline": [
                {"era": "34 ABY", "event": "Hosnian system destroyed; Starkiller Base operational"},
                {"era": "34 ABY", "event": "Starkiller Base destroyed; Han Solo dies"},
                {"era": "34 ABY", "event": "Snoke killed aboard Supremacy"},
                {"era": "34 ABY", "event": "Battle of Crait; Luke's final stand"},
                {"era": "35 ABY", "event": "Battle of Exegol; Palpatine permanently defeated"},
            ],
            "gallery": [
                G("rise-of-the-first-order", "First Order Star Destroyers over Starkiller Base"),
            ],
        },
        "new-jedi-order": {
            "dateRange": "4 ABY – onward",
            "government": GL("Jedi High Council", "governments/jedi-council"),
            "headOfState": GL(
                "Jedi Master Luke Skywalker",
                "jedi/luke-skywalker",
                emphasized=True,
                emphasis_tone="jedi",
            ),
            "overview": (
                "The New Jedi Order era encompasses the galaxy's long effort to rebuild "
                "Jedi tradition after the Purge — from Luke Skywalker's first academy to "
                "its destruction, his exile on Ahch-To, and Rey's journey to carry the "
                "light forward. It is an ongoing chronicle of restoration, failure, and "
                "renewed hope that the Force's guardians can exist without repeating the "
                "Old Order's fatal compromises."
            ),
            "history": (
                "When the Empire fell at Endor, the Jedi were a memory — two survivors "
                "in hiding and a handful of texts scattered across the galaxy. Luke "
                "Skywalker, the farmboy who redeemed Darth Vader, shouldered the burden "
                "of rebuilding. He recovered holocrons, searched ruins on Ossus and "
                "Devaron, and eventually trained a new generation of Force users including "
                "his nephew Ben Solo and students like those who would die when the "
                "Knights of Ren attacked.\n\n"
                "The [Jedi Code](the-force/jedi-code) guided Luke's curriculum — "
                "discipline, compassion, and non-attachment — but the shadow of the "
                "Clone Wars lingered. Luke feared Ben's darkness and briefly contemplated "
                "striking him down; that moment of hesitation helped push Ben toward "
                "Snoke and the dark side. The temple burning (~28 ABY) broke Luke's "
                "faith; he exiled himself to Ahch-To, site of the first Jedi temple, "
                "intending to die with the Order.\n\n"
                "Rey's emergence from Jakku reopened the path. Guided by Leia, Han, "
                "and the legacy voices of Obi-Wan and Yoda, she found Luke and demanded "
                "training. On Ahch-To, Luke taught her the Force's breadth — including "
                "its painful history — before sacrificing himself at Crait so the "
                "Resistance could survive. Rey carried his sabers, faced Palpatine on "
                "Exegol, and took the name Skywalker as honorific, not bloodline.\n\n"
                "Parallel threads enrich this era: Grogu trained under Luke at Ossus "
                "before returning to Din Djarin; Ahsoka Tano searched for Ezra Bridger "
                "in the Unknown Regions; Cal Kestis gathered survivors in *Jedi: Survivor*. "
                "Each story asks the same question — can the Jedi exist without the "
                "Republic's bureaucracy, without armies, without the hubris that doomed "
                "the prequel Order?\n\n"
                "The [Sith Code](the-force/sith-code) appeared defeated when Vader "
                "killed Palpatine at Endor, yet Sidious's clone body on Exegol proved "
                "the dark side's persistence. Rey's victory — supported by a chorus of "
                "past Jedi — suggested a new model: not a massive temple on Coruscant, "
                "but adaptable guardians embedded in the galaxy's fabric.\n\n"
                "As an open-ended era, the New Jedi Order continues in series, games, "
                "and future films — a promise that the Force's light side can be "
                "relearned after every catastrophe, and that the name 'Jedi' remains "
                "a choice rather than a birthright."
            ),
            "significance": (
                "The New Jedi Order is Star Wars's epilogue and prologue simultaneously "
                "— the bridge from Original Trilogy hope to Sequel Trilogy renewal and "
                "whatever comes next. Luke's failure with Ben is as important as his "
                "success with Rey: the Order must evolve or repeat history.\n\n"
                "Rey's yellow saber and Skywalker name signal intentional reinvention "
                "rather than restoration of old structures. Grogu, Ezra, and Cal represent "
                "distributed Jedi futures outside centralized temples.\n\n"
                "For fans, this era collects the franchise's meditation on legacy — "
                "what parents owe children, what teachers owe students, and whether "
                "the galaxy still needs Jedi when the Sith are gone."
            ),
            "majorEvents": [
                E(
                    "Luke Skywalker founds the new Jedi academy after the Galactic Civil War",
                    "wars-conflicts/galactic-civil-war",
                ),
                E(
                    "Destruction of Luke's temple; Ben Solo falls to the dark side",
                ),
                E(
                    "Rey trains with Luke on Ahch-To; Jedi texts preserved",
                ),
                E(
                    "Rey defeats Palpatine at Exegol with the strength of past Jedi",
                ),
                E(
                    "Rey adopts the Skywalker name; new Jedi path begins",
                ),
            ],
            "keyFactions": [],
            "majorCharacters": [
                L("Jedi", "Luke Skywalker", "jedi/luke-skywalker"),
                L("Character", "Rey", "characters/rey"),
                L("Jedi", "Grogu", "jedi/grogu"),
                L("Jedi", "Kanan Jarrus", "jedi/kanan-jarrus"),
                L("Sith", "Darth Vader", "sith/darth-vader"),
                L("Sith", "Darth Sidious", "sith/darth-sidious"),
            ],
            "planets": [
                L("Planet", "Ahch-To", "planet/ahch-to"),
                L("Planet", "Exegol", "planet/exegol"),
                L("Planet", "Tatooine", "tatooine"),
                L("Planet", "Coruscant", "coruscant"),
            ],
            "ships": [
                L("Ship", "Millennium Falcon", "ships/millennium-falcon"),
                L("Ship", "X-wing Starfighter", "ships/x-wing"),
            ],
            "films": [
                "Star Wars: Episode VI — Return of the Jedi",
                "Star Wars: Episode VII — The Force Awakens",
                "Star Wars: Episode VIII — The Last Jedi",
                "Star Wars: Episode IX — The Rise of Skywalker",
            ],
            "series": [
                "The Mandalorian",
                "The Book of Boba Fett",
                "Ahsoka",
            ],
            "games": [
                "Star Wars Jedi: Fallen Order",
                "Star Wars Jedi: Survivor",
            ],
            "books": [
                "The Legends of Luke Skywalker (Ken Liu)",
                "Shadow of the Sith (Adam Christopher)",
                "Star Wars: The Rise of Skywalker — Expanded Edition",
            ],
            "timeline": [
                {"era": "4 ABY", "event": "Luke begins searching for Jedi knowledge after Endor"},
                {"era": "c. 15 ABY", "event": "Luke establishes training academy"},
                {"era": "28 ABY", "event": "Temple destroyed; Luke exiles to Ahch-To"},
                {"era": "34 ABY", "event": "Rey finds Luke; Jedi texts recovered"},
                {"era": "35 ABY", "event": "Rey defeats Palpatine; adopts Skywalker name"},
            ],
            "gallery": [
                G("new-jedi-order", "Rey lifts Luke's X-wing from Ahch-To's stormy seas"),
            ],
        },
    }
