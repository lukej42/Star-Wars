#!/usr/bin/env python3
"""Hand-authored extended profiles for Factions Directory entries."""

from __future__ import annotations

FACTION_PROFILES: dict[str, dict] = {
    "republic": {
        "overview": (
            "The Galactic Republic was the dominant political union of the galaxy for more than a thousand "
            "generations, binding thousands of star systems through a federal Senate on Coruscant. "
            "It promised representation, trade, and peace — yet its final century was defined by "
            "institutional rot, corporate influence, and a slow surrender of emergency powers that "
            "would ultimately destroy it from within."
        ),
        "history": (
            "Founded after the defeat of the Sith at Ruusan, the Republic entered a long era of relative "
            "stability. Core Worlds prospered while the Rim often went underserved; senators traded "
            "favors, and megacorporations gained seats at the table through lobbying and proxy votes.\n\n"
            "The Trade Federation's blockade of Naboo exposed how fragile Republic authority had become. "
            "Chancellor Valorum's fall and Palpatine's rise marked a turning point: crises would now "
            "be answered with stronger executive power rather than structural reform.\n\n"
            "The Separatist Crisis and Clone Wars consumed the galaxy. Jedi served as generals, "
            "Kaminoan clones filled the ranks, and entire sectors burned while the Senate debated. "
            "When Order 66 executed and the Jedi Temple fell, Palpatine declared the Republic "
            "reorganized into the First Galactic Empire — the democracy died not in rebellion but "
            "in applause on the Senate floor."
        ),
        "significance": (
            "The Republic is the galaxy's great 'before' state: the benchmark rebels invoke when they "
            "speak of restoration, and the system Palpatine exploited to seize total control.\n\n"
            "Its story explains why the Jedi Order was politically vulnerable, why the Outer Rim "
            "mistrusted Coruscant, and why later governments struggled to balance security with liberty."
        ),
        "notableEvents": [
            "Ruusan Reformations establish the modern Republic (~1,000 BBY)",
            "Trade Federation blockades Naboo; Palpatine elected Supreme Chancellor",
            "Separatist movement forms under Count Dooku",
            "Clone Wars erupt across the galaxy",
            "Emergency powers centralize authority in the Chancellor's office",
            "Order 66 and the Great Jedi Purge",
            "Declaration of the Galactic Empire from the Senate chamber",
        ],
        "affiliations": [
            "Galactic Senate",
            "Jedi Order ( guardians, not rulers )",
            "Republic Navy and Grand Army of the Republic",
            "Core and Mid Rim member worlds",
            "Outer Rim territories ( often underrepresented )",
        ],
        "timeline": [
            {"era": "Old Republic", "event": "Republic consolidates after Sith defeat at Ruusan"},
            {"era": "Late Republic", "event": "Corporate influence and Rim neglect deepen"},
            {"era": "Invasion of Naboo", "event": "Palpatine rises to the chancellorship"},
            {"era": "Separatist Crisis", "event": "Systems secede; military buildup begins"},
            {"era": "Clone Wars", "event": "Full-scale galactic war under emergency powers"},
            {"era": "19 BBY", "event": "Republic reorganized into the Galactic Empire"},
        ],
    },
    "confederacy": {
        "overview": (
            "The Confederacy of Independent Systems — the Separatist Alliance — presented itself as "
            "a coalition of sovereign worlds rejecting Coruscant's taxation, corruption, and neglect. "
            "Led publicly by Count Dooku and backed by the Trade Federation, Banking Clan, and Techno Union, "
            "the Confederacy fielded vast droid armies. In truth, Darth Sidious engineered the movement "
            "to weaken the Republic and manufacture the war that would end democracy."
        ),
        "history": (
            "Decades of grievance over trade routes, Senate gridlock, and Rim exploitation created "
            "fertile ground for secession. Dooku, a former Jedi, offered aristocratic credibility "
            "to the movement while secret Sith funds armed foundries on Geonosis and beyond.\n\n"
            "The Battle of Geonosis opened the Clone Wars. Separatist fleets, led by figures like "
            "General Grievous, struck across the Mid and Outer Rims. Corporate interests profited "
            "from both sides while civilian populations suffered occupation and bombardment.\n\n"
            "As the war dragged on, internal rivalries among Separatist councils and corporate "
            "sponsors weakened coordination. When Anakin Skywalker killed Dooku and later Sidious "
            "ordered the shutdown of droid armies, the Confederacy collapsed overnight — a puppet "
            "alliance discarded once its purpose was served."
        ),
        "significance": (
            "The Confederacy embodies the tragedy of legitimate grievances weaponized by hidden "
            "authoritarians. Its droid legions forever changed galactic warfare, and its collapse "
            "left Rim worlds distrustful of both Coruscant and corporate sponsors.\n\n"
            "Imperial propaganda later recast all Separatists as traitors, erasing the complex "
            "political causes that had driven many systems to leave."
        ),
        "notableEvents": [
            "Raxus Secundus hosts Separatist parliament",
            "Geonosis droid foundries mass-produce battle units",
            "Corporate backers sign the treaty of alliance",
            "General Grievous leads strikes across the galaxy",
            "Sieges of contested Rim worlds and hyperspace lanes",
            "Mustafar summit and execution of Separatist leadership",
            "Remote shutdown ends Separatist droid armies ( 19 BBY )",
        ],
        "affiliations": [
            "Executive Separatist Council",
            "Trade Federation",
            "InterGalactic Banking Clan",
            "Techno Union",
            "Commerce Guild",
            "Retail Caucus and other corporate blocs",
            "Confederacy military ( droid army )",
        ],
        "timeline": [
            {"era": "24 BBY", "event": "Confederacy formally organized; Raxus becomes capital"},
            {"era": "22 BBY", "event": "First battle of Geonosis opens the Clone Wars"},
            {"era": "Clone Wars", "event": "Corporate-backed droid offensives across the Rim"},
            {"era": "Late Clone Wars", "event": "Grievous campaigns threaten the Core"},
            {"era": "19 BBY", "event": "Leadership eliminated; droid armies deactivated"},
        ],
    },
    "empire": {
        "overview": (
            "The Galactic Empire replaced the Republic with rule through fear, replacing the Senate's "
            "debate with Moffs, ISB surveillance, and fleet deployments. Emperor Palpatine ruled from "
            "the Imperial Center while the Death Star symbolized the doctrine that rebellion would "
            "mean planetary annihilation. For two decades the Empire appeared unassailable — until "
            "a growing Alliance proved that tyranny could be broken."
        ),
        "history": (
            "Born in the smoke of the Jedi Purge, the Empire rapidly militarized society. The clone "
            "army gave way to recruited stormtroopers; the Jedi were declared enemies of civilization; "
            "and regional governors gained sweeping authority over their sectors.\n\n"
            "Projects like the Death Star consumed resources on an unimaginable scale. Dissent was "
            "crushed on worlds like Lothal and Alderaan — the latter's destruction demonstrating "
            "that even peaceful opposition offered no safety.\n\n"
            "The Rebel Alliance grew in the shadows, winning moral victories at Scarif and a decisive "
            "strike at Yavin. Even after the second Death Star fell at Endor and Palpatine died, "
            "Imperial remnants fought on for years until the Battle of Jakku formally ended the "
            "Imperial Era in the New Republic's victory."
        ),
        "significance": (
            "The Empire is the saga's central tyranny — the force every generation of heroes must "
            "confront in some form, from Palpatine's open rule to the First Order's revival.\n\n"
            "Its machinery of oppression — Inquisitors, COMPNOR, Imperial Security Bureau — "
            "influenced every successor movement that tried to restore 'order' without freedom."
        ),
        "notableEvents": [
            "Proclamation of the New Order in the Senate",
            "Great Jedi Purge and hunting of survivors",
            "Construction of the first Death Star",
            "Dissolution of the Imperial Senate ( 0 BBY )",
            "Destruction of Alderaan as a terror demonstration",
            "Battle of Yavin — first major Rebel victory",
            "Battle of Endor — Emperor and second Death Star destroyed",
            "Battle of Jakku — Imperial capitulation to the New Republic",
        ],
        "affiliations": [
            "Imperial Ruling Council",
            "Imperial Navy and Stormtrooper Corps",
            "Imperial Security Bureau ( ISB )",
            "Inquisitorius",
            "COMPNOR and propaganda ministries",
            "Regional Moffs and sector commands",
        ],
        "timeline": [
            {"era": "19 BBY", "event": "Empire proclaimed; Jedi declared traitors"},
            {"era": "Imperial Era", "event": "Death Star program and Rim pacification campaigns"},
            {"era": "0 BBY", "event": "Senate dissolved; Death Star operational"},
            {"era": "Galactic Civil War", "event": "Rebellion escalates from cells to open war"},
            {"era": "4 ABY", "event": "Emperor killed at Endor; Empire fragments"},
            {"era": "5 ABY", "event": "Final defeat at Jakku"},
        ],
    },
    "rebel-alliance": {
        "overview": (
            "The Alliance to Restore the Republic united scattered rebel cells, dissident senators, "
            "and Rim freedom fighters into a coordinated resistance against the Galactic Empire. "
            "Outgunned and hunted, it survived through secrecy, sacrifice, and the conviction "
            "that a single starfighter could change the course of history."
        ),
        "history": (
            "Early resistance took the form of isolated cells — Saw Gerrera's partisans, Bail Organa's "
            "network, and Hera Syndulla's Spectres among them. Mon Mothma's Declaration of Rebellion "
            "on Chandrila gave the movement a public face and a shared cause.\n\n"
            "The Alliance operated from hidden bases: Dantooine, Yavin 4, Hoth, and others. Intelligence "
            "from spies like Cassian Andor and leaders like Leia Organa kept the fight coordinated while "
            "Admiral Ackbar and General Dodonna planned fleet actions.\n\n"
            "Victories at Scarif, Yavin, and Endor proved the Empire could bleed. The Alliance's "
            "success was never guaranteed — it lost bases, leaders, and entire squadrons — but its "
            "persistence culminated in the New Republic's founding and the Empire's defeat."
        ),
        "significance": (
            "The Rebellion is the template for every subsequent resistance: moral clarity against "
            "overwhelming force, coalition politics under pressure, and the idea that ordinary "
            "people — pilots, mechanics, senators — can topple empires.\n\n"
            "Its symbols, from the starbird to the orange flight suits, remain icons of defiance "
            "across the galaxy decades later."
        ),
        "notableEvents": [
            "Mon Mothma's Declaration of Rebellion",
            "Battle of Scarif — Death Star plans stolen",
            "Battle of Yavin — first Death Star destroyed",
            "Evacuation of Hoth and pursuit through the asteroid field",
            "Operation Yellow Moon and other intelligence campaigns",
            "Battle of Endor — second Death Star and Emperor destroyed",
            "Transition into the New Republic government",
        ],
        "affiliations": [
            "Alliance High Command",
            "Rebel Alliance Starfighter Corps",
            "Rebel Alliance Intelligence Service",
            "Massassi Group and other sector commands",
            "Allied governments ( Alderaan, Chandrila, etc. )",
            "Smugglers and Rim contacts ( unofficial )",
        ],
        "timeline": [
            {"era": "Early Rebellion", "event": "Cells operate independently against Imperial targets"},
            {"era": "2 BBY", "event": "Formal Alliance established under Mon Mothma"},
            {"era": "0 BBY", "event": "Death Star plans secured; Yavin victory"},
            {"era": "3 ABY", "event": "Hoth base lost; fleet scattered and regrouped"},
            {"era": "4 ABY", "event": "Decisive victory at Endor"},
        ],
    },
    "new-republic": {
        "overview": (
            "The New Republic restored democratic government after the Empire's fall, dismantling "
            "Imperial war machines and reopening the Senate on Chandrila. Mon Mothma envisioned a "
            "demilitarized, peaceful galaxy — but warlords, Imperial holdouts, and eventually the "
            "First Order ensured that victory at Endor was only the beginning of a long, fragile peace."
        ),
        "history": (
            "Founded in the wake of Endor, the New Republic moved quickly to claim legitimacy: "
            "senators returned, Imperial assets were seized or decommissioned, and the galaxy "
            "celebrated liberation. Chandrila served as the first capital before the seat of "
            "government eventually moved to Hosnian Prime.\n\n"
            "Demilitarization proved controversial. Some systems demanded strong defense against "
            "remnants; others feared repeating the Republic's militarization. The Galactic Concordance "
            "with surviving Imperial forces bought time but also allowed hidden fleets to regroup "
            "in the Unknown Regions.\n\n"
            "For decades the New Republic held, weathering crises like the Imperial resurgence on "
            "Jakku and political splits over how harshly to treat former Imperials. Its sudden "
            "destruction when Starkiller Base annihilated the Hosnian system ended an era in "
            "minutes — leaving a scattered Resistance to face the First Order alone."
        ),
        "significance": (
            "The New Republic represents the difficulty of building peace after war: institutions "
            "without armies, forgiveness without accountability, and the assumption that evil "
            "vanquished once stays vanquished.\n\n"
            "Its fall demonstrates how centralized democratic bodies remain vulnerable to "
            "existential strikes — a lesson the Resistance would learn painfully."
        ),
        "notableEvents": [
            "Galactic Senate reconvenes on Chandrila",
            "Imperial capitulation at Jakku ( 5 ABY )",
            "Galactic Concordance signed with Imperial remnants",
            "Capital relocated to Hosnian Prime",
            "Political debates over demilitarization and former Imperials",
            "Rise of the First Order in the Unknown Regions",
            "Destruction of the Hosnian system by Starkiller Base ( 34 ABY )",
        ],
        "affiliations": [
            "Galactic Senate ( New Republic )",
            "New Republic Defense Force ( later reduced )",
            "New Republic Intelligence",
            "Member systems across Core and Rim",
            "Populist and Centrist political factions",
        ],
        "timeline": [
            {"era": "4 ABY", "event": "Republic proclaimed after Endor"},
            {"era": "5 ABY", "event": "Jakku campaign ends open Imperial resistance"},
            {"era": "New Republic Era", "event": "Senate governs; military scaled back"},
            {"era": "Unknown Regions", "event": "First Order builds strength in secret"},
            {"era": "34 ABY", "event": "Hosnian system destroyed; government decapitated"},
        ],
    },
    "hutts": {
        "overview": (
            "The Hutt Cartel is not a conventional government but a network of kajidic clans whose "
            "wealth, violence, and patience have outlasted republics and empires alike. From Nal Hutta "
            "and Nar Shaddaa to desert palaces on Tatooine, Hutts control smuggling lanes, slavery, "
            "gambling, and bounty markets — trading stability with whoever holds power for a share "
            "of the shadow economy."
        ),
        "history": (
            "Hutt dominance predates the modern Republic by millennia. Their homeworld Nal Hutta "
            "( Glorious Jewel ) and its moon Nar Shaddaa became criminal capitals where law is "
            "negotiated in contracts and broken backs.\n\n"
            "During the Republic and Imperial eras, Hutts often played both sides: selling weapons, "
            "hosting fugitives, and enforcing debts through bounty hunters like Boba Fett. Jabba "
            "Desilijic Tiure's court on Tatooine exemplified Hutt power — a sovereign crime lord "
            "whose reach extended into the Core.\n\n"
            "Even when galactic governments claimed to oppose slavery and piracy, practical politics "
            "kept the Cartel entrenched in the Outer Rim. Successor powers from the New Republic "
            "to criminal syndicates like the Pykes continued to intersect with Hutt interests."
        ),
        "significance": (
            "The Cartel shows how power persists outside formal states. Hutts influence wars without "
            "flying battle fleets, and their longevity explains why the Rim often views Coruscant "
            "and Imperial Center as interchangeable occupiers.\n\n"
            "Hutt culture — kajidic hierarchy, the life debt, gaudy palaces — remains a fixture of "
            "underworld storytelling across eras."
        ),
        "notableEvents": [
            "Hutt Space established as semi-autonomous territory",
            "Nar Shaddaa becomes a smuggler's moon",
            "Republic and Empire tolerate Hutt neutrality in much of the Rim",
            "Jabba's court dominates Tatooine underworld",
            "Bounty hunter guilds operate under Hutt contracts",
            "Post-Imperial syndicate wars reshape Cartel influence",
        ],
        "affiliations": [
            "Kajidic clans ( Desilijic, Besadii, etc. )",
            "Hutt Grand Council",
            "Bounty Hunters' Guild ( patronage )",
            "Smuggler networks and spice runners",
            "Nar Shaddaa criminal districts",
        ],
        "timeline": [
            {"era": "Ancient Era", "event": "Hutt expansion across the Outer Rim"},
            {"era": "Old Republic", "event": "Hutt Space recognized as distinct sphere"},
            {"era": "Imperial Era", "event": "Uneasy coexistence with the Empire"},
            {"era": "Galactic Civil War", "event": "Hutts profit from both sides"},
            {"era": "New Republic Era", "event": "Syndicate conflicts reshape Cartel power"},
        ],
    },
    "sith-empire": {
        "overview": (
            "Long before Palpatine's Galactic Empire, ancient Sith built dark-side theocracies on "
            "Korriban, Dromund Kaas, and Ziost — empires forged in exile, betrayal, and war against "
            "the Jedi. From Naga Sadow's invasions to Vitiate's immortal reign, these Sith states "
            "reshaped the galaxy and left tombs, fleets, and doctrines that would echo for millennia."
        ),
        "history": (
            "Exiled Dark Jedi merged with the Sith species on Korriban, creating a culture obsessed "
            "with power, lineage, and the dark side. Sith Empires rose and fell in cycles of internal "
            "betrayal — the Rule of Two later emerged precisely because larger Sith orders "
            "destroyed themselves.\n\n"
            "Great Hyperspace War, Mandalorian Wars, and Jedi Civil War eras saw Sith armadas threaten "
            "the Republic itself. Tenebrae, who became the Sith Emperor Vitiate, consumed worlds and "
            "ruled from Dromund Kaas with near-immortal malice.\n\n"
            "Though the ancient Sith Empire eventually fractured, its legacy survived in holocrons, "
            "buried superweapons, and the secret ambition of Darths Bane, Sidious, and their successors "
            "— proof that Sith victory could be patient as well as violent."
        ),
        "significance": (
            "The Sith Empire is the deep history behind every 'Imperial' title in the saga. It explains "
            "Korriban's sacred status, why the Jedi feared attachment to power, and how dark-side "
            "governments differ from mere dictatorships — they sanctify cruelty as theology.\n\n"
            "Knights of the Old Republic and The Old Republic MMO eras draw heavily on this legacy."
        ),
        "notableEvents": [
            "Exiled Dark Jedi found the Sith on Korriban",
            "Great Hyperspace War against the Republic",
            "Exar Kun's Sith rebellion",
            "Revan and Malak's Sith Empire",
            "Vitiate's Eternal Empire from Dromund Kaas",
            "Repeated Jedi–Sith galactic wars",
            "Collapse and retreat into hidden traditions ( Rule of Two )",
        ],
        "affiliations": [
            "Sith Emperor and Dark Council",
            "Sith military and Imperial Guard",
            "Sith acolytes and Inquisitors ( ancient orders )",
            "Korriban Sith Academy",
            "Dromund Kaas power structure",
        ],
        "timeline": [
            {"era": "~6,900 BBY", "event": "Sith Empire forms on Korriban"},
            {"era": "Great Hyperspace War", "event": "Sith invasion of Republic space"},
            {"era": "Old Sith Wars", "event": "Revan, Malak, and Exar Kun eras"},
            {"era": "Vitiate's reign", "event": "Immortal Emperor rules from Dromund Kaas"},
            {"era": "Post–3,641 BBY", "event": "Empire fractures; Rule of Two begins"},
        ],
    },
    "first-order": {
        "overview": (
            "The First Order rose from Imperial ashes in the Unknown Regions — a militarized junta "
            "obsessed with superweapons, human uniformity, and the fantasy of restoring Palpatine's "
            "galaxy. Led by Supreme Leader Snoke and later Kylo Ren, it struck from secret bases "
            "with Starkiller Base and Resurgent-class dreadnoughts, shattering the New Republic "
            "before the Resistance could fully mobilize."
        ),
        "history": (
            "Imperial remnants fleeing the Battle of Jakku regrouped beyond the galactic frontier with "
            "secret funding and advisors who preserved Palpatine's doctrine. The First Order rebuilt "
            "stormtrooper legions from kidnapped children, purged weakness from its ranks, and hid "
            "its true strength while the New Republic debated disarmament.\n\n"
            "Snoke's leadership masked deeper Sith designs. General Hux's military ambition and "
            "Kylo Ren's volatile dark-side power competed for influence even as the Order prepared "
            "Starkiller Base — a planet-killer drawing energy from a star.\n\n"
            "The Hosnian cataclysm decapitated the New Republic Senate in an instant. Though the "
            "Resistance destroyed Starkiller Base and eventually Snoke fell, the First Order's "
            "fleets remained vast — culminating in the siege of Crait and the final rise of "
            "Palpatine's hidden Sith fleet on Exegol."
        ),
        "significance": (
            "The First Order proves that fascism adapts: younger uniforms, cultish loyalty, and "
            "terrorism against a demilitarized democracy too confident in its victory.\n\n"
            "Its stormtrooper program and hyperspace tracking technology represent evolution of "
            "Imperial methods — the same fear in a new generation."
        ),
        "notableEvents": [
            "Imperial exodus to the Unknown Regions after Jakku",
            "Supreme Leader Snoke consolidates the First Order",
            "Starkiller Base constructed and activated",
            "Destruction of the Hosnian system ( 34 ABY )",
            "Battle of Starkiller Base — superweapon destroyed",
            "Snoke assassinated aboard the Supremacy",
            "Siege of Crait and Resistance evacuation",
            "Final Order fleet revealed at Exegol",
        ],
        "affiliations": [
            "First Order High Command",
            "Stormtrooper Corps ( conscripted cadets )",
            "First Order Navy",
            "Knights of Ren",
            "Sith Eternal ( hidden alliance )",
            "Imperial Remnant ideologues",
        ],
        "timeline": [
            {"era": "Post-Jakku", "event": "Remnants reorganize in the Unknown Regions"},
            {"era": "Decades of secrecy", "event": "First Order builds fleets and Starkiller Base"},
            {"era": "34 ABY", "event": "Hosnian system destroyed; open war begins"},
            {"era": "34–35 ABY", "event": "Conflict with the Resistance escalates"},
            {"era": "35 ABY", "event": "Exegol fleet defeated; Order collapses"},
        ],
    },
    "resistance": {
        "overview": (
            "The Resistance was a private militia founded by Leia Organa when the New Republic "
            "refused to take the First Order seriously. Officially deniable but secretly supported "
            "by sympathetic senators and veterans, it operated from hidden bases like D'Qar and "
            "Crait — outnumbered, under-funded, and yet stubborn enough to locate Starkiller Base "
            "and keep hope alive after Hosnian Prime burned."
        ),
        "history": (
            "Leia's warnings about Imperial remnants in the Unknown Regions were politically "
            "unpopular. Stripped of formal rank, she rebuilt an network of pilots, spies, and "
            "soldiers who answered to conscience rather than Senate appropriations.\n\n"
            "Poe Dameron's Black Squadron, Finn's defection from the First Order, and Rey's "
            "emergence as a Force-sensitive hero gave the Resistance unexpected leverage. They "
            "destroyed Starkiller Base but paid dearly — bases lost, fleets scattered, and Leia "
            "left leading a remnant after the Supremacy's assault.\n\n"
            "At Crait, the Resistance narrowly escaped total annihilation. Rebuilding under "
            "Leia's guidance, they eventually united with the galaxy's citizens fleet to defeat "
            "Palpatine's Sith armada at Exegol — proving the Rebellion's spirit survived in a "
            "new generation."
        ),
        "significance": (
            "The Resistance shows what happens when democracies ignore fascism until it is almost "
            "too late — and how veterans and volunteers must fill the gap.\n\n"
            "Its orange insignia and cobbled-together fleet echo the Rebel Alliance while "
            "highlighting harsher odds: no governing Senate, no safe harbor, no assumption of victory."
        ),
        "notableEvents": [
            "Leia Organa forms the Resistance amid Senate denial",
            "Starkiller Base intelligence mission and destruction",
            "Evacuation of D'Qar under First Order bombardment",
            "Mutiny aboard the Raddus during hyperspace pursuit",
            "Holdo's sacrifice at hyperspace ramming speed",
            "Siege of Crait — Luke Skywalker's stand buys escape",
            "Citizens' fleet victory at Exegol",
        ],
        "affiliations": [
            "Resistance High Command ( General Organa )",
            "Resistance Starfighter Corps",
            "Resistance ground and naval units",
            "Sympathetic New Republic senators ( covert )",
            "Jedi legacy ( Luke, Rey )",
        ],
        "timeline": [
            {"era": "Post-Concordance", "event": "Leia organizes vigilance against First Order"},
            {"era": "34 ABY", "event": "Open conflict after Hosnian destruction"},
            {"era": "34 ABY", "event": "Starkiller Base destroyed; fleet hunted"},
            {"era": "34 ABY", "event": "Crait evacuation preserves core leadership"},
            {"era": "35 ABY", "event": "Galaxy-wide uprising at Exegol"},
        ],
    },
    "mandalorians": {
        "overview": (
            "The Mandalorians are a warrior culture defined by beskar armor, clan loyalty, and a "
            "complicated history with both Jedi and Sith. From the ancient Mandalorian Crusades "
            "to the pacifist New Mandalorian era, the Darksaber, and Bo-Katan's struggle to "
            "reclaim Mandalore, they have repeatedly reshaped galactic wars — sometimes as "
            "conquerors, sometimes as protectors, always as legends."
        ),
        "history": (
            "Mandalore's people forged an empire of conquest long before the Republic reached "
            "the Outer Rim. Their war with the Jedi scarred both cultures — Mandalorian iron "
            "against Force wielders — until internal division and outside intervention repeatedly "
            "fractured their homeworld.\n\n"
            "Duchess Satine Kryze's pacifist government clashed with Death Watch and Maul's "
            "Shadow Collective during the Clone Wars. The Empire later occupied Mandalore and "
            "the Great Purge of the Night of a Thousand Tears scattered survivors across the "
            "galaxy — including hidden enclaves like the Tribe on Nevarro.\n\n"
            "Din Djarin and Bo-Katan Kryze reignited the quest to retake Mandalore, confronting "
            "Imperial Remnants, the Darksaber's claim, and what it means to rule a people "
            "defined by the Creed. Mandalorian identity endures in covert foundlings and "
            "open warfare alike."
        ),
        "significance": (
            "Mandalorians bridge military history and cultural identity in Star Wars — neither "
            "a conventional state nor a simple mercenary guild.\n\n"
            "Beskar, the Darksaber, and the Creed influence bounty hunting, fleet tactics, and "
            "even Imperial anti-Jedi planning. Their story is essential to understanding "
            "Mandalore's place in galactic politics."
        ),
        "notableEvents": [
            "Mandalorian-Jedi war in ancient eras",
            "Mandalore crusades across the galaxy",
            "Death Watch challenges pacifist Mandalore",
            "Maul briefly rules Mandalore via Shadow Collective",
            "Imperial occupation and the Great Purge",
            "Din Djarin and Grogu's journeys with the Tribe",
            "Reclamation of Mandalore from Imperial Remnants",
        ],
        "affiliations": [
            "Mandalorian clans and Great Forge",
            "Death Watch ( historical )",
            "House Kryze and House Vizsla",
            "Children of the Watch",
            "Mandalorian Protectors ( historical )",
            "Bounty Hunters' Guild ( individual members )",
        ],
        "timeline": [
            {"era": "Ancient Era", "event": "Mandalorian crusades against Jedi and Rim worlds"},
            {"era": "Clone Wars", "event": "Civil war between New Mandalorians and Death Watch"},
            {"era": "Imperial Era", "event": "Occupation and Great Purge scatter clans"},
            {"era": "New Republic Era", "event": "Covert tribes preserve the Creed in hiding"},
            {"era": "9 ABY onward", "event": "Quest to retake and rebuild Mandalore"},
        ],
    },
    "trade-federation": {
        "overview": (
            "The Trade Federation was a megacorporation with its own droid security forces, "
            "Neimoidian leadership, and Lucrehulk battleships — a state within the state. "
            "Its blockade and invasion of Naboo exposed how corporate power could paralyze "
            "the Republic, while its alliance with the Separatists made it one of the Clone "
            "Wars' primary arms suppliers."
        ),
        "history": (
            "Born from legitimate commerce, the Federation amassed lobbying power in the Senate "
            "and private armies to protect 'trade interests.' Viceroy Nute Gunray's blockade of "
            "Naboo — secretly encouraged by Darth Sidious — was the opening move in Palpatine's "
            "decades-long plan.\n\n"
            "Despite defeat at Naboo, the Federation persisted, merging into the Separatist "
            "alliance and deploying battle droids by the billions. Its battleships and C-9979 "
            "landing craft became symbols of corporate warfare: profit-driven invasions dressed "
            "as policy disputes.\n\n"
            "When the Clone Wars ended, Federation leadership joined other Separatist executives "
            "on Mustafar — eliminated by Darth Vader as Sidious consolidated power under the "
            "Empire, which tolerated corporations only as subordinates."
        ),
        "significance": (
            "The Trade Federation illustrates how deregulated corporate militaries hollow out "
            "democracy — a theme that runs from the prequel trilogy through Andor's corporate "
            "occupations.\n\n"
            "Its battle droid legions foreshadowed the Separatist war machine and proved that "
            "economic power could rival planetary governments in firepower."
        ),
        "notableEvents": [
            "Senate grants trade route taxation disputes",
            "Blockade and invasion of Naboo ( 32 BBY )",
            "Battle droid armies deployed against Gungan and Naboo forces",
            "Alliance with Count Dooku and the Separatists",
            "Geonosis droid foundries supply the Clone Wars",
            "Executions on Mustafar end Federation leadership ( 19 BBY )",
        ],
        "affiliations": [
            "Neimoidian Trade Federation Directorate",
            "Trade Defense Force ( droid army )",
            "Separatist Alliance ( wartime )",
            "InterGalactic Banking Clan ( financial ties )",
            "Senate lobbying bloc ( Rim and corporate interests )",
        ],
        "timeline": [
            {"era": "Late Republic", "event": "Federation gains military droid contracts"},
            {"era": "32 BBY", "event": "Naboo blockade and invasion"},
            {"era": "Separatist Crisis", "event": "Federation joins Dooku's alliance"},
            {"era": "Clone Wars", "event": "Mass droid production fuels galactic war"},
            {"era": "19 BBY", "event": "Leadership eliminated; assets absorbed by Empire"},
        ],
    },
}
