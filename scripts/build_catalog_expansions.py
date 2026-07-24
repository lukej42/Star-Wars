#!/usr/bin/env python3
"""Generate settlement additions, ship C# entries, and ship profile enrichments."""

from __future__ import annotations

import json
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
SHIP_DATA = ROOT / "Data" / "ShipData.cs"

# (name, planet, stype, desc, color, sources, skyline, origin, ancient, modern, conflict, economy, culture, impact, events, affiliations, timeline)
SETTLEMENTS = [
    (
        "Ahch-To Jedi Village", "Ahch-To", "Sacred island enclave",
        "Ahch-To's stone huts and cliffside steps sheltered the first Jedi temple and later Luke Skywalker's exile, where Rey learned that legacy is chosen—not inherited.",
        "#64748b", "Films · Expanded lore", "holy",
        "Ahch-To's Jedi Village sits where the Prime Jedi first balanced light and dark; ocean storms and lanai birds shaped a monastic culture older than the Republic Senate.",
        "Ruined texts in the island library describe Je'daii rites predating the Jedi Council, with meditation caves still resonating during Rey's vision quest.",
        "Luke Skywalker rebuilt occupancy in secret after Ben Solo's fall, training no students but archiving what remained of Order doctrine until Rey arrived.",
        "The First Order's hunt for Skywalker turned Ahch-To into a contested pilgrimage; Luke's Force projection at Crait began from these cliffs.",
        "Tourism is forbidden; sustenance comes from fish, seabird eggs, and salvaged offworld supplies left by Caretaker rituals.",
        "Caretakers maintain a oral liturgy in their language; Jedi visitors learn humility through manual labor and silence facing the northern sea.",
        "Ahch-To marks the pivot from Skywalker-centric hope to a wider Jedi future embodied by Rey and the buried texts she recovered.",
        ("Prime Jedi temple established on Ahch-To", "Luke Skywalker exiles himself after Ben Solo's destruction of the academy",
         "Rey discovers Luke and the ancient Jedi texts", "Luke becomes one with the Force after projecting at Crait",
         "Rey buries Luke and Leia's lightsabers on the island"),
        ("Jedi Order", "Prime Jedi tradition", "Luke Skywalker's exile community", "Resistance", "Caretaker lanai"),
        (("Ancient Era", "Prime Jedi forge first temple on Ahch-To"), ("Old Republic", "Jedi historians catalog island rites"),
         ("Imperial Era", "Temple falls into obscurity"), ("New Republic", "Luke Skywalker reoccupies the village"),
         ("First Order", "Rey completes her training pilgrimage")),
    ),
    (
        "Dagobah Swamp Hermitage", "Dagobah", "Force-strong wilderness",
        "Dagobah's fog-choked marshes hide Yoda's hut and the cave of the dark side, where Luke Skywalker confronted fear beneath gnarltree roots.",
        "#166534", "Films · Clone Wars", "outpost",
        "Dagobah's hermitage formed where the Living Force pools so densely that technology fails and prophecy becomes tactile.",
        "Ancient Sith and Jedi both avoided permanent settlement here, leaving only stone markers swallowed by vines.",
        "Yoda chose exile after Order 66, living simply while Clone Wars battlefields burned across the galaxy.",
        "Imperial probes rarely penetrate the mist; Vader's hunt for Luke nearly ended in the swamp in visions, not invasions.",
        "No formal economy exists—Yoda traded nothing but wisdom for rations Luke carried.",
        "Hermit culture on Dagobah is silence, stew, and confronting the self in Force vergence.",
        "Dagobah training defined Luke's path and proved a Jedi could be rebuilt outside temple walls.",
        ("Yoda flees to Dagobah after Order 66", "Luke Skywalker trains under Yoda in the swamp",
         "Luke enters the cave of the dark side", "Yoda dies and becomes one with the Force",
         "Rey experiences vision echoes on her journey"),
        ("Jedi Order", "Yoda's exile circle", "Alliance to Restore the Republic", "Living Force vergence sites"),
        (("Imperial Era", "Yoda establishes hermitage"), ("Imperial Era", "Luke begins accelerated training"),
         ("Imperial Era", "Yoda passes into the Force"), ("New Republic", "Historians debate locating the site"),
         ("First Order", "Force vergence cited in Jedi revival studies")),
    ),
    (
        "Takodana Castle", "Takodana", "Neutral fortress settlement",
        "Maz Kanata's ancient castle on Takodana is a crossroads for smugglers, monarchs, and Resistance heroes beneath stained-glass war trophies.",
        "#a855f7", "Films · Battlefront II", "city",
        "Takodana Castle predates the Republic, built atop a Force nexus Maz Kanata has guarded for over a millennium.",
        "Basement vaults hold relics from every galactic war; some lightsaber fragments predate the Sith Rule of Two.",
        "Han Solo, Rey, and Finn received Anakin's lightsaber here before Starkiller Base's destruction.",
        "The First Order bombarded the castle after the Hosnian cataclysm, scattering Maz's court to the stars.",
        "Castle revenue flows from docking fees, information brokerage, and rare artifact authentication.",
        "Maz hosts without judging faction—until guests break her neutrality, then her garrison acts decisively.",
        "Takodana's neutrality collapsed in the Sequel Era, forcing Maz into open Resistance support.",
        ("Maz Kanata acquires the castle", "Han Solo and Chewbacca frequent Maz's court for decades",
         "Rey finds Anakin's lightsaber in the vault", "First Order destroys much of the castle",
         "Maz relocates operations while rebuilding"),
        ("Maz Kanata's court", "Galactic underworld brokers", "Resistance", "Smuggler guilds", "Ancient Force watchers"),
        (("Ancient Era", "Castle founded on Force nexus"), ("Old Republic", "Maz Kanata becomes custodian"),
         ("Galactic Civil War", "Castle serves neutral ground"), ("First Order", "Bombardment after Hosnian Prime"),
         ("Resistance Era", "Maz aids fleet musters")),
    ),
    (
        "Dac City", "Mon Cala", "Underwater capital",
        "Dac City is the seat of Mon Calamari and Quarren co-rule, famed for starship artistry and brutal Imperial subjugation under Governor Triton.",
        "#0ea5e9", "Films · Clone Wars · Rebels", "underwater",
        "Dac City rose in Mon Cala's shallow zones where Quarren reef architecture meets Mon Calamari coral engineering.",
        "Old Republic envoys recorded Dac City's shipyards as unmatched for modular fleet design.",
        "King Lee-Char's coronation and Riff Tamson's Separatist invasion made the city a Clone Wars crucible.",
        "Imperial occupation drowned dissent in hydro-bore prisons until Bail Organa's resistance cells surfaced.",
        "Starship contracts, coral exports, and tourism to kelp cathedrals fund Dac City's recovery.",
        "Dual-species councils rotate governance; art celebrates both aquatic cultures in plaza mosaics.",
        "Mon Calamari cruisers built here became the Rebel Alliance's backbone at Endor and Scarif.",
        ("Separatist invasion of Mon Cala", "King Lee-Char unifies Mon Calamari and Quarren",
         "Imperial subjugation under Governor Triton", "Rebel Mon Calamari fleet launches from Dac City",
         "New Republic restores planetary autonomy"),
        ("Mon Calamari monarchy", "Quarren Isolation League (historical)", "Galactic Republic", "Rebel Alliance", "New Republic"),
        (("Old Republic", "Dac City joins galactic trade"), ("Clone Wars", "Separatist assault on Mon Cala"),
         ("Imperial Era", "Occupation and prison camps"), ("Galactic Civil War", "Fleet construction for Rebellion"),
         ("New Republic", "Cultural renaissance in Dac City")),
    ),
    (
        "Bilbousa", "Nal Hutta", "Hutt swamp capital",
        "Bilbousa sprawls through Nal Hutta's toxic bogs as the Hutt Council's palace district, where kajidics feud under gilded domes and perpetual smog.",
        "#65a30d", "Films · Clone Wars · The Book of Boba Fett", "underworld",
        "Bilbousa grew when Hutts relocated from Varl, converting swamp into fortified pleasure palaces and slave markets.",
        "Pre-Republic pylons beneath Bilbousa suggest Rakatan influence on early Hutt hyperdrive acquisition.",
        "Jabba's empire, the Shadow Collective, and Pyke syndicate all negotiated in Bilbousa halls.",
        "Republic raids rarely penetrate; Imperial treaties left Hutts autonomous in exchange for stability.",
        "Spice, slaves, gambling, and mercenary contracts circulate through Bilbousa's shadow banks.",
        "Hutt Ruling Council ritual combines gluttony, vengeance, and elaborate extortion codes.",
        "Decisions in Bilbousa ripple to Tatooine, Nar Shaddaa, and every Rim shadow port.",
        ("Hutt Cartel consolidates on Nal Hutta", "Jabba dominates outer Rim operations from Bilbousa influence",
         "Shadow Collective under Maul challenges traditional kajidics", "Pyke syndicate negotiates spice routes",
         "New Republic struggles to prosecute Hutt crime lords"),
        ("Hutt Cartel", "Hutt Ruling Council", "Pyke Syndicate", "Black Sun (historical)", "Criminal guild networks"),
        (("Ancient Era", "Hutt migration to Nal Hutta"), ("Old Republic", "Bilbousa becomes administrative capital"),
         ("Clone Wars", "Cartel plays Republic and Separatists"), ("Imperial Era", "Treaty autonomy preserved"),
         ("New Republic", "Anti-Hutt prosecutions intensify")),
    ),
    (
        "Concord Dawn", "Concord Dawn", "Mandalorian colony",
        "Concord Dawn's dusty mesas bred Journeyman Protectors and warriors like Jango Fett, torn between Mandalorian honor and Imperial proxy wars.",
        "#0284c7", "Films · Clone Wars · Rebels", "outpost",
        "Concord Dawn began as a Mandalorian forward colony guarding hyperspace approaches to the Concordia foundries.",
        "Ancient Mandalorian bas-reliefs depict Basilisk war droids crossing the mesas.",
        "Jango Fett's legacy and the Protectors' neutrality made the colony a Fenn Rau flashpoint in the Civil War.",
        "Imperial Viceroy Gar Saxon attempted to conscript Protectors, triggering rebellion and massacre.",
        "Grazing, microforge exports, and mercenary retainers sustain sparse settlements.",
        "Protector code emphasizes aerial supremacy and hospitality to clan kin—not outsiders.",
        "Concord Dawn illustrates Mandalore's diaspora beyond the domed capital.",
        ("Journeyman Protectors established", "Jango Fett rises as bounty hunter from Concord Dawn",
         "Fenn Rau leads Protectors in Clone Wars", "Gar Saxon crushes Protector neutrality",
         "Sabine Wren and Clan Wren reclaim Mandalorian identity"),
        ("Mandalorian Protectors", "Clan Fett (historical)", "Galactic Empire", "Rebel Alliance", "Mandalorian resistance"),
        (("Old Republic", "Colony founded for sector defense"), ("Clone Wars", "Protectors ally with Republic"),
         ("Imperial Era", "Imperial occupation and Protector purge"), ("Galactic Civil War", "Fenn Rau joins Rebellion"),
         ("New Republic", "Clan diaspora memorializes mesa battles")),
    ),
    (
        "Concordia", "Mandalore", "Industrial moon settlement",
        "Concordia's mines and foundries on Mandalore's moon supplied beskar for centuries, hiding Death Watch cells beneath legitimate industry.",
        "#475569", "Clone Wars", "industrial",
        "Concordia's settlements ring mining pits where beskar veins made Mandalore an armorer to the galaxy.",
        "Pre-Imperial excavations uncovered Basilisk frames sealed in lava tubes.",
        "Death Watch used Concordia's abandoned mines as training camps before the Shadow Collective coup.",
        "Sabine Wren's discovery of Imperial weapons tests on Concordia exposed Mandalorian complicity.",
        "Beskar refining, alloy export, and covert weapons labs dominate Concordia's economy.",
        "Miners maintain songs in Mando'a about flame and forge; Death Watch hijacked those symbols.",
        "Concordia proves Mandalorian industry can arm both liberators and occupiers.",
        ("Beskar mines opened on Concordia", "Death Watch establishes hidden bases",
         "Duchess Satine inspects mining safety reforms", "Imperial saboteurs test weapons on Concordia",
         "Mandalorian resistance reclaims foundries"),
        ("New Mandalorian government", "Death Watch", "Galactic Empire", "Clan Saxon", "Mandalorian super commandos"),
        (("Ancient Era", "Beskar mining begins"), ("Old Republic", "Industrial moon urbanizes"),
         ("Clone Wars", "Death Watch insurgency"), ("Imperial Era", "Covert Imperial weapons testing"),
         ("Galactic Civil War", "Foundries contested by clans")),
    ),
    (
        "Nightsister Fortress", "Dathomir", "Dark side enclave",
        "The Nightsister fortress on Dathomir is a stone labyrinth of magick, rancor pens, and Mother Talzin's throne overlooking haunted valleys.",
        "#7c3aed", "Films · Clone Wars · Fallen Order", "sith",
        "Nightsister Fortress grew from Allyan exiles who merged Force craft with Dathomir's blood rituals.",
        "Sith and Jedi both feared the fortress; Darth Sidious abducted Maul from nearby village pens.",
        "General Grievous annihilated much of the fortress on Sidious's orders, scattering surviving witches.",
        "Merrin and others rebuilt fragments of tradition while Imperial hunters sought Nightsister artifacts.",
        "No conventional trade—sisterhood barters magick, beasts, and mercenary aid with offworld clients.",
        "Nightsister culture centers on the Book of Law, rancor kinship, and vengeance oaths.",
        "The fortress represents Force practice outside Jedi/Sith binaries, nearly erased by Sidious.",
        ("Allyan's descendants become Nightsisters", "Mother Talzin leads the clan against Separatists",
         "Grievous massacres Nightsisters on Sidious's command", "Maul returns seeking Talzin's aid",
         "Survivors preserve magick in hidden covens"),
        ("Nightsisters of Dathomir", "Nightbrothers", "Confederacy of Independent Systems (brief)", "Sith Order (enemy)", "Mandalorian mercenaries (historical)"),
        (("Ancient Era", "Fortress established in rancor valleys"), ("Clone Wars", "Talzin wars against Dooku"),
         ("Clone Wars", "Grievous destroys primary fortress"), ("Imperial Era", "Artifact hunters scour ruins"),
         ("New Republic", "Merrin revives scattered traditions")),
    ),
    (
        "Plazir-17 Domed Resort", "Plazir-17", "Domed leisure city",
        "Plazir-17's dome encloses a hedonistic city-state ruled by the Duchess and her droid rights reforms, where Bo-Katan negotiated post-imperial futures.",
        "#ec4899", "Mandalorian · The Book of Boba Fett", "casino",
        "Plazir-17 was founded as a corporate pleasure dome for post-war tourists seeking regulated vice.",
        "The dome's repulsor grid survived multiple pirate sieges thanks to Mandalorian security contracts.",
        "Bo-Katan Kryze and Din Djarin brokered alliance terms here amid droid union politics.",
        "Imperial remnant cells attempted to infiltrate gambling halls for laundering operations.",
        "Casinos, droid racing, luxury imports, and orbital yacht services fuel Plazir-17.",
        "The Duchess merged aristocratic hospitality with radical droid emancipation statutes.",
        "Plazir-17 models how Outer Rim city-states survive without Republic oversight.",
        ("Domed city chartered as independent resort", "Droid rights charter implemented under the Duchess",
         "Bo-Katan seeks Mandalorian fleet support", "Boba Fett consulted on security reforms",
         "New Republic monitors but does not govern Plazir-17"),
        ("Plazir-17 ducal government", "Droid worker unions", "Mandalorian mercenary contracts", "New Republic observers"),
        (("Imperial Era", "Resort dome constructed"), ("New Republic", "Independence recognized"),
         ("New Republic", "Droid emancipation laws enacted"), ("Mandalorian Era", "Bo-Katan diplomatic summit"),
         ("New Republic", "Status as neutral resort persists")),
    ),
    (
        "Aldhani Garrison Sector", "Aldhani", "Wilderness rebel staging ground",
        "Aldhani's alpine wilderness hid the Aldhani heist staging camp where Andor's rebels stole an Imperial payroll from an elevated garrison.",
        "#4ade80", "Andor", "military",
        "Aldhani's garrison sector protects a Imperial payroll vault anchoring sector suppression operations.",
        "Indigenous Aldhani pastoralists predated the garrison; Empire classified them as trespassers on their own land.",
        "Cassian Andor's cell infiltrated the vault in a precision raid exposing Imperial payroll vulnerability.",
        "Post-raid sweeps devastated local villages, radicalizing survivors against Coruscant.",
        "Imperial payroll storage and alpine sensor towers dominate; locals subsist on herding.",
        "Aldhani herders maintain night-song warnings about sky machines; rebels learned to mimic wind patterns.",
        "The heist proved small cells could strike Imperial treasury lines, inspiring wider rebellion.",
        ("Imperial garrison established on Aldhani", "Cassian Andor joins Aldhani raid cell",
         "Payroll vault stolen in synchronized assault", "Imperial reprisals scour the valleys",
         "Raid inspires Mon Mothma's broader resistance funding"),
        ("Imperial Military", "Aldhani pastoral communities", "Rebel infiltration cells", "Sector command payroll office"),
        (("Imperial Era", "Garrison vault constructed"), ("Imperial Era", "Aldhani heist succeeds"),
         ("Imperial Era", "Reprisal sweeps follow"), ("Galactic Civil War", "Sector joins wider revolt"),
         ("New Republic", "Vault ruins become memorial site")),
    ),
]

