#!/usr/bin/env python3
"""Hand-authored extended profiles for Timelines Directory entries."""

from __future__ import annotations

TIMELINE_PROFILES: dict[str, dict] = {
    "major-events": {
        "overview": (
            "Galactic history is not a smooth arc but a chain of catastrophes and recoveries — "
            "founding charters, superweapons, purges, and revolutions that reset the political order. "
            "These major events are the hinge points every era defines itself against: what was lost, "
            "what was gained, and who chose to resist when institutions failed."
        ),
        "history": (
            "The Republic's founding myths speak of uniting the Core against chaos, but the earliest "
            "recorded turning point for modern historians is the defeat of the Sith at Ruusan (~1,000 BBY), "
            "which ended the New Sith Wars and led to the Ruusan Reformations — a thousand-year peace "
            "that shaped the Jedi Order Palpatine would later destroy.\n\n"
            "The Trade Federation's blockade of Naboo (32 BBY) proved that corporate armies could "
            "paralyze Senate action. Palpatine's election as Chancellor turned crisis into opportunity, "
            "and the Separatist movement manufactured a war designed to exhaust democracy.\n\n"
            "Order 66 (19 BBY) and the Jedi Purge severed the Republic from its guardians in a single "
            "night. The Galactic Empire rose not by invasion but by legal decree — a lesson later "
            "generations would cite when warning against emergency powers.\n\n"
            "The Battle of Yavin (0 BBY/0 ABY) established the galaxy's common calendar and proved "
            "that a small rebel force could destroy a planet-killer. Endor (4 ABY) killed the Emperor "
            "and fragmented the Empire; Jakku (5 ABY) formalized the New Republic's victory.\n\n"
            "Starkiller Base (34 ABY) annihilated the Hosnian system in minutes — demonstrating that "
            "even a restored democracy could be decapitated by a hidden foe. Exegol (35 ABY) rallied "
            "the galaxy's citizens against Palpatine's final fleet, closing the Skywalker saga's loop."
        ),
        "significance": (
            "Major events are the narrative skeleton of Star Wars — the moments fans date everything from, "
            "and the references that connect films, series, games, and novels into a shared chronology.\n\n"
            "Understanding these turning points clarifies why the Jedi fell, why the Empire endured "
            "despite Endor, and why the New Republic's demilitarization had catastrophic consequences."
        ),
        "notableEvents": [
            "Ruusan Reformations establish the modern Republic (~1,000 BBY)",
            "Trade Federation blockades Naboo; Palpatine elected Chancellor (32 BBY)",
            "First Battle of Geonosis opens the Clone Wars (22 BBY)",
            "Order 66 and the Great Jedi Purge (19 BBY)",
            "Proclamation of the Galactic Empire (19 BBY)",
            "Battle of Yavin — first Death Star destroyed (0 BBY)",
            "Battle of Endor — Emperor Palpatine killed (4 ABY)",
            "Battle of Jakku — Imperial capitulation (5 ABY)",
            "Destruction of the Hosnian system by Starkiller Base (34 ABY)",
            "Battle of Exegol — Final Order defeated (35 ABY)",
        ],
        "affiliations": [
            "Galactic Republic / Empire / New Republic",
            "Jedi Order",
            "Confederacy of Independent Systems",
            "Rebel Alliance / Resistance",
            "Sith (Rule of Two and Eternal)",
        ],
        "timeline": [
            {"era": "~1,000 BBY", "event": "Ruusan Reformations reshape Republic and Jedi"},
            {"era": "32 BBY", "event": "Naboo crisis elevates Palpatine"},
            {"era": "22 BBY", "event": "Clone Wars begin at Geonosis"},
            {"era": "19 BBY", "event": "Empire rises; Jedi Purge executed"},
            {"era": "0 BBY", "event": "Battle of Yavin defines galactic dating"},
            {"era": "4 ABY", "event": "Endor victory ends Palpatine's reign"},
            {"era": "34 ABY", "event": "Hosnian cataclysm shatters New Republic"},
            {"era": "35 ABY", "event": "Galaxy unites at Exegol"},
        ],
    },
    "republic-era": {
        "overview": (
            "The Republic Era spans more than twenty-five millennia of democratic experiment — "
            "from the unification of the Core Worlds through the Jedi's long guardianship, the "
            "corporate corruption of the late Republic, and the final collapse into Empire. "
            "For most of this period the Republic was the default condition of civilized space."
        ),
        "history": (
            "Early Republic history is fragmented — tales of the Rakata, the Mandalorian crusades, "
            "and repeated Sith wars that scarred the galaxy. The Great Hyperspace War and subsequent "
            "conflicts proved that dark-side empires could threaten the entire known map.\n\n"
            "After Ruusan, the Republic entered a millennium of relative stability. The Jedi recast "
            "themselves as peacekeepers rather than warriors, taking younglings from across the galaxy "
            "and serving as negotiators in a slowly expanding union of worlds.\n\n"
            "The late Republic was defined by inequality: Core wealth, Rim neglect, and megacorporations "
            "with private armies. The Senate became a venue for trade disputes rather than justice. "
            "Chancellors like Valorum failed to act decisively until Palpatine demonstrated how "
            "crisis could centralize power.\n\n"
            "By 19 BBY the Republic was a war state — clones in every sector, Jedi as generals, "
            "and civil liberties suspended in the name of victory. When the war ended, the institution "
            "survived only long enough to vote itself out of existence."
        ),
        "significance": (
            "Every rebellion in Star Wars invokes the Republic as the lost ideal — proof that "
            "democracy once worked at galactic scale, however imperfectly.\n\n"
            "The era explains the Jedi Order's political role, the Outer Rim's distrust of Coruscant, "
            "and why Palpatine needed a war rather than a coup to seize control."
        ),
        "notableEvents": [
            "Founding and expansion of the Galactic Republic",
            "Multiple Jedi–Sith galactic wars",
            "Ruusan Reformations (~1,000 BBY)",
            "Mandalorian conflicts with Jedi and Republic",
            "Trade route disputes and corporate militarization",
            "Invasion of Naboo (32 BBY)",
            "Separatist Crisis (24–22 BBY)",
            "Transformation into the Galactic Empire (19 BBY)",
        ],
        "affiliations": [
            "Galactic Senate",
            "Jedi Order",
            "Republic Judicial Forces / later Grand Army",
            "Core and Mid Rim member worlds",
            "Outer Rim Territories",
        ],
        "timeline": [
            {"era": "25,000+ BBY", "event": "Republic consolidates Core governance"},
            {"era": "Old Republic wars", "event": "Repeated Sith and Mandalorian conflicts"},
            {"era": "~1,000 BBY", "event": "Ruusan peace begins Jedi's golden age"},
            {"era": "Late Republic", "event": "Corporate influence and Rim unrest grow"},
            {"era": "32–19 BBY", "event": "Palpatine's rise and Republic militarization"},
        ],
    },
    "high-republic": {
        "overview": (
            "The High Republic was an age of expansion and confidence — Jedi as heroes of the frontier, "
            "Starlight Beacons guiding hyperspace lanes, and a Republic that believed the light side "
            "could outshine any shadow. It ended not in one battle but in the revelation that "
            "hubris and neglect could breed horrors like the Nihil and the Drengir."
        ),
        "history": (
            "Centuries before the prequel trilogy, the Republic pushed into the Outer Rim with "
            "optimism unmatched in later eras. Chancellor Lina Soh's Great Hyperspace Rush opened "
            "new routes; Jedi like Avar Kriss, Elzar Mann, and Stellan Gios served as public "
            "symbols of justice rather than secretive monks.\n\n"
            "Starlight Beacons — massive space stations — became lighthouses for navigation and "
            "diplomacy. The Jedi Temple on Coruscant worked openly with the Senate, and many "
            "worlds welcomed Jedi as liberators rather than suspicious mystics.\n\n"
            "The Nihil — marauders led by Marchion Ro — weaponized hyperspace anomalies and "
            "demonstrated that the Republic's expansion had outpaced its ability to protect settlers. "
            "The destruction of Starlight Beacon and the Legacy Run disaster shattered the era's "
            "complacency.\n\n"
            "Parallel threats like the Drengir and the Nameless creatures forced Jedi to confront "
            "limits of the Force itself. By the time of the prequel era, the Order had retreated "
            "into caution — a shadow of the High Republic's open idealism."
        ),
        "significance": (
            "The High Republic reframes Jedi history — showing them beloved, visible, and politically "
            "trusted before the Clone Wars tarnished their reputation.\n\n"
            "It connects ancient threats to modern ones, and explains why later Jedi feared "
            "attachment, frontier expansion, and public celebrity."
        ),
        "notableEvents": [
            "Great Hyperspace Rush expands Republic frontiers",
            "Construction of Starlight Beacon network",
            "Legacy Run hyperspace disaster",
            "Nihil conflict and Marchion Ro's campaigns",
            "Drengir awakening in the Outer Rim",
            "Fall of Starlight Beacon",
            "Gradual retreat from High Republic optimism",
        ],
        "affiliations": [
            "Galactic Republic (High Republic period)",
            "Jedi Order — frontier guardians",
            "Starlight Beacon program",
            "Nihil marauders (antagonists)",
            "Outer Rim settlement charters",
        ],
        "timeline": [
            {"era": "~500 BBY", "event": "Republic enters High Republic phase"},
            {"era": "~232 BBY", "event": "Starlight Beacon era peak"},
            {"era": "Nihil crisis", "event": "Hyperspace terrorism devastates Rim"},
            {"era": "~136 BBY", "event": "High Republic confidence wanes"},
            {"era": "Prequel era", "event": "Jedi adopt more cautious public role"},
        ],
    },
    "clone-wars": {
        "overview": (
            "The Clone Wars were three years of total galactic war — the Republic and Confederacy "
            "fighting across thousands of worlds while Darth Sidious manipulated both sides toward "
            "a single outcome: Jedi extinction and Imperial birth. It was the Republic's last war "
            "and the Jedi Order's fatal trial."
        ),
        "history": (
            "Geonosis (22 BBY) transformed a political crisis into open warfare overnight. Kaminoan "
            "clone legions, ordered in secret by Sifo-Dyas and funded by Sidious, gave the Republic "
            "an army overnight — while Separatist droid foundries matched them ship for ship.\n\n"
            "Generals like Obi-Wan Kenobi, Anakin Skywalker, and Mace Windu became battlefield "
            "celebrities; Count Dooku and General Grievous served as Confederate figureheads. "
            "Corporate backers profited from both sides while Rim worlds burned.\n\n"
            "The war eroded Republic values: civilian casualties, military tribunals, and emergency "
            "powers that never expired. Anakin's secret marriage, Padmé's peace efforts, and Dooku's "
            "political arguments all competed with the simple fact that the war was designed not "
            "to be won — but to exhaust.\n\n"
            "When Grievous struck Coruscant and kidnapped Palpatine, the Chancellor's rescue "
            "provided cover for Anakin's fall. Order 66, issued moments after Dooku's death, "
            "turned every clone against their Jedi generals. The Separatist shutdown and Mustafar "
            "massacre ended the war in a day — with Sidious ruling both outcomes."
        ),
        "significance": (
            "The Clone Wars explain how a democracy dies with popular support — war as distraction, "
            "enemies manufactured, and heroes turned into weapons.\n\n"
            "The era connects the prequel films, The Clone Wars series, and Bad Batch — defining "
            "character arcs for Anakin, Ahsoka, Rex, and the galaxy that would accept the Empire."
        ),
        "notableEvents": [
            "First Battle of Geonosis (22 BBY)",
            "Battle of Christophsis and early Rim campaigns",
            "Mortis and Force-wielder encounters (Anakin's destiny)",
            "Siege of Mandalore and Darth Maul's schemes",
            "Battle of Coruscant — Chancellor 'rescued'",
            "Anakin Skywalker falls; becomes Darth Vader",
            "Order 66 executed across the galaxy",
            "Separatist leadership eliminated on Mustafar",
        ],
        "affiliations": [
            "Galactic Republic / Grand Army of the Republic",
            "Confederacy of Independent Systems",
            "Jedi Order (military command)",
            "Sith — Darth Sidious orchestrating both sides",
            "Mandalore, Neutral systems, Corporate sponsors",
        ],
        "timeline": [
            {"era": "22 BBY", "event": "War declared after Geonosis"},
            {"era": "Mid-war", "event": "Outer Rim sieges and hero campaigns"},
            {"era": "21–20 BBY", "event": "Political corruption deepens in Senate"},
            {"era": "19 BBY", "event": "Coruscant battle and Order 66"},
            {"era": "19 BBY", "event": "Empire proclaimed; war ends"},
        ],
    },
    "imperial-era": {
        "overview": (
            "The Imperial Era was twenty-three years of rule by fear — Palpatine's New Order replacing "
            "Senate debate with Moffs, the ISB, and fleet deployments. The Jedi were hunted to near "
            "extinction, dissent crushed on worlds from Lothal to Alderaan, and rebellion slowly "
            "kindled until Endor broke the Empire's myth of invincibility."
        ),
        "history": (
            "Day one of the Empire brought the Jedi Temple's burning broadcast as warning. Inquisitors "
            "hunted survivors; Kamino was sanitized; and the clone army gave way to recruited "
            "stormtroopers loyal to the Emperor alone.\n\n"
            "The Death Star program consumed entire budgets — a mobile world-killer meant to "
            "end rebellion before it started. Dissolution of the Senate (0 BBY) removed the last "
            "facade of democracy while the station neared completion.\n\n"
            "Rebellion grew in cells: Bail Organa's network, Hera's Spectres, Saw Gerrera's "
            "extremists, and eventually Mon Mothma's Alliance. Scarif delivered Death Star plans; "
            "Yavin destroyed the weapon; Hoth tested the Alliance's resolve.\n\n"
            "Endor (4 ABY) killed Palpatine and Vader, shattered the second Death Star, and "
            "inspired uprisings across occupied worlds. Imperial remnants fought for years — "
            "Thrawn in some timelines, warlords in others — until Jakku (5 ABY) ended the "
            "Imperial Era as a unified threat."
        ),
        "significance": (
            "The Empire is the saga's central tyranny — the benchmark for every 'order' movement "
            "that follows, from the First Order to fascist nostalgia in the New Republic Senate.\n\n"
            "Its institutions — COMPNOR, ISB, Inquisitorius — show how bureaucratic evil sustains "
            "itself beyond any single leader."
        ),
        "notableEvents": [
            "Proclamation of the New Order (19 BBY)",
            "Great Jedi Purge and Inquisitor campaigns",
            "Construction of the first Death Star",
            "Dissolution of the Imperial Senate (0 BBY)",
            "Destruction of Alderaan as terror demonstration",
            "Battle of Yavin — Rebel victory (0 BBY)",
            "Battle of Hoth and pursuit of the Alliance (3 ABY)",
            "Battle of Endor — Emperor killed (4 ABY)",
            "Battle of Jakku — Imperial surrender (5 ABY)",
        ],
        "affiliations": [
            "Galactic Empire",
            "Imperial Navy and Stormtrooper Corps",
            "Imperial Security Bureau",
            "Inquisitorius",
            "Rebel Alliance (opposition)",
        ],
        "timeline": [
            {"era": "19 BBY", "event": "Empire consolidates power; Jedi hunted"},
            {"era": "Imperial Era", "event": "Death Star and Rim pacification"},
            {"era": "0 BBY", "event": "Senate dissolved; Yavin battle"},
            {"era": "Galactic Civil War", "event": "Alliance escalates to open war"},
            {"era": "4–5 ABY", "event": "Endor and Jakku end Imperial unity"},
        ],
    },
    "new-republic": {
        "overview": (
            "The New Republic Era promised restoration after Endor — Senate chambers reopened, "
            "Imperial war machines dismantled, and Mon Mothma's vision of peace through diplomacy. "
            "For thirty years it held, but demilitarization, political division, and blindness "
            "to the First Order's rise left the galaxy vulnerable to another cataclysm."
        ),
        "history": (
            "Chandrila hosted the first restored Senate sessions. Former rebels became senators; "
            "Imperial officers faced trials or amnesty depending on faction; and the galaxy "
            "celebrated a hard-won peace.\n\n"
            "The Galactic Concordance (5 ABY) formalized Imperial surrender at Jakku, restricting "
            " remnant fleets and banning certain weapons — but also allowing hidden Imperial "
            "holdouts to flee into the Unknown Regions with sympathizers and resources.\n\n"
            "Capital moved to Hosnian Prime as the Republic expanded membership. Populists and "
            "Centrists debated demilitarization: should the New Republic maintain a fleet capable "
            "of deterring warlords, or trust that Endor had ended fascism forever?\n\n"
            "Leia Organa's warnings about Imperial remnants were sidelined. The Resistance formed "
            "unofficially while the Senate argued. Starkiller Base's strike (34 ABY) destroyed "
            "Hosnian Prime and most of the government in an instant — proving the New Republic "
            "had traded security for optimism once again."
        ),
        "significance": (
            "The New Republic shows the difficulty of peace-building — forgiveness vs accountability, "
            "security vs liberty, and the assumption that victory is permanent.\n\n"
            "Its fall sets the sequel trilogy's stakes and explains why the Resistance fought "
            "without official backing."
        ),
        "notableEvents": [
            "Proclamation of the New Republic (4 ABY)",
            "Battle of Jakku and Galactic Concordance (5 ABY)",
            "Demilitarization debates in the Senate",
            "Capital relocation to Hosnian Prime",
            "Leia Organa forms the Resistance (28 ABY)",
            "First Order emerges from Unknown Regions",
            "Destruction of the Hosnian system (34 ABY)",
        ],
        "affiliations": [
            "New Republic Senate",
            "New Republic Defense Force (reduced over time)",
            "Imperial Remnants / warlords",
            "Resistance (unofficial opposition to First Order)",
            "Populist and Centrist factions",
        ],
        "timeline": [
            {"era": "4 ABY", "event": "Republic restored after Endor"},
            {"era": "5 ABY", "event": "Jakku ends open Imperial war"},
            {"era": "Decades of peace", "event": "Senate governs; military scaled back"},
            {"era": "28 ABY", "event": "Leia marginalized; Resistance begins"},
            {"era": "34 ABY", "event": "Hosnian annihilation ends the era"},
        ],
    },
    "first-order-era": {
        "overview": (
            "The First Order Era compresses galactic crisis into a few explosive years — hidden "
            "Imperial revival, the Resistance's desperate fight, Starkiller Base, Snoke's Supremacy, "
            "and Palpatine's return on Exegol. It is the sequel trilogy's span: legacy, failure, "
            "and the question of whether the galaxy can break cycles of darkness."
        ),
        "history": (
            "After the Concordance, Imperial ideologues regrouped beyond the known map. Snoke — "
            "later revealed as a pawn of deeper Sith designs — molded Kylo Ren from Ben Solo's "
            "fall and rebuilt stormtrooper legions from abducted children.\n\n"
            "The New Republic's leadership refused full mobilization. Leia's Resistance operated "
            "covertly while the First Order tested borders. Starkiller Base's first firing "
            "destroyed five worlds including Hosnian Prime — the Senate, fleet, and bureaucracy "
            "gone in seconds.\n\n"
            "Rey, Finn, Poe, and Luke's legacy intersected in a race to destroy superweapons and "
            "reach Kylo Ren before Snoke consolidated absolute power. Holdo's hyperspace ram and "
            "Luke's projection at Crait preserved hope when defeat seemed total.\n\n"
            "Palpatine's reveal on Exegol (35 ABY) exposed the First Order as prelude to a "
            "Final Order. The citizens' fleet — ordinary pilots answering the call — defeated "
            "the Sith armada and ended the era with Ben Solo's redemption and Rey's choice of identity."
        ),
        "significance": (
            "This era closes the Skywalker narrative — asking whether destiny is blood or choice, "
            "and whether democracies must remain vigilant forever.\n\n"
            "It connects the original trilogy's heroes to a new generation burdened by their failures "
            "and their hope."
        ),
        "notableEvents": [
            "Ben Solo falls to the dark side; Knights of Ren formed",
            "Resistance intelligence locates Starkiller Base",
            "Hosnian system destroyed (34 ABY)",
            "Starkiller Base destroyed by Resistance",
            "Snoke killed aboard the Supremacy; Kylo Ren takes command",
            "Siege of Crait — Luke Skywalker's stand",
            "Palpatine revealed on Exegol (35 ABY)",
            "Battle of Exegol — Final Order defeated",
        ],
        "affiliations": [
            "First Order",
            "Resistance",
            "Knights of Ren",
            "Sith Eternal",
            "Citizens' fleet (final battle)",
        ],
        "timeline": [
            {"era": "28 ABY", "event": "Resistance organized amid Senate denial"},
            {"era": "34 ABY", "event": "Open war begins with Hosnian strike"},
            {"era": "34 ABY", "event": "Starkiller destroyed; fleet hunted"},
            {"era": "35 ABY", "event": "Exegol battle ends Palpatine and First Order"},
        ],
    },
    "legends-timeline": {
        "overview": (
            "Star Wars Legends is the Expanded Universe continuity that flourished before Lucasfilm "
            "declared it non-canon in 2014. Spanning comics, novels, games, and radio dramas, "
            "Legends told stories from Tales of the Jedi through Legacy — a parallel chronology "
            " fans still celebrate for its depth, contradictions, and ambition."
        ),
        "history": (
            "Legends began with early Marvel comics and Brian Daley's Han Solo adventures, then "
            "exploded with Timothy Zahn's Heir to the Empire trilogy — introducing Grand Admiral "
            "Thrawn and a post-Endor Empire that felt strategically terrifying.\n\n"
            "Dark Horse comics explored the Old Republic: Tales of the Jedi, Knights of the Old Republic, "
            "and the Mandalorian Wars that shaped Revan and Malak. BioWare's KOTOR games became "
            "touchstones for interactive Legends storytelling.\n\n"
            "The New Jedi Order novels pushed the galaxy into biological horror and moral ambiguity; "
            "Legacy comics jumped to 137 ABY with Cade Skywalker wielding a lightsaber against "
            "a Sith-dominated Empire. Clone Wars multimedia projects bridged prequel gaps until "
            "George Lucas's canon decisions diverged.\n\n"
            "When Disney acquired Lucasfilm, the Story Group reset continuity — canon films and "
            "series superseded Legends, though names like Thrawn, Rukh, and Korriban persist in "
            "adapted form. Legends remains available as 'Infinities' heritage — not official history, "
            "but essential cultural context for decades of fandom."
        ),
        "significance": (
            "Legends explains why so many fans reference Thrawn, Mara Jade, Revan, and Kyle Katarn — "
            "and why debates about canon still matter emotionally even when official timelines move on.\n\n"
            "It preserves thousands of years of storytelling that canon has only begun to re-explore "
            "through High Republic and Old Republic projects."
        ),
        "notableEvents": [
            "Tales of the Jedi — ancient Sith and Jedi wars",
            "Knights of the Old Republic — Revan and Malak",
            "Great Sith War and Mandalorian Wars",
            "Heir to the Empire — Thrawn campaigns (9 ABY)",
            "Dark Empire — Palpatine clones return",
            "New Jedi Order — Yuuzhan Vong invasion",
            "Legacy era — Cade Skywalker (137 ABY)",
            "2014 Lucasfilm continuity reset — Legends label applied",
        ],
        "affiliations": [
            "Expanded Universe publishing imprints",
            "Old Republic Jedi and Sith Empires (Legends)",
            "New Republic / Galactic Alliance (Legends)",
            "Yuuzhan Vong (Legends antagonists)",
            "Legacy Sith and Imperial Remnants",
        ],
        "timeline": [
            {"era": "25,000+ BBY", "event": "Legends ancient history — Rakata, early Jedi"},
            {"era": "Old Republic era", "event": "KOTOR, Tales of the Jedi stories"},
            {"era": "Post-Endor EU", "event": "Thrawn, Dark Empire, Jedi Academy"},
            {"era": "New Jedi Order", "event": "Vong war reshapes galaxy"},
            {"era": "Legacy comics", "event": "Far-future Skywalker line continues"},
            {"era": "2014", "event": "Legends designation; canon reset"},
        ],
    },
}
