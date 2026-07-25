using StarWars.Models;

namespace StarWars.Data;

public static class MilitaryUnitData
{
    public static IReadOnlyList<MilitaryUnitFaction> Factions { get; } =
    [
        new() { Name = "Confederacy of Independent Systems", Slug = "confederacy-of-independent-systems", Route = "military-units/confederacy-of-independent-systems", Color = "#3ecfb2" },
        new() { Name = "First Order", Slug = "first-order", Route = "military-units/first-order", Color = "#b91c1c" },
        new() { Name = "Galactic Empire", Slug = "galactic-empire", Route = "military-units/galactic-empire", Color = "#9ca3af" },
        new() { Name = "Galactic Republic", Slug = "galactic-republic", Route = "military-units/galactic-republic", Color = "#4a90d9" },
        new() { Name = "Mandalorian", Slug = "mandalorian", Route = "military-units/mandalorian", Color = "#64748b" },
        new() { Name = "New Republic", Slug = "new-republic", Route = "military-units/new-republic", Color = "#ffd166" },
        new() { Name = "Other", Slug = "other", Route = "military-units/other", Color = "#84cc16" },
        new() { Name = "Rebel Alliance", Slug = "rebel-alliance", Route = "military-units/rebel-alliance", Color = "#e85d04" },
        new() { Name = "Resistance", Slug = "resistance", Route = "military-units/resistance", Color = "#f97316" }
    ];