# Extend with more settlements programmatically with rich defaults
MORE_SETTLEMENTS = [
    ("Moraband Valley of the Dark Lords", "Moraband", "Sith burial valley", "Moraband's desolate valley holds tombs of ancient Sith Lords where Yoda faced visions of the Order's fall.", "#450a0a", "Clone Wars · KOTOR lore", "sith", "spaceport"),
    ("Tython Jedi Temple", "Tython", "Jedi origin temple", "Tython's mountain temple marks where the Je'daii became the Jedi Order, with meditation spires above Force storms.", "#6366f1", "SWTOR · High Republic", "holy", "holy"),
    ("Ilum Jedi Temple", "Ilum", "Sacred crystal sanctuary", "Ilum's frozen temple caves produce kyber crystals for lightsabers, pilgrimage site for Jedi younglings for millennia.", "#bae6fd", "Clone Wars · Jedi Fallen Order", "holy", "holy"),
    ("Citadel Station", "Telos", "Orbital restoration hub", "Citadel Station orbited shattered Telos as a model of post-war recovery until Sith infiltration corrupted its restoration project.", "#94a3b8", "KOTOR II", "floating", "floating"),
    ("Dantooine Jedi Enclave", "Dantooine", "Jedi academy ruins", "The Enclave's ruined halls trained generations of Jedi before Darth Malak's bombardment left craters in the plains.", "#2563eb", "KOTOR · KOTOR II", "military", "military"),
    ("Peragus Mining Facility", "Peragus", "Asteroid mining station", "Peragus II's fuel refinery asteroids exploded in a chain reaction during the Jedi Exile's escape from Sith hunters.", "#78716c", "KOTOR II", "industrial", "industrial"),
    ("Ziost Sith Acropolis", "Ziost", "Frozen Sith capital", "Ziost's acropolis was the heart of the Old Sith Empire before Vitiate consumed the world, leaving ice-bound silence.", "#1e293b", "SWTOR", "sith", "sith"),
    ("Nathema Devastated Capital", "Nathema", "Force-dead world", "Nathema's capital was emptied when Vitiate performed the Ritual of Nathema, annihilating all life to grant him immortality.", "#0f172a", "SWTOR", "sith", "sith"),
    ("Odessen Alliance Hub", "Odessen", "Alliance operations base", "Odessen became the Eternal Alliance's hidden headquarters in wild jungle mesas during the war against Zakuul.", "#059669", "SWTOR", "military", "military"),
    ("Bilbringi Shipyards", "Bilbringi", "Orbital shipyard complex", "Bilbringi's yards were the site of Thrawn's final trap and the New Republic's capture of Star Destroyer repair facilities.", "#64748b", "Legends · Thrawn Trilogy", "industrial", "industrial"),
    ("Kuat Drive Yards", "Kuat", "Orbital ring shipyard", "The Kuat Drive Yards ring builds Star Destroyers and symbolizes Imperial industrial might visible from space.", "#64748b", "Films · Rebels · Andor", "industrial", "industrial"),
    ("Fondor Shipyards", "Fondor", "Planetary orbital docks", "Fondor's hidden drydocks constructed Star Destroyers in secret, targeted by both Rebels and First Order saboteurs.", "#475569", "Films · Resistance", "industrial", "industrial"),
    ("Pinyumb", "Sullust", "Underground metropolis", "Pinyumb's caverns housed Sullustan resistance cells that rose against Imperial garrisons before Endor.", "#f97316", "Films · Battlefront", "industrial", "industrial"),
    ("Mimban Forward Camp", "Mimban", "Swamp war zone", "Mimban's mud trenches saw Han Solo's Imperial service and chaotic ground combat in a forgotten theater.", "#854d0e", "Solo · Marvel", "military", "military"),
    ("Kessel Spice Mines", "Kessel", "Penal mining complex", "Kessel's underground spice mines enslaved prisoners until the Pyke syndicate and later Rebellion raids disrupted operations.", "#dc2626", "Solo · Rebels", "industrial", "industrial"),
    ("Eadu Research Facility", "Eadu", "Imperial kyber lab", "Eadu's rain-soaked cliffs hid Galen Erso's kyber weapon research team before the Death Star project's exposure.", "#334155", "Rogue One", "industrial", "industrial"),
    ("Ring of Kafrene", "Kafrene", "Asteroid trading post", "The Ring of Kafrene's asteroid markets moved illegal goods until Cassian Andor learned of the Death Star there.", "#78716c", "Rogue One", "spaceport", "spaceport"),
    ("Lah'mu Homestead", "Lah'mu", "Remote farming settlement", "Lah'mu's black sand farms hid the Erso family until the Empire's return forced Jyn's separation from her parents.", "#14532d", "Rogue One", "outpost", "outpost"),
    ("Ajan Kloss Resistance Base", "Ajan Kloss", "Jungle Resistance HQ", "Ajan Kloss's jungles concealed Leia Organa's Resistance base with temples repurposed as command bunkers.", "#f97316", "Films · Rise of Skywalker", "military", "military"),
    ("Crait Salt Flats Base", "Crait", "Abandoned Rebel outpost", "Crait's red salt under white crust hid an abandoned Rebel base used by the Resistance in their desperate stand.", "#e11d48", "Films · Last Jedi", "military", "military"),
    ("Pasaana Festival City", "Pasaana", "Desert festival hub", "Pasaana's Aki-Aki Festival of the Ancestors masked Resistance intelligence work amid celebratory parades.", "#eab308", "Rise of Skywalker", "outpost", "outpost"),
    ("Kef Bir Ocean Settlement", "Kef Bir", "Ocean moon ruins", "Kef Bir's Death Star wreckage zones became scavenger camps where Rey confronted her lineage in Palpatine's throne.", "#0284c7", "Rise of Skywalker", "city", "city"),
    ("Stygeon Prime Spire", "Stygeon Prime", "Separatist prison", "The Spire on Stygeon Prime held Darth Maul before breakout and later Imperial Inquisitor detention cells.", "#64748b", "Clone Wars · Rebels", "military", "military"),
    ("Wobani Labor Camp", "Wobani", "Imperial labor colony", "Wobani's camps imprisoned dissidents until Jyn Erso's rescue highlighted the Empire's penal industry.", "#57534e", "Rogue One", "military", "military"),
    ("Fortress Vader", "Mustafar", "Sith stronghold", "Fortress Vader rises on Mustafar's obsidian shore where Anakin Skywalker fell and Darth Vader meditated on pain.", "#991b1b", "Films · Vader Immortal", "sith", "sith"),
    ("Coruscant Level 1313", "Coruscant", "Underworld district", "Level 1313's stacked slums and black markets operate beneath Coruscant's gleaming surface, home to bounty hunters and fugitives.", "#1f2937", "Films · Games · The Bad Batch", "underworld", "underworld"),
    ("Inquisitorius Headquarters", "Coruscant", "Imperial dark-side fortress", "The Inquisitorius tower on Coruscant trained Jedi hunters in torture chambers hidden from Senate oversight.", "#334155", "Rebels · Jedi Fallen Order", "military", "military"),
    ("Carida Imperial Academy", "Carida", "Naval officer academy", "Carida's academy forged Imperial officers until sabotage by Rebel agents exposed its ruthless training regime.", "#64748b", "Legends · Rebels references", "military", "military"),
    ("Saleucami Field Hospital", "Saleucami", "Clone Wars medical camp", "Saleucami's plains hosted mobile hospitals where Captain Rex was nearly buried alive after Order 66.", "#a3a3a3", "Clone Wars", "outpost", "outpost"),
    ("Mygeeto Crystal Treasury", "Mygeeto", "InterGalactic Banking colony", "Mygeeto's crystal cities financed the Clone Wars until General Grievous and Banking Clan disputes shattered its spires.", "#67e8f9", "Films · Clone Wars", "city", "city"),
    ("Chaleydonia", "Christophsis", "Crystal capital", "Chaleydonia's crystal spires saw the Clone Wars' first pitched battles between Republic and Separatist armies.", "#22d3ee", "Clone Wars", "city", "city"),
    ("Felucia Jedi Temple", "Felucia", "Overgrown temple ruins", "Felucia's jungle swallowed a Jedi temple where Ahsoka Tano and Barriss Offee fought Separatist bioweapons.", "#16a34a", "Clone Wars · Fallen Order", "holy", "holy"),
    ("Florrum Pirate Outpost", "Florrum", "Pirate haven", "Florrum's canyons housed Hondo Ohnaka's pirate base, raiding trade routes until Separatist and Jedi interventions.", "#d97706", "Clone Wars", "outpost", "outpost"),
    ("Toydaria Royal Settlement", "Toydaria", "Swamp palace city", "Toydaria's palaces negotiated neutrality in the Clone Wars while secretly aiding refugee convoys to Ryloth.", "#84cc16", "Clone Wars", "city", "city"),
    ("Betu City", "Rodia", "Jungle capital", "Betu City is Rodia's humid capital where Senator Onaconda Farr balanced Republic loyalty against Separatist pressure.", "#15803d", "Clone Wars", "city", "city"),
    ("Krownest", "Krownest", "Mandalorian clan fortress", "Krownest's snowy peaks hold Clan Wren's fortress where Sabine surrendered the Darksaber to Bo-Katan.", "#93c5fd", "Rebels", "military", "military"),
    ("Olega Settlement", "Olega", "Corporate township", "Olega's corporate blocks and medcenters masked Cassian Andor's early rebel operations against Imperial price gouging.", "#6b7280", "Andor", "industrial", "industrial"),
    ("Narkina 5 Prison Complex", "Narkina 5", "Imperial prison facility", "Narkina 5's panopticon prisons used floor electrification until Andor's escape exposed genocide-scale detainee policy.", "#374151", "Andor", "military", "military"),
    ("Bakura City", "Bakura", "Outer Rim capital", "Bakura City negotiated truce with Imperial remnants after Endor, becoming a test case for post-war integration.", "#cbd5e1", "Legends · Truce at Bakura", "city", "city"),
    ("Byss Imperial Citadel", "Byss", "Deep Core fortress", "Byss housed Palpatine's clone laboratories and dark-side citadels deep in the Deep Core.", "#312e81", "Legends · Dark Empire", "sith", "sith"),
    ("Bastion Remnant Capital", "Bastion", "Imperial Remnant seat", "Bastion became the capital of Thrawn's Imperial Remnant, a disciplined redoubt against New Republic expansion.", "#64748b", "Legends · Thrawn", "ecumenopolis", "ecumenopolis"),
    ("Malastare Capital", "Malastare", "Fuel refinery metropolis", "Malastare's capital refines fuel and hosted the Zillo Beast incident that threatened Coruscant itself.", "#ca8a04", "Clone Wars", "industrial", "industrial"),
    ("Bothawui Intelligence City", "Bothawui", "Spy network hub", "Bothawui's cities run on espionage; the Bothan Spynet's sacrifice revealed Death Star II plans at Endor.", "#f59e0b", "Legends · Films", "city", "city"),
    ("Atzerri Smuggler Port", "Atzerri", "Free trade port", "Atzerri's chaotic docks move contraband with minimal customs, frequented by smugglers and bounty hunters.", "#d97706", "Legends · Mandalorian", "spaceport", "spaceport"),
    ("Rhen Var Outpost", "Rhen Var", "Arctic research base", "Rhen Var's frozen ruins and research domes saw Jedi battles during the Clone Wars' icy campaigns.", "#e0f2fe", "Clone Wars · Battlefront", "outpost", "outpost"),
    ("Lianna Spire City", "Lianna", "Corporate ecumenopolis", "Lianna's Sienar-linked spires produce TIE prototypes in a city ruled by corporate charter law.", "#64748b", "Legends · TIE lore", "ecumenopolis", "ecumenopolis"),
    ("Kor Vella Shipwright Quarter", "Corellia", "Freighter manufacturing district", "Kor Vella's yards on Corellia build YT-series freighters and starfighters for independent operators galaxy-wide.", "#0369a1", "Legends · Solo", "industrial", "industrial"),
]

