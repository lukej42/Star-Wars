#!/usr/bin/env python3
"""Curated rich profile content for Organisations & Syndicates pages."""

from __future__ import annotations

# Shared media lists
CLONE_WARS_FILMS = [
    "Star Wars: Episode II — Attack of the Clones",
    "Star Wars: Episode III — Revenge of the Sith",
]
ORIGINAL_TRILOGY = [
    "Star Wars: Episode IV — A New Hope",
    "Star Wars: Episode V — The Empire Strikes Back",
    "Star Wars: Episode VI — Return of the Jedi",
]
CLONE_WARS_SERIES = [
    "Star Wars: The Clone Wars",
    "Star Wars: The Bad Batch",
]
UNDERWORLD_SERIES = [
    "Star Wars: The Clone Wars",
    "Star Wars: The Mandalorian",
    "Star Wars: The Book of Boba Fett",
]


def char(name: str, route: str) -> dict:
    return {"label": "Character", "value": name, "route": route}


def jedi(name: str, route: str) -> dict:
    return {"label": "Jedi", "value": name, "route": route}


def sith(name: str, route: str) -> dict:
    return {"label": "Sith", "value": name, "route": route}


def bh(name: str, route: str) -> dict:
    return {"label": "Bounty Hunter", "value": name, "route": route}


def planet(name: str, route: str) -> dict:
    return {"label": "Planet", "value": name, "route": route}


def faction(name: str, route: str) -> dict:
    return {"label": "Faction", "value": name, "route": route}


def org(name: str, route: str) -> dict:
    return {"label": "Organization", "value": name, "route": route}


def head(value: str, route: str = "") -> dict:
    return {"value": value, "route": route}


