using StarWars.Models;

namespace StarWars.Data;

public static class VehicleData
{
    public static IReadOnlyList<MilitaryVehicle> Vehicles { get; } =
    [
        // Galactic Republic — Ground
        new()
        {
            Name = "All Terrain Tactical Enforcer",
            Slug = "at-te",
            FactionSlug = "galactic-republic",
            Type = MilitaryVehicleType.Ground,
            VehicleClass = "Walker",
            Description = "Six-legged Republic assault walker whose massed laser turrets and troop pods defined Clone Wars battlefield breakthroughs from Geonosis to Utapau.",
            Color = "#4a90d9",
        },
        new()
        {
            Name = "All Terrain Recon Transport",
            Slug = "at-rt",
            FactionSlug = "galactic-republic",
            Type = MilitaryVehicleType.Ground,
            VehicleClass = "Walker",
            Description = "Light scout walker piloted by clone troopers for reconnaissance and rapid flanking strikes across forest and urban war zones.",
            Color = "#2563eb",
        },
        new()
        {
            Name = "Self-Propelled Heavy Artillery Turbolaser",
            Slug = "spha-t",
            FactionSlug = "galactic-republic",
            Type = MilitaryVehicleType.Ground,
            VehicleClass = "Artillery",
            Description = "Tracked turbolaser platform that delivered orbital-range fire support during sieges, including the Battle of Christophsis.",
            Color = "#1d4ed8",
        },
        new()
        {
            Name = "HAVw A6 Juggernaut",
            Slug = "havw-a6-juggernaut",
            FactionSlug = "galactic-republic",
            Type = MilitaryVehicleType.Ground,
            VehicleClass = "Heavy Transport",
            Description = "Ten-wheel heavy assault vehicle serving as mobile command post and troop carrier for extended planetary campaigns.",
            Color = "#3b82f6",
        },
        // Galactic Republic — Air
        new()
        {
            Name = "Low Altitude Assault Transport/infantry",
            Slug = "laat-i",
            FactionSlug = "galactic-republic",
            Type = MilitaryVehicleType.Air,
            VehicleClass = "Gunship",
            Description = "Iconic Republic gunship whose door-mounted turrets and rocket pods ferried clone platoons into hot landing zones across the Clone Wars.",
            Color = "#60a5fa",
        },
        new()
        {
            Name = "Low Altitude Assault Transport/carrier",
            Slug = "laat-c",
            FactionSlug = "galactic-republic",
            Type = MilitaryVehicleType.Air,
            VehicleClass = "Gunship",
            Description = "Cargo variant of the LAAT that deployed AT-TE walkers and speeder bikes from orbit directly into combat theaters.",
            Color = "#93c5fd",
        },
        new()
        {
            Name = "V-19 Torrent Starfighter",
            Slug = "v-19-torrent",
            FactionSlug = "galactic-republic",
            Type = MilitaryVehicleType.Air,
            VehicleClass = "Starfighter",
            Description = "Early-war Republic starfighter bridging the gap between aging Headhunters and the ARC-170 heavy fighters of later campaigns.",
            Color = "#1e40af",
        },
        new()
        {
            Name = "Aggressive ReConnaissance-170 Starfighter",
            Slug = "arc-170",
            FactionSlug = "galactic-republic",
            Type = MilitaryVehicleType.Air,
            VehicleClass = "Starfighter",
            Description = "Heavy three-seat starfighter whose forward cannons and tail gunner protected Republic fleet actions from Muunilinst to Coruscant.",
            Color = "#172554",
        },

        // Confederacy of Independent Systems — Ground
        new()
        {
            Name = "Multi-Troop Transport",
            Slug = "mtt",
            FactionSlug = "confederacy-of-independent-systems",
            Type = MilitaryVehicleType.Ground,
            VehicleClass = "Armored Transport",
            Description = "Trade Federation armored carrier that disgorged hundreds of battle droids through front-mounted deployment racks during planetary invasions.",
            Color = "#3ecfb2",
        },
        new()
        {
            Name = "Armored Assault Tank",
            Slug = "aat",
            FactionSlug = "confederacy-of-independent-systems",
            Type = MilitaryVehicleType.Ground,
            VehicleClass = "Hover Tank",
            Description = "Repulsorlift battle tank whose dual heavy lasers and crew compartment anchored Separatist armored pushes on Felucia and Christophsis.",
            Color = "#14b8a6",
        },
        new()
        {
            Name = "IG-227 Hailfire-class Droid Tank",
            Slug = "hailfire-droid",
            FactionSlug = "confederacy-of-independent-systems",
            Type = MilitaryVehicleType.Ground,
            VehicleClass = "Missile Tank",
            Description = "Wheel-driven droid artillery platform that unleashed volleys of shoulder-fired missiles before retreating at high speed.",
            Color = "#0d9488",
        },
        new()
        {
            Name = "OG-9 Homing Spider Droid",
            Slug = "og-9-spider-droid",
            FactionSlug = "confederacy-of-independent-systems",
            Type = MilitaryVehicleType.Ground,
            VehicleClass = "Walker",
            Description = "Stilt-legged droid walker whose central cannon targeted Republic armor across open battlefields on Geonosis and Mygeeto.",
            Color = "#2dd4bf",
        },
        // Confederacy of Independent Systems — Air
        new()
        {
            Name = "Vulture-class Droid Starfighter",
            Slug = "vulture-droid",
            FactionSlug = "confederacy-of-independent-systems",
            Type = MilitaryVehicleType.Air,
            VehicleClass = "Starfighter",
            Description = "Variable-geometry droid fighter that folded into walking mode for carrier storage before swarming Republic capital ships in massive wings.",
            Color = "#5eead4",
        },
        new()
        {
            Name = "Hyena-class Bomber",
            Slug = "hyena-bomber",
            FactionSlug = "confederacy-of-independent-systems",
            Type = MilitaryVehicleType.Air,
            VehicleClass = "Bomber",
            Description = "Droid bomber that delivered proton payloads against Republic ground columns and hangar installations during orbital assaults.",
            Color = "#115e59",
        },
        new()
        {
            Name = "Droid Tri-Fighter",
            Slug = "tri-fighter",
            FactionSlug = "confederacy-of-independent-systems",
            Type = MilitaryVehicleType.Air,
            VehicleClass = "Starfighter",
            Description = "Aggressive three-armed droid interceptor whose clustered engines and buzz droid payloads terrorized clone ace pilots late in the war.",
            Color = "#134e4a",
        },

        // Galactic Empire — Ground
        new()
        {
            Name = "All Terrain Armored Transport",
            Slug = "at-at",
            FactionSlug = "galactic-empire",
            Type = MilitaryVehicleType.Ground,
            VehicleClass = "Walker",
            Description = "Four-legged Imperial assault walker whose chin cannons and troop bay defined the Empire's ground doctrine from Hoth to Scarif.",
            Color = "#9ca3af",
        },
        new()
        {
            Name = "All Terrain Scout Transport",
            Slug = "at-st",
            FactionSlug = "galactic-empire",
            Type = MilitaryVehicleType.Ground,
            VehicleClass = "Walker",
            Description = "Two-legged scout walker escorting AT-AT formations and patrolling forest worlds like Endor with chin blasters and grenade launchers.",
            Color = "#6b7280",
        },
        new()
        {
            Name = "All Terrain Defense Pod",
            Slug = "at-dp",
            FactionSlug = "galactic-empire",
            Type = MilitaryVehicleType.Ground,
            VehicleClass = "Walker",
            Description = "Light Imperial patrol walker used for urban pacification and garrison security across occupied Core and Mid Rim worlds.",
            Color = "#4b5563",
        },
        new()
        {
            Name = "Imperial Troop Transport",
            Slug = "imperial-troop-transport",
            FactionSlug = "galactic-empire",
            Type = MilitaryVehicleType.Ground,
            VehicleClass = "Repulsorlift Transport",
            Description = "Open-air repulsorlift carrier that deployed stormtrooper squads through city streets and desert outposts under heavy blaster cover.",
            Color = "#374151",
        },
        // Galactic Empire — Air
        new()
        {
            Name = "TIE/ln Space Superiority Starfighter",
            Slug = "tie-fighter",
            FactionSlug = "galactic-empire",
            Type = MilitaryVehicleType.Air,
            VehicleClass = "Starfighter",
            Description = "Standard Imperial starfighter whose twin ion engines and panel wings symbolized the Empire's quantity-over-crew combat philosophy.",
            Color = "#d1d5db",
        },
        new()
        {
            Name = "TIE/sa Bomber",
            Slug = "tie-bomber",
            FactionSlug = "galactic-empire",
            Type = MilitaryVehicleType.Air,
            VehicleClass = "Bomber",
            Description = "Twin-pod Imperial bomber that delivered proton torpedoes against Rebel bases and capital-ship hangar bays with ruthless efficiency.",
            Color = "#e5e7eb",
        },
        new()
        {
            Name = "TIE/in Interceptor",
            Slug = "tie-interceptor",
            FactionSlug = "galactic-empire",
            Type = MilitaryVehicleType.Air,
            VehicleClass = "Starfighter",
            Description = "Late-war Imperial interceptor whose dagger wings and enhanced lasers hunted Rebel starfighters during the Battle of Endor.",
            Color = "#f3f4f6",
        },

        // Rebel Alliance — Ground
        new()
        {
            Name = "T2-B Repulsor Tank",
            Slug = "t2-b-repulsor-tank",
            FactionSlug = "rebel-alliance",
            Type = MilitaryVehicleType.Ground,
            VehicleClass = "Hover Tank",
            Description = "Rebel light tank whose twin blaster turrets supported infantry in hit-and-run strikes against Imperial garrison convoys.",
            Color = "#e85d04",
        },
        new()
        {
            Name = "AAC-1 Speeder Tank",
            Slug = "aac-1-speeder-tank",
            FactionSlug = "rebel-alliance",
            Type = MilitaryVehicleType.Ground,
            VehicleClass = "Hover Tank",
            Description = "Rebel hover tank adapted from civilian chassis with added armor plating for anti-infantry sweeps on forest and desert worlds.",
            Color = "#ea580c",
        },
        new()
        {
            Name = "74-Z Speeder Bike",
            Slug = "74-z-speeder-bike",
            FactionSlug = "rebel-alliance",
            Type = MilitaryVehicleType.Ground,
            VehicleClass = "Speeder Bike",
            Description = "Scout speeder bike used by Rebel pathfinders and Imperial deserters for rapid reconnaissance through dense woodland terrain.",
            Color = "#c2410c",
        },
        new()
        {
            Name = "A-A5 Speeder Truck",
            Slug = "a-a5-speeder-truck",
            FactionSlug = "rebel-alliance",
            Type = MilitaryVehicleType.Ground,
            VehicleClass = "Troop Transport",
            Description = "Armored repulsorlift truck that moved Alliance infantry and supplies between hidden bases under Imperial orbital surveillance.",
            Color = "#9a3412",
        },
        // Rebel Alliance — Air
        new()
        {
            Name = "T-47 Airspeeder",
            Slug = "snowspeeder",
            FactionSlug = "rebel-alliance",
            Type = MilitaryVehicleType.Air,
            VehicleClass = "Airspeeder",
            Description = "Modified Hoth airspeeder whose harpoon and tow cable tactics famously tripped Imperial AT-AT walkers during Echo Base's evacuation.",
            Color = "#fb923c",
        },
        new()
        {
            Name = "T-65 X-wing Starfighter",
            Slug = "x-wing",
            FactionSlug = "rebel-alliance",
            Type = MilitaryVehicleType.Air,
            VehicleClass = "Starfighter",
            Description = "Alliance multi-role starfighter whose S-foil attack profile and proton torpedoes destroyed both Death Stars.",
            Color = "#f97316",
        },
        new()
        {
            Name = "RZ-1 A-wing Interceptor",
            Slug = "a-wing",
            FactionSlug = "rebel-alliance",
            Type = MilitaryVehicleType.Air,
            VehicleClass = "Starfighter",
            Description = "Fastest Alliance interceptor of its era, flown by Green Squadron at Endor to harry Imperial capital ships and TIE swarms.",
            Color = "#fdba74",
        },
        new()
        {
            Name = "UT-60D U-wing Starfighter/Support Craft",
            Slug = "u-wing",
            FactionSlug = "rebel-alliance",
            Type = MilitaryVehicleType.Air,
            VehicleClass = "Gunship",
            Description = "Swing-wing troop gunship that inserted Rogue One strike teams onto Scarif under heavy Imperial shield gate fire.",
            Color = "#fed7aa",
        },

        // First Order — Ground
        new()
        {
            Name = "All Terrain MegaCaliber Six",
            Slug = "at-m6",
            FactionSlug = "first-order",
            Type = MilitaryVehicleType.Ground,
            VehicleClass = "Walker",
            Description = "First Order siege walker armed with a mega-caliber cannon designed to crack Resistance fortress shields on Crait.",
            Color = "#b91c1c",
        },
        new()
        {
            Name = "First Order Treadspeeder",
            Slug = "first-order-treadspeeder",
            FactionSlug = "first-order",
            Type = MilitaryVehicleType.Ground,
            VehicleClass = "Speeder",
            Description = "Single-pilot treaded speeder deployed by First Order stormtroopers for pursuit through urban and industrial combat zones.",
            Color = "#991b1b",
        },
        new()
        {
            Name = "First Order All Terrain Armored Transport",
            Slug = "first-order-at-at",
            FactionSlug = "first-order",
            Type = MilitaryVehicleType.Ground,
            VehicleClass = "Walker",
            Description = "Updated Imperial AT-AT design with heavier armor and upgraded chin cannons fielded during the occupation of Jakku and Crait.",
            Color = "#7f1d1d",
        },
        new()
        {
            Name = "Light Infantry Utility Vehicle",
            Slug = "light-infantry-utility-vehicle",
            FactionSlug = "first-order",
            Type = MilitaryVehicleType.Ground,
            VehicleClass = "Troop Transport",
            Description = "Open-top First Order transport that ferried stormtrooper squads across landing zones during planetary occupation operations.",
            Color = "#dc2626",
        },
        // First Order — Air
        new()
        {
            Name = "TIE/fo Space Superiority Fighter",
            Slug = "tie-fo",
            FactionSlug = "first-order",
            Type = MilitaryVehicleType.Air,
            VehicleClass = "Starfighter",
            Description = "First Order fleet fighter with upgraded solar arrays and deflector shields, replacing the Empire's unshielded TIE/ln design.",
            Color = "#fca5a5",
        },
        new()
        {
            Name = "TIE/sf Space Superiority Fighter",
            Slug = "tie-sf",
            FactionSlug = "first-order",
            Type = MilitaryVehicleType.Air,
            VehicleClass = "Starfighter",
            Description = "Special Forces two-seat TIE with enhanced sensors and weapons, flown by pilots like Poe Dameron's captors on Jakku.",
            Color = "#f87171",
        },
        new()
        {
            Name = "TIE/se Bomber",
            Slug = "tie-se-bomber",
            FactionSlug = "first-order",
            Type = MilitaryVehicleType.Air,
            VehicleClass = "Bomber",
            Description = "First Order bomber whose ordnance bays razed Resistance base perimeters and civilian ports during the war for the Unknown Regions.",
            Color = "#ef4444",
        },

        // Resistance — Ground
        new()
        {
            Name = "V-4X-D Ski Speeder",
            Slug = "v-4x-d-ski-speeder",
            FactionSlug = "resistance",
            Type = MilitaryVehicleType.Ground,
            VehicleClass = "Speeder",
            Description = "Crait salt-flats speeder with stabilizer ski that scraped crimson dust trails while harrying First Order AT-M6 walkers.",
            Color = "#f97316",
        },
        new()
        {
            Name = "Resistance Troop Transport",
            Slug = "resistance-troop-transport",
            FactionSlug = "resistance",
            Type = MilitaryVehicleType.Ground,
            VehicleClass = "Troop Transport",
            Description = "Armored repulsorlift carrier that moved Resistance Marines between hidden outposts when full fleet deployment was impossible.",
            Color = "#fb923c",
        },
        new()
        {
            Name = "CDF-7620 Landspeeder",
            Slug = "cdf-7620-landspeeder",
            FactionSlug = "resistance",
            Type = MilitaryVehicleType.Ground,
            VehicleClass = "Speeder",
            Description = "Modified civilian landspeeder retrofitted with blaster mounts for Resistance cell operations on Mid Rim worlds.",
            Color = "#ea580c",
        },
        // Resistance — Air
        new()
        {
            Name = "T-70 X-wing Starfighter",
            Slug = "t-70-x-wing",
            FactionSlug = "resistance",
            Type = MilitaryVehicleType.Air,
            VehicleClass = "Starfighter",
            Description = "Next-generation X-wing flown by Poe Dameron and Black Squadron, combining updated avionics with the classic S-foil strike profile.",
            Color = "#fdba74",
        },
        new()
        {
            Name = "RZ-2 A-wing Interceptor",
            Slug = "rz-2-a-wing",
            FactionSlug = "resistance",
            Type = MilitaryVehicleType.Air,
            VehicleClass = "Starfighter",
            Description = "Resistance interceptor evolution of the RZ-1, deployed for escort duty and capital-ship harassment during Starkiller Base's destruction.",
            Color = "#fed7aa",
        },
        new()
        {
            Name = "MG-100 StarFortress SF-17",
            Slug = "resistance-bomber",
            FactionSlug = "resistance",
            Type = MilitaryVehicleType.Air,
            VehicleClass = "Bomber",
            Description = "Resistance heavy bomber whose cobalt Vanguard squadrons sacrificed everything to cripple the Fulminatrix dreadnought at D'Qar.",
            Color = "#ffedd5",
        },

        // Mandalorian — Ground
        new()
        {
            Name = "Mandalorian Speeder Bike",
            Slug = "mandalorian-speeder-bike",
            FactionSlug = "mandalorian",
            Type = MilitaryVehicleType.Ground,
            VehicleClass = "Speeder Bike",
            Description = "Beskar-trimmed scout bike used by Mandalorian covert operatives for rapid extraction after bounty hunts and clan skirmishes.",
            Color = "#64748b",
        },
        new()
        {
            Name = "Aka'jor-class Assault Shuttle",
            Slug = "akajor-assault-shuttle",
            FactionSlug = "mandalorian",
            Type = MilitaryVehicleType.Ground,
            VehicleClass = "Shuttle",
            Description = "Mandalorian troop shuttle that lands vertically in tight canyon staging areas before deploying armored infantry in ground assaults.",
            Color = "#475569",
        },
        new()
        {
            Name = "Canderous-class Assault Tank",
            Slug = "canderous-assault-tank",
            FactionSlug = "mandalorian",
            Type = MilitaryVehicleType.Ground,
            VehicleClass = "Hover Tank",
            Description = "Heavy Mandalorian war tank whose mass-driver cannons and beskar-reinforced hull break siege lines on contested Rim worlds.",
            Color = "#334155",
        },
        // Mandalorian — Air
        new()
        {
            Name = "Kom'rk-class Fighter/Transport",
            Slug = "komrk-fighter-transport",
            FactionSlug = "mandalorian",
            Type = MilitaryVehicleType.Air,
            VehicleClass = "Gunship",
            Description = "Rotating-wing Mandalorian gunship flown by Death Watch and later Bo-Katan's Nite Owls for troop insertion and orbital strikes.",
            Color = "#94a3b8",
        },
        new()
        {
            Name = "Gauntlet Starfighter",
            Slug = "gauntlet-starfighter",
            FactionSlug = "mandalorian",
            Type = MilitaryVehicleType.Air,
            VehicleClass = "Starfighter",
            Description = "Mandalorian starfighter with distinctive forked prow flown by Protectors of Concord Dawn and Clan Wren aces.",
            Color = "#cbd5e1",
        },
        new()
        {
            Name = "Fang-class Fighter",
            Slug = "fang-class-fighter",
            FactionSlug = "mandalorian",
            Type = MilitaryVehicleType.Air,
            VehicleClass = "Starfighter",
            Description = "Agile Mandalorian interceptor whose compact frame and heavy cannons suit clan dogfights over Mandalore's shattered cityscapes.",
            Color = "#e2e8f0",
        },

        // Sith Empire — Ground
        new()
        {
            Name = "Sith Imperial Assault Tank",
            Slug = "sith-imperial-assault-tank",
            FactionSlug = "sith-empire",
            Type = MilitaryVehicleType.Ground,
            VehicleClass = "Hover Tank",
            Description = "Sith Empire front-line tank whose dark-side crew doctrines and red-trim hulls spearheaded invasions of Republic border worlds.",
            Color = "#991b1b",
        },
        new()
        {
            Name = "Sith Troop Carrier",
            Slug = "sith-troop-carrier",
            FactionSlug = "sith-empire",
            Type = MilitaryVehicleType.Ground,
            VehicleClass = "Troop Transport",
            Description = "Armored repulsorlift carrier that delivered Sith Imperial troopers into urban breach points during the Great Galactic War.",
            Color = "#7f1d1d",
        },
        new()
        {
            Name = "Mark VI Supremacy-class Land Crawler",
            Slug = "mark-vi-land-crawler",
            FactionSlug = "sith-empire",
            Type = MilitaryVehicleType.Ground,
            VehicleClass = "Siege Walker",
            Description = "Massive Sith siege crawler whose treads and heavy cannons reduced fortified Republic bastions on Alderaan and Corellia.",
            Color = "#450a0a",
        },
        // Sith Empire — Air
        new()
        {
            Name = "Fury-class Imperial Interceptor",
            Slug = "fury-interceptor",
            FactionSlug = "sith-empire",
            Type = MilitaryVehicleType.Air,
            VehicleClass = "Starfighter",
            Description = "Primary Sith Empire interceptor flown by Imperial pilots and Sith acolytes during the Old Republic galactic wars.",
            Color = "#b91c1c",
        },
        new()
        {
            Name = "B28 Extinction-class Bomber",
            Slug = "b28-extinction-bomber",
            FactionSlug = "sith-empire",
            Type = MilitaryVehicleType.Air,
            VehicleClass = "Bomber",
            Description = "Sith Empire long-range bomber that delivered fusion payloads against Republic shipyards and orbital defense platforms.",
            Color = "#dc2626",
        },
        new()
        {
            Name = "Sith Imperial Assault Shuttle",
            Slug = "sith-imperial-assault-shuttle",
            FactionSlug = "sith-empire",
            Type = MilitaryVehicleType.Air,
            VehicleClass = "Shuttle",
            Description = "Heavily armed Sith shuttle deploying strike teams and Sith Inquisitors onto captured worlds under escort fighter wings.",
            Color = "#ef4444",
        },
    ];