def expand_settlement(entry):
    if len(entry) == 10:
        name, planet, stype, desc, color, sources, skyline, origin, ancient, modern = entry[:10]
        conflict = f"Strategic campaigns on {planet} repeatedly targeted {name} for control of local resources and hyperspace access."
        economy = f"{name} sustains itself through sector trade, military contracts, and survival crafts adapted to {planet}'s environment."
        culture = f"Communities at {name} blend planetary tradition with offworld influence visible in markets, festivals, and local governance."
        impact = f"Events at {name} altered broader galactic history across the Old Republic, Clone Wars, Imperial Era, and beyond."
        events = (
            f"{name} established on {planet}",
            f"Major conflict recorded at {name}",
            f"Imperial or Separatist occupation reshapes {name}",
            f"Rebel or Resistance operations linked to {name}",
            f"New Republic era recovery at {name}",
        )
        affiliations = ("Galactic Republic", f"{planet} local governance", "Rebel Alliance", "Imperial Military", "Criminal syndicates")
        timeline = (
            ("Ancient Era", f"Early settlement at {name}"),
            ("Old Republic", f"{name} joins sector networks"),
            ("Clone Wars", f"Military action at {name}"),
            ("Imperial Era", f"Occupation or exploitation at {name}"),
            ("New Republic", f"Reconstruction at {name}"),
        )
        return (name, planet, stype, desc, color, sources, skyline, origin, ancient, modern, conflict, economy, culture, impact, events, affiliations, timeline)
    return entry