    public static IReadOnlyList<MilitaryUnit> Units { get; } =
    [
        // Galactic Republic
        Unit("galactic-republic", "clone-trooper-corps", "Clone Trooper Corps", "Infantry", "The backbone of the Grand Army of the Republic, cloned on Kamino and deployed across the Clone Wars.", "#4a90d9"),
        Unit("galactic-republic", "arc-troopers", "ARC Troopers", "Special forces", "Advanced Recon Commandos trained for independent missions and high-risk assaults.", "#2563eb"),
        Unit("galactic-republic", "clone-commandos", "Clone Commandos", "Special forces", "Elite squads such as Delta and Clone Force 99 operating behind enemy lines.", "#1d4ed8"),
        Unit("galactic-republic", "501st-legion", "501st Legion", "Legion", "Anakin Skywalker's famed legion, later Vader's Fist under the Empire.", "#3b82f6"),
        Unit("galactic-republic", "212th-battalion", "212th Attack Battalion", "Battalion", "Obi-Wan Kenobi's battalion distinguished by orange markings.", "#60a5fa"),
        Unit("galactic-republic", "wookiee-warriors", "Wookiee Warriors", "Allied infantry", "Kashyyyk defenders fighting alongside clone forces during the Outer Rim sieges.", "#854d0e"),
        Unit("galactic-republic", "republic-navy", "Republic Navy", "Fleet", "Venator-class Star Destroyers, Acclamators, and starfighter wings projecting Republic power.", "#0284c7"),
        Unit("galactic-republic", "jedi-generals", "Jedi Generals", "Command", "Jedi Knights and Masters leading clone armies as generals throughout the Clone Wars.", "#22c55e"),

        // Galactic Empire
        Unit("galactic-empire", "stormtrooper-corps", "Stormtrooper Corps", "Infantry", "White-armored shock troops enforcing Imperial rule across the galaxy.", "#9ca3af"),
        Unit("galactic-empire", "death-troopers", "Death Troopers", "Special forces", "Elite black-armored operatives guarding high-value Imperial projects.", "#374151"),
        Unit("galactic-empire", "scout-troopers", "Scout Troopers", "Reconnaissance", "Speeder bike–mounted troops deployed on forest worlds such as Endor.", "#6b7280"),
        Unit("galactic-empire", "imperial-navy", "Imperial Navy", "Fleet", "Star Destroyers, TIE fighters, and the Executor-class dreadnought projecting terror.", "#64748b"),
        Unit("galactic-empire", "imperial-army", "Imperial Army", "Ground forces", "AT-AT walkers, AT-STs, and garrison battalions occupying worlds.", "#71717a"),
        Unit("galactic-empire", "501st-legion", "501st Legion", "Legion", "Vader's elite legion hunting Jedi and crushing rebellion.", "#52525b"),
        Unit("galactic-empire", "royal-guard", "Emperor's Royal Guard", "Bodyguard", "Crimson-robed protectors of Emperor Palpatine.", "#dc2626"),

        // Rebel Alliance
        Unit("rebel-alliance", "rebel-troopers", "Rebel Troopers", "Infantry", "Volunteer soldiers of the Alliance to Restore the Republic.", "#e85d04"),
        Unit("rebel-alliance", "rebel-pathfinders", "Rebel Pathfinders", "Special forces", "Scarif and Endor assault teams breaching Imperial defenses.", "#ea580c"),
        Unit("rebel-alliance", "rebel-fleet", "Rebel Alliance Navy", "Fleet", "Mon Calamari cruisers, corvettes, and starfighter wings.", "#f97316"),
        Unit("rebel-alliance", "rogue-squadron", "Rogue Squadron", "Starfighter wing", "Elite X-wing pilots including Luke Skywalker and Wedge Antilles.", "#fb923c"),
        Unit("rebel-alliance", "massassi-group", "Massassi Group", "Command", "Rebel cell based on Yavin 4 coordinating major offensives.", "#c2410c"),

        // CIS
        Unit("confederacy-of-independent-systems", "b1-battle-droids", "B1 Battle Droids", "Infantry", "Mass-produced droid soldiers forming the Separatist front line.", "#3ecfb2"),
        Unit("confederacy-of-independent-systems", "super-battle-droids", "B2 Super Battle Droids", "Heavy infantry", "Armored droids with wrist blasters and reinforced plating.", "#14b8a6"),
        Unit("confederacy-of-independent-systems", "droidekas", "Droidekas", "Heavy infantry", "Shielded destroyer droids rolling into combat with twin blasters.", "#0d9488"),
        Unit("confederacy-of-independent-systems", "magna-guards", "IG-100 MagnaGuards", "Bodyguard", "Electrostaff-wielding droids protecting General Grievous.", "#2dd4bf"),
        Unit("confederacy-of-independent-systems", "separatist-navy", "Separatist Navy", "Fleet", "Providence-class destroyers and droid starfighter swarms.", "#5eead4"),
        Unit("confederacy-of-independent-systems", "techno-union-droids", "Techno Union Droids", "Industrial army", "Corporate droid divisions fielded by Techno Union holdings.", "#06b6d4"),

        // First Order
        Unit("first-order", "stormtrooper-corps", "First Order Stormtroopers", "Infantry", "Raised from birth and trained for fanatical loyalty to the First Order.", "#b91c1c"),
        Unit("first-order", "flametroopers", "Flametroopers", "Specialist", "Incinerator troops deployed against entrenched resistance.", "#991b1b"),
        Unit("first-order", "snowtroopers", "Snowtroopers", "Environment specialist", "Cold-weather troops garrisoning Starkiller Base.", "#7f1d1d"),
        Unit("first-order", "first-order-navy", "First Order Navy", "Fleet", "Resurgent-class Star Destroyers and TIE/fo squadrons.", "#ef4444"),
        Unit("first-order", "knights-of-ren", "Knights of Ren", "Force order", "Dark side warriors serving Supreme Leader Snoke and Kylo Ren.", "#450a0a"),

        // Resistance
        Unit("resistance", "resistance-troopers", "Resistance Troopers", "Infantry", "Volunteers opposing the First Order from hidden bases.", "#f97316"),
        Unit("resistance", "resistance-navy", "Resistance Navy", "Fleet", "MC85 cruisers, corvettes, and starfighter squadrons.", "#fb923c"),
        Unit("resistance", "resistance-bombers", "Resistance Bombers", "Starfighter wing", "Cobalt Hammer and other MG-100 StarFortress crews.", "#fdba74"),
        Unit("resistance", "resistance-starfighter-corps", "Resistance Starfighter Corps", "Starfighters", "T-70 X-wings and other craft flown by Poe Dameron and allies.", "#ea580c"),

        // New Republic
        Unit("new-republic", "new-republic-defense-fleet", "New Republic Defense Fleet", "Fleet", "Successor to the Rebel Alliance Navy policing the galaxy.", "#ffd166"),
        Unit("new-republic", "new-republic-soldiers", "New Republic Soldiers", "Infantry", "Peacekeeping troops deployed on member worlds.", "#fbbf24"),
        Unit("new-republic", "rapier-squadron", "Rapier Squadron", "Starfighter wing", "New Republic X-wing pilots including Poe Dameron's early career.", "#f59e0b"),

        // Mandalorian
        Unit("mandalorian", "death-watch", "Death Watch", "Mandalorian clan", "Extremist faction seeking to restore Mandalore's warrior past.", "#64748b"),
        Unit("mandalorian", "nite-owls", "Nite Owls", "Mandalorian clan", "Bo-Katan Kryze's warriors allied against Maul and the Empire.", "#475569"),
        Unit("mandalorian", "mandalorian-super-commandos", "Mandalorian Super Commandos", "Special forces", "Gar Saxon's Imperial-aligned Mandalorian soldiers.", "#334155"),
        Unit("mandalorian", "mandalorian-fleet", "Mandalorian Fleet", "Fleet", "Kom'rk-class fighters and Mandalorian cruisers.", "#94a3b8"),

        // Other — user-requested groups
        Unit("other", "nightsister-warriors", "Nightsister Warriors", "Force cult army", "Dathomir witches wielding magick, staffs, and dark rituals against invaders.", "#84cc16"),
        Unit("other", "gungan-grand-army", "Gungan Grand Army", "Amphibious army", "Boomas, kaadu cavalry, and shielded formations defending Naboo.", "#65a30d"),
        Unit("other", "naboo-royal-security-forces", "Naboo Royal Security Forces", "Planetary defense", "Royal Guard and security detachments protecting Theed and Naboo.", "#4d7c0f"),
        Unit("other", "trade-federation-army", "Trade Federation Army", "Corporate army", "Battle droids and landing craft deployed during the Naboo blockade.", "#a3e635"),
        Unit("other", "hutt-cartel-enforcers", "Hutt Cartel Enforcers", "Criminal army", "Gamorrean guards, bounty hunters, and mercenaries serving the Hutts.", "#bef264"),
        Unit("other", "crimson-dawn-soldiers", "Crimson Dawn Soldiers", "Criminal syndicate", "Maul's shadowy enforcers operating across the underworld.", "#dc2626"),
        Unit("other", "pyke-syndicate-forces", "Pyke Syndicate Forces", "Criminal army", "Pyke guards and spice hauler escorts from Oba Diah.", "#16a34a"),
        Unit("other", "black-sun-enforcers", "Black Sun Enforcers", "Criminal syndicate", "Assassins and soldiers of the galaxy's most feared crime cartel.", "#14532d"),
    ];

    public static MilitaryUnitFaction? GetFactionBySlug(string slug) =>
        Factions.FirstOrDefault(faction => faction.Slug.Equals(slug, StringComparison.OrdinalIgnoreCase));

    public static MilitaryUnit? GetUnitBySlug(string factionSlug, string unitSlug) =>
        Units.FirstOrDefault(unit =>
            unit.FactionSlug.Equals(factionSlug, StringComparison.OrdinalIgnoreCase) &&
            unit.Slug.Equals(unitSlug, StringComparison.OrdinalIgnoreCase));

    public static IReadOnlyList<MilitaryUnit> GetUnitsForFaction(string factionSlug) =>
        Units.Where(unit => unit.FactionSlug.Equals(factionSlug, StringComparison.OrdinalIgnoreCase))
            .OrderBy(unit => unit.Name)
            .ToList();

    private static MilitaryUnit Unit(string factionSlug, string slug, string name, string unitType, string description, string color) =>
        new()
        {
            FactionSlug = factionSlug,
            Slug = slug,
            Name = name,
            UnitType = unitType,
            Description = description,
            Color = color
        };
}
