using StarWars.Models;

namespace StarWars.Data;

public static class CharacterData
{
    public static IReadOnlyList<Character> Characters { get; } =
    [
        new()
        {
            Name = "Admiral Ackbar",
            Slug = "admiral-ackbar",
            Route = "characters/admiral-ackbar",
            Role = "Rebel Admiral",
            Description = "A Mon Calamari military genius whose tactical brilliance helped destroy the second Death Star at Endor.",
            Color = "#0891b2",
        },
        new()
        {
            Name = "Agent Kallus",
            Slug = "agent-kallus",
            Route = "characters/agent-kallus",
            Role = "Imperial Agent",
            Description = "An ISB agent who hunted the Ghost crew before his conscience turned him into a Rebel spy.",
            Color = "#64748b",
        },
        new()
        {
            Name = "Allegiant General Pryde",
            Slug = "general-pryde",
            Route = "characters/general-pryde",
            Role = "First Order General",
            Description = "A veteran Imperial officer who served Palpatine and later commanded the Final Order's Sith fleet until he died aboard the Steadfast during the Battle of Exegol.",
            Color = "#334155",
        },
        new()
        {
            Name = "Amilyn Holdo",
            Slug = "amilyn-holdo",
            Route = "characters/amilyn-holdo",
            Role = "Resistance Vice Admiral",
            Description = "Leia Organa's eccentric and brilliant friend who sacrificed the Raddus in hyperspace to destroy the First Order fleet at Crait, saving the Resistance remnant.",
            Color = "#a855f7",
        },
        new()
        {
            Name = "Atton Rand",
            Slug = "atton-rand",
            Route = "characters/atton-rand",
            Role = "Smuggler",
            Description = "A cynical former Sith trooper turned scoundrel who became a loyal companion during the Jedi Exile's journey.",
            Color = "#d97706",
        },
        new()
        {
            Name = "Bail Organa",
            Slug = "bail-organa",
            Route = "characters/bail-organa",
            Role = "Senator of Alderaan",
            Description = "A noble senator who secretly founded the Rebel Alliance and adopted Leia as his daughter.",
            Color = "#6366f1",
        },
        new()
        {
            Name = "Bastila Shan",
            Slug = "bastila-shan",
            Route = "characters/bastila-shan",
            Role = "Jedi Padawan",
            Description = "A young Jedi Battle Meditation prodigy captured by Darth Malak whose bond with Revan became central to the galaxy's fate during the Jedi Civil War.",
            Color = "#3b82f6",
        },
        new()
        {
            Name = "Baze Malbus",
            Slug = "baze-malbus",
            Route = "characters/baze-malbus",
            Role = "Rebel Guard",
            Description = "A heavily armed Guardian of the Whills who fought alongside Chirrut on Jedha and Scarif.",
            Color = "#78716c",
        },
        new()
        {
            Name = "BB-8",
            Slug = "bb-8",
            Route = "characters/bb-8",
            Role = "Astromech Droid",
            Description = "Poe Dameron's loyal spherical astromech who carried vital Resistance intelligence across the galaxy.",
            Color = "#f97316",
        },
        new()
        {
            Name = "Beru Lars",
            Slug = "beru-lars",
            Route = "characters/beru-lars",
            Role = "Moisture Farmer",
            Description = "Owen Lars's wife and Luke Skywalker's aunt, who raised the boy as her own with warmth and practical wisdom until Imperial stormtroopers burned the Lars homestead on Tatooine.",
            Color = "#ca8a04",
        },
        new()
        {
            Name = "Bib Fortuna",
            Slug = "bib-fortuna",
            Route = "characters/bib-fortuna",
            Role = "Majordomo",
            Description = "Jabba the Hutt's Twi'lek majordomo who managed the palace's daily cruelty until Boba Fett seized power on Tatooine and removed him from court.",
            Color = "#6b7280",
        },
        new()
        {
            Name = "Bo-Katan Kryze",
            Slug = "bo-katan-kryze",
            Route = "characters/bo-katan-kryze",
            Role = "Mandalorian Leader",
            Description = "A Nite Owl warrior who fought to reclaim Mandalore and wielded the Darksaber in the fight against the Empire.",
            Color = "#0284c7",
        },
        new()
        {
            Name = "Boba Fett",
            Slug = "boba-fett",
            Route = "characters/boba-fett",
            Role = "Bounty Hunter",
            Description = "The legendary Mandalorian-armored hunter who tracked Han Solo for Jabba and later ruled Tatooine's underworld.",
            Color = "#65a30d",
        },
        new()
        {
            Name = "Boss Nass",
            Slug = "boss-nass",
            Route = "characters/boss-nass",
            Role = "Gungan Leader",
            Description = "The bombastic Boss of the Gungan Grand Army who reluctantly allied with Queen Amidala to drive the Trade Federation from Naboo after centuries of tension between Gungans and humans.",
            Color = "#16a34a",
        },
        new()
        {
            Name = "C-3PO",
            Slug = "c-3po",
            Route = "characters/c-3po",
            Role = "Protocol Droid",
            Description = "An anxious golden protocol droid fluent in over six million forms of communication who served the Skywalker family for decades.",
            Color = "#eab308",
        },
        new()
        {
            Name = "Cad Bane",
            Slug = "cad-bane",
            Route = "characters/cad-bane",
            Role = "Bounty Hunter",
            Description = "A ruthless Duro gunslinger regarded as the galaxy's greatest bounty hunter during the Clone Wars era.",
            Color = "#dc2626",
        },
        new()
        {
            Name = "Canderous Ordo",
            Slug = "canderous-ordo",
            Route = "characters/canderous-ordo",
            Role = "Mandalorian Warrior",
            Description = "A fierce Mandalorian mercenary who fought beside Revan and later united his people as Mandalore the Preserver.",
            Color = "#b45309",
        },
        new()
        {
            Name = "Captain Panaka",
            Slug = "captain-panaka",
            Route = "characters/captain-panaka",
            Role = "Royal Security",
            Description = "Head of security for Naboo's monarch who protected Queen Amidala through invasion, exile, and return, exemplifying loyal service to the throne across the Prequel era.",
            Color = "#6366f1",
        },
        new()
        {
            Name = "Captain Phasma",
            Slug = "captain-phasma",
            Route = "characters/captain-phasma",
            Role = "First Order Captain",
            Description = "A chrome-armored stormtrooper commander who enforced brutal discipline within the First Order ranks.",
            Color = "#94a3b8",
        },
        new()
        {
            Name = "Captain Rex",
            Slug = "captain-rex",
            Route = "characters/captain-rex",
            Role = "Clone Captain",
            Description = "An ARC trooper who served under Anakin and Ahsoka before removing his inhibitor chip and joining the Rebellion.",
            Color = "#ea580c",
        },
        new()
        {
            Name = "Cara Dune",
            Slug = "cara-dune",
            Route = "characters/cara-dune",
            Role = "Mercenary",
            Description = "A former Rebel shock trooper who became a marshal on Nevarro and ally to Din Djarin.",
            Color = "#059669",
        },
        new()
        {
            Name = "Carth Onasi",
            Slug = "carth-onasi",
            Route = "characters/carth-onasi",
            Role = "Republic Soldier",
            Description = "A veteran Republic pilot haunted by the destruction of Taris who guided the amnesiac Revan across the galaxy.",
            Color = "#2563eb",
        },
        new()
        {
            Name = "Cassian Andor",
            Slug = "cassian-andor",
            Route = "characters/cassian-andor",
            Role = "Rebel Intelligence Officer",
            Description = "A hardened intelligence operative who sacrificed everything to steal the Death Star plans on Scarif.",
            Color = "#475569",
        },
        new()
        {
            Name = "Cham Syndulla",
            Slug = "cham-syndulla",
            Route = "characters/cham-syndulla",
            Role = "Ryloth Freedom Fighter",
            Description = "Hera Syndulla's father and the legendary Twi'lek resistance leader who fought Separatists and Empire alike to free Ryloth from occupation.",
            Color = "#059669",
        },
        new()
        {
            Name = "Chewbacca",
            Slug = "chewbacca",
            Route = "characters/chewbacca",
            Role = "Wookiee Warrior",
            Description = "A loyal Wookiee co-pilot and fierce companion to Han Solo and the Rebel cause.",
            Color = "#92400e",
        },
        new()
        {
            Name = "Chirrut Îmwe",
            Slug = "chirrut-imwe",
            Route = "characters/chirrut-imwe",
            Role = "Guardian of the Whills",
            Description = "A blind warrior monk who trusted in the Force and defended the Temple of the Kyber on Jedha.",
            Color = "#a16207",
        },
        new()
        {
            Name = "Cliegg Lars",
            Slug = "cliegg-lars",
            Route = "characters/cliegg-lars",
            Role = "Moisture Farmer",
            Description = "Owen's father who freed and married Shmi Skywalker, losing a leg rescuing her from Tusken captivity before Anakin returned to Tatooine during the Clone Wars.",
            Color = "#a16207",
        },
        new()
        {
            Name = "Commander Cody",
            Slug = "commander-cody",
            Route = "characters/commander-cody",
            Role = "Clone Commander",
            Description = "Obi-Wan Kenobi's trusted clone marshal who led the 212th Attack Battalion throughout the Clone Wars.",
            Color = "#f97316",
        },
        new()
        {
            Name = "Crosshair",
            Slug = "crosshair",
            Route = "characters/crosshair",
            Role = "Clone Commando",
            Description = "The Bad Batch's elite sniper whose inhibitor chip briefly turned him against his brothers before he rejoined the team.",
            Color = "#64748b",
        },
        new()
        {
            Name = "Dedra Meero",
            Slug = "dedra-meero",
            Route = "characters/dedra-meero",
            Role = "ISB Supervisor",
            Description = "A relentless Imperial Security Bureau supervisor who hunted Cassian Andor and the growing Rebel network.",
            Color = "#374151",
        },
        new()
        {
            Name = "Dexter Jettster",
            Slug = "dexter-jettster",
            Route = "characters/dexter-jettster",
            Role = "Diner Owner",
            Description = "A Besalisk informant and diner owner on Coruscant whose vast underworld contacts helped Obi-Wan Kenobi identify a Kamino saberdart during the clone army investigation.",
            Color = "#ea580c",
        },
        new()
        {
            Name = "Din Djarin",
            Slug = "din-djarin",
            Route = "characters/din-djarin",
            Role = "Mandalorian Bounty Hunter",
            Description = "A lone Mandalorian bounty hunter who found a new purpose protecting Grogu and reuniting his people.",
            Color = "#64748b",
        },
        new()
        {
            Name = "Director Krennic",
            Slug = "director-krennic",
            Route = "characters/director-krennic",
            Role = "Imperial Director",
            Description = "The ambitious Imperial officer who oversaw the Death Star project and ruthlessly eliminated anyone in his way.",
            Color = "#ffffff",
        },
        new()
        {
            Name = "Dormé",
            Slug = "dorme",
            Route = "characters/dorme",
            Role = "Handmaiden",
            Description = "One of Padmé Amidala's loyal handmaidens who served as decoy and confidante during the Separatist crisis, risking her life to protect the senator's identity and mission.",
            Color = "#c084fc",
        },
        new()
        {
            Name = "Dr. Pershing",
            Slug = "dr-pershing",
            Route = "characters/dr-pershing",
            Role = "Imperial Scientist",
            Description = "A Kaminoan-trained scientist recruited by Moff Gideon to study Grogu's blood for cloning research tied to the Emperor's posthumous designs.",
            Color = "#e2e8f0",
        },
        new()
        {
            Name = "Dryden Vos",
            Slug = "dryden-vos",
            Route = "characters/dryden-vos",
            Role = "Crimson Dawn Leader",
            Description = "A scarred near-human crime lord who led Crimson Dawn from his yacht, manipulating Han Solo and Qi'ra until betrayal ended his reign in a violent standoff.",
            Color = "#dc2626",
        },
        new()
        {
            Name = "Echo",
            Slug = "echo",
            Route = "characters/echo",
            Role = "Clone Commando",
            Description = "An ARC trooper believed dead on Lola Sayu who was rescued from Separatist captivity and joined the Bad Batch.",
            Color = "#0ea5e9",
        },
        new()
        {
            Name = "Enfys Nest",
            Slug = "enfys-nest",
            Route = "characters/enfys-nest",
            Role = "Cloud-Riders Leader",
            Description = "The masked leader of the Cloud-Riders who fought Crimson Dawn and revealed herself as a revolutionary building an alliance against galactic exploitation.",
            Color = "#f59e0b",
        },
        new()
        {
            Name = "Fennec Shand",
            Slug = "fennec-shand",
            Route = "characters/fennec-shand",
            Role = "Assassin",
            Description = "A deadly sharpshooter who worked as a bounty hunter before becoming Boba Fett's right hand on Tatooine.",
            Color = "#15803d",
        },
        new()
        {
            Name = "Finn",
            Slug = "finn",
            Route = "characters/finn",
            Role = "Resistance Hero",
            Description = "A stormtrooper who defected from the First Order and became a courageous fighter for the Resistance.",
            Color = "#3b82f6",
        },
        new()
        {
            Name = "Fives",
            Slug = "fives",
            Route = "characters/fives",
            Role = "ARC Trooper",
            Description = "A clone who uncovered the inhibitor chip conspiracy before being silenced by his own brothers.",
            Color = "#ea580c",
        },
        new()
        {
            Name = "Gar Saxon",
            Slug = "gar-saxon",
            Route = "characters/gar-saxon",
            Role = "Imperial Super Commando",
            Description = "Mandalore's Imperial viceroy who enforced occupation with brutality until Bo-Katan Kryze and Sabine Wren ended his tyranny in a civil war for Mandalore's soul.",
            Color = "#64748b",
        },
        new()
        {
            Name = "General Grievous",
            Slug = "general-grievous",
            Route = "characters/general-grievous",
            Role = "Separatist General",
            Description = "A cyborg warlord who collected Jedi lightsabers and commanded the droid armies of the Confederacy.",
            Color = "#6b7280",
        },
        new()
        {
            Name = "General Hux",
            Slug = "general-hux",
            Route = "characters/general-hux",
            Role = "First Order General",
            Description = "A fanatical First Order general who commanded Starkiller Base and rivaled Kylo Ren for Snoke's favor.",
            Color = "#1e293b",
        },
        new()
        {
            Name = "Governor Pryce",
            Slug = "governor-pryce",
            Route = "characters/governor-pryce",
            Role = "Imperial Governor",
            Description = "Lothal's ambitious Imperial governor who destroyed her homeworld's economy chasing promotion, clashing with the Ghost crew until her defeat at the Lothal liberation.",
            Color = "#475569",
        },
        new()
        {
            Name = "Grand Moff Tarkin",
            Slug = "grand-moff-tarkin",
            Route = "characters/grand-moff-tarkin",
            Role = "Imperial Governor",
            Description = "The cold and calculating governor who commanded the Death Star and destroyed Alderaan to terrify the galaxy.",
            Color = "#71717a",
        },
        new()
        {
            Name = "Greef Karga",
            Slug = "greef-karga",
            Route = "characters/greef-karga",
            Role = "Bounty Hunter Guild Agent",
            Description = "A Magistrate and former Guild agent on Nevarro who became an ally to Din Djarin and Grogu.",
            Color = "#ca8a04",
        },
        new()
        {
            Name = "Han Solo",
            Slug = "han-solo",
            Route = "characters/han-solo",
            Role = "Smuggler",
            Description = "A roguish smuggler and captain of the Millennium Falcon who joined the Rebellion.",
            Color = "#d97706",
        },
        new()
        {
            Name = "Hera Syndulla",
            Slug = "hera-syndulla",
            Route = "characters/hera-syndulla",
            Role = "Rebel Pilot",
            Description = "The Twi'lek captain of the Ghost who led Phoenix Squadron and became a general in the Rebel Alliance.",
            Color = "#059669",
        },
        new()
        {
            Name = "HK-47",
            Slug = "hk-47",
            Route = "characters/hk-47",
            Role = "Assassin Droid",
            Description = "A sarcastic assassin droid built by Revan who delighted in precision violence and calling organics meatbags.",
            Color = "#dc2626",
        },
        new()
        {
            Name = "Hondo Ohnaka",
            Slug = "hondo-ohnaka",
            Route = "characters/hondo-ohnaka",
            Role = "Pirate Captain",
            Description = "A Weequay pirate king whose charming schemes and shifting loyalties made him a recurring thorn for heroes and villains alike.",
            Color = "#b45309",
        },
        new()
        {
            Name = "Hunter",
            Slug = "hunter",
            Route = "characters/hunter",
            Role = "Clone Sergeant",
            Description = "The leader of Clone Force 99 who protected his squad of genetically enhanced troopers through the fall of the Republic.",
            Color = "#ea580c",
        },
        new()
        {
            Name = "IG-11",
            Slug = "ig-11",
            Route = "characters/ig-11",
            Role = "Assassin Droid",
            Description = "A reprogrammed nurse droid who sacrificed himself protecting Grogu on Nevarro.",
            Color = "#94a3b8",
        },
        new()
        {
            Name = "Jabba the Hutt",
            Slug = "jabba-the-hutt",
            Route = "characters/jabba-the-hutt",
            Role = "Crime Lord",
            Description = "The corpulent Tatooine gangster who controlled smuggling routes and held Han Solo frozen in carbonite.",
            Color = "#84cc16",
        },
        new()
        {
            Name = "Jango Fett",
            Slug = "jango-fett",
            Route = "characters/jango-fett",
            Role = "Bounty Hunter",
            Description = "The Mandalorian-foundling template for the clone army and father of Boba Fett.",
            Color = "#65a30d",
        },
        new()
        {
            Name = "Jar Jar Binks",
            Slug = "jar-jar-binks",
            Route = "characters/jar-jar-binks",
            Role = "Gungan Representative",
            Description = "An awkward Gungan outcast whose clumsy heroism helped unite Naboo against the Trade Federation and who later, tragically, proposed the emergency powers that enabled Palpatine's rise.",
            Color = "#22c55e",
        },
        new()
        {
            Name = "Jolee Bindo",
            Slug = "jolee-bindo",
            Route = "characters/jolee-bindo",
            Role = "Hermit Jedi",
            Description = "A cynical former Jedi who exiled himself on Kashyyyk's shadowlands, offering Revan unorthodox wisdom about the Force, love, and the gray paths between light and dark.",
            Color = "#15803d",
        },
        new()
        {
            Name = "Jyn Erso",
            Slug = "jyn-erso",
            Route = "characters/jyn-erso",
            Role = "Rebel Soldier",
            Description = "A reluctant fighter who rallied Rogue One to steal the Death Star plans and complete her father's work.",
            Color = "#78716c",
        },
        new()
        {
            Name = "K-2SO",
            Slug = "k-2so",
            Route = "characters/k-2so",
            Role = "Security Droid",
            Description = "A reprogrammed Imperial security droid whose blunt honesty and combat skills served Cassian Andor's mission.",
            Color = "#64748b",
        },
        new()
        {
            Name = "Kuiil",
            Slug = "kuiil",
            Route = "characters/kuiil",
            Role = "Ugnaught Mechanic",
            Description = "A patient moisture farmer and mechanic on Arvala-7 who helped Din Djarin and declared he had spoken.",
            Color = "#a16207",
        },
        new()
        {
            Name = "Lando Calrissian",
            Slug = "lando-calrissian",
            Route = "characters/lando-calrissian",
            Role = "Administrator",
            Description = "A smooth-talking gambler and Cloud City administrator who became a general in the Rebel Alliance.",
            Color = "#eab308",
        },
        new()
        {
            Name = "Leia Organa",
            Slug = "leia-organa",
            Route = "characters/leia-organa",
            Role = "Rebel Leader",
            Description = "Princess of Alderaan, senator, and a founding leader of the Rebel Alliance.",
            Color = "#c084fc",
        },
        new()
        {
            Name = "Lor San Tekka",
            Slug = "lor-san-tekka",
            Route = "characters/lor-san-tekka",
            Role = "Church of the Force Elder",
            Description = "An explorer and faith keeper who guarded map fragments to Luke Skywalker until the First Order's Kylo Ren executed him on Jakku searching for the missing Jedi.",
            Color = "#78716c",
        },
        new()
        {
            Name = "Luthen Rael",
            Slug = "luthen-rael",
            Route = "characters/luthen-rael",
            Role = "Rebel Handler",
            Description = "A secretive antiquities dealer who built and sacrificed everything to fund the early Rebel insurgency.",
            Color = "#475569",
        },
        new()
        {
            Name = "Maz Kanata",
            Slug = "maz-kanata",
            Route = "characters/maz-kanata",
            Role = "Pirate Queen",
            Description = "An ancient pirate queen on Takodana who counseled heroes and guarded Luke Skywalker's lightsaber for years.",
            Color = "#f59e0b",
        },
        new()
        {
            Name = "Meetra Surik",
            Slug = "meetra-surik",
            Route = "characters/meetra-surik",
            Role = "Jedi Exile",
            Description = "A Jedi General exiled after the Mandalorian Wars who returned to face the Sith Triumvirate and ended the threat on Malachor V.",
            Color = "#2563eb",
        },
        new()
        {
            Name = "Mission Vao",
            Slug = "mission-vao",
            Route = "characters/mission-vao",
            Role = "Scoundrel",
            Description = "A quick-witted Twi'lek orphan from Taris who joined Revan's crew alongside her Wookiee companion Zaalbar.",
            Color = "#22c55e",
        },
        new()
        {
            Name = "Moff Gideon",
            Slug = "moff-gideon",
            Route = "characters/moff-gideon",
            Role = "Imperial Warlord",
            Description = "A remnant Imperial officer who hunted Grogu and wielded the Darksaber in his bid to restore the Empire.",
            Color = "#1e293b",
        },
        new()
        {
            Name = "Mon Mothma",
            Slug = "mon-mothma",
            Route = "characters/mon-mothma",
            Role = "Rebel Leader",
            Description = "A Chandrilan senator who publicly denounced the Empire and became the political leader of the Alliance.",
            Color = "#6366f1",
        },
        new()
        {
            Name = "Morgan Elsbeth",
            Slug = "morgan-elsbeth",
            Route = "characters/morgan-elsbeth",
            Role = "Magistrate",
            Description = "A Nightsister survivor who ruled Corvus and served Grand Admiral Thrawn as a magistrate and dark acolyte.",
            Color = "#7c3aed",
        },
        new()
        {
            Name = "Nute Gunray",
            Slug = "nute-gunray",
            Route = "characters/nute-gunray",
            Role = "Trade Federation Viceroy",
            Description = "The cowardly Neimoidian leader who blockaded Naboo and later served the Separatist cause during the Clone Wars.",
            Color = "#84cc16",
        },
        new()
        {
            Name = "Omega",
            Slug = "omega",
            Route = "characters/omega",
            Role = "Clone",
            Description = "An unmodified female clone who served as the heart of Clone Force 99 and held the key to their future.",
            Color = "#f472b6",
        },
        new()
        {
            Name = "Onaconda Farr",
            Slug = "onaconda-farr",
            Route = "characters/onaconda-farr",
            Role = "Senator",
            Description = "Rodian senator from Savareen whose desperation during the Clone Wars led him to briefly betray Padmé Amidala before redeeming himself with a sacrificial act in the Senate.",
            Color = "#4ade80",
        },
        new()
        {
            Name = "Owen Lars",
            Slug = "owen-lars",
            Route = "characters/owen-lars",
            Role = "Moisture Farmer",
            Description = "Luke Skywalker's cautious uncle who raised him on Tatooine and tried to keep him from his Jedi destiny.",
            Color = "#d97706",
        },
        new()
        {
            Name = "Padmé Amidala",
            Slug = "padme-amidala",
            Route = "characters/padme-amidala",
            Role = "Senator of Naboo",
            Description = "Former Queen of Naboo and senator who fought tirelessly for peace and democracy.",
            Color = "#ec4899",
        },
        new()
        {
            Name = "Poe Dameron",
            Slug = "poe-dameron",
            Route = "characters/poe-dameron",
            Role = "Resistance Pilot",
            Description = "The Resistance's best starfighter pilot whose daring raids and leadership challenged the First Order.",
            Color = "#f97316",
        },
        new()
        {
            Name = "Qi'ra",
            Slug = "qira",
            Route = "characters/qira",
            Role = "Crimson Dawn Lieutenant",
            Description = "Han Solo's former partner who rose through the criminal underworld to serve Dryden Vos and Crimson Dawn.",
            Color = "#dc2626",
        },
        new()
        {
            Name = "R2-D2",
            Slug = "r2-d2",
            Route = "characters/r2-d2",
            Role = "Astromech Droid",
            Description = "A brave astromech droid who served generations of heroes from the Clone Wars through the Resistance.",
            Color = "#3b82f6",
        },
        new()
        {
            Name = "Rey",
            Slug = "rey",
            Route = "characters/rey",
            Role = "Scavenger",
            Description = "A Jakku scavenger who discovered her connection to the Force and confronted the legacy of the Sith.",
            Color = "#fbbf24",
        },
        new()
        {
            Name = "Ric Olié",
            Slug = "ric-olie",
            Route = "characters/ric-olie",
            Role = "Naboo Pilot",
            Description = "A veteran Naboo Royal Space Fighter Corps pilot who flew the queen's starship through the blockade and later led Bravo Squadron against the Trade Federation droid control ship.",
            Color = "#818cf8",
        },
        new()
        {
            Name = "Rio Durant",
            Slug = "rio-durant",
            Route = "characters/rio-durant",
            Role = "Ardennian Pilot",
            Description = "A four-armed Ardennian pilot and Beckett crew member whose cheerful competence ended when he was killed during the failed Vandor coaxium robbery.",
            Color = "#38bdf8",
        },
        new()
        {
            Name = "Rose Tico",
            Slug = "rose-tico",
            Route = "characters/rose-tico",
            Role = "Resistance Mechanic",
            Description = "A Canto Bight maintenance worker who joined the Resistance after losing her sister Paige, teaching Finn that saving what you love matters more than destroying what you hate.",
            Color = "#f472b6",
        },
        new()
        {
            Name = "Rush Clovis",
            Slug = "rush-clovis",
            Route = "characters/rush-clovis",
            Role = "Banking Clan Senator",
            Description = "A charismatic InterGalactic Banking Clan operative entangled with Padmé Amidala and Anakin Skywalker's jealousy, whose schemes drew him into Separatist finance and a fatal conspiracy.",
            Color = "#94a3b8",
        },
        new()
        {
            Name = "Sabine Wren",
            Slug = "sabine-wren",
            Route = "characters/sabine-wren",
            Role = "Mandalorian Artist",
            Description = "A Mandalorian explosives expert and graffiti artist who helped ignite the rebellion on Lothal.",
            Color = "#ec4899",
        },
        new()
        {
            Name = "Satele Shan",
            Slug = "satele-shan",
            Route = "characters/satele-shan",
            Role = "Jedi Grand Master",
            Description = "A legendary Jedi Battle Meditation master who led the Republic against the resurgent Sith Empire and later served as Grand Master during the Great Galactic War era.",
            Color = "#1d4ed8",
        },
        new()
        {
            Name = "Satine Kryze",
            Slug = "satine-kryze",
            Route = "characters/satine-kryze",
            Role = "Duchess of Mandalore",
            Description = "The pacifist ruler of Mandalore who fought to keep her world neutral during the Clone Wars.",
            Color = "#06b6d4",
        },
        new()
        {
            Name = "Saw Gerrera",
            Slug = "saw-gerrera",
            Route = "characters/saw-gerrera",
            Role = "Partisan Leader",
            Description = "An Onderonian freedom fighter whose extremist methods made him both ally and liability to the Rebellion.",
            Color = "#78716c",
        },
        new()
        {
            Name = "Sebulba",
            Slug = "sebulba",
            Route = "characters/sebulba",
            Role = "Podracer Pilot",
            Description = "A ruthless Dug podracing champion on Tatooine who sabotaged rivals and nearly killed Anakin Skywalker during the Boonta Eve Classic before the young human won against all odds.",
            Color = "#7c3aed",
        },
        new()
        {
            Name = "Shmi Skywalker",
            Slug = "shmi-skywalker",
            Route = "characters/shmi-skywalker",
            Role = "Moisture Farmer",
            Description = "Anakin Skywalker's devoted mother who endured slavery on Tatooine with quiet strength, believing in her son's goodness until her death at the hands of Tusken Raiders shattered the last tether to his compassion.",
            Color = "#d4a574",
        },
        new()
        {
            Name = "Snap Wexley",
            Slug = "snap-wexley",
            Route = "characters/snap-wexley",
            Role = "Resistance Pilot",
            Description = "A veteran Rebellion pilot who flew at Endor and later led Black Squadron until his death during the assault on Starkiller Base flying alongside Poe Dameron.",
            Color = "#f97316",
        },
        new()
        {
            Name = "Sy Snootles",
            Slug = "sy-snootles",
            Route = "characters/sy-snootles",
            Role = "Singer",
            Description = "A Pa'lowick singer and spy for the Hutt Clan who infiltrated Ziro's entourage and assassinated him on Teth to protect Jabba's criminal interests.",
            Color = "#ec4899",
        },
        new()
        {
            Name = "T3-M4",
            Slug = "t3-m4",
            Route = "characters/t3-m4",
            Role = "Utility Droid",
            Description = "A custom utility droid who served Revan with hacking skills and unwavering loyalty across the Jedi Civil War.",
            Color = "#60a5fa",
        },
        new()
        {
            Name = "Tech",
            Slug = "tech",
            Route = "characters/tech",
            Role = "Clone Commando",
            Description = "The Bad Batch's genius technician who could slice systems, decode languages, and engineer solutions under fire.",
            Color = "#0ea5e9",
        },
        new()
        {
            Name = "Temmin Wexley",
            Slug = "temmin-wexley",
            Route = "characters/temmin-wexley",
            Role = "Resistance Pilot",
            Description = "Snap Wexley's son and a skilled pilot-mechanic from Akiva who flew with Black Squadron and helped the Resistance against the First Order alongside his droid Mister Bones.",
            Color = "#fb923c",
        },
        new()
        {
            Name = "The Armorer",
            Slug = "the-armorer",
            Route = "characters/the-armorer",
            Role = "Mandalorian Smith",
            Description = "A mysterious Mandalorian keeper of the covert forge on Nevarro who forged Din Djarin's beskar armor and guarded the secrets of the Darksaber and Mandalorian Creed.",
            Color = "#71717a",
        },
        new()
        {
            Name = "Thrawn",
            Slug = "thrawn",
            Route = "characters/thrawn",
            Role = "Grand Admiral",
            Description = "A brilliant Chiss tactician who studied his enemies' art and nearly crushed the Rebellion with methodical precision.",
            Color = "#0369a1",
        },
        new()
        {
            Name = "Tobias Beckett",
            Slug = "tobias-beckett",
            Route = "characters/tobias-beckett",
            Role = "Criminal Mentor",
            Description = "A seasoned outlaw who mentored Han Solo during a coaxium heist before attempting to double-cross the young smuggler and dying on Savareen.",
            Color = "#78716c",
        },
        new()
        {
            Name = "Unkar Plutt",
            Slug = "unkar-plutt",
            Route = "characters/unkar-plutt",
            Role = "Jakku Scrapper",
            Description = "A Crolute junk boss on Jakku who exploited scavengers including Rey for rations until she escaped offworld with BB-8 and Finn toward a destiny among the stars.",
            Color = "#57534e",
        },
        new()
        {
            Name = "Val",
            Slug = "val",
            Route = "characters/val",
            Role = "Professional Thief",
            Description = "Tobias Beckett's partner and wife whose sacrifice during the Vandor train heist forced Beckett down a path of increasingly ruthless survival.",
            Color = "#64748b",
        },
        new()
        {
            Name = "Watto",
            Slug = "watto",
            Route = "characters/watto",
            Role = "Junk Dealer",
            Description = "A Toydarian junk shop owner on Tatooine who owned Anakin and Shmi Skywalker until Qui-Gon Jinn won the boy's freedom in a podrace wager with a rigged chance cube.",
            Color = "#84cc16",
        },
        new()
        {
            Name = "Wedge Antilles",
            Slug = "wedge-antilles",
            Route = "characters/wedge-antilles",
            Role = "Rebel Pilot",
            Description = "A Corellian pilot who survived both Death Star runs and became a founding hero of Rogue Squadron.",
            Color = "#ef4444",
        },
        new()
        {
            Name = "Wrecker",
            Slug = "wrecker",
            Route = "characters/wrecker",
            Role = "Clone Commando",
            Description = "The Bad Batch's powerhouse demolitions expert whose love of explosions was matched only by his loyalty to his squad.",
            Color = "#ea580c",
        },
        new()
        {
            Name = "Zaalbar",
            Slug = "zaalbar",
            Route = "characters/zaalbar",
            Role = "Wookiee Warrior",
            Description = "Mission Vao's loyal Wookiee companion whose life-debt and ferocious strength aided Revan during the Jedi Civil War on Taris and beyond.",
            Color = "#92400e",
        },
        new()
        {
            Name = "Ziro the Hutt",
            Slug = "ziro-the-hutt",
            Route = "characters/ziro-the-hutt",
            Role = "Crime Lord",
            Description = "Jabba the Hutt's flamboyant uncle who conspired with Count Dooku to kidnap Rotta the Huttlet and later paid Sy Snootles to silence him before the galaxy's underworld caught up.",
            Color = "#a855f7",
        },
    ];

    public static Character? GetBySlug(string slug) =>
        Characters.FirstOrDefault(c => c.Slug.Equals(slug, StringComparison.OrdinalIgnoreCase));
}