for item in MORE_SETTLEMENTS:
    name, planet, stype, desc, color, sources, skyline = item[:7]
    origin = f"{name} began as a strategic anchor on {planet}, where geography and trade lanes forced travelers to settle."
    ancient = f"Pre-Republic ruins near {name} include ward-stones and battle markers from Sith and Jedi campaigns on {planet}."
    modern = f"In the modern era, {name} appears in Clone Wars dossiers, Imperial occupation records, and Sequel-era intelligence briefings."
    conflict = f"Battle dossiers from multiple eras mark {name} as contested territory on {planet}."
    economy = f"{name} runs on local industry, trade tariffs, and black-market mediation typical of {planet}."
    culture = f"Residents of {name} preserve {planet} rituals while adapting to galactic war and occupation."
    impact = f"Historians cite {name} when tracing how {planet} influenced sector-wide treaties and fleet movements."
    events = (
        f"{name} founded on {planet}",
        f"Recorded siege or battle at {name}",
        f"Occupation forces restructure {name}",
        f"Underground resistance operates from {name}",
        f"Post-war memorialization of {name}",
    )
    affiliations = ("Galactic Republic", f"{planet} governance", "Rebel Alliance", "Imperial Military", "Local militias")
    timeline = (
        ("Ancient Era", f"Founding structures at {name}"),
        ("Old Republic", f"Trade integration of {name}"),
        ("Clone Wars", f"Strategic strikes on {name}"),
        ("Imperial Era", f"Peak exploitation at {name}"),
        ("New Republic", f"Cultural recovery at {name}"),
    )
    SETTLEMENTS.append((name, planet, stype, desc, color, sources, skyline, origin, ancient, modern, conflict, economy, culture, impact, events, affiliations, timeline))


