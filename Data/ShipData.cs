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
        }
    ];

    public static Ship? GetBySlug(string slug) =>
        Ships.FirstOrDefault(ship => ship.Slug.Equals(slug, StringComparison.OrdinalIgnoreCase));
}