    public static MilitaryVehicle? GetBySlug(string factionSlug, MilitaryVehicleType type, string slug) =>
        Vehicles.FirstOrDefault(vehicle =>
            vehicle.FactionSlug.Equals(factionSlug, StringComparison.OrdinalIgnoreCase) &&
            vehicle.Type == type &&
            vehicle.Slug.Equals(slug, StringComparison.OrdinalIgnoreCase));

    public static IReadOnlyList<MilitaryVehicle> GetByFaction(string factionSlug) =>
        Vehicles.Where(vehicle => vehicle.FactionSlug.Equals(factionSlug, StringComparison.OrdinalIgnoreCase))
            .OrderBy(vehicle => vehicle.Type)
            .ThenBy(vehicle => vehicle.Name)
            .ToList();

    public static IReadOnlyList<MilitaryVehicle> GetGround(string factionSlug) =>
        Vehicles.Where(vehicle =>
                vehicle.FactionSlug.Equals(factionSlug, StringComparison.OrdinalIgnoreCase) &&
                vehicle.Type == MilitaryVehicleType.Ground)
            .OrderBy(vehicle => vehicle.Name)
            .ToList();

    public static IReadOnlyList<MilitaryVehicle> GetAir(string factionSlug) =>
        Vehicles.Where(vehicle =>
                vehicle.FactionSlug.Equals(factionSlug, StringComparison.OrdinalIgnoreCase) &&
                vehicle.Type == MilitaryVehicleType.Air)
            .OrderBy(vehicle => vehicle.Name)
            .ToList();
}