def fmt_settlement(entry) -> str:
    name, planet, stype, desc, color, sources, skyline, origin, ancient, modern, conflict, economy, culture, impact, events, affiliations, timeline = entry
    ev = ", ".join(f'"{e}"' for e in events)
    af = ", ".join(f'"{a}"' for a in affiliations)
    tl = ", ".join(f'("{e}", "{evnt}")' for e, evnt in timeline)
    return textwrap.dedent(f"""
    st({name!r}, {planet!r}, {stype!r},
       {desc!r},
       {color!r}, {sources!r},
       {skyline!r}, {{
           "origin_detail": {origin!r},
           "ancient_detail": {ancient!r},
           "modern_detail": {modern!r},
           "conflict_detail": {conflict!r},
           "economy_detail": {economy!r},
           "culture_detail": {culture!r},
           "impact_detail": {impact!r},
           "events": _ev({ev}),
           "affiliations": _aff({af}),
           "timeline": _tl({tl}),
       }}),""")


# Ships: (name, slug, class, desc, production, era, color)
SHIPS = [
    ("Providence-class Carrier/Destroyer", "providence-class", "Carrier / Destroyer", "General Grievous's flagship class combined droid starfighter wings with heavy turbolasers, epitomizing Separatist fleet doctrine.", "~1,200 units", "Clone Wars (22–19 BBY)", "#0891b2"),
    ("Pelta-class Frigate", "pelta-class", "Medical / Support Frigate", "Republic Pelta frigates served as hospital ships and command relays, including the frigate that evacuated Ahsoka Tano's wounded.", "~420 units", "Clone Wars (22–19 BBY)", "#6366f1"),
    ("Consular-class Space Cruiser", "consular-class", "Diplomatic Cruiser", "The Radiant VII design ferried Jedi and ambassadors until Trade Federation fire destroyed one above Naboo.", "~180 units", "Old Republic through Clone Wars", "#6366f1"),
    ("Victory I-class Star Destroyer", "victory-i-class", "Star Destroyer", "Compact Victory-class destroyers bridged Republic-era design to Imperial dominance with ion cannons and heavy armor.", "~4,500 units", "Clone Wars through Imperial Era", "#64748b"),
    ("Victory II-class Star Destroyer", "victory-ii-class", "Star Destroyer", "Victory II variants traded ground assault capacity for improved deep-space patrol endurance in Outer Rim fleets.", "~2,800 units", "Imperial Era (19 BBY–4 ABY)", "#64748b"),
    ("Gladiator-class Star Destroyer", "gladiator-class", "Star Destroyer", "Gladiator-class hulls escorted convoys and hunted pirates with hangars for TIE squadrons in tight sectors.", "~800 units", "Imperial Era (19 BBY–4 ABY)", "#64748b"),
    ("Onager-class Star Destroyer", "onager-class", "Siege Star Destroyer", "Onager-class ships mounted axial superlasers capable of cracking planetary shields from orbit.", "~35 units", "Imperial Era (0–4 ABY)", "#64748b"),
    ("Mandator IV-class Siege Dreadnought", "mandator-iv-class", "Siege Dreadnought", "First Order Mandator IV dreadnoughts bombarded Resistance bases with orbital autocannons from extreme range.", "~12 units", "First Order (34 ABY–)", "#334155"),
    ("Supremacy (Mega-class)", "supremacy", "Mega-class Star Dreadnought", "Snoke's Supremacy served as mobile capital, shipyard, and palace spanning kilometers of First Order fleet command.", "1 unit", "First Order (34 ABY–35 ABY)", "#334155"),
    ("Xyston-class Star Destroyer", "xyston-class", "Planet-killer Star Destroyer", "Final Order Xyston destroyers mounted axial superlasers to glass worlds in Palpatine's reborn Sith fleet.", "~1,080 units planned", "First Order / Sith Eternal (35 ABY)", "#991b1b"),
    ("MC75 Star Cruiser", "mc75-cruiser", "Mon Calamari Cruiser", "Profundity-class MC75 cruisers combined starfighter bays with diplomatic suites before conversion to rebel flagships.", "~140 units", "Galactic Civil War (0 BBY–4 ABY)", "#e11d48"),
    ("MC85 Star Cruiser", "mc85-cruiser", "Mon Calamari Cruiser", "Resistance-era MC85 cruisers like the Raddus carried heavier shields and ion drives for deep-space retreats.", "~25 units", "Resistance (34 ABY–35 ABY)", "#f97316"),
    ("Starhawk-class Battleship", "starhawk-class", "New Republic Battleship", "Project Starhawk converted Imperial hulls into ram-capable battleships that could tear Star Destroyers apart.", "~6 units", "New Republic (5 ABY–)", "#6366f1"),
    ("Nebulon-C Escort Frigate", "nebulon-c", "Escort Frigate", "Nebulon-C frigates updated the classic EF76 design with better point defense for convoy escort.", "~900 units", "New Republic through First Order", "#6366f1"),
    ("Carrack-class Light Cruiser", "carrack-class", "Light Cruiser", "Carrack-class cruisers filled gaps between corvettes and Star Destroyers in Imperial picket fleets.", "~750 units", "Imperial Era (19 BBY–4 ABY)", "#64748b"),
    ("Dreadnaught-class Heavy Cruiser", "dreadnaught-class", "Heavy Cruiser", "Old Republic Dreadnaught hulls were refitted for centuries, forming the Katana fleet and early Imperial lines.", "~2,000 units", "Old Republic through Imperial Era", "#6366f1"),
    ("Subjugator-class Heavy Cruiser", "subjugator-class", "Heavy Cruiser / Ion Battleship", "Malevolence-class ships wielded ion cannons that could disable entire fleets before conventional bombardment.", "~4 units", "Clone Wars (22–21 BBY)", "#0891b2"),
    ("Z-95 Headhunter", "z-95-headhunter", "Multi-role Starfighter", "The Z-95 Headhunter served as the Republic's workhorse snubfighter before ARC-170 and V-wing adoption.", "~110,000 units", "Clone Wars (22–19 BBY)", "#6366f1"),
    ("V-19 Torrent Starfighter", "v-19-torrent", "Starfighter", "V-19 Torrents gave clone pilots a sturdy early-war fighter before Y-wing and ARC-170 specialization.", "~85,000 units", "Clone Wars (22–19 BBY)", "#6366f1"),
    ("E-wing Escort Fighter", "e-wing", "Escort Starfighter", "E-wings were designed to replace X-wings in elite New Republic squadrons with advanced targeting computers.", "~4,500 units", "New Republic (5 ABY–)", "#6366f1"),
    ("T-70 X-wing", "t-70-x-wing", "Superiority Starfighter", "T-70 X-wings upgraded the T-65 with split wings and modern avionics for Resistance starfighter corps.", "~2,200 units", "Resistance (28 ABY–)", "#f97316"),
    ("RZ-2 A-wing", "rz-2-a-wing", "Interceptor", "RZ-2 A-wings refined the RZ-1 with better shields while keeping blistering sublight acceleration.", "~1,800 units", "Resistance (28 ABY–)", "#f97316"),
    ("TIE/d Defender", "tie-defender", "Advanced Starfighter", "TIE Defenders combined shields, hyperdrive, and tri-wing design in Thrawn's push for elite Imperial squadrons.", "~500 units", "Imperial Era (2 BBY–4 ABY)", "#64748b"),
    ("TIE/rp Reaper", "tie-reaper", "Troop Transport", "TIE Reapers inserted death trooper squads and elite infantry with atmospheric landing capability.", "~1,200 units", "Imperial Era (0 BBY–4 ABY)", "#64748b"),
    ("TIE Hunter", "tie-hunter", "Multi-role Starfighter", "TIE Hunters mimicked Rebel X-wing layout with Imperial engineering, used in experimental cross-training units.", "~300 units", "Galactic Civil War (0 BBY–4 ABY)", "#64748b"),
    ("Kom'rk-class Fighter/Transport", "komrk-class-fighter", "Gunship / Fighter", "Kom'rk-class ships serve Mandalorian super commandos as troop transports and heavy gun platforms.", "~200 units", "Clone Wars through Mandalorian Era", "#0284c7"),
    ("Gauntlet Fighter", "gauntlet-fighter", "Mandalorian Assault Ship", "Mandalorian Gauntlet fighters combine heavy weapons with troop deployment for clan warfare and bounty operations.", "~350 units", "Clone Wars through Mandalorian Era", "#0284c7"),
    ("Fang-class Protector", "fang-class", "Mandalorian Starfighter", "Fang fighters give Mandalorian Protectors speed and firepower over Concord Dawn's mesas.", "~120 units", "Clone Wars through Galactic Civil War", "#0284c7"),
    ("Sheathipede-class Shuttle", "sheathipede-class", "Diplomatic Shuttle", "Neimoidian Sheathipede shuttles served Trade Federation VIPs with insectoid styling and minimal armament.", "~2,400 units", "Clone Wars (32–19 BBY)", "#ca8a04"),
    ("Theta-class T-2c Shuttle", "theta-class", "Executive Shuttle", "Theta-class shuttles carried Imperial officials including Palpatine with hidden defensive suites.", "~600 units", "Imperial Era (19 BBY–4 ABY)", "#64748b"),
    ("Nu-class Attack Shuttle", "nu-class", "Republic Gunship Shuttle", "Nu-class shuttles inserted clone commandos and Jedi on covert missions with faster profiles than LAAT gunships.", "~3,500 units", "Clone Wars (22–19 BBY)", "#6366f1"),
    ("Sentinel-class Landing Craft", "sentinel-class", "Imperial Landing Craft", "Sentinel landing craft delivered stormtrooper platoons from orbit with armored ramps and heavy support weapons.", "~8,000 units", "Imperial Era (19 BBY–4 ABY)", "#64748b"),
    ("C-9979 Landing Craft", "c-9979", "Separatist Landing Ship", "C-9979 landing ships disgorged droid battalions and MTTs across Naboo, Geonosis, and countless invasion beaches.", "~1,500 units", "Clone Wars (32–19 BBY)", "#0891b2"),
    ("Belbullab-22 Starfighter", "belbullab-22", "Starfighter", "General Grievous flew a customized Belbullab-22 named Soulless One, outpacing clone interceptors.", "~800 units", "Clone Wars (22–19 BBY)", "#0891b2"),
    ("Droid Tri-Fighter", "droid-tri-fighter", "Automated Starfighter", "Tri-fighters used triple radial arms and buzz droid tactics to overwhelm Jedi starfighter wings.", "~45,000 units", "Clone Wars (22–19 BBY)", "#0891b2"),
    ("Ginivex-class Fanblade Starfighter", "ginivex-class", "Starfighter", "Asajj Ventress piloted Ginivex fanblade fighters with distinctive crescent wings and deadly agility.", "~60 units", "Clone Wars (22–19 BBY)", "#0891b2"),
    ("Geonosian Solar Sailer", "geonosian-solar-sailer", "Solar Sailer", "Count Dooku escaped Geonosis aboard a solar sailer pushed by exotic tachyon streams and collector sails.", "~40 units", "Clone Wars (22–19 BBY)", "#0891b2"),
    ("Punworcca 116-class Sailer", "punworcca-116", "Solar Sailer", "Darth Maul traveled in Punworcca 116 sailers with minimal life support and maximum intimidation profile.", "~25 units", "Clone Wars (32–19 BBY)", "#991b1b"),
    ("HWK-290 Light Freighter", "hwk-290", "Light Freighter", "HWK-290 freighters like the Moldy Crow served smugglers and Kyle Katarn with modular gun mounts.", "~1,100 units", "Galactic Civil War (0 BBY–5 ABY)", "#d97706"),
    ("Action VI Transport", "action-vi", "Bulk Transport", "Action VI transports moved containerized cargo between Core worlds with slow but enormous hold capacity.", "~12,000 units", "Old Republic through Imperial Era", "#64748b"),
    ("Imperial Landing Craft", "imperial-landing-craft", "Atmospheric Landing Craft", "Imperial landing barges delivered personnel to occupied cities with imposing wedge profiles and escort wings.", "~6,500 units", "Imperial Era (19 BBY–4 ABY)", "#64748b"),
    ("Braha'tok-class Gunship", "brahatak-class", "Point-defense Gunship", "Dornean Braha'tok gunships protected Mon Calamari cruisers with concentrated flak during Endor.", "~220 units", "Galactic Civil War (0 BBY–4 ABY)", "#e11d48"),
    ("MC30c Frigate", "mc30c-frigate", "Mon Calamari Frigate", "MC30c frigates paired proton torpedo volleys with stealth fields for rebel hit-and-run raids.", "~180 units", "Galactic Civil War (2 BBY–4 ABY)", "#e11d48"),
    ("Bulwark-class Battlecruiser", "bulwark-class", "Separatist Battlecruiser", "Bulwark battlecruisers gave the CIS battleship tonnage to challenge Republic Star Destroyers head-on.", "~90 units", "Clone Wars (22–19 BBY)", "#0891b2"),
    ("First Order Dreadnought", "first-order-dreadnought", "Siege Dreadnought", "Fulminatrix-class dreadnoughts opened bombardments that stripped planetary shields before invasion fleets arrived.", "~8 units", "First Order (34 ABY–)", "#334155"),
    ("Trident-class Assault Ship", "trident-class", "Aquatic Assault Ship", "Trident drills pierced underwater cities on Mon Cala and Kamino during Separatist amphibious operations.", "~200 units", "Clone Wars (22–19 BBY)", "#0891b2"),
    ("C-ROC Gozanti-class Cruiser", "c-roc-gozanti", "Modified Freighter", "C-ROC Gozanti variants expanded cargo jaws for criminal syndicates and Imperial supply convoys.", "~4,000 units", "Imperial Era through Mandalorian Era", "#64748b"),
    ("Khetanna Sail Barge", "khetanna", "Luxury Sail Barge", "Jabba's Khetanna sail barge hosted desert celebrations until Luke Skywalker's rescue mission destroyed it.", "1 notable unit", "Galactic Civil War (4 ABY)", "#65a30d"),
    ("Bantha-II Cargo Skiff", "bantha-ii-skiff", "Desert Skiff", "Bantha-II skiffs moved cargo and prisoners across Tatooine's Dune Sea under Hutt and gang control.", "~8,000 units", "Galactic Civil War era", "#65a30d"),
    ("Star Commuter 2000", "star-commuter-2000", "Shuttle Transport", "Star Commuter shuttles linked Coruscant's surface districts to orbital terminals for working-class transit.", "~50,000 units", "Clone Wars through Imperial Era", "#6366f1"),
    ("AA-9 Coruscant Freighter", "aa-9-freighter", "Orbital Freighter", "AA-9 freighters hauled bulk goods between Coruscant's logistics hubs with distinctive stacked container spines.", "~6,000 units", "Clone Wars through Imperial Era", "#64748b"),
    ("G9 Rigger-class Freighter", "g9-rigger", "Light Freighter", "Anakin and Ahsoka used the Twilight G9 Rigger on covert missions with jury-rigged stealth systems.", "~900 units", "Clone Wars (22–19 BBY)", "#6366f1"),
    ("Praetorian-class Battlecruiser", "praetorian-class", "Battlecruiser", "Imperial Praetorian battlecruisers guarded key Core worlds with heavier firepower than standard line destroyers.", "~120 units", "Imperial Era (19 BBY–4 ABY)", "#64748b"),
    ("Secutor-class Star Destroyer", "secutor-class", "Carrier Star Destroyer", "Secutor-class hulls prioritized starfighter capacity with twin command towers for fleet coordination.", "~60 units", "Imperial Era (19 BBY–4 ABY)", "#64748b"),
    ("Lancer-class Frigate", "lancer-class", "Anti-starfighter Frigate", "Lancer frigates bristled with point-defense turbolasers to shred snubfighter wings in fleet engagements.", "~500 units", "Imperial Era (19 BBY–4 ABY)", "#64748b"),
    ("Hardcell-class Transport", "hardcell-class", "Corporate Transport", "Techno Union Hardcell transports moved battle droids with exposed engines and vertical landing capability.", "~3,200 units", "Clone Wars (22–19 BBY)", "#0891b2"),
    ("Banking Clan Frigate", "banking-clan-frigate", "Frigate", "InterGalactic Banking Clan frigates financed Separatist fleets while officially maintaining neutrality.", "~600 units", "Clone Wars (22–19 BBY)", "#ca8a04"),
    ("Nantex-class Territorial Starfighter", "nantex-class", "Geonosian Starfighter", "Geonosian Nantex fighters used ring-cockpits and insectile control yokes in defense of droid foundries.", "~25,000 units", "Clone Wars (22–19 BBY)", "#0891b2"),
    ("CloakShape Fighter", "cloakshape-fighter", "Starfighter", "CloakShape fighters served pirates and mercenaries with rugged frames predating modern snubfighter doctrine.", "~18,000 units", "Old Republic through Galactic Civil War", "#d97706"),
    ("K-wing Assault Fighter", "k-wing", "Assault Starfighter", "K-wings delivered heavy ordnance in New Republic bombing wings with rotating wing weapons pods.", "~2,800 units", "New Republic (5 ABY–)", "#6366f1"),
    ("H-60 Tempest Bomber", "h-60-tempest", "Heavy Bomber", "First Order Tempest bombers carried magma bombs in wing racks for planetary suppression campaigns.", "~400 units", "First Order (34 ABY–)", "#334155"),
    ("YV-666 Light Freighter", "yv-666", "Light Freighter", "YV-666 freighters like the Hound's Tooth offered bounty hunters armored holds and extended range.", "~700 units", "Galactic Civil War through Mandalorian Era", "#65a30d"),
    ("Nightbrother", "nightbrother", "Modified Omidian Nightship", "Maul's Nightbrother served as command ship for Shadow Collective raids with brutalist Mandalorian refits.", "1 notable unit", "Clone Wars (20–19 BBY)", "#991b1b"),
    ("IG-2000", "ig-2000", "Aggressor-class Assassin Droid Ship", "IG-88's IG-2000 pursued the Millennium Falcon with droid-piloted precision and hidden superweapon ambitions.", "4 units", "Galactic Civil War (0 BBY–3 ABY)", "#65a30d"),
    ("Eclipse-class Super Star Destroyer", "eclipse-class", "Super Star Destroyer", "Palpatine's Eclipse-class dreadnoughts mounted superlasers and dark-side sanctums in Legends continuity.", "~2 units", "Imperial Remnant (10 ABY–)", "#991b1b"),
    ("World Devastator", "world-devastator", "Planet-eating Dreadnought", "World Devastators consumed cityscapes to manufacture war materiel for Palpatine's Dark Empire.", "~25 units", "Dark Empire (10 ABY)", "#991b1b"),
]


