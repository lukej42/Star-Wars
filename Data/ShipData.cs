using StarWars.Models;

namespace StarWars.Data;

public static class ShipData
{
    // Colour key: Rebel #e11d48, Empire #64748b, Republic #6366f1, CIS #0891b2,
    // Trade Fed #ca8a04, Naboo #eab308, Mandalorian #0284c7, Smuggler #d97706,
    // Old Republic #2563eb, Sith Empire #991b1b, First Order #334155, Resistance #f97316, Bounty #65a30d

    public static IReadOnlyList<Ship> Ships { get; } =
    [
        new()
        {
            Name = "Acclamator-class Assault Ship",
            Slug = "acclamator-class",
            Route = "ships/acclamator-class",
            Class = "Assault Ship / Star Destroyer",
            Description = "The Republic's first true warship of the Clone Wars, delivering legions of clone troopers to contested worlds under heavy escort.",
            ProductionCount = "~500 units",
            Era = "Clone Wars (22–19 BBY)",
            Color = "#6366f1"
        },
        new()
        {
            Name = "ARC-170 Starfighter",
            Slug = "arc-170",
            Route = "ships/arc-170",
            Class = "Heavy Starfighter",
            Description = "A rugged three-seat fighter that bridged the gap between the Clone Wars and the early Imperial era with heavy shields and torpedoes.",
            ProductionCount = "~150,000 units",
            Era = "Clone Wars (22–19 BBY)",
            Color = "#6366f1"
        },
        new()
        {
            Name = "Arquitens-class Light Cruiser",
            Slug = "arquitens-class",
            Route = "ships/arquitens-class",
            Class = "Light Cruiser",
            Description = "A versatile Imperial patrol vessel used for blockades, convoy escort, and hunting rebel cells across the Outer Rim.",
            ProductionCount = "~1,100 units",
            Era = "Imperial Era (19 BBY–4 ABY)",
            Color = "#64748b"
        },
        new()
        {
            Name = "A-wing (RZ-1)",
            Slug = "a-wing",
            Route = "ships/a-wing",
            Class = "Interceptor",
            Description = "The fastest snubfighter in the Alliance fleet, sacrificing shields for blistering speed in hit-and-run raids.",
            ProductionCount = "~7,500 units",
            Era = "Galactic Civil War (4 BBY–5 ABY)",
            Color = "#e11d48"
        },
        new()
        {
            Name = "B-wing (A/SF-01)",
            Slug = "b-wing",
            Route = "ships/b-wing",
            Class = "Assault Starfighter",
            Description = "An rotating-wing gunship designed to punch holes in Star Destroyer hulls during the Battle of Endor.",
            ProductionCount = "~3,200 units",
            Era = "Galactic Civil War (2 BBY–5 ABY)",
            Color = "#e11d48"
        },
        new()
        {
            Name = "CR90 Corvette",
            Slug = "cr90-corvette",
            Route = "ships/cr90-corvette",
            Class = "Blockade Runner",
            Description = "A fast Alderaanian diplomatic vessel that became the backbone of early Rebel convoys, famously including the Tantive IV.",
            ProductionCount = "~1,400 units",
            Era = "Clone Wars through Galactic Civil War",
            Color = "#e11d48"
        },
        new()
        {
            Name = "Death Star I",
            Slug = "death-star-i",
            Route = "ships/death-star-i",
            Class = "Battle Station",
            Description = "The Empire's planet-killing superweapon, destroyed at Yavin after a proton torpedo struck its thermal exhaust port.",
            ProductionCount = "1 unit",
            Era = "Imperial Era (19 BBY–0 BBY)",
            Color = "#64748b"
        },
        new()
        {
            Name = "Death Star II",
            Slug = "death-star-ii",
            Route = "ships/death-star-ii",
            Class = "Battle Station",
            Description = "An unfinished second battle station orbiting Endor, designed to be fully operational and trap the Rebel fleet.",
            ProductionCount = "1 unit",
            Era = "Galactic Civil War (4 ABY)",
            Color = "#64748b"
        },
        new()
        {
            Name = "Delta-7 Aethersprite",
            Slug = "delta-7",
            Route = "ships/delta-7",
            Class = "Jedi Starfighter",
            Description = "An elegant wedge-shaped interceptor flown by Jedi Knights before the Clone Wars, often paired with a hyperdrive ring.",
            ProductionCount = "~8,000 units",
            Era = "Clone Wars (22–19 BBY)",
            Color = "#6366f1"
        },
        new()
        {
            Name = "Droid Control Ship",
            Slug = "droid-control-ship",
            Route = "ships/droid-control-ship",
            Class = "Command Sphere",
            Description = "A Trade Federation sphere that relayed orders to droid armies across entire invasion fleets during the Naboo blockade.",
            ProductionCount = "~50 units",
            Era = "Clone Wars (32–19 BBY)",
            Color = "#ca8a04"
        },
        new()
        {
            Name = "Ebon Hawk",
            Slug = "ebon-hawk",
            Route = "ships/ebon-hawk",
            Class = "Dynamic-class Freighter",
            Description = "A heavily modified smuggler's freighter that carried Revan and the Jedi Exile across the galaxy during the Jedi Civil War.",
            ProductionCount = "1 known hull (unique refit)",
            Era = "Old Republic (3,956–3,951 BBY)",
            Color = "#2563eb"
        },
        new()
        {
            Name = "Endar Spire",
            Slug = "endar-spire",
            Route = "ships/endar-spire",
            Class = "Hammerhead-class Cruiser",
            Description = "A Republic cruiser destroyed above Taris at the opening of the Jedi Civil War, launching Bastila Shan and Revan's escape pods.",
            ProductionCount = "~120 Hammerhead-class hulls",
            Era = "Old Republic (3,956 BBY)",
            Color = "#2563eb"
        },
        new()
        {
            Name = "ETA-2 Actis Interceptor",
            Slug = "eta-2",
            Route = "ships/eta-2",
            Class = "Jedi Interceptor",
            Description = "The sleek successor to the Delta-7, flown by Obi-Wan Kenobi and Anakin Skywalker in the final days of the Clone Wars.",
            ProductionCount = "~12,000 units",
            Era = "Clone Wars (22–19 BBY)",
            Color = "#6366f1"
        },
        new()
        {
            Name = "Executor-class Star Dreadnought",
            Slug = "executor-class",
            Route = "ships/executor-class",
            Class = "Super Star Destroyer",
            Description = "Darth Vader's flagship and the Empire's most terrifying capital ship, over 19 kilometres long with enough firepower to subjugate systems.",
            ProductionCount = "~13 units",
            Era = "Imperial Era (0 BBY–4 ABY)",
            Color = "#64748b"
        },
        new()
        {
            Name = "First Order Transporter",
            Slug = "first-order-transporter",
            Route = "ships/first-order-transporter",
            Class = "Atmospheric Assault Lander",
            Description = "A heavily armoured troop carrier deployed during the attack on Takodana and the siege of Crait.",
            ProductionCount = "~4,000 units",
            Era = "First Order (34 ABY–35 ABY)",
            Color = "#334155"
        },
        new()
        {
            Name = "Fury-class Imperial Interceptor",
            Slug = "fury-class",
            Route = "ships/fury-class",
            Class = "Imperial Interceptor",
            Description = "The Sith Empire's standard space superiority fighter during the Great Galactic War and Cold War eras.",
            ProductionCount = "~80,000 units",
            Era = "Sith Empire (3,681–3,640 BBY)",
            Color = "#991b1b"
        },
        new()
        {
            Name = "Ghost (VCX-100)",
            Slug = "ghost",
            Route = "ships/ghost",
            Class = "Light Freighter",
            Description = "Hera Syndulla's modified Corellian freighter and mobile base for the Spectres rebel cell on Lothal.",
            ProductionCount = "1 known hull (unique refit)",
            Era = "Imperial Era (5 BBY–1 BBY)",
            Color = "#e11d48"
        },
        new()
        {
            Name = "Gozanti-class Cruiser",
            Slug = "gozanti-class",
            Route = "ships/gozanti-class",
            Class = "Armed Transport",
            Description = "A twin-fuselage Imperial cargo hauler used to ferry TIE fighters and stormtrooper garrisons between worlds.",
            ProductionCount = "~5,500 units",
            Era = "Imperial Era (19 BBY–4 ABY)",
            Color = "#64748b"
        },
        new()
        {
            Name = "GR-75 Medium Transport",
            Slug = "gr-75-transport",
            Route = "ships/gr-75-transport",
            Class = "Medium Transport",
            Description = "A bulky Gallofree Yards hauler that served as the Rebel Alliance's primary logistics lifeline at Hoth and Endor.",
            ProductionCount = "~900 units",
            Era = "Galactic Civil War (2 BBY–5 ABY)",
            Color = "#e11d48"
        },
        new()
        {
            Name = "Hammerhead Corvette",
            Slug = "hammerhead-corvette",
            Route = "ships/hammerhead-corvette",
            Class = "Corvette",
            Description = "An ancient Rendili design revived by the Rebel Alliance, capable of ramming Star Destroyers in desperate fleet actions.",
            ProductionCount = "~60 Rebel refits",
            Era = "Galactic Civil War (2 BBY–5 ABY)",
            Color = "#e11d48"
        },
        new()
        {
            Name = "Harrower-class Dreadnought",
            Slug = "harrower-class",
            Route = "ships/harrower-class",
            Class = "Dreadnought",
            Description = "The backbone of the Sith Imperial Navy during the Great Galactic War, bristling with turbolasers and fighter bays.",
            ProductionCount = "~200 units",
            Era = "Sith Empire (3,681–3,640 BBY)",
            Color = "#991b1b"
        },
        new()
        {
            Name = "Hyena-class Bomber",
            Slug = "hyena-class",
            Route = "ships/hyena-class",
            Class = "Droid Bomber",
            Description = "A Separatist strike bomber derived from vulture droid architecture, used to saturate Republic capital ships.",
            ProductionCount = "~45,000 units",
            Era = "Clone Wars (22–19 BBY)",
            Color = "#0891b2"
        },
        new()
        {
            Name = "Imperial I-class Star Destroyer",
            Slug = "imperial-i-class",
            Route = "ships/imperial-i-class",
            Class = "Star Destroyer",
            Description = "The symbol of Imperial might — a kilometre-long wedge capable of blockading a planet alone.",
            ProductionCount = "~25,000 units (both classes)",
            Era = "Imperial Era (19 BBY–4 ABY)",
            Color = "#64748b"
        },
        new()
        {
            Name = "Imperial II-class Star Destroyer",
            Slug = "imperial-ii-class",
            Route = "ships/imperial-ii-class",
            Class = "Star Destroyer",
            Description = "An upgraded Star Destroyer with heavier weapons and improved command systems, including the Avenger at Hoth.",
            ProductionCount = "~25,000 units (both classes)",
            Era = "Imperial Era (0 BBY–4 ABY)",
            Color = "#64748b"
        },
        new()
        {
            Name = "Immobilizer 418 Interdictor",
            Slug = "interdictor-class",
            Route = "ships/interdictor-class",
            Class = "Interdictor Cruiser",
            Description = "An Imperial cruiser equipped with gravity well projectors to pull ships out of hyperspace and trap fleeing convoys.",
            ProductionCount = "~50 units",
            Era = "Imperial Era (19 BBY–4 ABY)",
            Color = "#64748b"
        },
        new()
        {
            Name = "Invisible Hand",
            Slug = "invisible-hand",
            Route = "ships/invisible-hand",
            Class = "Providence-class Dreadnought",
            Description = "General Grievous's flagship during the Clone Wars, where Chancellor Palpatine was rescued in the Battle of Coruscant.",
            ProductionCount = "~120 Providence-class hulls",
            Era = "Clone Wars (22–19 BBY)",
            Color = "#0891b2"
        },
        new()
        {
            Name = "J-type 327 Naboo Royal Starship",
            Slug = "j-type-327",
            Route = "ships/j-type-327",
            Class = "Royal Cruiser",
            Description = "Queen Amidala's chrome-hulled diplomatic vessel, famously shielded and maintained by Naboo's finest engineers.",
            ProductionCount = "~15 units",
            Era = "Clone Wars (32–19 BBY)",
            Color = "#eab308"
        },
        new()
        {
            Name = "Kom'rk-class Fighter",
            Slug = "komrk-class",
            Route = "ships/komrk-class",
            Class = "Assault Fighter",
            Description = "Mandalorian Gauntlet fighters used by Death Watch and Clan Kryze, capable of atmospheric and space combat.",
            ProductionCount = "~800 units",
            Era = "Clone Wars through Imperial Era",
            Color = "#0284c7"
        },
        new()
        {
            Name = "Lambda-class T-4a Shuttle",
            Slug = "lambda-class",
            Route = "ships/lambda-class",
            Class = "Armed Shuttle",
            Description = "The iconic Imperial shuttle with folding wings, used by dignitaries and the stolen Tydirium at Endor.",
            ProductionCount = "~1,200 units",
            Era = "Imperial Era (19 BBY–4 ABY)",
            Color = "#64748b"
        },
        new()
        {
            Name = "LAAT/i Gunship",
            Slug = "laat-i",
            Route = "ships/laat-i",
            Class = "Republic Gunship",
            Description = "The Republic's primary dropship, ferrying clone troopers and AT-TE walkers into battle across countless war zones.",
            ProductionCount = "~8,500 units",
            Era = "Clone Wars (22–19 BBY)",
            Color = "#6366f1"
        },
        new()
        {
            Name = "Leviathan",
            Slug = "leviathan",
            Route = "ships/leviathan",
            Class = "Interdictor-class Cruiser",
            Description = "Darth Malak's flagship during the Jedi Civil War, a Sith warship that hunted the Ebon Hawk across the Outer Rim.",
            ProductionCount = "~30 Interdictor-class hulls",
            Era = "Old Republic (3,956–3,951 BBY)",
            Color = "#991b1b"
        },
        new()
        {
            Name = "Lucrehulk-class Battleship",
            Slug = "lucrehulk-class",
            Route = "ships/lucrehulk-class",
            Class = "Droid Control Battleship",
            Description = "A converted Trade Federation cargo ring that served as a carrier and command ship for Separatist blockades.",
            ProductionCount = "~220 units",
            Era = "Clone Wars (22–19 BBY)",
            Color = "#ca8a04"
        },
        new()
        {
            Name = "MC80 Star Cruiser",
            Slug = "mc80-cruiser",
            Route = "ships/mc80-cruiser",
            Class = "Star Cruiser",
            Description = "Mon Calamari-built capital ships that formed the backbone of the Rebel fleet, including Admiral Ackbar's Home One.",
            ProductionCount = "~40 units",
            Era = "Galactic Civil War (0 BBY–5 ABY)",
            Color = "#e11d48"
        },
        new()
        {
            Name = "MG-100 StarFortress",
            Slug = "mg-100-bomber",
            Route = "ships/mg-100-bomber",
            Class = "Heavy Bomber",
            Description = "A Resistance bomber that sacrificed itself to destroy the First Order Dreadnought Supremacy above D'Qar.",
            ProductionCount = "~120 units",
            Era = "First Order (34 ABY)",
            Color = "#f97316"
        },
        new()
        {
            Name = "Millennium Falcon",
            Slug = "millennium-falcon",
            Route = "ships/millennium-falcon",
            Class = "YT-1300 Light Freighter",
            Description = "The fastest hunk of junk in the galaxy — Han Solo and Chewbacca's legendary Corellian freighter that made the Kessel Run in less than twelve parsecs.",
            ProductionCount = "1 known hull (unique refit)",
            Era = "Imperial Era through First Order",
            Color = "#d97706"
        },
        new()
        {
            Name = "Munificent-class Frigate",
            Slug = "munificent-class",
            Route = "ships/munificent-class",
            Class = "Frigate",
            Description = "Banking Clan frigates that formed the economic backbone of Separatist fleet actions during the Clone Wars.",
            ProductionCount = "~780 units",
            Era = "Clone Wars (22–19 BBY)",
            Color = "#0891b2"
        },
        new()
        {
            Name = "N-1 Starfighter",
            Slug = "n-1-starfighter",
            Route = "ships/n-1-starfighter",
            Class = "Planetary Starfighter",
            Description = "Naboo's sleek yellow-and-chrome starfighter, flown by Anakin Skywalker in the Battle of Naboo and later by Din Djarin.",
            ProductionCount = "~240 units",
            Era = "Clone Wars through New Republic",
            Color = "#eab308"
        },
        new()
        {
            Name = "Naboo Royal Yacht",
            Slug = "naboo-royal-yacht",
            Route = "ships/naboo-royal-yacht",
            Class = "Diplomatic Yacht",
            Description = "Padmé Amidala's personal J-type yacht used for covert diplomatic missions during the Separatist Crisis.",
            ProductionCount = "~8 units",
            Era = "Clone Wars (22–19 BBY)",
            Color = "#eab308"
        },
        new()
        {
            Name = "Nebulon-B Frigate",
            Slug = "nebulon-b",
            Route = "ships/nebulon-b",
            Class = "Escort Frigate",
            Description = "A Kuat design repurposed by the Rebel Alliance as a medical and command frigate, including the Redemption at Hoth.",
            ProductionCount = "~70 Rebel captures",
            Era = "Galactic Civil War (2 BBY–5 ABY)",
            Color = "#e11d48"
        },
        new()
        {
            Name = "Quasar Fire-class Carrier",
            Slug = "quasar-fire-class",
            Route = "ships/quasar-fire-class",
            Class = "Starfighter Carrier",
            Description = "An Imperial bulk cruiser converted by the Rebels to launch TIE fighters captured during convoy raids.",
            ProductionCount = "~30 Rebel conversions",
            Era = "Galactic Civil War (2 BBY–5 ABY)",
            Color = "#e11d48"
        },
        new()
        {
            Name = "Raider-class Corvette",
            Slug = "raider-class",
            Route = "ships/raider-class",
            Class = "Corvette",
            Description = "A compact Imperial patrol ship designed to hunt down rebel starfighters in tight asteroid fields.",
            ProductionCount = "~600 units",
            Era = "Imperial Era (19 BBY–4 ABY)",
            Color = "#64748b"
        },
        new()
        {
            Name = "Razor Crest",
            Slug = "razor-crest",
            Route = "ships/razor-crest",
            Class = "ST-70 Assault Ship",
            Description = "Din Djarin's gunship, a pre-Imperial design used by Mandalorian bounty hunters to transport bounties and Grogu.",
            ProductionCount = "1 known hull (destroyed)",
            Era = "Imperial Era (9 ABY)",
            Color = "#0284c7"
        },
        new()
        {
            Name = "Recusant-class Destroyer",
            Slug = "recusant-class",
            Route = "ships/recusant-class",
            Class = "Light Destroyer",
            Description = "A thin-hulled Separatist destroyer mass-produced by the Commerce Guild for swarm tactics against Republic fleets.",
            ProductionCount = "~1,100 units",
            Era = "Clone Wars (22–19 BBY)",
            Color = "#0891b2"
        },
        new()
        {
            Name = "Resurgent-class Star Destroyer",
            Slug = "resurgent-class",
            Route = "ships/resurgent-class",
            Class = "Battlecruiser",
            Description = "The First Order's answer to the Imperial Star Destroyer, nearly twice as large and built for terror campaigns.",
            ProductionCount = "~12 units",
            Era = "First Order (34 ABY–35 ABY)",
            Color = "#334155"
        },
        new()
        {
            Name = "Sith Interceptor",
            Slug = "sith-interceptor",
            Route = "ships/sith-interceptor",
            Class = "Heavy Starfighter",
            Description = "A twin-boom interceptor flown by Sith acolytes during the Jedi Civil War, armed with heavy laser cannons.",
            ProductionCount = "~2,500 units",
            Era = "Old Republic (3,956–3,951 BBY)",
            Color = "#991b1b"
        },
        new()
        {
            Name = "Slave I",
            Slug = "slave-i",
            Route = "ships/slave-i",
            Class = "Firespray-31 Patrol Craft",
            Description = "A heavily armed bounty hunter ship with a distinctive vertical profile, flown by Jango and Boba Fett.",
            ProductionCount = "~6 Firespray hulls (most scrapped)",
            Era = "Clone Wars through New Republic",
            Color = "#65a30d"
        },
        new()
        {
            Name = "Snowspeeder (T-47)",
            Slug = "snowspeeder",
            Route = "ships/snowspeeder",
            Class = "Airspeeder",
            Description = "A modified Incom airspeeder armed with tow cables, used by Rogue Group to bring down Imperial walkers at Hoth.",
            ProductionCount = "~38 Hoth deployment",
            Era = "Galactic Civil War (3 ABY)",
            Color = "#e11d48"
        },
        new()
        {
            Name = "TIE Advanced x1",
            Slug = "tie-advanced-x1",
            Route = "ships/tie-advanced-x1",
            Class = "Prototype Starfighter",
            Description = "Darth Vader's custom TIE with hyperdrive and deflector shields, the prototype for the TIE Defender program.",
            ProductionCount = "~4 prototypes",
            Era = "Galactic Civil War (0 BBY–4 ABY)",
            Color = "#64748b"
        },
        new()
        {
            Name = "TIE Bomber",
            Slug = "tie-bomber",
            Route = "ships/tie-bomber",
            Class = "Space Superiority Bomber",
            Description = "A dual-pod Imperial bomber used to flatten rebel bases and deploy orbital mines in fleet engagements.",
            ProductionCount = "~15,000 units",
            Era = "Imperial Era (19 BBY–4 ABY)",
            Color = "#64748b"
        },
        new()
        {
            Name = "TIE Fighter",
            Slug = "tie-fighter",
            Route = "ships/tie-fighter",
            Class = "Space Superiority Fighter",
            Description = "The Empire's mass-produced starfighter — fast, agile, and expendable, with no hyperdrive or shields.",
            ProductionCount = "~4.6 million units",
            Era = "Imperial Era (19 BBY–4 ABY)",
            Color = "#64748b"
        },
        new()
        {
            Name = "TIE Interceptor",
            Slug = "tie-interceptor",
            Route = "ships/tie-interceptor",
            Class = "Interceptor",
            Description = "The Empire's late-war answer to rebel snubfighters, with dagger wings and four laser cannons.",
            ProductionCount = "~240,000 units",
            Era = "Galactic Civil War (0 BBY–4 ABY)",
            Color = "#64748b"
        },
        new()
        {
            Name = "TIE/fo Fighter",
            Slug = "tie-fo",
            Route = "ships/tie-fo",
            Class = "Space Superiority Fighter",
            Description = "The First Order's upgraded TIE with deflector shields and improved avionics for elite pilots.",
            ProductionCount = "~210,000 units",
            Era = "First Order (34 ABY–35 ABY)",
            Color = "#334155"
        },
        new()
        {
            Name = "TIE/sf Fighter",
            Slug = "tie-sf",
            Route = "ships/tie-sf",
            Class = "Special Forces Fighter",
            Description = "A two-seat TIE variant with sensor packages and heavy weapons for First Order special operations.",
            ProductionCount = "~45,000 units",
            Era = "First Order (34 ABY–35 ABY)",
            Color = "#334155"
        },
        new()
        {
            Name = "U-wing",
            Slug = "u-wing",
            Route = "ships/u-wing",
            Class = "Support Gunship",
            Description = "An Incom troop dropship that saw heavy use during the theft of the Death Star plans on Scarif.",
            ProductionCount = "~1,000 units",
            Era = "Galactic Civil War (0 BBY–5 ABY)",
            Color = "#e11d48"
        },
        new()
        {
            Name = "Venator-class Star Destroyer",
            Slug = "venator-class",
            Route = "ships/venator-class",
            Class = "Star Destroyer",
            Description = "The Republic Navy's signature capital ship with dual bridges and a ventral hangar bay for starfighter wings.",
            ProductionCount = "~1,050 units",
            Era = "Clone Wars (22–19 BBY)",
            Color = "#6366f1"
        },
        new()
        {
            Name = "Vulture Droid",
            Slug = "vulture-droid",
            Route = "ships/vulture-droid",
            Class = "Droid Starfighter",
            Description = "A Trade Federation droid fighter that could walk on landing legs or unfold into attack mode in space.",
            ProductionCount = "~150,000 units",
            Era = "Clone Wars (22–19 BBY)",
            Color = "#0891b2"
        },
        new()
        {
            Name = "V-wing",
            Slug = "v-wing",
            Route = "ships/v-wing",
            Class = "Starfighter",
            Description = "A fast arrowhead interceptor that escorted Palpatine's shuttle and became an early Imperial mainstay.",
            ProductionCount = "~7,200 units",
            Era = "Clone Wars (22–19 BBY)",
            Color = "#6366f1"
        },
        new()
        {
            Name = "X-wing (T-65B)",
            Slug = "x-wing",
            Route = "ships/x-wing",
            Class = "Space Superiority Starfighter",
            Description = "The Rebellion's workhorse snubfighter, famous for proton torpedo runs against Death Stars at Yavin and Endor.",
            ProductionCount = "~10,500 units",
            Era = "Galactic Civil War (0 BBY–5 ABY)",
            Color = "#e11d48"
        },
        new()
        {
            Name = "Y-wing (BTL-A4)",
            Slug = "y-wing",
            Route = "ships/y-wing",
            Class = "Assault Starfighter / Bomber",
            Description = "An aging Koensayr bomber stripped to the frame, still capable of delivering crippling ion torpedo strikes.",
            ProductionCount = "~8,000 units",
            Era = "Galactic Civil War (0 BBY–5 ABY)",
            Color = "#e11d48"
        },
        new()
        {
            Name = "YT-2400 Light Freighter",
            Slug = "yt-2400",
            Route = "ships/yt-2400",
            Class = "Light Freighter",
            Description = "A Corellian freighter design similar to the YT-1300, famously flown by Dash Rendar as the Outrider.",
            ProductionCount = "~320 units",
            Era = "Galactic Civil War (3 BBY–4 ABY)",
            Color = "#d97706"
        },
        new()
        {
            Name = "Providence-class Carrier/Destroyer",
            Slug = "providence-class",
            Route = "ships/providence-class",
            Class = "Carrier / Destroyer",
            Description = "General Grievous's flagship class combined droid starfighter wings with heavy turbolasers, epitomizing Separatist fleet doctrine.",
            ProductionCount = "~1,200 units",
            Era = "Clone Wars (22–19 BBY)",
            Color = "#0891b2"
        },
        new()
        {
            Name = "Pelta-class Frigate",
            Slug = "pelta-class",
            Route = "ships/pelta-class",
            Class = "Medical / Support Frigate",
            Description = "Republic Pelta frigates served as hospital ships and command relays, including the frigate that evacuated Ahsoka Tano's wounded.",
            ProductionCount = "~420 units",
            Era = "Clone Wars (22–19 BBY)",
            Color = "#6366f1"
        },
        new()
        {
            Name = "Consular-class Space Cruiser",
            Slug = "consular-class",
            Route = "ships/consular-class",
            Class = "Diplomatic Cruiser",
            Description = "The Radiant VII design ferried Jedi and ambassadors until Trade Federation fire destroyed one above Naboo.",
            ProductionCount = "~180 units",
            Era = "Old Republic through Clone Wars",
            Color = "#6366f1"
        },
        new()
        {
            Name = "Victory I-class Star Destroyer",
            Slug = "victory-i-class",
            Route = "ships/victory-i-class",
            Class = "Star Destroyer",
            Description = "Compact Victory-class destroyers bridged Republic-era design to Imperial dominance with ion cannons and heavy armor.",
            ProductionCount = "~4,500 units",
            Era = "Clone Wars through Imperial Era",
            Color = "#64748b"
        },
        new()
        {
            Name = "Victory II-class Star Destroyer",
            Slug = "victory-ii-class",
            Route = "ships/victory-ii-class",
            Class = "Star Destroyer",
            Description = "Victory II variants traded ground assault capacity for improved deep-space patrol endurance in Outer Rim fleets.",
            ProductionCount = "~2,800 units",
            Era = "Imperial Era (19 BBY–4 ABY)",
            Color = "#64748b"
        },
        new()
        {
            Name = "Gladiator-class Star Destroyer",
            Slug = "gladiator-class",
            Route = "ships/gladiator-class",
            Class = "Star Destroyer",
            Description = "Gladiator-class hulls escorted convoys and hunted pirates with hangars for TIE squadrons in tight sectors.",
            ProductionCount = "~800 units",
            Era = "Imperial Era (19 BBY–4 ABY)",
            Color = "#64748b"
        },
        new()
        {
            Name = "Onager-class Star Destroyer",
            Slug = "onager-class",
            Route = "ships/onager-class",
            Class = "Siege Star Destroyer",
            Description = "Onager-class ships mounted axial superlasers capable of cracking planetary shields from orbit.",
            ProductionCount = "~35 units",
            Era = "Imperial Era (0–4 ABY)",
            Color = "#64748b"
        },
        new()
        {
            Name = "Mandator IV-class Siege Dreadnought",
            Slug = "mandator-iv-class",
            Route = "ships/mandator-iv-class",
            Class = "Siege Dreadnought",
            Description = "First Order Mandator IV dreadnoughts bombarded Resistance bases with orbital autocannons from extreme range.",
            ProductionCount = "~12 units",
            Era = "First Order (34 ABY–)",
            Color = "#334155"
        },
        new()
        {
            Name = "Supremacy (Mega-class)",
            Slug = "supremacy",
            Route = "ships/supremacy",
            Class = "Mega-class Star Dreadnought",
            Description = "Snoke's Supremacy served as mobile capital, shipyard, and palace spanning kilometers of First Order fleet command.",
            ProductionCount = "1 unit",
            Era = "First Order (34 ABY–35 ABY)",
            Color = "#334155"
        },
        new()
        {
            Name = "Xyston-class Star Destroyer",
            Slug = "xyston-class",
            Route = "ships/xyston-class",
            Class = "Planet-killer Star Destroyer",
            Description = "Final Order Xyston destroyers mounted axial superlasers to glass worlds in Palpatine's reborn Sith fleet.",
            ProductionCount = "~1,080 units planned",
            Era = "First Order / Sith Eternal (35 ABY)",
            Color = "#991b1b"
        },
        new()
        {
            Name = "MC75 Star Cruiser",
            Slug = "mc75-cruiser",
            Route = "ships/mc75-cruiser",
            Class = "Mon Calamari Cruiser",
            Description = "Profundity-class MC75 cruisers combined starfighter bays with diplomatic suites before conversion to rebel flagships.",
            ProductionCount = "~140 units",
            Era = "Galactic Civil War (0 BBY–4 ABY)",
            Color = "#e11d48"
        },
        new()
        {
            Name = "MC85 Star Cruiser",
            Slug = "mc85-cruiser",
            Route = "ships/mc85-cruiser",
            Class = "Mon Calamari Cruiser",
            Description = "Resistance-era MC85 cruisers like the Raddus carried heavier shields and ion drives for deep-space retreats.",
            ProductionCount = "~25 units",
            Era = "Resistance (34 ABY–35 ABY)",
            Color = "#f97316"
        },
        new()
        {
            Name = "Starhawk-class Battleship",
            Slug = "starhawk-class",
            Route = "ships/starhawk-class",
            Class = "New Republic Battleship",
            Description = "Project Starhawk converted Imperial hulls into ram-capable battleships that could tear Star Destroyers apart.",
            ProductionCount = "~6 units",
            Era = "New Republic (5 ABY–)",
            Color = "#6366f1"
        },
        new()
        {
            Name = "Nebulon-C Escort Frigate",
            Slug = "nebulon-c",
            Route = "ships/nebulon-c",
            Class = "Escort Frigate",
            Description = "Nebulon-C frigates updated the classic EF76 design with better point defense for convoy escort.",
            ProductionCount = "~900 units",
            Era = "New Republic through First Order",
            Color = "#6366f1"
        },
        new()
        {
            Name = "Carrack-class Light Cruiser",
            Slug = "carrack-class",
            Route = "ships/carrack-class",
            Class = "Light Cruiser",
            Description = "Carrack-class cruisers filled gaps between corvettes and Star Destroyers in Imperial picket fleets.",
            ProductionCount = "~750 units",
            Era = "Imperial Era (19 BBY–4 ABY)",
            Color = "#64748b"
        },
        new()
        {
            Name = "Dreadnaught-class Heavy Cruiser",
            Slug = "dreadnaught-class",
            Route = "ships/dreadnaught-class",
            Class = "Heavy Cruiser",
            Description = "Old Republic Dreadnaught hulls were refitted for centuries, forming the Katana fleet and early Imperial lines.",
            ProductionCount = "~2,000 units",
            Era = "Old Republic through Imperial Era",
            Color = "#6366f1"
        },
        new()
        {
            Name = "Subjugator-class Heavy Cruiser",
            Slug = "subjugator-class",
            Route = "ships/subjugator-class",
            Class = "Heavy Cruiser / Ion Battleship",
            Description = "Malevolence-class ships wielded ion cannons that could disable entire fleets before conventional bombardment.",
            ProductionCount = "~4 units",
            Era = "Clone Wars (22–21 BBY)",
            Color = "#0891b2"
        },
        new()
        {
            Name = "Z-95 Headhunter",
            Slug = "z-95-headhunter",
            Route = "ships/z-95-headhunter",
            Class = "Multi-role Starfighter",
            Description = "The Z-95 Headhunter served as the Republic's workhorse snubfighter before ARC-170 and V-wing adoption.",
            ProductionCount = "~110,000 units",
            Era = "Clone Wars (22–19 BBY)",
            Color = "#6366f1"
        },
        new()
        {
            Name = "V-19 Torrent Starfighter",
            Slug = "v-19-torrent",
            Route = "ships/v-19-torrent",
            Class = "Starfighter",
            Description = "V-19 Torrents gave clone pilots a sturdy early-war fighter before Y-wing and ARC-170 specialization.",
            ProductionCount = "~85,000 units",
            Era = "Clone Wars (22–19 BBY)",
            Color = "#6366f1"
        },
        new()
        {
            Name = "E-wing Escort Fighter",
            Slug = "e-wing",
            Route = "ships/e-wing",
            Class = "Escort Starfighter",
            Description = "E-wings were designed to replace X-wings in elite New Republic squadrons with advanced targeting computers.",
            ProductionCount = "~4,500 units",
            Era = "New Republic (5 ABY–)",
            Color = "#6366f1"
        },
        new()
        {
            Name = "T-70 X-wing",
            Slug = "t-70-x-wing",
            Route = "ships/t-70-x-wing",
            Class = "Superiority Starfighter",
            Description = "T-70 X-wings upgraded the T-65 with split wings and modern avionics for Resistance starfighter corps.",
            ProductionCount = "~2,200 units",
            Era = "Resistance (28 ABY–)",
            Color = "#f97316"
        },
        new()
        {
            Name = "RZ-2 A-wing",
            Slug = "rz-2-a-wing",
            Route = "ships/rz-2-a-wing",
            Class = "Interceptor",
            Description = "RZ-2 A-wings refined the RZ-1 with better shields while keeping blistering sublight acceleration.",
            ProductionCount = "~1,800 units",
            Era = "Resistance (28 ABY–)",
            Color = "#f97316"
        },
        new()
        {
            Name = "TIE/d Defender",
            Slug = "tie-defender",
            Route = "ships/tie-defender",
            Class = "Advanced Starfighter",
            Description = "TIE Defenders combined shields, hyperdrive, and tri-wing design in Thrawn's push for elite Imperial squadrons.",
            ProductionCount = "~500 units",
            Era = "Imperial Era (2 BBY–4 ABY)",
            Color = "#64748b"
        },
        new()
        {
            Name = "TIE/rp Reaper",
            Slug = "tie-reaper",
            Route = "ships/tie-reaper",
            Class = "Troop Transport",
            Description = "TIE Reapers inserted death trooper squads and elite infantry with atmospheric landing capability.",
            ProductionCount = "~1,200 units",
            Era = "Imperial Era (0 BBY–4 ABY)",
            Color = "#64748b"
        },
        new()
        {
            Name = "TIE Hunter",
            Slug = "tie-hunter",
            Route = "ships/tie-hunter",
            Class = "Multi-role Starfighter",
            Description = "TIE Hunters mimicked Rebel X-wing layout with Imperial engineering, used in experimental cross-training units.",
            ProductionCount = "~300 units",
            Era = "Galactic Civil War (0 BBY–4 ABY)",
            Color = "#64748b"
        },
        new()
        {
            Name = "Kom'rk-class Fighter/Transport",
            Slug = "komrk-class-fighter",
            Route = "ships/komrk-class-fighter",
            Class = "Gunship / Fighter",
            Description = "Kom'rk-class ships serve Mandalorian super commandos as troop transports and heavy gun platforms.",
            ProductionCount = "~200 units",
            Era = "Clone Wars through Mandalorian Era",
            Color = "#0284c7"
        },
        new()
        {
            Name = "Gauntlet Fighter",
            Slug = "gauntlet-fighter",
            Route = "ships/gauntlet-fighter",
            Class = "Mandalorian Assault Ship",
            Description = "Mandalorian Gauntlet fighters combine heavy weapons with troop deployment for clan warfare and bounty operations.",
            ProductionCount = "~350 units",
            Era = "Clone Wars through Mandalorian Era",
            Color = "#0284c7"
        },
        new()
        {
            Name = "Fang-class Protector",
            Slug = "fang-class",
            Route = "ships/fang-class",
            Class = "Mandalorian Starfighter",
            Description = "Fang fighters give Mandalorian Protectors speed and firepower over Concord Dawn's mesas.",
            ProductionCount = "~120 units",
            Era = "Clone Wars through Galactic Civil War",
            Color = "#0284c7"
        },
        new()
        {
            Name = "Sheathipede-class Shuttle",
            Slug = "sheathipede-class",
            Route = "ships/sheathipede-class",
            Class = "Diplomatic Shuttle",
            Description = "Neimoidian Sheathipede shuttles served Trade Federation VIPs with insectoid styling and minimal armament.",
            ProductionCount = "~2,400 units",
            Era = "Clone Wars (32–19 BBY)",
            Color = "#ca8a04"
        },
        new()
        {
            Name = "Theta-class T-2c Shuttle",
            Slug = "theta-class",
            Route = "ships/theta-class",
            Class = "Executive Shuttle",
            Description = "Theta-class shuttles carried Imperial officials including Palpatine with hidden defensive suites.",
            ProductionCount = "~600 units",
            Era = "Imperial Era (19 BBY–4 ABY)",
            Color = "#64748b"
        },
        new()
        {
            Name = "Nu-class Attack Shuttle",
            Slug = "nu-class",
            Route = "ships/nu-class",
            Class = "Republic Gunship Shuttle",
            Description = "Nu-class shuttles inserted clone commandos and Jedi on covert missions with faster profiles than LAAT gunships.",
            ProductionCount = "~3,500 units",
            Era = "Clone Wars (22–19 BBY)",
            Color = "#6366f1"
        },
        new()
        {
            Name = "Sentinel-class Landing Craft",
            Slug = "sentinel-class",
            Route = "ships/sentinel-class",
            Class = "Imperial Landing Craft",
            Description = "Sentinel landing craft delivered stormtrooper platoons from orbit with armored ramps and heavy support weapons.",
            ProductionCount = "~8,000 units",
            Era = "Imperial Era (19 BBY–4 ABY)",
            Color = "#64748b"
        },
        new()
        {
            Name = "C-9979 Landing Craft",
            Slug = "c-9979",
            Route = "ships/c-9979",
            Class = "Separatist Landing Ship",
            Description = "C-9979 landing ships disgorged droid battalions and MTTs across Naboo, Geonosis, and countless invasion beaches.",
            ProductionCount = "~1,500 units",
            Era = "Clone Wars (32–19 BBY)",
            Color = "#0891b2"
        },
        new()
        {
            Name = "Belbullab-22 Starfighter",
            Slug = "belbullab-22",
            Route = "ships/belbullab-22",
            Class = "Starfighter",
            Description = "General Grievous flew a customized Belbullab-22 named Soulless One, outpacing clone interceptors.",
            ProductionCount = "~800 units",
            Era = "Clone Wars (22–19 BBY)",
            Color = "#0891b2"
        },
        new()
        {
            Name = "Droid Tri-Fighter",
            Slug = "droid-tri-fighter",
            Route = "ships/droid-tri-fighter",
            Class = "Automated Starfighter",
            Description = "Tri-fighters used triple radial arms and buzz droid tactics to overwhelm Jedi starfighter wings.",
            ProductionCount = "~45,000 units",
            Era = "Clone Wars (22–19 BBY)",
            Color = "#0891b2"
        },
        new()
        {
            Name = "Ginivex-class Fanblade Starfighter",
            Slug = "ginivex-class",
            Route = "ships/ginivex-class",
            Class = "Starfighter",
            Description = "Asajj Ventress piloted Ginivex fanblade fighters with distinctive crescent wings and deadly agility.",
            ProductionCount = "~60 units",
            Era = "Clone Wars (22–19 BBY)",
            Color = "#0891b2"
        },
        new()
        {
            Name = "Geonosian Solar Sailer",
            Slug = "geonosian-solar-sailer",
            Route = "ships/geonosian-solar-sailer",
            Class = "Solar Sailer",
            Description = "Count Dooku escaped Geonosis aboard a solar sailer pushed by exotic tachyon streams and collector sails.",
            ProductionCount = "~40 units",
            Era = "Clone Wars (22–19 BBY)",
            Color = "#0891b2"
        },
        new()
        {
            Name = "Punworcca 116-class Sailer",
            Slug = "punworcca-116",
            Route = "ships/punworcca-116",
            Class = "Solar Sailer",
            Description = "Darth Maul traveled in Punworcca 116 sailers with minimal life support and maximum intimidation profile.",
            ProductionCount = "~25 units",
            Era = "Clone Wars (32–19 BBY)",
            Color = "#991b1b"
        },
        new()
        {
            Name = "HWK-290 Light Freighter",
            Slug = "hwk-290",
            Route = "ships/hwk-290",
            Class = "Light Freighter",
            Description = "HWK-290 freighters like the Moldy Crow served smugglers and Kyle Katarn with modular gun mounts.",
            ProductionCount = "~1,100 units",
            Era = "Galactic Civil War (0 BBY–5 ABY)",
            Color = "#d97706"
        },
        new()
        {
            Name = "Action VI Transport",
            Slug = "action-vi",
            Route = "ships/action-vi",
            Class = "Bulk Transport",
            Description = "Action VI transports moved containerized cargo between Core worlds with slow but enormous hold capacity.",
            ProductionCount = "~12,000 units",
            Era = "Old Republic through Imperial Era",
            Color = "#64748b"
        },
        new()
        {
            Name = "Imperial Landing Craft",
            Slug = "imperial-landing-craft",
            Route = "ships/imperial-landing-craft",
            Class = "Atmospheric Landing Craft",
            Description = "Imperial landing barges delivered personnel to occupied cities with imposing wedge profiles and escort wings.",
            ProductionCount = "~6,500 units",
            Era = "Imperial Era (19 BBY–4 ABY)",
            Color = "#64748b"
        },
        new()
        {
            Name = "Braha'tok-class Gunship",
            Slug = "brahatak-class",
            Route = "ships/brahatak-class",
            Class = "Point-defense Gunship",
            Description = "Dornean Braha'tok gunships protected Mon Calamari cruisers with concentrated flak during Endor.",
            ProductionCount = "~220 units",
            Era = "Galactic Civil War (0 BBY–4 ABY)",
            Color = "#e11d48"
        },
        new()
        {
            Name = "MC30c Frigate",
            Slug = "mc30c-frigate",
            Route = "ships/mc30c-frigate",
            Class = "Mon Calamari Frigate",
            Description = "MC30c frigates paired proton torpedo volleys with stealth fields for rebel hit-and-run raids.",
            ProductionCount = "~180 units",
            Era = "Galactic Civil War (2 BBY–4 ABY)",
            Color = "#e11d48"
        },
        new()
        {
            Name = "Bulwark-class Battlecruiser",
            Slug = "bulwark-class",
            Route = "ships/bulwark-class",
            Class = "Separatist Battlecruiser",
            Description = "Bulwark battlecruisers gave the CIS battleship tonnage to challenge Republic Star Destroyers head-on.",
            ProductionCount = "~90 units",
            Era = "Clone Wars (22–19 BBY)",
            Color = "#0891b2"
        },
        new()
        {
            Name = "First Order Dreadnought",
            Slug = "first-order-dreadnought",
            Route = "ships/first-order-dreadnought",
            Class = "Siege Dreadnought",
            Description = "Fulminatrix-class dreadnoughts opened bombardments that stripped planetary shields before invasion fleets arrived.",
            ProductionCount = "~8 units",
            Era = "First Order (34 ABY–)",
            Color = "#334155"
        },
        new()
        {
            Name = "Trident-class Assault Ship",
            Slug = "trident-class",
            Route = "ships/trident-class",
            Class = "Aquatic Assault Ship",
            Description = "Trident drills pierced underwater cities on Mon Cala and Kamino during Separatist amphibious operations.",
            ProductionCount = "~200 units",
            Era = "Clone Wars (22–19 BBY)",
            Color = "#0891b2"
        },
        new()
        {
            Name = "C-ROC Gozanti-class Cruiser",
            Slug = "c-roc-gozanti",
            Route = "ships/c-roc-gozanti",
            Class = "Modified Freighter",
            Description = "C-ROC Gozanti variants expanded cargo jaws for criminal syndicates and Imperial supply convoys.",
            ProductionCount = "~4,000 units",
            Era = "Imperial Era through Mandalorian Era",
            Color = "#64748b"
        },
        new()
        {
            Name = "Khetanna Sail Barge",
            Slug = "khetanna",
            Route = "ships/khetanna",
            Class = "Luxury Sail Barge",
            Description = "Jabba's Khetanna sail barge hosted desert celebrations until Luke Skywalker's rescue mission destroyed it.",
            ProductionCount = "1 notable unit",
            Era = "Galactic Civil War (4 ABY)",
            Color = "#65a30d"
        },
        new()
        {
            Name = "Bantha-II Cargo Skiff",
            Slug = "bantha-ii-skiff",
            Route = "ships/bantha-ii-skiff",
            Class = "Desert Skiff",
            Description = "Bantha-II skiffs moved cargo and prisoners across Tatooine's Dune Sea under Hutt and gang control.",
            ProductionCount = "~8,000 units",
            Era = "Galactic Civil War era",
            Color = "#65a30d"
        },
        new()
        {
            Name = "Star Commuter 2000",
            Slug = "star-commuter-2000",
            Route = "ships/star-commuter-2000",
            Class = "Shuttle Transport",
            Description = "Star Commuter shuttles linked Coruscant's surface districts to orbital terminals for working-class transit.",
            ProductionCount = "~50,000 units",
            Era = "Clone Wars through Imperial Era",
            Color = "#6366f1"
        },
        new()
        {
            Name = "AA-9 Coruscant Freighter",
            Slug = "aa-9-freighter",
            Route = "ships/aa-9-freighter",
            Class = "Orbital Freighter",
            Description = "AA-9 freighters hauled bulk goods between Coruscant's logistics hubs with distinctive stacked container spines.",
            ProductionCount = "~6,000 units",
            Era = "Clone Wars through Imperial Era",
            Color = "#64748b"
        },
        new()
        {
            Name = "G9 Rigger-class Freighter",
            Slug = "g9-rigger",
            Route = "ships/g9-rigger",
            Class = "Light Freighter",
            Description = "Anakin and Ahsoka used the Twilight G9 Rigger on covert missions with jury-rigged stealth systems.",
            ProductionCount = "~900 units",
            Era = "Clone Wars (22–19 BBY)",
            Color = "#6366f1"
        },
        new()
        {
            Name = "Praetorian-class Battlecruiser",
            Slug = "praetorian-class",
            Route = "ships/praetorian-class",
            Class = "Battlecruiser",
            Description = "Imperial Praetorian battlecruisers guarded key Core worlds with heavier firepower than standard line destroyers.",
            ProductionCount = "~120 units",
            Era = "Imperial Era (19 BBY–4 ABY)",
            Color = "#64748b"
        },
        new()
        {
            Name = "Secutor-class Star Destroyer",
            Slug = "secutor-class",
            Route = "ships/secutor-class",
            Class = "Carrier Star Destroyer",
            Description = "Secutor-class hulls prioritized starfighter capacity with twin command towers for fleet coordination.",
            ProductionCount = "~60 units",
            Era = "Imperial Era (19 BBY–4 ABY)",
            Color = "#64748b"
        },
        new()
        {
            Name = "Lancer-class Frigate",
            Slug = "lancer-class",
            Route = "ships/lancer-class",
            Class = "Anti-starfighter Frigate",
            Description = "Lancer frigates bristled with point-defense turbolasers to shred snubfighter wings in fleet engagements.",
            ProductionCount = "~500 units",
            Era = "Imperial Era (19 BBY–4 ABY)",
            Color = "#64748b"
        },
        new()
        {
            Name = "Hardcell-class Transport",
            Slug = "hardcell-class",
            Route = "ships/hardcell-class",
            Class = "Corporate Transport",
            Description = "Techno Union Hardcell transports moved battle droids with exposed engines and vertical landing capability.",
            ProductionCount = "~3,200 units",
            Era = "Clone Wars (22–19 BBY)",
            Color = "#0891b2"
        },
        new()
        {
            Name = "Banking Clan Frigate",
            Slug = "banking-clan-frigate",
            Route = "ships/banking-clan-frigate",
            Class = "Frigate",
            Description = "InterGalactic Banking Clan frigates financed Separatist fleets while officially maintaining neutrality.",
            ProductionCount = "~600 units",
            Era = "Clone Wars (22–19 BBY)",
            Color = "#ca8a04"
        },
        new()
        {
            Name = "Nantex-class Territorial Starfighter",
            Slug = "nantex-class",
            Route = "ships/nantex-class",
            Class = "Geonosian Starfighter",
            Description = "Geonosian Nantex fighters used ring-cockpits and insectile control yokes in defense of droid foundries.",
            ProductionCount = "~25,000 units",
            Era = "Clone Wars (22–19 BBY)",
            Color = "#0891b2"
        },
        new()
        {
            Name = "CloakShape Fighter",
            Slug = "cloakshape-fighter",
            Route = "ships/cloakshape-fighter",
            Class = "Starfighter",
            Description = "CloakShape fighters served pirates and mercenaries with rugged frames predating modern snubfighter doctrine.",
            ProductionCount = "~18,000 units",
            Era = "Old Republic through Galactic Civil War",
            Color = "#d97706"
        },
        new()
        {
            Name = "K-wing Assault Fighter",
            Slug = "k-wing",
            Route = "ships/k-wing",
            Class = "Assault Starfighter",
            Description = "K-wings delivered heavy ordnance in New Republic bombing wings with rotating wing weapons pods.",
            ProductionCount = "~2,800 units",
            Era = "New Republic (5 ABY–)",
            Color = "#6366f1"
        },
        new()
        {
            Name = "H-60 Tempest Bomber",
            Slug = "h-60-tempest",
            Route = "ships/h-60-tempest",
            Class = "Heavy Bomber",
            Description = "First Order Tempest bombers carried magma bombs in wing racks for planetary suppression campaigns.",
            ProductionCount = "~400 units",
            Era = "First Order (34 ABY–)",
            Color = "#334155"
        },
        new()
        {
            Name = "YV-666 Light Freighter",
            Slug = "yv-666",
            Route = "ships/yv-666",
            Class = "Light Freighter",
            Description = "YV-666 freighters like the Hound's Tooth offered bounty hunters armored holds and extended range.",
            ProductionCount = "~700 units",
            Era = "Galactic Civil War through Mandalorian Era",
            Color = "#65a30d"
        },
        new()
        {
            Name = "Nightbrother",
            Slug = "nightbrother",
            Route = "ships/nightbrother",
            Class = "Modified Omidian Nightship",
            Description = "Maul's Nightbrother served as command ship for Shadow Collective raids with brutalist Mandalorian refits.",
            ProductionCount = "1 notable unit",
            Era = "Clone Wars (20–19 BBY)",
            Color = "#991b1b"
        },
        new()
        {
            Name = "IG-2000",
            Slug = "ig-2000",
            Route = "ships/ig-2000",
            Class = "Aggressor-class Assassin Droid Ship",
            Description = "IG-88's IG-2000 pursued the Millennium Falcon with droid-piloted precision and hidden superweapon ambitions.",
            ProductionCount = "4 units",
            Era = "Galactic Civil War (0 BBY–3 ABY)",
            Color = "#65a30d"
        },
        new()
        {
            Name = "Eclipse-class Super Star Destroyer",
            Slug = "eclipse-class",
            Route = "ships/eclipse-class",
            Class = "Super Star Destroyer",
            Description = "Palpatine's Eclipse-class dreadnoughts mounted superlasers and dark-side sanctums in Legends continuity.",
            ProductionCount = "~2 units",
            Era = "Imperial Remnant (10 ABY–)",
            Color = "#991b1b"
        },
        new()
        {
            Name = "World Devastator",
            Slug = "world-devastator",
            Route = "ships/world-devastator",
            Class = "Planet-eating Dreadnought",
            Description = "World Devastators consumed cityscapes to manufacture war materiel for Palpatine's Dark Empire.",
            ProductionCount = "~25 units",
            Era = "Dark Empire (10 ABY)",
            Color = "#991b1b"
        },

    ];

    public static Ship? GetBySlug(string slug) =>
        Ships.FirstOrDefault(ship => ship.Slug.Equals(slug, StringComparison.OrdinalIgnoreCase));
}
