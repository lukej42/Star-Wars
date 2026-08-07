#!/usr/bin/env python3
"""New battles to merge into BattleData.cs — films, TCW, Rebels, KOTOR, Old Sith Empire, SWTOR, books."""

from __future__ import annotations

# Each entry: war_slug, slug, name, era, color, planet (optional), scene, archives (optional)
# archives: list of (label, value, route)


def b(
    war: str,
    slug: str,
    name: str,
    era: str,
    color: str,
    planet: str = "",
    scene: str = "",
    archives: list[tuple[str, str, str]] | None = None,
) -> dict:
    return {
        "war_slug": war,
        "slug": slug,
        "name": name,
        "era": era,
        "color": color,
        "planet": planet,
        "scene": scene,
        "archives": archives or [],
    }


NEW_BATTLES: list[dict] = [
    # ── Clone Wars (films + TCW) ─────────────────────────────────────────────
    b(
        "clone-wars",
        "battle-of-christophsis",
        "Battle of Christophsis",
        "22 BBY",
        "#3ecfb2",
        "Christophsis",
        "Clone troopers and Jedi Generals Anakin Skywalker and Obi-Wan Kenobi defending crystal cities "
        "from Separatist droid armies while AV-7 Anti-Vehicle cannons fire across Christophsis skyline",
        [
            ("Jedi", "Anakin Skywalker", "jedi/anakin-skywalker"),
            ("Jedi", "Obi-Wan Kenobi", "jedi/obi-wan-kenobi"),
            ("Faction", "Confederacy of Independent Systems", "factions/confederacy"),
            ("Planet", "Christophsis", "planet/christophsis"),
        ],
    ),
    b(
        "clone-wars",
        "battle-of-ryloth",
        "Battle of Ryloth",
        "22 BBY",
        "#14b8a6",
        "Ryloth",
        "Republic LAAT gunships and Mace Windu's assault force liberating Ryloth's dusty mesas from "
        "Separatist occupation while Twi'lek resistance fighters ambush droid patrols",
        [
            ("Jedi", "Mace Windu", "jedi/mace-windu"),
            ("Character", "Cham Syndulla", "characters/cham-syndulla"),
            ("Planet", "Ryloth", "planet/ryloth"),
            ("Faction", "Confederacy of Independent Systems", "factions/confederacy"),
        ],
    ),
    b(
        "clone-wars",
        "second-battle-of-geonosis",
        "Second Battle of Geonosis",
        "21 BBY",
        "#0d9488",
        "Geonosis",
        "Republic forces assaulting Geonosis droid foundries with AT-TE walkers crossing red rock "
        "plains while Luminara Unduli and Anakin Skywalker strike the primary factory complex",
        [
            ("Jedi", "Anakin Skywalker", "jedi/anakin-skywalker"),
            ("Jedi", "Luminara Unduli", "jedi/luminara-unduli"),
            ("Battle", "First Battle of Geonosis", "wars-conflicts/battles/first-battle-of-geonosis"),
            ("Planet", "Geonosis", "planet/geonosis"),
        ],
    ),
    b(
        "clone-wars",
        "battle-of-umbara",
        "Battle of Umbara",
        "20 BBY",
        "#2dd4bf",
        "Umbara",
        "501st clone troopers marching through bioluminescent Umbaran jungle under treasonous General "
        "Pong Krell while AT-RT scouts clash with shadowy Umbaran militia",
        [
            ("Jedi", "Anakin Skywalker", "jedi/anakin-skywalker"),
            ("Character", "Captain Rex", "characters/captain-rex"),
            ("Planet", "Umbara", "planet/umbara"),
            ("Military unit", "501st Legion", "military-units/galactic-republic/army/501st-legion"),
        ],
    ),
    b(
        "clone-wars",
        "defense-of-kamino",
        "Defense of Kamino",
        "21 BBY",
        "#5eead4",
        "Kamino",
        "Tipoca City under aquatic assault as Separatist aqua droids and Trident drills breach Kamino "
        "cloning facilities while ARC troopers and Jedi defend the rainy ocean platforms",
        [
            ("Jedi", "Obi-Wan Kenobi", "jedi/obi-wan-kenobi"),
            ("Jedi", "Anakin Skywalker", "jedi/anakin-skywalker"),
            ("Planet", "Kamino", "planet/kamino"),
            ("Faction", "Confederacy of Independent Systems", "factions/confederacy"),
        ],
    ),
    b(
        "clone-wars",
        "battle-of-sullust",
        "Battle of Sullust",
        "20 BBY",
        "#06b6d4",
        "Sullust",
        "Asajj Ventress and Count Dooku dueling amid volcanic Sullust factory districts while "
        "Separatist and Republic starfighter wings clash over glowing magma vents",
        [
            ("Sith", "Count Dooku", "sith/darth-tyranus"),
            ("Sith", "Asajj Ventress", "sith/asajj-ventress"),
            ("Planet", "Sullust", "planet/sullust"),
        ],
    ),
    b(
        "clone-wars",
        "battle-of-felucia",
        "Battle of Felucia",
        "19 BBY",
        "#3ecfb2",
        "Felucia",
        "Jungle war on Felucia's fungal plains as Aayla Secura's clone troopers advance through "
        "giant mushroom forests before Order 66 turns their blasters on their Jedi commander",
        [
            ("Jedi", "Aayla Secura", "jedi/aayla-secura"),
            ("Battle", "Jedi Purge", "wars-conflicts/battles/jedi-purge"),
            ("Planet", "Felucia", "planet/felucia"),
        ],
    ),
    b(
        "clone-wars",
        "battle-of-saleucami",
        "Battle of Saleucami",
        "19 BBY",
        "#14b8a6",
        "Saleucami",
        "Stass Allie's 91st Mobile Recon Corps pursuing Separatist forces across Saleucami's "
        "misty wetlands on speeder bikes before clone troopers execute Order 66",
        [
            ("Jedi", "Stass Allie", "jedi/stass-allie"),
            ("Battle", "Jedi Purge", "wars-conflicts/battles/jedi-purge"),
            ("Planet", "Saleucami", "planet/saleucami"),
        ],
    ),
    b(
        "clone-wars",
        "battle-of-anaxes",
        "Battle of Anaxes",
        "19 BBY",
        "#0d9488",
        "Anaxes",
        "Republic naval yard siege on Anaxes with Bad Batch commandos infiltrating Separatist "
        "algorithm core while Venator Star Destroyers exchange turbolaser fire over shipyards",
        [
            ("Character", "Captain Rex", "characters/captain-rex"),
            ("Jedi", "Anakin Skywalker", "jedi/anakin-skywalker"),
            ("Planet", "Anaxes", "planet/anaxes"),
        ],
    ),
    b(
        "clone-wars",
        "battle-of-cato-neimoidia",
        "Battle of Cato Neimoidia",
        "19 BBY",
        "#2dd4bf",
        "Cato Neimoidia",
        "Plo Koon's starfighter wing patrolling bridge cities of Cato Neimoidia when clone wingmen "
        "open fire during Order 66 over the Neimoidian purse world",
        [
            ("Jedi", "Plo Koon", "jedi/plo-koon"),
            ("Battle", "Jedi Purge", "wars-conflicts/battles/jedi-purge"),
            ("Planet", "Cato Neimoidia", "planet/cato-neimoidia"),
        ],
    ),
    b(
        "clone-wars",
        "battle-of-ringo-vinda",
        "Battle of Ringo Vinda",
        "19 BBY",
        "#5eead4",
        "Ringo Vinda",
        "Orbital ring-world battle station above Ringo Vinda with Tup's inhibitor chip malfunction "
        "triggering premature Order 66 execution in a crowded clone trooper barracks",
        [
            ("Jedi", "Anakin Skywalker", "jedi/anakin-skywalker"),
            ("Jedi", "Tiplar", "jedi/tiplar"),
            ("Planet", "Ringo Vinda", "planet/ringo-vinda"),
        ],
    ),
    b(
        "clone-wars",
        "battle-of-mygeeto",
        "Battle of Mygeeto",
        "19 BBY",
        "#06b6d4",
        "Mygeeto",
        "Ki-Adi-Mundi leading clone troopers across Mygeeto's crystalline ice bridges while Separatist "
        "banking clan droids defend InterGalactic Banking Clan vaults under aurora skies",
        [
            ("Jedi", "Ki-Adi-Mundi", "jedi/ki-adi-mundi"),
            ("Battle", "Jedi Purge", "wars-conflicts/battles/jedi-purge"),
            ("Planet", "Mygeeto", "planet/mygeeto"),
        ],
    ),
    b(
        "clone-wars",
        "battle-of-quell",
        "Battle of Quell",
        "22 BBY",
        "#3ecfb2",
        "Quell",
        "Republic cruiser convoy ambushed over Quell as Ahsoka Tano and Anakin Skywalker crash-land "
        "on a Resolute-class carrier amid flaming debris and vulture droid swarms",
        [
            ("Jedi", "Ahsoka Tano", "jedi/ahsoka-tano"),
            ("Jedi", "Anakin Skywalker", "jedi/anakin-skywalker"),
            ("Planet", "Quell", "planet/quell"),
        ],
    ),
    b(
        "clone-wars",
        "battle-of-malastare",
        "Battle of Malastare",
        "21 BBY",
        "#14b8a6",
        "Malastare",
        "Republic electro-proton bomb detonating on Malastare plains to collapse Separatist droid ranks "
        "while the Zillo Beast awakens beneath the battlefield rubble",
        [
            ("Jedi", "Anakin Skywalker", "jedi/anakin-skywalker"),
            ("Jedi", "Mace Windu", "jedi/mace-windu"),
            ("Creature", "Zillo Beast", "creatures/zillo-beast"),
            ("Planet", "Malastare", "planet/malastare"),
        ],
    ),
    b(
        "clone-wars",
        "battle-of-boz-pity",
        "Battle of Boz Pity",
        "19 BBY",
        "#0d9488",
        "Boz Pity",
        "Republic assault on Separatist hospital world Boz Pity with gunships landing amid ruined "
        "medical towers while Asajj Ventress and General Grievous counterattack",
        [
            ("Character", "General Grievous", "characters/general-grievous"),
            ("Sith", "Asajj Ventress", "sith/asajj-ventress"),
            ("Planet", "Boz Pity", "planet/boz-pity"),
        ],
    ),
    # ── Galactic Civil War (9 films + Rebels + Rogue One + Solo) ─────────────
    b(
        "galactic-civil-war",
        "battle-of-atollon",
        "Battle of Atollon",
        "2 BBY",
        "#ffd166",
        "Atollon",
        "Grand Admiral Thrawn's Seventh Fleet blockading Atollon with Interdictor cruisers while "
        "Phoenix Squadron X-wings attempt to break through over coral mesas and Chopper Base",
        [
            ("Character", "Thrawn", "characters/thrawn"),
            ("Character", "Hera Syndulla", "characters/hera-syndulla"),
            ("Jedi", "Ezra Bridger", "jedi/ezra-bridger"),
            ("Planet", "Atollon", "planet/atollon"),
        ],
    ),
    b(
        "galactic-civil-war",
        "siege-of-lothal",
        "Siege of Lothal",
        "1 BBY",
        "#fbbf24",
        "Lothal",
        "Imperial Star Destroyers bombarding Lothal's capital while Spectre cell rebels defend "
        "dome settlements and Ezra Bridger summons purrgil to cripple the blockade",
        [
            ("Jedi", "Ezra Bridger", "jedi/ezra-bridger"),
            ("Character", "Grand Admiral Thrawn", "characters/thrawn"),
            ("Planet", "Lothal", "planet/lothal"),
        ],
    ),
    b(
        "galactic-civil-war",
        "skirmish-on-jedha",
        "Skirmish on Jedha",
        "0 BBY",
        "#f59e0b",
        "Jedha",
        "Saw Gerrera's Partisans ambushing Imperial patrols in Jedha City's desert shrines while "
        "Kyber crystal convoys move toward the Death Star under crimson kyber-lit skies",
        [
            ("Character", "Saw Gerrera", "characters/saw-gerrera"),
            ("Faction", "Galactic Empire", "factions/empire"),
            ("Planet", "Jedha", "planet/jedha"),
            ("Battle", "Battle of Scarif", "wars-conflicts/battles/battle-of-scarif"),
        ],
    ),
    b(
        "galactic-civil-war",
        "battle-on-eadu",
        "Battle on Eadu",
        "0 BBY",
        "#eab308",
        "Eadu",
        "Rebel commandos raiding Imperial kyber research facility on storm-lashed Eadu cliffs "
        "while X-wings strafe landing platforms above the research spire",
        [
            ("Character", "Cassian Andor", "characters/cassian-andor"),
            ("Character", "Jyn Erso", "characters/jyn-erso"),
            ("Planet", "Eadu", "planet/eadu"),
            ("Battle", "Battle of Scarif", "wars-conflicts/battles/battle-of-scarif"),
        ],
    ),
    b(
        "galactic-civil-war",
        "battle-of-mimban",
        "Battle of Mimban",
        "10 BBY",
        "#ca8a04",
        "Mimban",
        "Imperial mud trenches on Mimban with swamp troopers and Han Solo's infantry unit advancing "
        "through toxic fog while AT-HA walkers sink into the mire",
        [
            ("Character", "Han Solo", "characters/han-solo"),
            ("Character", "Tobias Beckett", "characters/tobias-beckett"),
            ("Planet", "Mimban", "planet/mimban"),
            ("Faction", "Galactic Empire", "factions/empire"),
        ],
    ),
    b(
        "galactic-civil-war",
        "battle-of-kessel",
        "Battle of Kessel",
        "10 BBY",
        "#fde047",
        "Kessel",
        "Millennium Falcon leading a spice mine revolt on Kessel while coaxium coaxing through "
        "the Kessel Run pursued by Imperial TIE patrols and pyke syndicate guards",
        [
            ("Character", "Han Solo", "characters/han-solo"),
            ("Character", "Lando Calrissian", "characters/lando-calrissian"),
            ("Ship", "Millennium Falcon", "ships/millennium-falcon"),
            ("Planet", "Kessel", "planet/kessel"),
        ],
    ),
    b(
        "galactic-civil-war",
        "liberation-of-sullust",
        "Liberation of Sullust",
        "4 ABY",
        "#ffd166",
        "Sullust",
        "New Republic commandos and Sullustan resistance fighters seizing Imperial factory districts "
        "after Endor while Star Destroyer debris still burns in orbit",
        [
            ("Character", "Lando Calrissian", "characters/lando-calrissian"),
            ("Battle", "Battle of Endor", "wars-conflicts/battles/battle-of-endor"),
            ("Planet", "Sullust", "planet/sullust"),
        ],
    ),
    b(
        "galactic-civil-war",
        "defense-of-naboo-galactic-civil-war",
        "Defense of Naboo (Galactic Civil War)",
        "4 ABY",
        "#fbbf24",
        "Naboo",
        "Rebel fleet and Naboo starfighters repelling Imperial Operation: Cinder bombardment of "
        "Naboo's oceans while Leia Organa coordinates planetary defense from Theed",
        [
            ("Character", "Leia Organa", "characters/leia-organa"),
            ("Character", "Leia Organa", "characters/leia-organa"),
            ("Planet", "Naboo", "naboo"),
            ("Battle", "Battle of Endor", "wars-conflicts/battles/battle-of-endor"),
        ],
    ),
    # ── Mandalorian Wars (KOTOR era) ─────────────────────────────────────────
    b(
        "mandalorian-wars",
        "battle-of-serroco",
        "Battle of Serroco",
        "3963 BBY",
        "#64748b",
        "Serroco",
        "Mandalorian nuclear bombardment flattening Serroco's Stereb cities while Republic fleet "
        "officers watch frigates vaporize from Basilisk war droid strikes",
        [
            ("Character", "Carth Onasi", "characters/carth-onasi"),
            ("Faction", "Mandalorians", "factions/mandalorians"),
            ("Planet", "Serroco", "planet/serroco"),
        ],
    ),
    b(
        "mandalorian-wars",
        "siege-of-rhen-var",
        "Siege of Rhen Var",
        "3964 BBY",
        "#475569",
        "Rhen Var",
        "Frozen citadel siege on Rhen Var with Republic soldiers defending ice temples against "
        "Mandalorian shock troops under aurora-lit polar storms",
        [
            ("Faction", "Mandalorians", "factions/mandalorians"),
            ("Planet", "Rhen Var", "planet/rhen-var"),
        ],
    ),
    b(
        "mandalorian-wars",
        "battle-of-onderon-mandalorian-wars",
        "Battle of Onderon (Mandalorian Wars)",
        "3962 BBY",
        "#334155",
        "Onderon",
        "Mandalorian Basilisk war droids strafing Onderon's jungle canopy while Republic forces "
        "and beast-riders counterattack beneath Iziz city walls",
        [
            ("Faction", "Mandalorians", "factions/mandalorians"),
            ("Planet", "Onderon", "planet/onderon"),
            ("Battle", "Battle of Dxun", "wars-conflicts/battles/battle-of-dxun"),
        ],
    ),
    b(
        "mandalorian-wars",
        "battle-of-vanquo",
        "Battle of Vanquo",
        "3963 BBY",
        "#94a3b8",
        "Vanquo",
        "Republic miners and Jedi strike teams ambushing Mandalorian convoys on Vanquo's dusty "
        "mining mesas before the front collapses toward Taris",
        [
            ("Jedi", "Revan", "jedi/revan"),
            ("Faction", "Mandalorians", "factions/mandalorians"),
            ("Planet", "Vanquo", "planet/vanquo"),
        ],
    ),
    b(
        "mandalorian-wars",
        "assault-on-dantooine-enclave",
        "Assault on Dantooine Enclave",
        "3958 BBY",
        "#71717a",
        "Dantooine",
        "Mandalorian raiders bombarding the Jedi Enclave on Dantooine's grassy plains while "
        "Padawans evacuate through subterranean root cellars",
        [
            ("Planet", "Dantooine", "dantooine"),
            ("Faction", "Mandalorians", "factions/mandalorians"),
        ],
    ),
    b(
        "mandalorian-wars",
        "mandalorian-siege-of-taris",
        "Mandalorian Siege of Taris",
        "3962 BBY",
        "#52525b",
        "Taris",
        "Mandalorian Neo-Crusaders besieging Taris upper city while Republic evacuation ships "
        "lift off from the Undercity as orbital bombardment lights the skyline",
        [
            ("Faction", "Mandalorians", "factions/mandalorians"),
            ("Planet", "Taris", "planet/taris"),
            ("Battle", "Siege of Taris", "wars-conflicts/battles/siege-of-tar-is"),
        ],
    ),
    b(
        "mandalorian-wars",
        "battle-of-jagelland",
        "Battle of Jagelland",
        "3964 BBY",
        "#64748b",
        "Althir",
        "Republic hammerhead cruisers engaging Mandalorian warships over Althir's polar seas "
        "while boarding parties clash on frost-covered carrier decks",
        [
            ("Faction", "Mandalorians", "factions/mandalorians"),
            ("Planet", "Althir", "planet/althir"),
        ],
    ),
    b(
        "mandalorian-wars",
        "raid-on-cathar-survivors",
        "Raid on Cathar Survivors",
        "3963 BBY",
        "#475569",
        "Cathar",
        "Mandalorian extermination squads hunting remaining Cathar refugees across coastal cliffs "
        "years after the Devastation of Cathar under blood-red skies",
        [
            ("Faction", "Mandalorians", "factions/mandalorians"),
            ("Battle", "Devastation of Cathar", "wars-conflicts/battles/devastation-of-cathar"),
            ("Planet", "Cathar", "planet/cathar"),
        ],
    ),
    b(
        "mandalorian-wars",
        "final-confrontation-at-malachor-v",
        "Final Confrontation at Malachor V",
        "3960 BBY",
        "#334155",
        "Malachor V",
        "Revan and Malak leading Republic forces against Mandalorian clans at the mass shadow "
        "generator superweapon site with fractured ground and violet energy storms",
        [
            ("Jedi", "Revan", "jedi/revan"),
            ("Sith", "Darth Malak", "sith/darth-malak"),
            ("Battle", "Battle of Malachor V", "wars-conflicts/battles/battle-of-malachor-v"),
            ("Planet", "Malachor V", "planet/malachor-v"),
        ],
    ),
    # ── Great Sith War (Old Sith Empire / Tales of the Jedi) ──────────────────
    b(
        "great-sith-war",
        "battle-of-foerost",
        "Battle of Foerost",
        "3996 BBY",
        "#dc2626",
        "Foerost",
        "Krath and Sith fleet capturing Republic shipyards at Foerost with Sith sorcery storms "
        "rolling over orbital construction rings and fleeing Jedi cruisers",
        [
            ("Sith", "Exar Kun", "sith/exar-kun"),
            ("Planet", "Foerost", "planet/foerost"),
        ],
    ),
    b(
        "great-sith-war",
        "invasion-of-korriban-great-sith-war",
        "Invasion of Korriban (Great Sith War)",
        "3996 BBY",
        "#b91c1c",
        "Korriban",
        "Sith Massassi warriors reclaiming Korriban tombs while Republic expeditionary forces "
        "descend into the Valley of the Dark Lords under crimson storm clouds",
        [
            ("Sith", "Exar Kun", "sith/exar-kun"),
            ("Planet", "Korriban", "korriban"),
        ],
    ),
    b(
        "great-sith-war",
        "krath-coup-of-empress-teta",
        "Krath Coup of Empress Teta",
        "3997 BBY",
        "#991b1b",
        "Empress Teta",
        "Krath cultists seizing Empress Teta's carbonite palaces with dark-side ritual fires "
        "reflecting off tetan spires as Jedi negotiators are massacred",
        [
            ("Sith", "Ulic Qel-Droma", "sith/ulic-qel-droma"),
            ("Planet", "Empress Teta", "planet/empress-teta"),
        ],
    ),
    b(
        "great-sith-war",
        "assault-on-ossus-library",
        "Assault on the Ossus Great Library",
        "3996 BBY",
        "#ef4444",
        "Ossus",
        "Jedi evacuating holocrons from Ossus Great Library mesas as Sith warships bombard "
        "mountain archives and Naga Sadow's forces storm terraced campuses",
        [
            ("Battle", "Battle of Ossus", "wars-conflicts/battles/battle-of-ossus"),
            ("Planet", "Ossus", "planet/ossus"),
        ],
    ),
    b(
        "great-sith-war",
        "duel-on-yavin-4-great-sith-war",
        "Duel on Yavin 4 (Great Sith War)",
        "3997 BBY",
        "#f87171",
        "Yavin 4",
        "Exar Kun corrupting Jedi apprentices in Massassi temples on Yavin 4 jungle moon with "
        "Sith alchemical pyramids glowing under green canopies",
        [
            ("Sith", "Exar Kun", "sith/exar-kun"),
            ("Planet", "Yavin 4", "planet/yavin-4"),
        ],
    ),
    b(
        "great-sith-war",
        "sith-bombardment-of-ambria",
        "Sith Bombardment of Ambria",
        "3996 BBY",
        "#7f1d1d",
        "Ambria",
        "Sith fleet glassing Ambria's wasteland surface where Naddist cultists once ruled, "
        "Jedi evacuation shuttles lifting off through ash clouds",
        [
            ("Planet", "Ambria", "planet/ambria"),
            ("Sith", "Exar Kun", "sith/exar-kun"),
        ],
    ),
    b(
        "great-sith-war",
        "battle-of-cyax-system",
        "Battle of the Cyax System",
        "3996 BBY",
        "#dc2626",
        "Ossus",
        "Republic and Jedi fleet engaging Sith battle groups near Ossus with capital ship "
        "broadside exchanges lighting the nebula between wrecked frigates",
        [
            ("Battle", "Sith Invasion of Ossus", "wars-conflicts/battles/sith-invasion-of-ossus"),
            ("Planet", "Ossus", "planet/ossus"),
        ],
    ),
    # ── Great Galactic War (Old Sith Empire vs Republic) ─────────────────────
    b(
        "great-galactic-war",
        "sith-invasion-of-taris",
        "Sith Invasion of Taris",
        "3683 BBY",
        "#b91c1c",
        "Taris",
        "Sith Imperial troopers marching through Taris Undercity rubble while Republic "
        "evacuation transports lift off under orbital bombardment",
        [
            ("Planet", "Taris", "planet/taris"),
            ("Faction", "Sith Empire", "factions/sith-empire"),
        ],
    ),
    b(
        "great-galactic-war",
        "battle-of-voss",
        "Battle of Voss",
        "3645 BBY",
        "#dc2626",
        "Voss",
        "Republic and Sith forces clashing on Voss's misty mountain plateaus near Mystic "
        "temples while Gormak war parties watch from ridgelines",
        [
            ("Planet", "Voss", "planet/voss"),
            ("Faction", "Sith Empire", "factions/sith-empire"),
        ],
    ),
    b(
        "great-galactic-war",
        "battle-of-quesh-great-galactic-war",
        "Battle of Quesh (Great Galactic War)",
        "3643 BBY",
        "#991b1b",
        "Quesh",
        "Toxic Quesh venom refineries exploding as Republic and Sith troopers fight in "
        "hazmat armor amid yellow-green chemical fog",
        [
            ("Planet", "Quesh", "planet/quesh"),
            ("Faction", "Sith Empire", "factions/sith-empire"),
        ],
    ),
    b(
        "great-galactic-war",
        "battle-of-tython-great-galactic-war",
        "Battle of Tython (Great Galactic War)",
        "3660 BBY",
        "#ef4444",
        "Tython",
        "Sith invasion force breaching Je'daii temple mesas on Tython with crimson saber "
        "fire reflecting off ancient stone arches",
        [
            ("Planet", "Tython", "planet/tython"),
            ("Faction", "Sith Empire", "factions/sith-empire"),
        ],
    ),
    b(
        "great-galactic-war",
        "sith-assault-on-dromund-kaas",
        "Sith Assault on Dromund Kaas",
        "3679 BBY",
        "#f87171",
        "Dromund Kaas",
        "Republic infiltration teams sabotaging Sith citadel landing platforms on storm-wracked "
        "Dromund Kaas while Imperial guards mobilize in rain-swept plazas",
        [
            ("Planet", "Dromund Kaas", "planet/dromund-kaas"),
            ("Faction", "Sith Empire", "factions/sith-empire"),
        ],
    ),
    b(
        "great-galactic-war",
        "sith-victory-at-ziost",
        "Sith Victory at Ziost",
        "3685 BBY",
        "#7f1d1d",
        "Ziost",
        "Sith Imperial occupation of Ziost's frozen citadels with dark-side ice storms swirling "
        "above ancient Sith monoliths and chained prisoners",
        [
            ("Planet", "Ziost", "planet/ziost"),
            ("Faction", "Sith Empire", "factions/sith-empire"),
        ],
    ),
    b(
        "great-galactic-war",
        "battle-of-manaan-great-galactic-war",
        "Battle of Manaan (Great Galactic War)",
        "3667 BBY",
        "#b91c1c",
        "Manaan",
        "Underwater Selkath cities on Manaan rocked by depth charges as Republic submersibles "
        "skirmish with Sith aqua troopers near kolto harvesting stations",
        [
            ("Planet", "Manaan", "planet/manaan"),
            ("Faction", "Sith Empire", "factions/sith-empire"),
        ],
    ),
    b(
        "great-galactic-war",
        "siege-of-nal-hutta-great-galactic-war",
        "Siege of Nal Hutta (Great Galactic War)",
        "3668 BBY",
        "#dc2626",
        "Nal Hutta",
        "Republic blockade of Nal Hutta's polluted swamps while Hutt Cartel mercenaries negotiate "
        "with both Sith and Republic envoys under neon-lit palaces",
        [
            ("Organization", "Hutt Smuggling Rings", "organizations/hutt-smuggling-rings"),
            ("Planet", "Nal Hutta", "planet/nal-hutta"),
        ],
    ),
    # ── Stark Hyperspace War ─────────────────────────────────────────────────
    b(
        "stark-hyperspace-war",
        "siege-of-formos",
        "Siege of Formos",
        "44 BBY",
        "#f97316",
        "Formos",
        "Stark Commercial Combine mercenaries defending Formos mining colonies against "
        "Trade Federation droid landing craft in dusty canyon firefights",
        [
            ("Faction", "Trade Federation", "factions/trade-federation"),
            ("Planet", "Formos", "planet/formos"),
        ],
    ),
    b(
        "stark-hyperspace-war",
        "naval-battle-over-troiken",
        "Naval Battle over Troiken",
        "44 BBY",
        "#ea580c",
        "Troiken",
        "Republic Judicial Forces frigates exchanging turbolaser fire with Stark Combine "
        "cruisers above Troiken's ice world while troop shuttles descend to frozen caves",
        [
            ("Battle", "Battle of Troiken", "wars-conflicts/battles/battle-of-troiken"),
            ("Planet", "Troiken", "planet/troiken"),
        ],
    ),
    b(
        "stark-hyperspace-war",
        "stark-hyperspace-ambush-at-taanab",
        "Stark Hyperspace Ambush at Taanab",
        "44 BBY",
        "#fb923c",
        "Taanab",
        "Corporate raiders ambushing Republic spice convoys near Taanab's agricultural "
        "orbital stations with hyperspace mines detonating among cargo freighters",
        [
            ("Planet", "Taanab", "planet/taanab"),
        ],
    ),
    b(
        "stark-hyperspace-war",
        "blockade-of-thyferra",
        "Blockade of Thyferra",
        "44 BBY",
        "#fdba74",
        "Thyferra",
        "Trade Federation Lucrehulk blockade sphere holding Thyferra bacta convoys hostage "
        "while Republic negotiators arrive under fighter escort",
        [
            ("Faction", "Trade Federation", "factions/trade-federation"),
            ("Planet", "Thyferra", "planet/thyferra"),
        ],
    ),
    b(
        "stark-hyperspace-war",
        "jedi-intervention-at-coruscant",
        "Jedi Intervention at Coruscant",
        "44 BBY",
        "#c2410c",
        "Bordal",
        "Jedi negotiators and Republic troops intervening in Bordal corporate riots sparked "
        "by Stark Hyperspace War economic collapse under senate spires",
        [
            ("Jedi", "Qui-Gon Jinn", "jedi/qui-gon-jinn"),
            ("Planet", "Coruscant", "coruscant"),
        ],
    ),
    # ── Hundred-Year Darkness / Old Sith Empire birth ────────────────────────
    b(
        "hundred-year-darkness",
        "exile-to-korriban",
        "Exile to Korriban",
        "6900 BBY",
        "#7c3aed",
        "Korriban",
        "Exiled Dark Jedi fleet arriving on Korriban red deserts to subjugate native Sith species "
        "and forge the first Sith Empire beneath thunderous violet skies",
        [
            ("Planet", "Korriban", "korriban"),
            ("The Force", "Ancient Force Orders", "the-force/ancient-force-orders"),
        ],
    ),
    b(
        "hundred-year-darkness",
        "founding-of-the-sith-empire",
        "Founding of the Sith Empire",
        "6900 BBY",
        "#6d28d9",
        "Korriban",
        "First Sith Lords crowning themselves in Korriban's Valley of the Dark Lords with "
        "crimson Force lightning illuminating ancient tombs and Massassi slaves",
        [
            ("Planet", "Korriban", "korriban"),
            ("The Force", "Conflict Between Light and Dark", "the-force/conflict-between-light-and-dark-side"),
        ],
    ),
    b(
        "hundred-year-darkness",
        "dark-jedi-uprising-on-coruscant",
        "Dark Jedi Uprising on Coruscant",
        "6950 BBY",
        "#5b21b6",
        "Coruscant",
        "Fallen Jedi battling loyalist Knights on Coruscant temple steps during the Hundred-Year "
        "Darkness schism with Force storms tearing skyscrapers",
        [
            ("Planet", "Coruscant", "coruscant"),
            ("The Force", "Jedi Code", "the-force/jedi-code"),
        ],
    ),
    b(
        "hundred-year-darkness",
        "battle-of-korriban-ancient",
        "Battle of Korriban (Ancient)",
        "6900 BBY",
        "#8b5cf6",
        "Korriban",
        "Dark Jedi conquerors dueling native Sith kings in Korriban tombs with red blades "
        "reflecting off desert cliffs and Sith holocrons",
        [
            ("Planet", "Korriban", "korriban"),
        ],
    ),
    b(
        "hundred-year-darkness",
        "sith-temple-construction-on-korriban",
        "Sith Temple Construction on Korriban",
        "6899 BBY",
        "#a78bfa",
        "Korriban",
        "Massassi slaves raising monolithic Sith temples on Korriban ridgelines while Dark "
        "Jedi architects channel Force energy into stone foundations",
        [
            ("Planet", "Korriban", "korriban"),
        ],
    ),
    # ── New Sith Wars / Old Sith Empire (Brotherhood of Darkness) ────────────
    b(
        "new-sith-wars",
        "first-battle-of-ruusan",
        "First Battle of Ruusan",
        "1010 BBY",
        "#991b1b",
        "Ruusan",
        "Opening clash of the Ruusan campaign with Jedi Army of Light skirmishing Brotherhood "
        "of Darkness Sith infantry across misty Ruusan valleys",
        [
            ("Battle", "Battle of Ruusan", "wars-conflicts/battles/battle-of-ruusan"),
            ("Planet", "Ruusan", "planet/ruusan"),
        ],
    ),
    b(
        "new-sith-wars",
        "second-battle-of-ruusan",
        "Second Battle of Ruusan",
        "1006 BBY",
        "#7f1d1d",
        "Ruusan",
        "Lord Kaan's Sith forces pushing Jedi lines back through Ruusan forests under "
        "perpetual storm clouds and crimson banners",
        [
            ("Planet", "Ruusan", "planet/ruusan"),
        ],
    ),
    b(
        "new-sith-wars",
        "third-battle-of-ruusan",
        "Third Battle of Ruusan",
        "1002 BBY",
        "#b91c1c",
        "Ruusan",
        "Jedi Lord Hoth's Army of Light encircling Sith fortifications on Ruusan ridges "
        "before the thought bomb campaign begins",
        [
            ("Planet", "Ruusan", "planet/ruusan"),
        ],
    ),
    b(
        "new-sith-wars",
        "fourth-battle-of-ruusan",
        "Fourth Battle of Ruusan",
        "1001 BBY",
        "#dc2626",
        "Ruusan",
        "Close-quarters trench warfare between Sith and Jedi on Ruusan muddy front lines "
        "with artillery shells carving glowing craters",
        [
            ("Planet", "Ruusan", "planet/ruusan"),
        ],
    ),
    b(
        "new-sith-wars",
        "fifth-battle-of-ruusan",
        "Fifth Battle of Ruusan",
        "1001 BBY",
        "#ef4444",
        "Ruusan",
        "Sith counteroffensive breaking Jedi perimeter defenses on Ruusan canyon passes "
        "with Brotherhood warlords fighting among themselves",
        [
            ("Planet", "Ruusan", "planet/ruusan"),
        ],
    ),
    b(
        "new-sith-wars",
        "sixth-battle-of-ruusan",
        "Sixth Battle of Ruusan",
        "1000 BBY",
        "#450a0a",
        "Ruusan",
        "Final approach to the thought bomb valley as Jedi and Sith armies converge on "
        "Ruusan underground caverns under grey storm skies",
        [
            ("Battle", "Seventh Battle of Ruusan", "wars-conflicts/battles/seventh-battle-of-ruusan"),
            ("Planet", "Ruusan", "planet/ruusan"),
        ],
    ),
    b(
        "new-sith-wars",
        "rise-of-darth-bane",
        "Rise of Darth Bane",
        "1000 BBY",
        "#991b1b",
        "Ruusan",
        "Lone Sith survivor Darth Bane observing the thought bomb detonation from Ruusan cliffs "
        "and forging the Rule of Two amid violet Force energy",
        [
            ("Sith", "Darth Bane", "sith/darth-bane"),
            ("Battle", "Thought Bomb Detonation", "wars-conflicts/battles/thought-bomb-detonation"),
            ("Planet", "Ruusan", "planet/ruusan"),
        ],
    ),
    b(
        "new-sith-wars",
        "sith-lord-skirmish-on-tython",
        "Sith Lord Skirmish on Tython",
        "1018 BBY",
        "#7f1d1d",
        "Tython",
        "Brotherhood of Darkness acolytes raiding Jedi outposts on Tython's mountain mesas "
        "before the Ruusan campaign escalates",
        [
            ("Planet", "Tython", "planet/tython"),
        ],
    ),
    # ── Cold War / Sequel trilogy ────────────────────────────────────────────
    b(
        "cold-war",
        "battle-of-kef-bir",
        "Battle of Kef Bir",
        "35 ABY",
        "#ef4444",
        "Kef Bir",
        "Rey and Resistance strike team navigating Death Star II wreckage oceans on Kef Bir "
        "while First Order treadspeeders chase them across rusted superstructure",
        [
            ("Character", "Rey", "characters/rey"),
            ("Character", "Finn", "characters/finn"),
            ("Planet", "Kef Bir", "planet/kef-bir"),
        ],
    ),
    b(
        "cold-war",
        "battle-of-kijimi",
        "Battle of Kijimi",
        "35 ABY",
        "#b91c1c",
        "Kijimi",
        "First Order occupation troops patrolling Kijimi's snow alleys while Resistance "
        "saboteurs extract droidsmiths from crimson-lit workshops",
        [
            ("Character", "Rey", "characters/rey"),
            ("Character", "Poe Dameron", "characters/poe-dameron"),
            ("Planet", "Kijimi", "planet/kijimi"),
        ],
    ),
    b(
        "cold-war",
        "battle-of-pasaana",
        "Battle of Pasaana",
        "35 ABY",
        "#991b1b",
        "Pasaana",
        "Speeder chase through Pasaana desert festival canyons as Resistance agents flee "
        "First Order jet troopers amid cheering crowds and spice mines",
        [
            ("Character", "Rey", "characters/rey"),
            ("Character", "Finn", "characters/finn"),
            ("Planet", "Pasaana", "planet/pasaana"),
        ],
    ),
    b(
        "cold-war",
        "attack-on-ahch-to",
        "Attack on Ahch-To",
        "34 ABY",
        "#dc2626",
        "Ahch To",
        "Luke Skywalker confronting Kylo Ren with a Force projection on Ahch-To's storm cliffs "
        "while Resistance evacuates from Crait in the distance",
        [
            ("Jedi", "Luke Skywalker", "jedi/luke-skywalker"),
            ("Faction", "First Order", "factions/first-order"),
            ("Planet", "Ahch-To", "planet/ahch-to"),
            ("Battle", "Battle of Crait", "wars-conflicts/battles/battle-of-crait"),
        ],
    ),
    b(
        "cold-war",
        "battle-of-ord-mantell-cold-war",
        "Battle of Ord Mantell (Cold War)",
        "34 ABY",
        "#dc2626",
        "Ord Mantell",
        "Mandalorian covert team rescuing Grogu from Imperial remnant forces on Ord Mantell "
        "spaceport while TIE fighters strafe docking rings",
        [
            ("Character", "Din Djarin", "characters/din-djarin"),
            ("Jedi", "Grogu", "jedi/grogu"),
            ("Planet", "Ord Mantell", "planet/ord-mantell"),
        ],
    ),
    b(
        "cold-war",
        "siege-of-maz-kanatas-castle",
        "Siege of Maz Kanata's Castle",
        "34 ABY",
        "#f87171",
        "Takodana",
        "First Order TIE fighters and stormtroopers destroying Maz Kanata's lakeside castle "
        "while Resistance X-wings arrive through forest canopy",
        [
            ("Battle", "Battle of Takodana", "wars-conflicts/battles/battle-of-takodana"),
            ("Planet", "Takodana", "planet/takodana"),
        ],
    ),
    b(
        "cold-war",
        "assault-on-starkiller-base-trench",
        "Assault on Starkiller Base Trench",
        "34 ABY",
        "#7f1d1d",
        "Starkiller Base",
        "Resistance X-wings diving through Starkiller Base thermal oscillator trenches "
        "while Han Solo's strike team plants charges inside icy corridors",
        [
            ("Battle", "Battle of Starkiller Base", "wars-conflicts/battles/battle-of-starkiller-base"),
            ("Character", "Han Solo", "characters/han-solo"),
            ("Planet", "Starkiller Base", "planet/starkiller-base"),
        ],
    ),
    b(
        "cold-war",
        "battle-of-ajan-kloss",
        "Battle of Ajan Kloss",
        "35 ABY",
        "#ef4444",
        "Ajan Kloss",
        "Resistance command center on Ajan Kloss mobilizing the final fleet muster against "
        "Exegol while starfighters launch through jungle canopy bunkers",
        [
            ("Character", "Poe Dameron", "characters/poe-dameron"),
            ("Character", "Leia Organa", "characters/leia-organa"),
            ("Battle", "Battle of Exegol", "wars-conflicts/battles/battle-of-exegol"),
            ("Planet", "Ajan Kloss", "planet/ajan-kloss"),
        ],
    ),
    # ── Great War (SWTOR) ────────────────────────────────────────────────────
    b(
        "great-war",
        "battle-of-taris-great-war",
        "Battle of Taris (Great War)",
        "3642 BBY",
        "#2563eb",
        "Taris",
        "Republic restoration efforts on Taris overrun by Sith Imperial invasion with "
        "undercity rakghoul outbreaks amid orbital bombardment",
        [
            ("Planet", "Taris", "planet/taris"),
            ("Faction", "Sith Empire", "factions/sith-empire"),
        ],
    ),
    b(
        "great-war",
        "battle-of-hoth-great-war",
        "Battle of Hoth (Great War)",
        "3642 BBY",
        "#1d4ed8",
        "Hoth",
        "SWTOR-era Republic and Imperial forces clashing in Hoth's ice trenches around "
        "downed dreadnought wreckage under blizzard-white skies",
        [
            ("Planet", "Hoth", "hoth"),
            ("Faction", "Sith Empire", "factions/sith-empire"),
        ],
    ),
    b(
        "great-war",
        "battle-of-dromund-kaas-great-war",
        "Battle of Dromund Kaas (Great War)",
        "3641 BBY",
        "#3b82f6",
        "Dromund Kaas",
        "Republic covert assault on Dromund Kaas Imperial citadel spires during renewed "
        "war offensives with lightning storms over the Sith capital",
        [
            ("Planet", "Dromund Kaas", "planet/dromund-kaas"),
            ("Faction", "Sith Empire", "factions/sith-empire"),
        ],
    ),
    b(
        "great-war",
        "battle-of-dantooine-great-war",
        "Battle of Dantooine (Great War)",
        "3642 BBY",
        "#60a5fa",
        "Dantooine",
        "Republic troopers defending Dantooine agricultural settlements against Sith Imperial "
        "invasion dropships over grassy plains",
        [
            ("Planet", "Dantooine", "dantooine"),
            ("Faction", "Sith Empire", "factions/sith-empire"),
        ],
    ),
    b(
        "great-war",
        "battle-of-ord-mantell-great-war",
        "Battle of Ord Mantell (Great War)",
        "3643 BBY",
        "#1e40af",
        "Ord Mantell",
        "Separatist-style urban warfare on Ord Mantell junkyard plains as Republic militia "
        "engage Sith Imperial troopers among rusted starship hulks",
        [
            ("Planet", "Ord Mantell", "planet/ord-mantell"),
            ("Faction", "Sith Empire", "factions/sith-empire"),
        ],
    ),
    b(
        "great-war",
        "battle-of-ziost-great-war",
        "Battle of Ziost (Great War)",
        "3636 BBY",
        "#93c5fd",
        "Ziost",
        "Vitiate's Sith ritual consuming Ziost's surface in black-winged dark-side energy "
        "while Republic evac ships flee the frozen world",
        [
            ("Planet", "Ziost", "planet/ziost"),
            ("Sith", "Vitiate", "sith/darth-vitiate"),
        ],
    ),
    b(
        "great-war",
        "battle-of-manaan-great-war",
        "Battle of Manaan (Great War)",
        "3641 BBY",
        "#2563eb",
        "Manaan",
        "Underwater battle for Manaan kolto fields with Republic submarines engaging Imperial "
        "depth charges near Ahto City domes",
        [
            ("Planet", "Manaan", "planet/manaan"),
            ("Faction", "Sith Empire", "factions/sith-empire"),
        ],
    ),
    b(
        "great-war",
        "battle-of-voss-great-war",
        "Battle of Voss (Great War)",
        "3641 BBY",
        "#1d4ed8",
        "Voss",
        "Republic and Imperial forces skirmishing on Voss mountain shrines while Voss Mystics "
        "observe from mist-shrouded cliffs",
        [
            ("Planet", "Voss", "planet/voss"),
            ("Faction", "Sith Empire", "factions/sith-empire"),
        ],
    ),
    b(
        "great-war",
        "siege-of-kaon-great-war",
        "Siege of Kaon (Great War)",
        "3641 BBY",
        "#3b82f6",
        "Kaon",
        "Imperial troopers defending Kaon weapon forges while Republic assault pods breach "
        "red-lit industrial hive spires",
        [
            ("Battle", "Siege of Kaon", "wars-conflicts/battles/siege-of-kaon"),
            ("Planet", "Kaon", "planet/kaon"),
        ],
    ),
    b(
        "great-war",
        "battle-of-nal-hutta-great-war",
        "Battle of Nal Hutta (Great War)",
        "3640 BBY",
        "#60a5fa",
        "Nal Hutta",
        "Hutt Cartel mercenaries fighting alongside Sith Imperial units in Nal Hutta swamp "
        "palace districts during a Republic raid",
        [
            ("Organization", "Hutt Smuggling Rings", "organizations/hutt-smuggling-rings"),
            ("Planet", "Nal Hutta", "planet/nal-hutta"),
        ],
    ),
]