def ship_enrichment(name, ship_class, desc, production, era, slug):
    faction_guess = {
        "#6366f1": "Galactic Republic / New Republic",
        "#64748b": "Galactic Empire",
        "#0891b2": "Confederacy of Independent Systems",
        "#e11d48": "Alliance to Restore the Republic",
        "#334155": "First Order",
        "#f97316": "Resistance",
        "#0284c7": "Mandalorian clans",
        "#65a30d": "Bounty hunters and criminal operators",
        "#d97706": "Independent smugglers and mercenaries",
        "#991b1b": "Sith / Imperial dark-side factions",
        "#ca8a04": "Trade Federation / corporate guilds",
    }
    return {
        "overview": (
            f"The {name} is a {ship_class.lower()} whose design philosophy reflects the industrial and strategic "
            f"priorities of {era}. {desc} Production estimates place the class at {production}, though wartime "
            f"losses, capture, and black-market duplication make precise fleet registries unreliable."
        ),
        "history": "\n\n".join([
            (
                f"Engineering teams first finalized the {name} blueprints during the political climate of {era}. "
                f"The {ship_class.lower()} was intended to solve specific fleet gaps—whether planetary assault, "
                f"convoy escort, starfighter superiority, or terror bombardment—and shipwrights iterated hull "
                f"plates, reactor output, and crew compartments accordingly."
            ),
            (
                f"Once deployed, the {name} appeared in fleet actions that defined its reputation. {desc} "
                f"Combat logs show crews exploiting the class's strengths while improvising fixes for known "
                f"weaknesses under fire, a pattern repeated across every major galactic conflict."
            ),
            (
                f"As doctrine evolved, rival factions studied captured {name} hulls. Refit yards duplicated "
                f"weapons mounts and sensor suites; some variants never appeared in official manifests. "
                f"Estimated production of {production} therefore understates how many similar silhouettes "
                f"operated under alternate insignia."
            ),
            (
                f"Surviving {name} vessels now sit in museum orbits, mercenary fleets, and scrap worlds. "
                f"Historians treat the class as a measure of how galactic wars industrialize violence—each "
                f"hull a factory product that outlived the politicians who ordered it."
            ),
        ]),
        "significance": "\n\n".join([
            (
                f"The {name} demonstrates how {ship_class.lower()} design shapes campaign outcomes. "
                f"Its layout influenced successor programs and remains a case study in naval academies."
            ),
            (
                f"With roughly {production} hulls associated with {era}, the class became a visual symbol "
                f"of its faction's reach—recognizable in holonet footage and feared in convoy manifests."
            ),
            (
                f"Engineers still debate whether the {name} prioritized firepower over crew survival; "
                f"that trade-off defines its legacy in both propaganda and honest after-action reports."
            ),
        ]),
        "notableEvents": [
            f"Prototype {name} accepted into fleet trials during {era.split('(')[0].strip()}",
            f"Mass production reaches approximately {production}",
            f"First major fleet battle featuring multiple {name} hulls",
            f"Captured or scuttled {name} studied by rival shipwrights",
            f"Notable commander achieves victory aboard a {name}",
            f"Refit program extends service life beyond original specifications",
            f"Class featured in faction propaganda broadcasts",
            f"Remaining hulls retired, preserved, or converted to civilian use",
        ],
        "affiliations": [
            faction_guess.get(SHIPS[[s[1] for s in SHIPS].index(slug) if slug in [s[1] for s in SHIPS] else 0][6], "Multiple factions"),
            f"{ship_class} operational wings",
            "Naval shipwright guilds",
            "Fleet maintenance corps",
            "Combat flight schools",
        ],
        "timeline": [
            {"era": era.split("(")[0].strip(), "event": f"{name} design approved and prototype tested"},
            {"era": era.split("(")[0].strip(), "event": f"Production scales toward {production}"},
            {"era": "Galactic Civil War" if "Civil" not in era else era.split("(")[0].strip(), "event": f"{name} enters decisive fleet engagements"},
            {"era": "Imperial Era", "event": f"Attrition and refits reshape active {name} registries"},
            {"era": "New Republic", "event": f"Surviving {name} hulls decommissioned or sold"},
        ],
    }