ORG_PROFILES: dict[str, dict] = {
    "techno-union": {
        "dateRange": "c. 300 BBY – 19 BBY",
        "headOfState": head("Wat Tambor"),
        "headOfGovernment": head("Techno Union Foreman Council"),
        "planets": [
            planet("Skako", "planet/skako"),
            planet("Foundry worlds of the Outer Rim", "planet/geonosis"),
            planet("Muunilinst", "planet/muunilinst"),
        ],
        "overview": (
            "The Techno Union is a Skakoan-led manufacturing combine whose foundries, droid assembly lines, "
            "and research contracts made it one of the Confederacy of Independent Systems' most indispensable "
            "corporate backers. Publicly a trade guild with Senate representation, the Union privately "
            "equipped Separatist armies with battle droids, heavy walkers, and orbital construction platforms "
            "while its Foreman, Wat Tambor, treated entire worlds as company property.\n\n"
            "Union facilities on worlds such as Geonosis and Xagobah became symbols of industrialized warfare "
            "during the Clone Wars. Republic intelligence repeatedly flagged Techno Union vaults on Skako Minor "
            "and Muunilinst as dual-use sites where civilian production lines could be retooled for military "
            "output within days. When the war ended, the Union's assets were seized or dissolved — yet its "
            "design patents and droid schematics continued to circulate through black markets for generations."
        ),
        "history": (
            "The Techno Union rose from Skako's pressure-domed cities, where Skakoan engineers perfected "
            "atmospheric containment and precision metallurgy long before the Republic standardized "
            "hyperspace trade lanes. By the late Republic era the Union held Senate seats, lobbied tariff "
            "codes, and operated foundry networks that supplied both civilian infrastructure and covert "
            "military prototypes.\n\n"
            "When [Count Dooku](sith/darth-tyranus) assembled the Separatist bloc, Wat Tambor pledged Techno Union "
            "factories to the cause. Foundries on Geonosis produced B1 battle droids at scale, while Union "
            "research divisions field-tested tri-droids, crab droids, and experimental orbital weapons. "
            "[General Grievous](characters/general-grievous) often coordinated strikes to protect Union "
            "shipments, treating corporate logistics as strategic military assets.\n\n"
            "Republic offensives targeted Union holdings across the Outer Rim. Jedi-led assaults on "
            "Xagobah and Skako Minor attempted to capture Tambor and disrupt droid production, while "
            "Muunilinst became a financial and industrial hub linked to Techno Union subsidiaries. "
            "[Anakin Skywalker](jedi/anakin-skywalker) and [Obi-Wan Kenobi](jedi/obi-wan-kenobi) "
            "fought Separatist forces on multiple worlds where Union emblems marked factory perimeters.\n\n"
            "After [Darth Sidious](sith/darth-sidious) issued Order 66 and the Separatist leadership was "
            "eliminated, Techno Union charters were voided and its leaders became fugitives or casualties. "
            "Imperial records absorbed Union patents into state conglomerates, erasing Skakoan sovereignty "
            "in official histories while scavenger markets still traded Union stamp codes on salvaged droid "
            "frames."
        ),
        "significance": (
            "The Techno Union exemplifies how megacorporations can wage war without flying their own "
            "national banners — supplying armies, lobbying senates, and treating populations as labor "
            "pools. Its Clone Wars role foreshadowed later Imperial state-corporate fusion.\n\n"
            "For historians, Tambor's Union demonstrates the vulnerability of democratic institutions "
            "when industrial combines hold veto power over rearmament votes and trade sanctions."
        ),
        "notableEvents": [
            "Techno Union granted Republic Senate representation while expanding private armies",
            "Wat Tambor signs Separatist accords with Count Dooku",
            "Geonosis foundries mass-produce battle droids for the Confederacy",
            "Republic raids on Xagobah target Tambor's production vaults",
            "Skako Minor facilities resist Jedi assault teams",
            "Muunilinst financial ties deepen Union–IGBC cooperation",
            "Corporate dissolution after Separatist defeat at war's end",
            "Imperial absorption of Union patents and foundry leases",
        ],
        "majorCharacters": [
            char("General Grievous", "characters/general-grievous"),
            jedi("Anakin Skywalker", "jedi/anakin-skywalker"),
            jedi("Obi-Wan Kenobi", "jedi/obi-wan-kenobi"),
            sith("Darth Tyranus", "sith/darth-tyranus"),
        ],
        "keyFactions": [faction("Confederacy of Independent Systems", "factions/confederacy")],
        "affiliations": [
            "Confederacy of Independent Systems",
            "Skakoan industrial guilds",
            "Geonosis droid foundries",
            "Separatist Droid Army suppliers",
        ],
        "timeline": [
            {"era": "Old Republic", "event": "Techno Union chartered as galactic manufacturing combine"},
            {"era": "Separatist Crisis", "event": "Wat Tambor aligns Union assets with Count Dooku"},
            {"era": "Clone Wars", "event": "Mass battle droid production accelerates on Geonosis"},
            {"era": "Clone Wars", "event": "Republic targets Skako Minor and Xagobah facilities"},
            {"era": "Imperial Era", "event": "Union dissolved; patents absorbed by Imperial industry"},
        ],
        "films": CLONE_WARS_FILMS,
        "series": CLONE_WARS_SERIES,
    },
    "intergalactic-banking-clan": {
        "dateRange": "c. 25,000 BBY – present (reorganized)",
        "headOfState": head("San Hill"),
        "headOfGovernment": head("IGBC Executive Board"),
        "planets": [
            planet("Muunilinst", "planet/muunilinst"),
            planet("Mygeeto", "planet/mygeeto"),
        ],
        "overview": (
            "The InterGalactic Banking Clan (IGBC) is a Muun-dominated financial institution whose vault "
            "networks, currency reserves, and war-bond markets have funded republics, empires, and "
            "corporate armies alike. During the Clone Wars the IGBC underwrote Separatist payrolls while "
            "maintaining enough Republic-facing legitimacy to keep Muunilinst's skylines glittering with "
            "neutral-banker rhetoric.\n\n"
            "Hego Damask holdings and IGBC subsidiary charters linked the Clan to Sith long-game planning "
            "as well as open Separatist finance. When the war ended, the Clan's structures were reorganized "
            "under Imperial oversight — yet Muun financiers continued to shape Rim debt markets from "
            "shadow boards."
        ),
        "history": (
            "Muunilinst's banking towers predated the modern Republic, and the IGBC grew by offering "
            "hyperspace-clearing services to worlds the Senate could not afford to bail out. The Clan's "
            "executives perfected the art of lending to both sides: Separatist droid foundries and "
            "Republic reconstruction bonds could both appear on the same quarterly ledger through "
            "shell holdings.\n\n"
            "[San Hill](characters/nute-gunray) is often cited alongside Muun leadership in Separatist "
            "councils, but the IGBC's true influence was structural — without Clan credit, [General Grievous](characters/general-grievous) "
            "could not pay fleet crews and [Nute Gunray](characters/nute-gunray)'s Trade Federation "
            "blockades could not sustain prolonged sieges. [Rush Clovis](characters/rush-clovis) later "
            "infiltrated IGBC circles on Scipio, exposing how deeply banking clans penetrated the "
            "Republic's own treasury apparatus.\n\n"
            "The Battle of Muunilinst became a signature Republic victory partly because seizing IGBC "
            "vaults struck at Separatist liquidity itself. [Obi-Wan Kenobi](jedi/obi-wan-kenobi) and "
            "clone commanders fought through Muun cityscapes where credit terminals outnumbered civilian "
            "markets. Mygeeto's crystal trenches — financed by IGBC mining loans — saw heavy Jedi combat "
            "late in the war.\n\n"
            "Imperial consolidation merged IGBC assets into state banks, but Muun financiers persisted "
            "as advisors to governors and syndicate treasurers. Crimson Dawn, Pyke spice routes, and "
            "Rebel procurement all eventually touched IGBC legacy routing codes."
        ),
        "significance": (
            "The IGBC proves that galactic wars are often decided in vaults before they are decided on "
            "battlefields. Its Clone Wars duplicity remains a case study in corporate neutrality as "
            "operational camouflage.\n\n"
            "Muunilinst's survival as a financial capital across eras shows how money outlasts whichever "
            "flag flies over the Senate dome."
        ),
        "notableEvents": [
            "IGBC funds Republic infrastructure and Rim development loans",
            "San Hill joins Separatist Council while maintaining banking charters",
            "War bonds underwrite Separatist droid army payrolls",
            "Rush Clovis exposes IGBC–Senate corruption on Scipio",
            "Battle of Muunilinst targets Clan vault networks",
            "Mygeeto crystal operations financed by IGBC mining credit",
            "Imperial reorganization of IGBC holdings after war's end",
        ],
        "majorCharacters": [
            char("Nute Gunray", "characters/nute-gunray"),
            char("Rush Clovis", "characters/rush-clovis"),
            char("General Grievous", "characters/general-grievous"),
            jedi("Obi-Wan Kenobi", "jedi/obi-wan-kenobi"),
        ],
        "keyFactions": [
            faction("Confederacy of Independent Systems", "factions/confederacy"),
            faction("Trade Federation", "factions/trade-federation"),
        ],
        "affiliations": [
            "Confederacy of Independent Systems",
            "Muun financial houses",
            "Hego Damask holdings (historical)",
            "Separatist treasury proxies",
        ],
        "timeline": [
            {"era": "Old Republic", "event": "IGBC becomes dominant galactic clearing house"},
            {"era": "Separatist Crisis", "event": "Clan executives fund secessionist militias"},
            {"era": "Clone Wars", "event": "Battle of Muunilinst threatens Separatist liquidity"},
            {"era": "Clone Wars", "event": "Scipio scandal exposes dual-faction lending"},
            {"era": "Imperial Era", "event": "IGBC reorganized under Imperial treasury oversight"},
        ],
        "films": CLONE_WARS_FILMS,
        "series": CLONE_WARS_SERIES,
    },
    "commerce-guild": {
        "dateRange": "c. 700 BBY – 19 BBY",
        "headOfState": head("Shu Mai"),
        "headOfGovernment": head("Commerce Guild Presidium"),
        "planets": [
            planet("Castell", "planet/castell"),
            planet("Felucia", "planet/felucia"),
        ],
        "overview": (
            "The Commerce Guild is a Gossam-dominated trade association whose private security flotillas, "
            "procurement monopolies, and customs-enforcement contracts made it a pillar of Separatist "
            "economic warfare. Based on Castell, the Guild presented itself as a neutral trade facilitator "
            "while its Presidente, Shu Mai, signed droid allocation treaties that fed Count Dooku's armies.\n\n"
            "Guild escort frigates guarded convoys carrying raw materials from Felucia and other "
            "agricultural worlds, blurring the line between corporate security and full naval combat "
            "during the Clone Wars."
        ),
        "history": (
            "Castell's Gossam merchants built the Commerce Guild to negotiate tariff exemptions the "
            "Republic Senate would never grant individual worlds. Guild security forces began as "
            "anti-piracy escorts and evolved into private armies with jurisdiction clauses on "
            "dozens of Rim trade routes.\n\n"
            "When [Darth Tyranus](sith/darth-tyranus) opened Separatist negotiations, Shu Mai pledged "
            "Guild convoy protection to CIS fleets and allowed battle droid garrisons aboard Guild "
            "stations. [Padmé Amidala](characters/padme-amidala) repeatedly challenged Guild "
            "monopolies in Senate hearings, arguing that corporate militias eroded planetary sovereignty.\n\n"
            "Felucia became a contested Guild supply world where Jedi and clone troopers fought Separatist "
            "and corporate forces among fungal jungles and nysillin farms. [Ahsoka Tano](jedi/ahsoka-tano) "
            "and [Anakin Skywalker](jedi/anakin-skywalker) led campaigns to break Guild-backed blockades "
            "that starved civilian populations while stockpiling war materiel.\n\n"
            "After the Separatist collapse, Commerce Guild charters were revoked and Castell's fleets "
            "were disarmed under Imperial supervision. Gossam traders persisted as intermediaries in "
            "Hutt and Pyke markets, carrying institutional memory of Guild routing tables."
        ),
        "significance": (
            "The Commerce Guild demonstrates how 'trade facilitation' can mask resource extraction and "
            "siege economics. Its Felucia campaigns link corporate power directly to environmental "
            "devastation and farmer displacement.\n\n"
            "Guild history informs modern debates over private military companies operating under "
            "commercial law instead of military accountability."
        ),
        "notableEvents": [
            "Commerce Guild secures Castell as extraterritorial trade capital",
            "Shu Mai joins Separatist Council on Geonosis",
            "Guild escorts merge with CIS convoy doctrine",
            "Felucia supply lines contested by Republic forces",
            "Senate hearings expose Guild monopoly abuses",
            "Post-war disarmament of Guild security flotillas",
        ],
        "majorCharacters": [
            char("Padmé Amidala", "characters/padme-amidala"),
            jedi("Ahsoka Tano", "jedi/ahsoka-tano"),
            jedi("Anakin Skywalker", "jedi/anakin-skywalker"),
            sith("Darth Tyranus", "sith/darth-tyranus"),
        ],
        "keyFactions": [faction("Confederacy of Independent Systems", "factions/confederacy")],
        "affiliations": [
            "Confederacy of Independent Systems",
            "Gossam trade houses of Castell",
            "Felucia agricultural contractors",
        ],
        "timeline": [
            {"era": "Old Republic", "event": "Commerce Guild chartered on Castell"},
            {"era": "Separatist Crisis", "event": "Shu Mai aligns Guild fleets with Dooku"},
            {"era": "Clone Wars", "event": "Felucia campaigns disrupt Guild supply chains"},
            {"era": "Imperial Era", "event": "Guild militias disbanded; trade routes nationalized"},
        ],
        "films": CLONE_WARS_FILMS,
        "series": CLONE_WARS_SERIES,
    },
    "corporate-alliance": {
        "dateRange": "c. 500 BBY – 19 BBY",
        "headOfState": head("Passel Argente"),
        "headOfGovernment": head("Corporate Alliance Magistrate Council"),
        "planets": [
            planet("Coruscant", "coruscant"),
            planet("Geonosis", "planet/geonosis"),
        ],
        "overview": (
            "The Corporate Alliance is Passel Argente's corporate militia conglomerate — a holding structure "
            "for NR-N99 Persuader tanks, droid enforcers, and planetary security contracts that backed "
            "Separatist ground campaigns across the Mid and Outer Rim. Argente sat on the Separatist "
            "Council as Magistrate, translating board votes directly into battlefield deployments.\n\n"
            "Alliance logos marked occupation forces on worlds where 'corporate stabilization' replaced "
            "Republic governance, making the Alliance one of the most visible faces of Separatist "
            "territorial control."
        ),
        "history": (
            "Passel Argente built the Corporate Alliance by acquiring distressed planetary militias and "
            "rebranding them as security subsidiaries. Persuader tanks — nicknamed 'Corporate Alliance "
            "tanks' on HoloNet feeds — became symbols of Separatist mechanized assault.\n\n"
            "On Geonosis, Alliance units fought alongside Techno Union droids during the war's opening "
            "battle. [Mace Windu](jedi/mace-windu) and the Jedi assault team encountered Alliance "
            "hardware in the arena staging yards before clone reinforcements arrived.\n\n"
            "[Count Dooku](sith/darth-tyranus) relied on Argente to hold provisional governments on "
            "captured worlds, installing corporate magistrates who answered to Serenno and Castell "
            "before they answered to local populations. [Padmé Amidala](characters/padme-amidala) "
            "documented Alliance atrocities in Senate petitions that rarely reached quorum.\n\n"
            "When Separatist command collapsed, Alliance subsidiaries were dismantled and Argente "
            "died with the Council on Mustafar. Persuader chassis remained in pirate service for decades."
        ),
        "significance": (
            "The Corporate Alliance shows how privatized occupation forces can implement regime change "
            "without formal invasion declarations. Its tank legions link boardroom votes to civilian "
            "displacement in a single supply chain.\n\n"
            "Alliance records remain primary sources for understanding Separatist ground doctrine "
            "outside droid-centric stereotypes."
        ),
        "notableEvents": [
            "Passel Argente consolidates planetary militias under Alliance charter",
            "NR-N99 Persuader tanks debut on Geonosis",
            "Alliance magistrates installed on occupied Rim worlds",
            "Corporate security forces merge with CIS army command",
            "Mustafar Council massacre ends Alliance leadership",
        ],
        "majorCharacters": [
            char("Padmé Amidala", "characters/padme-amidala"),
            jedi("Mace Windu", "jedi/mace-windu"),
            sith("Darth Tyranus", "sith/darth-tyranus"),
        ],
        "keyFactions": [faction("Confederacy of Independent Systems", "factions/confederacy")],
        "affiliations": [
            "Confederacy of Independent Systems",
            "Corporate magistrate networks",
            "Persuader tank registries",
        ],
        "timeline": [
            {"era": "Old Republic", "event": "Corporate Alliance forms from acquired militias"},
            {"era": "Clone Wars", "event": "Persuader tanks deployed on Geonosis"},
            {"era": "Clone Wars", "event": "Alliance magistrates govern occupied territories"},
            {"era": "Imperial Era", "event": "Alliance dissolved after Separatist defeat"},
        ],
        "films": CLONE_WARS_FILMS,
        "series": CLONE_WARS_SERIES,
    },
    "retail-caucus": {
        "dateRange": "c. 200 BBY – 19 BBY",
        "headOfState": head("Po Nudo"),
        "headOfGovernment": head("Retail Caucus Logistics Directorate"),
        "planets": [
            planet("Ando", "planet/ando"),
            planet("Coruscant", "coruscant"),
        ],
        "overview": (
            "The Retail Caucus is a consumer-goods megacorp bloc whose logistics hubs, warehousing monopolies, "
            "and shipping manifests quietly sustained Separatist supply lines throughout the Clone Wars. "
            "Led by Aqualish executive Po Nudo, the Caucus translated retail dominance into wartime "
            "quartermaster power — moving rations, spare parts, and droid components under civilian "
            "packaging codes.\n\n"
            "Republic analysts often underestimated the Caucus because its HoloNet presence focused on "
            "marketplaces rather than battlefields, yet front-line Separatist armies depended on "
            "Caucus routing tables to keep foundries fed."
        ),
        "history": (
            "Retail Caucus members built fortunes by controlling last-mile distribution on congested "
            "Core trade lanes, then leveraged that leverage to extract manufacturing concessions from "
            "supplier worlds. Po Nudo's Aqualish syndicate ties linked the Caucus to broader Rim "
            "networks beyond polite corporate branding.\n\n"
            "When Po Nudo joined the Separatist Council, Caucus freighters gained CIS naval escorts "
            "while maintaining Republic retail licenses on paper. [Senator Onaconda Farr](characters/onaconda-farr) "
            "and [Padmé Amidala](characters/padme-amidala) investigated supply shortages that traced "
            "back to Caucus hoarding on Rodia and nearby sectors.\n\n"
            "[General Grievous](characters/general-grievous) coordinated with Caucus quartermasters to "
            "prioritize droid foundry deliveries over civilian relief — a strategy that starved "
            "loyalist worlds while keeping Separatist factories at capacity. Jedi raids on Caucus "
            "warehouses rarely made headlines but materially shortened siege timelines.\n\n"
            "Imperial post-war audits seized Caucus manifests as evidence of systemic profiteering, "
            "yet many subsidiary brands survived under new corporate shells."
        ),
        "significance": (
            "The Retail Caucus illustrates how logistics monopolies can wage war by allocation rather "
            "than artillery. Its story complements better-known Separatist militaries with a "
            "supply-chain perspective historians now treat as decisive.\n\n"
            "Caucus archives inform modern sanctions doctrine against dual-use consumer shipping."
        ),
        "notableEvents": [
            "Retail Caucus monopolizes Core–Rim consumer distribution lanes",
            "Po Nudo joins Separatist Council",
            "Caucus warehouses implicated in Rim relief hoarding",
            "Jedi strike teams target Caucus quartermaster hubs",
            "Imperial seizure of Caucus subsidiary brands",
        ],
        "majorCharacters": [
            char("Onaconda Farr", "characters/onaconda-farr"),
            char("Padmé Amidala", "characters/padme-amidala"),
            char("General Grievous", "characters/general-grievous"),
        ],
        "keyFactions": [faction("Confederacy of Independent Systems", "factions/confederacy")],
        "affiliations": [
            "Confederacy of Independent Systems",
            "Aqualish trade networks",
            "Core retail distribution monopolies",
        ],
        "timeline": [
            {"era": "Old Republic", "event": "Retail Caucus consolidates consumer logistics"},
            {"era": "Clone Wars", "event": "Po Nudo pledges Caucus supply chains to CIS"},
            {"era": "Clone Wars", "event": "Rodia shortages expose hoarding operations"},
            {"era": "Imperial Era", "event": "Caucus assets absorbed into Imperial procurement"},
        ],
        "films": CLONE_WARS_FILMS,
        "series": CLONE_WARS_SERIES,
    },
    "pyke-syndicate": {
        "dateRange": "Ancient era – present",
        "headOfState": head("Pyke capo families of Oba Diah"),
        "headOfGovernment": head("Pyke Syndicate Council"),
        "planets": [
            planet("Oba Diah", "planet/oba-diah"),
            planet("Kessel", "planet/kessel"),
            planet("Tatooine", "tatooine"),
        ],
        "overview": (
            "The Pyke Syndicate is a spice cartel native to Oba Diah whose refineries, assassin cadres, and "
            "slave-labor contracts dominated the Kessel Run for centuries. Pyke capos treat glitterstim "
            "and raw spice as sovereign currency, negotiating with empires, hutts, and smuggler guilds "
            "while enforcing territory through masked enforcers and orbital blockades.\n\n"
            "During the Clone Wars and Imperial eras the Syndicate became indispensable to shadow "
            "economies — supplying cartels like Crimson Dawn, hiring hunters such as [Cad Bane](bounty-hunters/cad-bane), "
            "and maintaining refineries that Republic law never successfully shut down."
        ),
        "history": (
            "Pyke evolution on Oba Diah favored hierarchical capo structures and chemical processing "
            "guilds that could refine spice faster than competitors could steal shipments. The Syndicate "
            "expanded along the Kessel slave routes, partnering with labor brokers who treated prisoners "
            "as disposable refinery crews.\n\n"
            "Jedi investigations into Sifo-Dyas's missing shuttle eventually led [Obi-Wan Kenobi](jedi/obi-wan-kenobi) "
            "and [Anakin Skywalker](jedi/anakin-skywalker) to Oba Diah, exposing Pyke cooperation with "
            "[Count Dooku](sith/darth-tyranus) and [Darth Sidious](sith/darth-sidious). The Syndicate's "
            "willingness to sell Sith secrets for profit revealed how criminal networks could destabilize "
            "the Republic from beneath tariff law.\n\n"
            "Under the Empire, Pyke operations persisted through bribed Moff offices and Hutt buffer "
            "zones. [Han Solo](characters/han-solo) and [Chewbacca](characters/chewbacca) famously "
            "escaped Kessel aboard the Millennium Falcon — a heist that humiliated Pyke labor contractors "
            "and inspired spice-runner guild legends.\n\n"
            "The New Republic era saw Pyke syndicates negotiate with [Maul](sith/darth-maul)-aligned "
            "Crimson Dawn splinters and later with Imperial remnants. [Cad Bane](bounty-hunters/cad-bane) "
            "often operated on Pyke retainers, extracting debts from clients who defaulted on spice loans."
        ),
        "significance": (
            "The Pyke Syndicate anchors Star Wars underworld economics — connecting slavery, spice, and "
            "political corruption in one supply chain. Oba Diah's refineries demonstrate how Outer Rim "
            "crime can influence Core wars when Jedi secrets and clone troopers are on the ledger.\n\n"
            "Pyke iconography — masked enforcers, obsidian spires — remains synonymous with spice "
            "violence across films, series, and games."
        ),
        "notableEvents": [
            "Pyke capos establish Oba Diah as spice refining capital",
            "Kessel slave-labor routes chartered under Pyke contracts",
            "Sifo-Dyas shuttle cover-up implicates Pyke leadership",
            "Obi-Wan and Anakin raid Oba Diah Syndicate vaults",
            "Han Solo's Kessel Run undermines Pyke smuggling prestige",
            "Pyke–Crimson Dawn cooperation during Imperial collapse",
            "Cad Bane executes Pyke retainer contracts across the Rim",
        ],
        "majorCharacters": [
            bh("Cad Bane", "bounty-hunters/cad-bane"),
            char("Han Solo", "characters/han-solo"),
            char("Chewbacca", "characters/chewbacca"),
            jedi("Obi-Wan Kenobi", "jedi/obi-wan-kenobi"),
            jedi("Anakin Skywalker", "jedi/anakin-skywalker"),
            sith("Darth Tyranus", "sith/darth-tyranus"),
        ],
        "keyFactions": [faction("Hutts", "factions/hutts")],
        "affiliations": [
            "Spice refining cartels",
            "Kessel labor contractors",
            "Bounty hunter retainer networks",
            "Shadow ports of the Outer Rim",
        ],
        "timeline": [
            {"era": "Ancient Era", "event": "Pyke capo dynasties consolidate Oba Diah"},
            {"era": "Clone Wars", "event": "Syndicate implicated in Sifo-Dyas conspiracy"},
            {"era": "Imperial Era", "event": "Kessel operations expand under Imperial corruption"},
            {"era": "Galactic Civil War", "event": "Han Solo's Kessel Run disrupts Pyke routes"},
            {"era": "New Republic Era", "event": "Syndicate wars with rival Dawn and Hutt interests"},
        ],
        "films": [
            "Star Wars: Episode IV — A New Hope",
            *CLONE_WARS_FILMS,
            "Solo: A Star Wars Story",
        ],
        "series": ["Star Wars: The Clone Wars", "Star Wars: The Mandalorian"],
    },
    "black-sun": {
        "dateRange": "c. 1,000 BBY – present",
        "headOfState": head("Black Sun Vigo Council"),
        "headOfGovernment": head("Black Sun Underboss network"),
        "planets": [
            planet("Mustafar", "mustafar"),
            planet("Coruscant", "coruscant"),
        ],
        "overview": (
            "Black Sun is a galaxy-spanning crime syndicate whose Vigo governors, assassin retainer pools, "
            "and Mustafar fortress-banks control smuggling, slavery, and extortion markets from the Clone "
            "Wars through the Imperial era and beyond. Unlike kajidic clans that advertise palace spectacle, "
            "Black Sun prefers shadow councils, disposable lieutenants, and sector bosses who answer to "
            "no single throne.\n\n"
            "Its reach intersects every major underworld story — from [Maul](sith/darth-maul)'s early "
            "power plays to [Boba Fett](characters/boba-fett)'s bounty markets and Imperial intelligence "
            "backchannels on Coruscant."
        ),
        "history": (
            "Black Sun grew by franchising crime: each Vigo received territory charters, tax quotas, and "
            "assassin support in exchange for tribute upstream. Mustafar's lava-refinery fortresses "
            "became symbolic headquarters where disputes were settled with blades rather than courts.\n\n"
            "During the Clone Wars, [Darth Maul](sith/darth-maul) briefly attempted to absorb Black Sun "
            "into his Shadow Collective, killing Vigos who resisted and installing compliant lieutenants. "
            "[Obi-Wan Kenobi](jedi/obi-wan-kenobi) and [Ahsoka Tano](jedi/ahsoka-tano) later encountered "
            "Black Sun operatives on missions where syndicate politics collided with Sith vendettas.\n\n"
            "Under the Empire, Black Sun balanced cooperation and defiance — selling intelligence to "
            "Imperial Security Bureau while smuggling weapons to dissidents. Imperial-era legends of "
            "Prince Xizor competing with [Darth Vader](sith/darth-vader) for Palpatine's favor remain "
            "disputed in New Republic archives.\n\n"
            "[Boba Fett](characters/boba-fett), [Fennec Shand](characters/fennec-shand), and independent "
            "hunters frequently worked Black Sun contracts on Nar Shaddaa and Tatooine, treating Vigo "
            "payout tables as industry standard pricing."
        ),
        "significance": (
            "Black Sun defines the 'modern' galactic syndicate — decentralized, franchise-based, and "
            "durable enough to survive Sith coups and Imperial purges alike.\n\n"
            "Mustafar's pairing with Black Sun in popular memory links crime to volcanic industrial "
            "horror, influencing how later regimes hide torture facilities inside refinery complexes."
        ),
        "notableEvents": [
            "Black Sun Vigo system formalized across Rim sectors",
            "Mustafar fortress-banks become syndicate arbitration sites",
            "Darth Maul's Shadow Collective absorbs resistant Vigos",
            "Imperial era cooperation with ISB shadow desks",
            "Nar Shaddaa markets standardize Black Sun contract law",
            "Post-Endor succession wars among competing Vigos",
        ],
        "majorCharacters": [
            sith("Darth Maul", "sith/darth-maul"),
            char("Boba Fett", "characters/boba-fett"),
            char("Fennec Shand", "characters/fennec-shand"),
            jedi("Obi-Wan Kenobi", "jedi/obi-wan-kenobi"),
            jedi("Ahsoka Tano", "jedi/ahsoka-tano"),
            sith("Darth Vader", "sith/darth-vader"),
        ],
        "keyFactions": [faction("Hutts", "factions/hutts")],
        "affiliations": [
            "Vigo territorial charters",
            "Mustafar fortress-banks",
            "Assassin retainer guilds",
            "Nar Shaddaa shadow markets",
        ],
        "timeline": [
            {"era": "Old Republic", "event": "Black Sun Vigo councils formalized"},
            {"era": "Clone Wars", "event": "Maul's Shadow Collective challenges Vigo independence"},
            {"era": "Imperial Era", "event": "Syndicate operates dual contracts with ISB and smugglers"},
            {"era": "New Republic Era", "event": "Vigo succession conflicts reshape Rim crime map"},
        ],
        "films": CLONE_WARS_FILMS + ["Star Wars: Episode VI — Return of the Jedi"],
        "series": CLONE_WARS_SERIES + ["Star Wars: The Mandalorian", "Star Wars: The Book of Boba Fett"],
    },
    "crimson-dawn": {
        "dateRange": "c. 19 BBY – 10 BBY (primary era)",
        "headOfState": head("Dryden Vos", "characters/dryden-vos"),
        "headOfGovernment": head("Maul's Shadow Council"),
        "planets": [
            planet("Dathomir", "planet/dathomir"),
            planet("Savareen", "planet/savareen"),
            planet("Corellia", "planet/corellia"),
        ],
        "overview": (
            "Crimson Dawn is [Darth Maul](sith/darth-maul)'s shadow syndicate — a refinement-and-extortion "
            "network that exploited Imperial transition chaos through front companies, spice ports, and "
            "assassin cadres loyal to the former Sith Lord. Public-facing leadership passed through "
            "figures like [Dryden Vos](characters/dryden-vos) on Savareen, while [Qi'ra](characters/qira) "
            "managed Corellia operations and eventually ascended to Maul's inner circle.\n\n"
            "Crimson Dawn competed with Pyke, Black Sun, and Hutt kajidics by offering Imperial officials "
            "a single vendor for spice, weapons, and discreet violence — making it a template for "
            "post-Republic criminal consolidation."
        ),
        "history": (
            "After [Darth Sidious](sith/darth-sidious) discarded Maul on Naboo, the Zabrak rebuilt power "
            "through crime rather than Sith titles. Crimson Dawn emerged as the brand — crimson sigils on "
            "refinery towers, yacht casinos, and coercion contracts that frightened Rim governors faster "
            "than Separatist droid logos ever had.\n\n"
            "On Savareen, [Dryden Vos](characters/dryden-vos) ran Dawn operations from a yacht palace, "
            "employing enforcers with martial-art retainer traditions and Pyke spice shipments. "
            "[Qi'ra](characters/qira) — a Corellian survivor of street syndicates — rose from lieutenant "
            "to trusted executor, eventually contacting Maul directly after Vos's death.\n\n"
            "[Han Solo](characters/han-solo), [Chewbacca](characters/chewbacca), [Lando Calrissian](characters/lando-calrissian), "
            "and [Tobias Beckett](characters/tobias-beckett) intersected Crimson Dawn during the "
            "coaxium heist era, stealing refined coaxium that Vos intended as tribute upstream. "
            "Beckett's betrayal and Vos's demise reshuffled Dawn leadership under Qi'ra's secret mandate.\n\n"
            "Maul used Dawn to probe [Darth Vader](sith/darth-vader) and Imperial hierarchy, but the "
            "syndicate fractured after Maul's death on Tatooine. Remnants persisted as splinter cells "
            "negotiating with Pyke capos and Imperial Moffs into the New Republic era."
        ),
        "significance": (
            "Crimson Dawn links Sith vendetta culture to corporate crime — showing how dark-side actors "
            "weaponize supply chains when they cannot hold official thrones.\n\n"
            "Qi'ra's arc makes Dawn a character-driven syndicate unlike anonymous Vigo councils, "
            "influencing later stories about women leading Rim shadow governments."
        ),
        "notableEvents": [
            "Maul founds Crimson Dawn after Shadow Collective collapse",
            "Dryden Vos establishes Savareen refinement yacht operations",
            "Qi'ra elevated as Corellia sector executor",
            "Coaxium heist on Vandor and Kessel Run fallout",
            "Death of Dryden Vos during Solo crew confrontation",
            "Qi'ra reports directly to Maul on Dathomir",
            "Dawn splinters after Maul's demise",
        ],
        "majorCharacters": [
            sith("Darth Maul", "sith/darth-maul"),
            char("Dryden Vos", "characters/dryden-vos"),
            char("Qi'ra", "characters/qira"),
            char("Han Solo", "characters/han-solo"),
            char("Chewbacca", "characters/chewbacca"),
            char("Lando Calrissian", "characters/lando-calrissian"),
            char("Tobias Beckett", "characters/tobias-beckett"),
        ],
        "keyFactions": [
            faction("Pyke Syndicate", "organizations/pyke-syndicate"),
            faction("Black Sun", "organizations/black-sun"),
        ],
        "affiliations": [
            "Maul's Shadow Council",
            "Savareen coaxium refineries",
            "Corellia street syndicate cells",
            "Pyke spice shipment partners",
        ],
        "timeline": [
            {"era": "Imperial Era", "event": "Crimson Dawn brand established by Maul"},
            {"era": "Imperial Era", "event": "Dryden Vos controls Savareen operations"},
            {"era": "Imperial Era", "event": "Qi'ra assumes Corellia leadership"},
            {"era": "Imperial Era", "event": "Coaxium heist disrupts Dawn tribute schedules"},
            {"era": "Imperial Era", "event": "Syndicate fragments after Maul's death"},
        ],
        "films": ["Solo: A Star Wars Story"],
        "series": ["Star Wars: The Clone Wars"],
    },
    "inquisitorius": {
        "dateRange": "19 BBY – c. 5 BBY",
        "headOfState": head("The Grand Inquisitor", "sith/grand-inquisitor"),
        "headOfGovernment": head("Darth Vader", "sith/darth-vader"),
        "planets": [
            planet("Coruscant", "coruscant"),
            planet("Mustafar", "mustafar"),
        ],
        "overview": (
            "The Inquisitorius is [Darth Sidious](sith/darth-sidious) and [Darth Vader](sith/darth-vader)'s "
            "dark-side hunter order — a cadre of former Jedi turned interrogators, trackers, and "
            "executioners tasked with eliminating Jedi survivors after Order 66. Led initially by "
            "[The Grand Inquisitor](sith/grand-inquisitor), the Inquisitors wield spinning double-bladed "
            "lightsabers, Imperial intelligence resources, and fortress facilities such as the "
            "Fortress Inquisitorius on Nur.\n\n"
            "They are neither fully Sith nor merely Imperial officers; Palpatine designed them as "
            "disposable weapons who could hunt Force-sensitives without violating Rule of Two "
            "economics."
        ),
        "history": (
            "In the immediate aftermath of Order 66, surviving Jedi scattered across the Rim while "
            "Imperial propaganda declared the Order extinct. Vader selected fallen Jedi and dark-side "
            " adepts to become Inquisitors — granting them truncated training, rank insignia, and "
            "hunting charters in exchange for absolute obedience.\n\n"
            "[The Grand Inquisitor](sith/grand-inquisitor) pursued [Kanan Jarrus](jedi/kanan-jarrus) and "
            "[Ezra Bridger](jedi/ezra-bridger) across Lothal and beyond, while [The Second Sister](sith/second-sister) "
            "and [The Ninth Sister](sith/ninth-sister) targeted Cal Kestis-era fugitives in Jedi: Survivor "
            "canon pathways. [Ahsoka Tano](jedi/ahsoka-tano) escaped Inquisitorius custody narratives "
            "repeatedly cited in classified ISB files.\n\n"
            "Fortress Inquisitorius on Nur became a torture and experimentation site where children "
            "with Force sensitivity were abducted for Project Harvester. [Darth Vader](sith/darth-vader) "
            "personally oversaw high-value captures, treating Inquisitors as extensions of his "
            "hunt for Obi-Wan Kenobi and other high-profile survivors.\n\n"
            "The Grand Inquisitor's death over Mustafar weakened central coordination, yet individual "
            "Inquisitors remained dangerous through the early Rebellion era until attrition and "
            "internal purges reduced their numbers."
        ),
        "significance": (
            "The Inquisitorius embodies the Imperial Jedi Purge as institutional policy — not a single "
            "massacre but a sustained counterinsurgency against Force traditions.\n\n"
            "Their spinning sabers and pale visages became HoloNet nightmares that discouraged "
            "public sympathy for hidden Jedi, aiding Palpatine's narrative of Order betrayal."
        ),
        "notableEvents": [
            "Order 66 triggers Inquisitorius charter under Vader",
            "Grand Inquisitor appointed master hunter of fugitive Jedi",
            "Fortress Inquisitorius constructed on Nur",
            "Project Harvester abducts Force-sensitive children",
            "Hunts for Kanan Jarrus and Ezra Bridger on Lothal",
            "Second Sister and Ninth Sister deployed against Jedi survivors",
            "Grand Inquisitor dies over Mustafar reactor duel",
        ],
        "majorCharacters": [
            sith("The Grand Inquisitor", "sith/grand-inquisitor"),
            sith("Darth Vader", "sith/darth-vader"),
            sith("Darth Sidious", "sith/darth-sidious"),
            sith("Second Sister", "sith/second-sister"),
            sith("Ninth Sister", "sith/ninth-sister"),
            sith("Fifth Brother", "sith/fifth-brother"),
            jedi("Kanan Jarrus", "jedi/kanan-jarrus"),
            jedi("Ezra Bridger", "jedi/ezra-bridger"),
            jedi("Ahsoka Tano", "jedi/ahsoka-tano"),
        ],
        "jediFallen": [
            jedi("Ki-Adi-Mundi", "jedi/ki-adi-mundi"),
            jedi("Plo Koon", "jedi/plo-koon"),
            jedi("Depa Billaba", "jedi/depa-billaba"),
        ],
        "jediSurvived": [
            jedi("Kanan Jarrus", "jedi/kanan-jarrus"),
            jedi("Ahsoka Tano", "jedi/ahsoka-tano"),
            jedi("Obi-Wan Kenobi", "jedi/obi-wan-kenobi"),
            jedi("Yoda", "jedi/yoda"),
        ],
        "keyFactions": [faction("Galactic Empire", "factions/empire")],
        "affiliations": [
            "Imperial Security Bureau liaisons",
            "Fortress Inquisitorius garrisons",
            "Project Harvester teams",
            "Dark-side interrogation academies",
        ],
        "timeline": [
            {"era": "Imperial Era", "event": "Inquisitorius founded after Order 66"},
            {"era": "Imperial Era", "event": "Grand Inquisitor leads purge operations"},
            {"era": "Imperial Era", "event": "Nur fortress activated for Jedi detention"},
            {"era": "Imperial Era", "event": "Lothal hunts target Spectres cell"},
            {"era": "Imperial Era", "event": "Order attrition reduces active Inquisitors"},
        ],
        "films": ["Star Wars: Episode III — Revenge of the Sith"],
        "series": [
            "Star Wars Rebels",
            "Star Wars: Obi-Wan Kenobi",
            "Star Wars: Tales of the Jedi",
        ],
        "games": ["Star Wars Jedi: Fallen Order", "Star Wars Jedi: Survivor"],
        "majorEvents": [
            {"text": "Jedi Purge — Order 66 and the Inquisitorius hunt", "route": "wars-conflicts/battles/jedi-purge"},
        ],
    },
    "mining-guild": {
        "dateRange": "c. 1,000 BBY – present",
        "headOfState": head("Mining Guild Directorate"),
        "headOfGovernment": head("Guild claim-rights arbitration board"),
        "planets": [
            planet("Asteroid belts of the Outer Rim", "planet/hoth"),
            planet("Mustafar", "mustafar"),
            planet("Cato Neimoidia", "planet/cato-neimoidia"),
        ],
        "overview": (
            "The Mining Guild is an industrial charter conglomerate whose ore freighters, claim rights, and "
            "private security fleets extract resources from asteroids, toxic worlds, and gas giants under "
            "Imperial and corporate licenses. Guild symbolography — winged pick sigils on yellow hulls — "
            "marks tugs and refineries from Kessel belts to Mustafar lava mines.\n\n"
            "During the Imperial era the Guild operated as a semi-sovereign contractor, supplying "
            "TIE-adjacent escorts and strip-mining platforms that stripped worlds faster than "
            "environmental law could respond."
        ),
        "history": (
            "Mining Guild roots lie in Rim prospector cooperatives that pooled security costs against "
            "pirate raids. As claim-rights law codified, successful cooperatives became guilds with "
            "Senate lobbyists and private orbital stations.\n\n"
            "Under the Empire, [Grand Moff Tarkin](characters/grand-moff-tarkin) and sector Moffs "
            "granted Guild charters in exchange for resource quotas feeding Death Star and "
            "Star Destroyer construction. [Agent Kallus](characters/agent-kallus) and Imperial "
            "overseers often rode Guild tugs during Lothal and Atollon sector operations.\n\n"
            "[Hera Syndulla](characters/hera-syndulla) and the Spectres attacked Guild convoys "
            "when strip-mining threatened civilian worlds. [Sabine Wren](characters/sabine-wren) "
            "recognized Guild insignia on targets that supplied Imperial shipyards.\n\n"
            "Post-Endor, Guild fleets fragmented — some cells negotiated with the New Republic, "
            "others sold ore to First Order remnant yards under false transponder codes."
        ),
        "significance": (
            "The Mining Guild shows how resource extraction becomes military infrastructure when "
            "states outsource strip-mining to chartered militias.\n\n"
            "Its yellow-wing iconography makes Guild tugs instantly recognizable in Rebels-era "
            "space battles, linking economic crime to visible fleet actions."
        ),
        "notableEvents": [
            "Mining Guild chartered as claim-rights arbitration body",
            "Imperial contracts tie Guild output to Death Star materiel",
            "Strip-mining operations expand on Lothal and Atollon",
            "Rebel cells intercept Guild convoys supplying Imperial yards",
            "Post-Imperial fragmentation of Guild security fleets",
        ],
        "majorCharacters": [
            char("Grand Moff Tarkin", "characters/grand-moff-tarkin"),
            char("Agent Kallus", "characters/agent-kallus"),
            char("Hera Syndulla", "characters/hera-syndulla"),
            char("Sabine Wren", "characters/sabine-wren"),
        ],
        "keyFactions": [faction("Galactic Empire", "factions/empire")],
        "affiliations": [
            "Imperial resource quotas",
            "Asteroid belt claim registries",
            "Guild security tug regiments",
        ],
        "timeline": [
            {"era": "Old Republic", "event": "Prospector cooperatives merge into Mining Guild"},
            {"era": "Imperial Era", "event": "Guild charters expand under Tarkin doctrine"},
            {"era": "Imperial Era", "event": "Rebel attacks on Guild convoys escalate"},
            {"era": "New Republic Era", "event": "Guild cells split between Republic and remnant buyers"},
        ],
        "films": ["Star Wars: Episode IV — A New Hope"],
        "series": ["Star Wars Rebels", "Star Wars: The Mandalorian"],
    },
    "smuggler-guilds": {
        "dateRange": "Ancient era – present",
        "headOfState": head("Convoy charter captains' council"),
        "headOfGovernment": head("Shadow port syndics"),
        "planets": [
            planet("Nar Shaddaa", "settlements/nar-shaddaa"),
            planet("Tatooine", "tatooine"),
            planet("Corellia", "planet/corellia"),
        ],
        "overview": (
            "Smuggler Guilds are umbrella charter networks — not a single corporation but a directory "
            "of convoy codes, shadow-port syndics, and freight captains who move contraband between "
            "Hutt space and the Outer Rim. Guild membership buys transponder masks, dispute arbitration, "
            "and collective bargaining against Imperial customs cutters.\n\n"
            "From spice runners on the Kessel Run to Corellian YT-series captains, smuggler guilds "
            "translate individual outlaw reputations into institutional endurance across eras."
        ),
        "history": (
            "Smuggling predates the Republic, but formal guild charters emerged when Hutt kajidics "
            "and Rim governors realized regulated contraband was easier to tax than eradicated piracy. "
            "Shadow ports like Nar Shaddaa and Mos Eisley hosted guild syndics who recorded debts, "
            "posted bounties, and enforced convoy truce days.\n\n"
            "[Han Solo](characters/han-solo) and [Lando Calrissian](characters/lando-calrissian) "
            "operated within guild customs even when they mocked guild bureaucracy — paying dues when "
            "convenient and defying guild bosses when profitable. [Hondo Ohnaka](characters/hondo-ohnaka) "
            "ran pirate-smuggler hybrids that guild purists denounced yet secretly hired for escort violence.\n\n"
            "Imperial crackdowns pushed guilds deeper into Pyke and Hutt patronage networks. "
            "[Cad Bane](bounty-hunters/cad-bane) and [Boba Fett](characters/boba-fett) enforced "
            "guild contracts when captains defaulted on spice loans.\n\n"
            "New Republic legalization debates never fully absorbed guild charters, leaving "
            "Spice Runners' Guild and Corellian Smuggler Guild descendants active under "
            "semi-recognized codes."
        ),
        "significance": (
            "Smuggler guilds frame Star Wars' rogues as an economy — not lone heroes but participants "
            "in arbitration systems, convoy law, and shadow diplomacy.\n\n"
            "The category hub links child guilds that specialize in spice, Corellian freight, and "
            "Hutt-backed rings."
        ),
        "notableEvents": [
            "Shadow port syndics codify smuggler convoy law",
            "Imperial customs wars drive guild consolidation",
            "Han Solo and Lando Calrissian rise through guild-adjacent careers",
            "Pyke and Hutt patronage splits guild loyalties",
            "New Republic charter debates fail to unify guild law",
        ],
        "majorCharacters": [
            char("Han Solo", "characters/han-solo"),
            char("Lando Calrissian", "characters/lando-calrissian"),
            char("Hondo Ohnaka", "characters/hondo-ohnaka"),
            bh("Cad Bane", "bounty-hunters/cad-bane"),
            char("Boba Fett", "characters/boba-fett"),
        ],
        "affiliations": [
            "Shadow port syndics",
            "Convoy charter captains",
            "Hutt-backed freight rings",
        ],
        "timeline": [
            {"era": "Old Republic", "event": "Shadow ports formalize smuggler arbitration"},
            {"era": "Imperial Era", "event": "Guild charters proliferate under customs crackdowns"},
            {"era": "Galactic Civil War", "event": "Rebel cells rely on guild smugglers for supply"},
            {"era": "New Republic Era", "event": "Guild descendants survive partial legalization talks"},
        ],
        "films": ORIGINAL_TRILOGY + ["Solo: A Star Wars Story"],
        "series": UNDERWORLD_SERIES,
    },
    "corporate-blocs": {
        "dateRange": "c. 25,000 BBY – present",
        "headOfState": head("Megacorporate holding chairpersons"),
        "headOfGovernment": head("Directorate interlock committees"),
        "planets": [
            planet("Coruscant", "coruscant"),
            planet("Neimoidia", "planet/neimoidia"),
            planet("Muunilinst", "planet/muunilinst"),
        ],
        "overview": (
            "Corporate Blocs are megacorporate holding structures whose interlocking directorates, private "
            "armies, and tariff lawyers shape galactic trade beyond any single government code. This "
            "category hub tracks formal boards — such as the Trade Federation Directorate and "
            "InterGalactic Banking Holding — that translate shareholder votes into blockades and "
            "battle droid deployments.\n\n"
            "Where factions fly national banners, corporate blocs fly logos that outlast regimes."
        ),
        "history": (
            "Republic-era trade law allowed corporate entities to purchase Senate influence through "
            "lobbyist corps and sector sponsorship. Neimoidian directorates and Muun holding companies "
            " perfected dual-use accounting — civilian shipping lines that could pivot to siege "
            "blockades within a fiscal quarter.\n\n"
            "[Nute Gunray](characters/nute-gunray) and the Trade Federation Directorate commanded "
            "droid armies while claiming diplomatic immunity, forcing [Padmé Amidala](characters/padme-amidala) "
            "to argue that corporations had become sovereign belligerents. [Rush Clovis](characters/rush-clovis) "
            "later revealed how deeply IGBC holdings penetrated Republic finance.\n\n"
            "Separatist-era corporate blocs merged militias with Separatist Council votes, while "
            "Imperial-era blocs were nationalized or absorbed into COMPNOR procurement chains. "
            "[Director Krennic](characters/director-krennic) and [Grand Moff Tarkin](characters/grand-moff-tarkin) "
            "both relied on corporate subcontractors for Death Star materiel.\n\n"
            "Modern historians treat corporate blocs as continuous institutions — the same holding "
            "math that funded Naboo blockades later funded First Order shipyard shells."
        ),
        "significance": (
            "Corporate blocs explain why Star Wars wars are often trade wars — blockades, debt traps, "
            "and directorate votes precede fleet engagements.\n\n"
            "The hub organizes child entries for Trade Federation and IGBC holding structures."
        ),
        "notableEvents": [
            "Trade Federation Directorate blockades Naboo",
            "IGBC holding companies fund Separatist and Republic debt alike",
            "Corporate militias granted Separatist Council seats",
            "Imperial nationalization of select megacorp assets",
            "Corporate shells persist into First Order shipbuilding era",
        ],
        "majorCharacters": [
            char("Nute Gunray", "characters/nute-gunray"),
            char("Padmé Amidala", "characters/padme-amidala"),
            char("Rush Clovis", "characters/rush-clovis"),
            char("Director Krennic", "characters/director-krennic"),
            char("Grand Moff Tarkin", "characters/grand-moff-tarkin"),
        ],
        "keyFactions": [
            faction("Trade Federation", "factions/trade-federation"),
            faction("Confederacy of Independent Systems", "factions/confederacy"),
        ],
        "affiliations": [
            "Trade Federation Directorate",
            "InterGalactic Banking Holding",
            "Neimoidian trade dynasties",
            "Muun vault interlocks",
        ],
        "timeline": [
            {"era": "Old Republic", "event": "Megacorporate holdings gain Senate leverage"},
            {"era": "Separatist Crisis", "event": "Directorates arm private militias"},
            {"era": "Clone Wars", "event": "Corporate blocs sit on Separatist Council"},
            {"era": "Imperial Era", "event": "Select blocs nationalized or subcontracted"},
        ],
        "films": [
            "Star Wars: Episode I — The Phantom Menace",
            *CLONE_WARS_FILMS,
        ],
        "series": CLONE_WARS_SERIES,
    },
    "crime-families": {
        "dateRange": "Ancient era – present",
        "headOfState": head("Kajidic clan elders"),
        "headOfGovernment": head("Grand Hutt Council observers"),
        "planets": [
            planet("Nal Hutta", "planet/nal-hutta"),
            planet("Tatooine", "tatooine"),
            planet("Nar Shaddaa", "settlements/nar-shaddaa"),
        ],
        "overview": (
            "Crime Families — chiefly Hutt kajidic clans and syndicate councils — govern the galactic "
            "underworld through blood oaths, spice routes, bounty ledgers, and palace courts that "
            "outlast republics. This hub tracks major kajidics such as Desilijic and Besadii alongside "
            "Black Sun's Vigo Council, linking family structure to sector-scale criminal policy.\n\n"
            "Where empires claim law, kajidics claim contracts — and enforce them with rancors, "
            "hunters, and fleet blockades."
        ),
        "history": (
            "Hutt kajidics evolved on Nal Hutta and Nar Shaddaa, using family name suffixes "
            "(Desilijic, Besadii, etc.) to mark succession rights, debt inheritance, and territorial "
            "charters. [Jabba the Hutt](characters/jabba-the-hutt)'s Desilijic clan turned Tatooine "
            "into a palace state where [Boba Fett](characters/boba-fett), [Bib Fortuna](characters/bib-fortuna), "
            "and [Sy Snootles](characters/sy-snootles) played court politics with life-or-death stakes.\n\n"
            "Besadii kajidic rivals contested Kessel labor monopolies and spice pricing, led in "
            "later eras by [Durga Besadii](characters/jabba-the-hutt) legends contested in New Republic "
            "archives. Black Sun's Vigo Council offered a non-Hutt parallel — franchise crime families "
            "with Mustafar arbitration instead of palace spectacle.\n\n"
            "[Cad Bane](bounty-hunters/cad-bane), [Fennec Shand](characters/fennec-shand), and "
            "[Din Djarin](characters/din-djarin) navigated kajidic law when retrieving bounties or "
            "negotiating truces. [Luke Skywalker](jedi/luke-skywalker) and [Leia Organa](characters/leia-organa) "
            "confronted Desilijic power directly during the rescue of Han Solo from Jabba's court.\n\n"
            "After Jabba's death, [Boba Fett](characters/boba-fett) briefly claimed Tatooine "
            "underworld leadership, reshuffling kajidic alliances across Hutt Space."
        ),
        "significance": (
            "Crime families anchor Star Wars' underworld as political actors — not background color "
            "but governance systems with succession law, foreign policy, and military capacity.\n\n"
            "The hub connects child entries for Desilijic, Besadii, and Black Sun Vigo structures."
        ),
        "notableEvents": [
            "Kajidic charters formalize Hutt succession and debt law",
            "Desilijic establishes Tatooine palace governance under Jabba",
            "Besadii challenges Desilijic spice monopolies",
            "Rescue of Han Solo from Jabba's court",
            "Boba Fett assumes Tatooine underworld leadership",
            "Black Sun Vigo Council coordinates non-Hutt franchise crime",
        ],
        "majorCharacters": [
            char("Jabba the Hutt", "characters/jabba-the-hutt"),
            char("Bib Fortuna", "characters/bib-fortuna"),
            char("Boba Fett", "characters/boba-fett"),
            char("Sy Snootles", "characters/sy-snootles"),
            jedi("Luke Skywalker", "jedi/luke-skywalker"),
            char("Leia Organa", "characters/leia-organa"),
            bh("Cad Bane", "bounty-hunters/cad-bane"),
        ],
        "keyFactions": [faction("Hutts", "factions/hutts")],
        "affiliations": [
            "Desilijic kajidic",
            "Besadii kajidic",
            "Black Sun Vigo Council",
            "Bounty Hunters' Guild patronage networks",
        ],
        "timeline": [
            {"era": "Ancient Era", "event": "Hutt kajidics consolidate Nal Hutta power"},
            {"era": "Imperial Era", "event": "Jabba's Desilijic court dominates Tatooine"},
            {"era": "Galactic Civil War", "event": "Rescue of Han Solo destabilizes Desilijic"},
            {"era": "New Republic Era", "event": "Boba Fett reshapes Tatooine underworld"},
        ],
        "films": ORIGINAL_TRILOGY,
        "series": ["Star Wars: The Book of Boba Fett", *UNDERWORLD_SERIES],
    },
    "spice-runners-guild": {
        "dateRange": "c. 1,000 BBY – present",
        "headOfState": head("Kessel Run route captains' syndic"),
        "headOfGovernment": head("Pyke contract arbitration board"),
        "planets": [
            planet("Kessel", "planet/kessel"),
            planet("Oba Diah", "planet/oba-diah"),
        ],
        "overview": (
            "The Spice Runners' Guild charters pilots who move glitterstim and refined spice along the "
            "Kessel Run under Pyke Syndicate contracts while evading Imperial customs patrols. Guild "
            "membership provides route codes, emergency hideouts, and collective leverage against "
            "single-captain price fixing by labor brokers.\n\n"
            "The guild's mythology centers on speed — parsecs as reputation, coaxium as temptation, "
            "and Pyke enforcers as the penalty for late delivery."
        ),
        "history": (
            "Kessel's spice mines generated demand for specialized pilots who could navigate "
            "Maw Cluster turbulence faster than customs interdictors. Spice Runners' Guild syndics "
            "on Kessel registered captain times, enforced Pyke tribute schedules, and posted "
            "bounties on crews who stole shipments.\n\n"
            "[Han Solo](characters/han-solo)'s record Kessel Run — aided by [Chewbacca](characters/chewbacca) "
            "and L3-37's navicomputer hacks in some accounts — made guild recruitment surge across "
            "the Rim. [Qi'ra](characters/qira) and Crimson Dawn later exploited guild rivalries to "
            "redirect coaxium flows during the Imperial consolidation era.\n\n"
            "[Cad Bane](bounty-hunters/cad-bane) tracked guild defaulters for Pyke capos, while "
            "Rebel cells occasionally hired spice runners for covert supply under false manifests."
        ),
        "significance": (
            "The Spice Runners' Guild connects Kessel astronomy to smuggler hero lore — making "
            "industrial slavery's product into a pilot prestige economy.\n\n"
            "Child of the Smuggler Guilds hub, it links to Pyke Syndicate parent economics."
        ),
        "notableEvents": [
            "Guild syndics register Kessel Run route times",
            "Pyke contracts formalize spice tribute schedules",
            "Han Solo completes record Kessel Run",
            "Crimson Dawn exploits guild route rivalries",
            "Imperial customs interdictors target guild convoys",
        ],
        "majorCharacters": [
            char("Han Solo", "characters/han-solo"),
            char("Chewbacca", "characters/chewbacca"),
            char("Qi'ra", "characters/qira"),
            bh("Cad Bane", "bounty-hunters/cad-bane"),
        ],
        "keyFactions": [org("Pyke Syndicate", "organizations/pyke-syndicate")],
        "affiliations": [
            "Pyke Syndicate contracts",
            "Kessel labor broker networks",
            "Smuggler Guilds umbrella charter",
        ],
        "timeline": [
            {"era": "Old Republic", "event": "Kessel spice routes attract specialist pilots"},
            {"era": "Imperial Era", "event": "Guild syndics formalize under Pyke oversight"},
            {"era": "Imperial Era", "event": "Han Solo's Run becomes guild legend"},
        ],
        "films": ["Star Wars: Episode IV — A New Hope", "Solo: A Star Wars Story"],
        "series": ["Star Wars: The Mandalorian"],
    },
    "corellian-smuggler-guild": {
        "dateRange": "c. 500 BBY – present",
        "headOfState": head("Corellian shadow-dock foremen council"),
        "headOfGovernment": head("YT-series registry board"),
        "planets": [
            planet("Corellia", "planet/corellia"),
            planet("Nar Shaddaa", "settlements/nar-shaddaa"),
        ],
        "overview": (
            "The Corellian Smuggler Guild dominates the Corellian Run black market through YT-series "
            "freighter captains, shadow-dock foremen, and registry boards that launder transponder "
            "codes faster than Imperial customs can decode them. Corellian shipyards produce hulls "
            "built for modification — smuggling compartments, hidden guns, and sensor-baffling plates "
            "installed as factory options.\n\n"
            "The guild embodies Corellia's dual identity: Imperial naval recruitment world and "
            "smuggler birthplace alike."
        ),
        "history": (
            "Corellia's shipwright culture produced the YT-1300 and successor freighters that became "
            "smuggler standard issue. Guild foremen on Coronet City shadow docks charged fees to "
            "file false manifests and bribe port inspectors — services [Han Solo](characters/han-solo) "
            "used long before joining the Rebellion.\n\n"
            "[Qi'ra](characters/qira) and [Tobias Beckett](characters/tobias-beckett) operated "
            "Corellia street syndicates adjacent to guild halls, feeding recruits into larger "
            "charter networks. [Lando Calrissian](characters/lando-calrissian) managed guild-adjacent "
            "gambling debts that could seize freighter liens overnight.\n\n"
            "During the Galactic Civil War, Corellian guild captains split between Imperial "
            "patrol service and Rebel supply runs — [Wedge Antilles](characters/wedge-antilles) "
            "and [Han Solo](characters/han-solo) representing divergent Corellian loyalties."
        ),
        "significance": (
            "The Corellian Smuggler Guild explains why so many iconic freighters share hull families "
            "— smuggling is industrial policy, not individual improvisation.\n\n"
            "Corellia's guild ties bind Solo, Qi'ra, and Lando narratives into one geographic hub."
        ),
        "notableEvents": [
            "YT-series registry board formalizes smuggler modifications",
            "Shadow-dock foremen codify Corellian Run bribe schedules",
            "Qi'ra rises through Corellia street syndicates",
            "Han Solo wins the Millennium Falcon from Lando Calrissian",
            "Guild captains split loyalties during Galactic Civil War",
        ],
        "majorCharacters": [
            char("Han Solo", "characters/han-solo"),
            char("Qi'ra", "characters/qira"),
            char("Lando Calrissian", "characters/lando-calrissian"),
            char("Tobias Beckett", "characters/tobias-beckett"),
            char("Wedge Antilles", "characters/wedge-antilles"),
        ],
        "affiliations": [
            "Smuggler Guilds umbrella charter",
            "Corellian Engineering Corporation shadow docks",
            "Nar Shaddaa transponder laundering cells",
        ],
        "timeline": [
            {"era": "Old Republic", "event": "Corellian yards standardize smuggler freighter hulls"},
            {"era": "Imperial Era", "event": "Guild foremen expand shadow-dock operations"},
            {"era": "Galactic Civil War", "event": "Corellian captains divide between Empire and Rebellion"},
        ],
        "films": ["Solo: A Star Wars Story", *ORIGINAL_TRILOGY],
        "series": UNDERWORLD_SERIES,
    },
    "hutt-smuggling-rings": {
        "dateRange": "Ancient era – present",
        "headOfState": head("Kajidic convoy masters"),
        "headOfGovernment": head("Nal Hutta shipping lane syndics"),
        "planets": [
            planet("Nal Hutta", "planet/nal-hutta"),
            planet("Tatooine", "tatooine"),
        ],
        "overview": (
            "Hutt Smuggling Rings are loose kajidic-backed convoy networks that ferry spice, slaves, "
            "and weapons through Nal Hutta's protected shipping lanes. Unlike formal guilds with "
            "published charters, Hutt rings operate through oral contracts, palace favor, and "
            "punitive rancor enforcement.\n\n"
            "Rings overlap Desilijic and Besadii interests — cooperation when profitable, assassination "
            "when inheritance disputes demand it."
        ),
        "history": (
            "Hutt Space tolerated smuggling as governance: kajidics taxed contraband rather than "
            "eliminating it. Convoy masters registered routes with Grand Council observers, paying "
            "tribute upstream while hiring [Boba Fett](characters/boba-fett) or [Cad Bane](bounty-hunters/cad-bane) "
            "to recover stolen shipments.\n\n"
            "[Jabba the Hutt](characters/jabba-the-hutt) coordinated rings linking Tatooine palaces "
            "to Nal Hutta vaults, moving spice and weapons under Imperial noses. [Han Solo](characters/han-solo)'s "
            "debts to Jabba exemplified ring economics — personal obligation scaled to fleet policy.\n\n"
            "[Din Djarin](characters/din-djarin) and [Boba Fett](characters/boba-fett) later "
            "negotiated ring truces when Imperial collapse created power vacuums on Tatooine."
        ),
        "significance": (
            "Hutt smuggling rings merge family law with logistics — inheritance, marriage, and "
            "succession directly alter convoy routes.\n\n"
            "They bridge the Smuggler Guilds hub and Hutt kajidic crime families."
        ),
        "notableEvents": [
            "Kajidic convoy masters register Nal Hutta lane codes",
            "Jabba integrates Tatooine rings into Desilijic policy",
            "Han Solo accumulates debt to Hutt ring creditors",
            "Post-Jabba power vacuum reshuffles ring leadership",
        ],
        "majorCharacters": [
            char("Jabba the Hutt", "characters/jabba-the-hutt"),
            char("Han Solo", "characters/han-solo"),
            char("Boba Fett", "characters/boba-fett"),
            char("Din Djarin", "characters/din-djarin"),
            bh("Cad Bane", "bounty-hunters/cad-bane"),
        ],
        "keyFactions": [faction("Hutts", "factions/hutts")],
        "affiliations": [
            "Desilijic convoy cells",
            "Besadii rival ring networks",
            "Smuggler Guilds umbrella charter",
        ],
        "timeline": [
            {"era": "Ancient Era", "event": "Hutt rings formalize protected shipping lanes"},
            {"era": "Imperial Era", "event": "Jabba dominates Tatooine–Nal Hutta routes"},
            {"era": "New Republic Era", "event": "Succession conflicts fragment ring leadership"},
        ],
        "films": ORIGINAL_TRILOGY,
        "series": ["Star Wars: The Book of Boba Fett", "Star Wars: The Mandalorian"],
    },
    "desilijic-kajidic": {
        "dateRange": "Ancient era – 4 ABY (Jabba era apex)",
        "headOfState": head("Jabba the Hutt", "characters/jabba-the-hutt"),
        "headOfGovernment": head("Bib Fortuna", "characters/bib-fortuna"),
        "planets": [
            planet("Tatooine", "tatooine"),
            planet("Nal Hutta", "planet/nal-hutta"),
        ],
        "overview": (
            "The Desilijic kajidic — epitomized by [Jabba the Hutt](characters/jabba-the-hutt)'s court "
            "on Tatooine — anchored spice, bounty, and slave trade across Hutt Space for generations. "
            "Palace governance blended spectacle and terror: rancor pits, sail barge processions, and "
            "bounty boards that could ruin Coreward dignitaries.\n\n"
            "Desilijic power made Tatooine a sovereign criminal world within Imperial borders."
        ),
        "history": (
            "Desilijic succession law tied clan name to palace assets — sail barges, rancor pits, "
            "and dock tolls passed through Hutt littermates and majordomos like [Bib Fortuna](characters/bib-fortuna). "
            "[Jabba the Hutt](characters/jabba-the-hutt) leveraged Desilijic reach to post bounties on "
            "[Han Solo](characters/han-solo), imprison [Chewbacca](characters/chewbacca), and "
            "humiliate [Luke Skywalker](jedi/luke-skywalker) with a public execution sentence.\n\n"
            "[Leia Organa](characters/leia-organa)'s assassination of Jabba aboard the sail barge "
            "and [Luke Skywalker](jedi/luke-skywalker)'s rancor pit victory shattered Desilijic "
            "prestige overnight. [Sy Snootles](characters/sy-snootles) and [Bib Fortuna](characters/bib-fortuna) "
            "played internal succession games that continued until [Boba Fett](characters/boba-fett) "
            "claimed Tatooine.\n\n"
            "[Boba Fett](characters/boba-fett) and [Fennec Shand](characters/fennec-shand) later "
            "navigated Desilijic debts and palace ruins when rebuilding Mos Espa underworld order."
        ),
        "significance": (
            "Desilijic is Star Wars' most visible kajidic — palace culture, rancor horror, and "
            "bounty economics in one narrative bundle.\n\n"
            "Jabba's court links Original Trilogy rescue arcs to Book of Boba Fett succession stories."
        ),
        "notableEvents": [
            "Jabba establishes Tatooine palace as Desilijic capital",
            "Bounty posted on Han Solo after spice shipment loss",
            "Luke Skywalker slays rancor beneath palace throne room",
            "Leia Organa kills Jabba aboard sail barge at Great Pit of Carkoon",
            "Bib Fortuna briefly succeeds Jabba before Fett intervention",
        ],
        "majorCharacters": [
            char("Jabba the Hutt", "characters/jabba-the-hutt"),
            char("Bib Fortuna", "characters/bib-fortuna"),
            char("Sy Snootles", "characters/sy-snootles"),
            char("Han Solo", "characters/han-solo"),
            char("Chewbacca", "characters/chewbacca"),
            jedi("Luke Skywalker", "jedi/luke-skywalker"),
            char("Leia Organa", "characters/leia-organa"),
            char("Boba Fett", "characters/boba-fett"),
        ],
        "keyFactions": [faction("Hutts", "factions/hutts")],
        "affiliations": [
            "Crime Families hub",
            "Tatooine dock toll monopolies",
            "Bounty Hunters' Guild patronage",
        ],
        "timeline": [
            {"era": "Old Republic", "event": "Desilijic kajidic rises on Nal Hutta"},
            {"era": "Imperial Era", "event": "Jabba's Tatooine palace becomes clan capital"},
            {"era": "Galactic Civil War", "event": "Rescue of Han Solo kills Jabba"},
            {"era": "New Republic Era", "event": "Boba Fett inherits Tatooine underworld mantle"},
        ],
        "films": ORIGINAL_TRILOGY,
        "series": ["Star Wars: The Book of Boba Fett"],
    },
    "besadii-kajidic": {
        "dateRange": "Ancient era – present",
        "headOfState": head("Durga the Hutt"),
        "headOfGovernment": head("Besadii estate regents"),
        "planets": [
            planet("Nal Hutta", "planet/nal-hutta"),
            planet("Kessel", "planet/kessel"),
        ],
        "overview": (
            "The Besadii kajidic is Desilijic's great rival — a Hutt clan led in its modern apex by "
            "Durga Besadii that contested spice monopolies, Kessel labor contracts, and Nar Shaddaa "
            "dock rights through the New Republic era. Besadii preferred corporate fronts and "
            "bulk freighter fleets over Jabba-style palace theatre.\n\n"
            "Where Desilijic ruled through spectacle, Besadii ruled through spreadsheets and "
            "slave-labor quotas."
        ),
        "history": (
            "Besadii investments in Kessel spice mines made the clan indispensable to Pyke refineries "
            "and Imperial labor brokers alike. Contract disputes with Desilijic often ended in "
            "assassination or sabotage rather than open fleet battles.\n\n"
            "Durga Besadii's expansion during the New Republic era threatened to unify Hutt Space "
            "under a single non-Desilijic banner until internal sabotage and Jedi-adjacent "
            "interventions — including [Leia Organa](characters/leia-organa)'s diplomatic missions — "
            "fractured Besadii credit lines.\n\n"
            "[Han Solo](characters/han-solo)'s Kessel Run debts and [Chewbacca](characters/chewbacca)'s "
            "Imperial entanglements occasionally intersected Besadii labor brokers, linking smuggler "
            "hero lore to kajidic economics."
        ),
        "significance": (
            "Besadii proves Hutt power is not monolithic — rival kajidics wage economic war as "
            "ferociously as any corporate bloc.\n\n"
            "Kessel labor history cannot be told without Besadii contract archives."
        ),
        "notableEvents": [
            "Besadii secures Kessel labor broker monopolies",
            "Rival assassinations with Desilijic over spice pricing",
            "Durga Besadii expands during New Republic power vacuum",
            "Diplomatic and sabotage campaigns reduce Besadii unity",
        ],
        "majorCharacters": [
            char("Han Solo", "characters/han-solo"),
            char("Chewbacca", "characters/chewbacca"),
            char("Leia Organa", "characters/leia-organa"),
            char("Jabba the Hutt", "characters/jabba-the-hutt"),
        ],
        "keyFactions": [faction("Hutts", "factions/hutts")],
        "affiliations": [
            "Crime Families hub",
            "Kessel labor contractors",
            "Pyke Syndicate shipping partners",
        ],
        "timeline": [
            {"era": "Old Republic", "event": "Besadii kajidic formalizes on Nal Hutta"},
            {"era": "Imperial Era", "event": "Kessel contracts expand Besadii wealth"},
            {"era": "New Republic Era", "event": "Durga Besadii challenges Desilijic vacuum"},
        ],
        "films": ["Star Wars: Episode IV — A New Hope"],
        "series": UNDERWORLD_SERIES,
    },
    "black-sun-vigo-council": {
        "dateRange": "c. 1,000 BBY – present",
        "headOfState": head("Senior Vigo quorum"),
        "headOfGovernment": head("Black Sun Underboss cadre"),
        "planets": [
            planet("Mustafar", "mustafar"),
            planet("Coruscant", "coruscant"),
        ],
        "overview": (
            "The Black Sun Vigo Council coordinates sector bosses, assassin retainer contracts, and "
            "syndicate succession disputes from hidden fortresses — chiefly Mustafar's refinery citadels. "
            "Each Vigo governs a territory quota; the Council resolves conflicts that would otherwise "
            "fragment Black Sun into warring bands.\n\n"
            "The Council is crime-family governance without Hutt blood oaths — franchise law instead "
            "of kajidic inheritance."
        ),
        "history": (
            "Vigo councils emerged when Black Sun outgrew single-boss rule. Mustafar fortresses hosted "
            "summits where Vigos traded assassin pools and smuggling lanes like diplomatic treaties.\n\n"
            "[Darth Maul](sith/darth-maul) decapitated resistant Vigos when building the Shadow "
            "Collective, forcing the Council to accept Sith oversight temporarily. [Obi-Wan Kenobi](jedi/obi-wan-kenobi) "
            "and Republic intelligence monitored Council channels during Clone Wars underworld arcs.\n\n"
            "Imperial-era Councils sold ISB informants while smuggling for Rebel cells — double "
            "ledgers that survived Palpatine's fall. [Fennec Shand](characters/fennec-shand) and "
            "[Boba Fett](characters/boba-fett) frequently cited Vigo contract law in bounty disputes."
        ),
        "significance": (
            "The Vigo Council explains Black Sun's longevity — territorial franchise with arbitration "
            "instead of charismatic single rulers.\n\n"
            "Mustafar's pairing with Council summits links crime governance to volcanic industrial horror."
        ),
        "notableEvents": [
            "Vigo territorial quotas formalized across Rim sectors",
            "Mustafar fortress summits become Council tradition",
            "Maul's Shadow Collective purges resistant Vigos",
            "Imperial double-contract era with ISB informants",
            "Post-Endor succession crises among Vigo heirs",
        ],
        "majorCharacters": [
            sith("Darth Maul", "sith/darth-maul"),
            jedi("Obi-Wan Kenobi", "jedi/obi-wan-kenobi"),
            char("Boba Fett", "characters/boba-fett"),
            char("Fennec Shand", "characters/fennec-shand"),
        ],
        "keyFactions": [faction("Black Sun", "organizations/black-sun")],
        "affiliations": [
            "Crime Families hub",
            "Mustafar fortress-banks",
            "Assassin retainer guilds",
        ],
        "timeline": [
            {"era": "Old Republic", "event": "Vigo council system codified"},
            {"era": "Clone Wars", "event": "Maul challenges Council independence"},
            {"era": "Imperial Era", "event": "Council operates ISB double contracts"},
            {"era": "New Republic Era", "event": "Vigo succession wars reshape territories"},
        ],
        "films": CLONE_WARS_FILMS,
        "series": CLONE_WARS_SERIES + ["Star Wars: The Mandalorian"],
    },
    "trade-federation-directorate": {
        "dateRange": "c. 350 BBY – 19 BBY",
        "headOfState": head("Nute Gunray", "characters/nute-gunray"),
        "headOfGovernment": head("Neimoidian Trade Viceroy council"),
        "planets": [
            planet("Cato Neimoidia", "planet/cato-neimoidia"),
            planet("Naboo", "naboo"),
        ],
        "overview": (
            "The Trade Federation Directorate is the Neimoidian board commanding Trade Federation "
            "blockades, battle droid armies, and occupation administrations — most infamously during "
            "the Naboo invasion led by [Nute Gunray](characters/nute-gunray). The Directorate "
            "claims corporate sovereignty while deploying military assets that rival planetary "
            "defense forces.\n\n"
            "See also the Trade Federation faction profile for full wartime fleet history."
        ),
        "history": (
            "Neimoidian merchant lords built the Directorate to manage droid manufacturing subsidiaries "
            "and shipping cartels from Cato Neimoidia vault-world palaces. [Nute Gunray](characters/nute-gunray) "
            "and [Rune Haako](characters/nute-gunray) — titles contested in archives — orchestrated "
            "the Naboo blockade that forced [Padmé Amidala](characters/padme-amidala) to seek "
            "Republic intervention.\n\n"
            "[Darth Sidious](sith/darth-sidious) manipulated the Directorate as early Separatist "
            "muscle, ensuring battle droid output continued through [Geonosis](planet/geonosis) "
            "foundries. [Count Dooku](sith/darth-tyranus) later seated Gunray on the Separatist Council.\n\n"
            "[Anakin Skywalker](jedi/anakin-skywalker) and [Obi-Wan Kenobi](jedi/obi-wan-kenobi) "
            "fought Federation droid armies across the Clone Wars until the Directorate leadership "
            "died on Mustafar with other Separatist executives."
        ),
        "significance": (
            "The Trade Federation Directorate is the archetype of corporate belligerence — blockade "
            "as policy, droids as occupation troops.\n\n"
            "Naboo's invasion remains mandatory study in Republic military academies."
        ),
        "notableEvents": [
            "Directorate blockades Naboo trade lanes",
            "Battle droid army occupies Theed",
            "Padmé Amidala retakes Naboo with Gungan alliance",
            "Directorate joins Separatist Council on Geonosis",
            "Leadership massacred on Mustafar after war's end",
        ],
        "majorCharacters": [
            char("Nute Gunray", "characters/nute-gunray"),
            char("Padmé Amidala", "characters/padme-amidala"),
            char("Jar Jar Binks", "characters/jar-jar-binks"),
            char("Captain Panaka", "characters/captain-panaka"),
            jedi("Obi-Wan Kenobi", "jedi/obi-wan-kenobi"),
            jedi("Anakin Skywalker", "jedi/anakin-skywalker"),
            sith("Darth Sidious", "sith/darth-sidious"),
            sith("Darth Tyranus", "sith/darth-tyranus"),
        ],
        "keyFactions": [
            faction("Trade Federation", "factions/trade-federation"),
            faction("Confederacy of Independent Systems", "factions/confederacy"),
        ],
        "affiliations": [
            "Corporate Blocs hub",
            "Neimoidian vault-world elites",
            "Battle droid manufacturing subsidiaries",
        ],
        "timeline": [
            {"era": "Old Republic", "event": "Directorate chartered on Cato Neimoidia"},
            {"era": "Separatist Crisis", "event": "Naboo blockade triggers Senate crisis"},
            {"era": "Clone Wars", "event": "Directorate holds Separatist Council seat"},
            {"era": "Imperial Era", "event": "Directorate dissolved after Mustafar massacre"},
        ],
        "films": [
            "Star Wars: Episode I — The Phantom Menace",
            *CLONE_WARS_FILMS,
        ],
        "series": CLONE_WARS_SERIES,
    },
    "intergalactic-banking-holding": {
        "dateRange": "c. 25,000 BBY – present",
        "headOfState": head("Muun executive chair"),
        "headOfGovernment": head("IGBC interlock directorate"),
        "planets": [
            planet("Muunilinst", "planet/muunilinst"),
            planet("Scipio", "planet/scipio"),
        ],
        "overview": (
            "The InterGalactic Banking Holding is the parent company consolidating IGBC assets, war "
            "loans, and corporate charter stakes across the galaxy. Where the Banking Clan operates "
            "public vaults, the Holding moves subsidiary shells, shadow dividends, and Separatist "
            "payroll routes through boards that never appear on HoloNet finance shows.\n\n"
            "Muun executives treat galactic war as a liquidity event — an opportunity to refinance "
            "both belligerents."
        ),
        "history": (
            "Holding company structures let Muun financiers survive political reversals: when "
            "public Clan reputations collapsed, Holding boards reissued assets under new logos. "
            "[San Hill](characters/nute-gunray) era Separatist finance flowed through Holding "
            "pipelines even as Republic ambassadors dined with Clan lobbyists on Coruscant.\n\n"
            "[Rush Clovis](characters/rush-clovis) infiltrated Scipio banking citadels exposing "
            "how Holding votes influenced Republic treasury policy — a scandal that nearly "
            "toppled [Padmé Amidala](characters/padme-amidala)'s coalition allies. "
            "[Anakin Skywalker](jedi/anakin-skywalker) and [Obi-Wan Kenobi](jedi/obi-wan-kenobi) "
            "fought Separatist forces on Scipio and Muunilinst where Holding towers doubled as "
            "fortified vault complexes.\n\n"
            "Imperial absorption merged Holding ledgers into state banks, yet Muun advisors "
            "continued to manage Moff debt and syndicate laundering into the New Republic era."
        ),
        "significance": (
            "The Holding explains IGBC resilience — wars end, logos change, Muun spreadsheets persist.\n\n"
            "Scipio and Muunilinst campaigns link Jedi military history to corporate finance directly."
        ),
        "notableEvents": [
            "Holding company consolidates IGBC subsidiary charters",
            "Separatist payroll routed through shadow boards",
            "Rush Clovis exposes Scipio corruption scandal",
            "Battles of Muunilinst and Scipio threaten Holding vaults",
            "Imperial nationalization merges Holding into state banks",
        ],
        "majorCharacters": [
            char("Rush Clovis", "characters/rush-clovis"),
            char("Padmé Amidala", "characters/padme-amidala"),
            jedi("Anakin Skywalker", "jedi/anakin-skywalker"),
            jedi("Obi-Wan Kenobi", "jedi/obi-wan-kenobi"),
            char("Nute Gunray", "characters/nute-gunray"),
        ],
        "keyFactions": [
            faction("Confederacy of Independent Systems", "factions/confederacy"),
            org("InterGalactic Banking Clan", "organizations/intergalactic-banking-clan"),
        ],
        "affiliations": [
            "Corporate Blocs hub",
            "Muun vault interlocks",
            "Scipio banking citadels",
        ],
        "timeline": [
            {"era": "Old Republic", "event": "Holding structure shields Muun assets from political risk"},
            {"era": "Clone Wars", "event": "Shadow boards finance Separatist droid payrolls"},
            {"era": "Clone Wars", "event": "Scipio scandal exposes Republic corruption ties"},
            {"era": "Imperial Era", "event": "Holding absorbed into Imperial treasury apparatus"},
        ],
        "films": CLONE_WARS_FILMS,
        "series": CLONE_WARS_SERIES,
    },
}