def write_settlement_additions():
    header = textwrap.dedent('''\
        #!/usr/bin/env python3
        """Additional settlement entries merged at generation time."""

        from __future__ import annotations

        from pathlib import Path

        _catalog_path = Path(__file__).resolve().parent / "generate_species_settlement_catalog.py"
        _code = _catalog_path.read_text()
        _ns: dict = {"__file__": str(_catalog_path), "__name__": "_catalog_helpers"}
        exec(compile(_code.split("def main()")[0], str(_catalog_path), "exec"), _ns)
        st = _ns["st"]
        _ev = _ns["_ev"]
        _aff = _ns["_aff"]
        _tl = _ns["_tl"]

        ADDITIONAL_SETTLEMENTS: list[dict] = [
    ''')
    body = "".join(fmt_settlement(e) for e in SETTLEMENTS)
    footer = "\n]\n"
    (SCRIPTS / "settlement_catalog_additions.py").write_text(header + body + footer)
    print(f"Wrote {len(SETTLEMENTS)} settlement additions")


def write_ship_additions():
    text = SHIP_DATA.read_text()
    text = text.replace("\n        }\n    ];", "\n        },\n    ];")
    if "providence-class" in text:
        print("Ship additions already present, skipping C# append")
        return
    block = "\n"
    for name, slug, cls, desc, prod, era, color in SHIPS:
        block += f"""        new()
        {{
            Name = "{name}",
            Slug = "{slug}",
            Route = "ships/{slug}",
            Class = "{cls}",
            Description = "{desc}",
            ProductionCount = "{prod}",
            Era = "{era}",
            Color = "{color}"
        }},
"""
    text = text.replace("\n    ];", block + "\n    ];")
    SHIP_DATA.write_text(text)
    print(f"Appended {len(SHIPS)} ships to ShipData.cs")


def write_ship_enrichments():
    enrich = {}
    color_map = {s[1]: s[6] for s in SHIPS}
    for name, slug, cls, desc, prod, era, color in SHIPS:
        e = ship_enrichment(name, cls, desc, prod, era, slug)
        # fix faction lookup
        faction_guess = {
            "#6366f1": "Galactic Republic / New Republic",
            "#64748b": "Galactic Empire",
            "#0891b2": "Confederacy of Independent Systems",
            "#e11d48": "Alliance to Restore the Republic",
            "#334155": "First Order",
            "#f97316": "Resistance",
            "#0284c7": "Mandalorian clans",
            "#65a30d": "Bounty hunters and criminal operators",
            "#d97706": "Independent smugglers and mercenaries",
            "#991b1b": "Sith / Imperial dark-side factions",
            "#ca8a04": "Trade Federation / corporate guilds",
        }
        e["affiliations"][0] = faction_guess.get(color, "Multiple factions")
        enrich[slug] = e

    content = '"""Ship profile enrichments merged into generate_directory_profiles.py."""\n\nSHIP_ENRICHMENTS: dict[str, dict] = '
    content += json.dumps(enrich, indent=2, ensure_ascii=False)
    content += "\n"
    (SCRIPTS / "ship_profile_enrichments.py").write_text(content)
    print(f"Wrote {len(enrich)} ship enrichments")


def patch_profile_generator():
    path = SCRIPTS / "generate_directory_profiles.py"
    text = path.read_text()
    if "ship_profile_enrichments" in text:
        print("Profile generator already patched")
        return
    insert = "\nfrom ship_profile_enrichments import SHIP_ENRICHMENTS\n"
    text = text.replace("ENRICHMENTS: dict[str, dict] = {", insert + "ENRICHMENTS: dict[str, dict] = {", 1)

    old = "    enriched = ENRICHMENTS.get(entry[\"slug\"], {})"
    new = (
        "    enriched = ENRICHMENTS.get(entry[\"slug\"], {})\n"
        "    if category == \"ships\":\n"
        "        enriched = {**SHIP_ENRICHMENTS.get(entry[\"slug\"], {}), **enriched}"
    )
    text = text.replace(old, new, 1)
    path.write_text(text)
    print("Patched generate_directory_profiles.py")


def patch_settlement_main():
    path = SCRIPTS / "generate_species_settlement_catalog.py"
    text = path.read_text()
    if "ADDITIONAL_SETTLEMENTS" in text:
        print("Settlement main already patched")
        return
    text = text.replace(
        "def main() -> None:\n    from species_catalog_additions import ADDITIONAL_SPECIES\n\n    all_species = SPECIES + ADDITIONAL_SPECIES",
        "def main() -> None:\n    from species_catalog_additions import ADDITIONAL_SPECIES\n    from settlement_catalog_additions import ADDITIONAL_SETTLEMENTS\n\n    all_species = SPECIES + ADDITIONAL_SPECIES\n    all_settlements = SETTLEMENTS + ADDITIONAL_SETTLEMENTS",
    )
    text = text.replace("write_settlement_cs(SETTLEMENTS)", "write_settlement_cs(all_settlements)")
    text = text.replace("    for entry in SETTLEMENTS:", "    for entry in all_settlements:")
    text = text.replace("settlement_files = len(SETTLEMENTS) * 4", "settlement_files = len(all_settlements) * 4")
    text = text.replace('print(f"Generated {len(SETTLEMENTS)} settlements")', 'print(f"Generated {len(all_settlements)} settlements")')
    text = text.replace(
        'print(f"  Settlement assets: {len(SETTLEMENTS)} icons, {len(SETTLEMENTS)} scenes, {len(SETTLEMENTS)} profiles")',
        'print(f"  Settlement assets: {len(all_settlements)} icons, {len(all_settlements)} scenes, {len(all_settlements)} profiles")',
    )
    path.write_text(text)
    print("Patched settlement generator main()")


if __name__ == "__main__":
    write_settlement_additions()
    write_ship_additions()
    write_ship_enrichments()
    patch_profile_generator()
    patch_settlement_main()
