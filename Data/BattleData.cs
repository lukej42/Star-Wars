using StarWars.Models;

namespace StarWars.Data;

public static class BattleData
{
    public static IReadOnlyList<FamousBattle> Battles { get; } =
    [

        // Clone Wars
        Battle("clone-wars", "battle-of-anaxes", "Battle of Anaxes", "19 BBY", "#0d9488"),
        Battle("clone-wars", "battle-of-boz-pity", "Battle of Boz Pity", "19 BBY", "#0d9488"),
        Battle("clone-wars", "battle-of-cato-neimoidia", "Battle of Cato Neimoidia", "19 BBY", "#2dd4bf"),
        Battle("clone-wars", "battle-of-christophsis", "Battle of Christophsis", "22 BBY", "#3ecfb2"),
        Battle("clone-wars", "battle-of-coruscant", "Battle of Coruscant", "19 BBY", "#14b8a6"),
        Battle("clone-wars", "battle-of-felucia", "Battle of Felucia", "19 BBY", "#3ecfb2"),
        Battle("clone-wars", "battle-of-kashyyyk", "Battle of Kashyyyk", "19 BBY", "#2dd4bf"),
        Battle("clone-wars", "battle-of-malastare", "Battle of Malastare", "21 BBY", "#14b8a6"),
        Battle("clone-wars", "battle-of-mon-cala", "Battle of Mon Cala", "20 BBY", "#06b6d4"),
        Battle("clone-wars", "battle-of-mygeeto", "Battle of Mygeeto", "19 BBY", "#06b6d4"),
        Battle("clone-wars", "battle-of-quell", "Battle of Quell", "22 BBY", "#3ecfb2"),
        Battle("clone-wars", "battle-of-ringo-vinda", "Battle of Ringo Vinda", "19 BBY", "#5eead4"),
        Battle("clone-wars", "battle-of-ryloth", "Battle of Ryloth", "22 BBY", "#14b8a6"),
        Battle("clone-wars", "battle-of-saleucami", "Battle of Saleucami", "19 BBY", "#14b8a6"),
        Battle("clone-wars", "battle-of-sullust", "Battle of Sullust", "20 BBY", "#06b6d4"),
        Battle("clone-wars", "battle-of-umbara", "Battle of Umbara", "20 BBY", "#2dd4bf"),
        Battle("clone-wars", "battle-of-utapau", "Battle of Utapau", "19 BBY", "#0d9488"),
        Battle("clone-wars", "defense-of-kamino", "Defense of Kamino", "21 BBY", "#5eead4"),
        Battle("clone-wars", "first-battle-of-geonosis", "First Battle of Geonosis", "22 BBY", "#3ecfb2"),
        Battle("clone-wars", "jedi-purge", "Jedi Purge", "19 BBY", "#991b1b"),
        Battle("clone-wars", "second-battle-of-geonosis", "Second Battle of Geonosis", "21 BBY", "#0d9488"),
        Battle("clone-wars", "siege-of-mandalore", "Siege of Mandalore", "19 BBY", "#5eead4"),

        // Galactic Civil War
        Battle("galactic-civil-war", "assault-on-cloud-city", "Assault on Cloud City", "3 ABY", "#fde047"),
        Battle("galactic-civil-war", "battle-of-atollon", "Battle of Atollon", "2 BBY", "#ffd166"),
        Battle("galactic-civil-war", "battle-of-endor", "Battle of Endor", "4 ABY", "#f59e0b"),
        Battle("galactic-civil-war", "battle-of-hoth", "Battle of Hoth", "3 ABY", "#fbbf24"),
        Battle("galactic-civil-war", "battle-of-jakku", "Battle of Jakku", "5 ABY", "#ca8a04"),
        Battle("galactic-civil-war", "battle-of-kessel", "Battle of Kessel", "10 BBY", "#fde047"),
        Battle("galactic-civil-war", "battle-of-mimban", "Battle of Mimban", "10 BBY", "#ca8a04"),
        Battle("galactic-civil-war", "battle-of-scarif", "Battle of Scarif", "0 BBY", "#eab308"),
        Battle("galactic-civil-war", "battle-of-yavin", "Battle of Yavin", "0 BBY", "#ffd166"),
        Battle("galactic-civil-war", "battle-on-eadu", "Battle on Eadu", "0 BBY", "#eab308"),
        Battle("galactic-civil-war", "defense-of-naboo-galactic-civil-war", "Defense of Naboo (Galactic Civil War)", "4 ABY", "#fbbf24"),
        Battle("galactic-civil-war", "liberation-of-sullust", "Liberation of Sullust", "4 ABY", "#ffd166"),
        Battle("galactic-civil-war", "siege-of-lothal", "Siege of Lothal", "1 BBY", "#fbbf24"),
        Battle("galactic-civil-war", "skirmish-on-jedha", "Skirmish on Jedha", "0 BBY", "#f59e0b"),

        // Mandalorian Wars
        Battle("mandalorian-wars", "assault-on-dantooine-enclave", "Assault on Dantooine Enclave", "3958 BBY", "#71717a"),
        Battle("mandalorian-wars", "battle-of-althir", "Battle of Althir", "3965 BBY", "#52525b"),
        Battle("mandalorian-wars", "battle-of-dxun", "Battle of Dxun", "3963 BBY", "#475569"),
        Battle("mandalorian-wars", "battle-of-jagelland", "Battle of Jagelland", "3964 BBY", "#64748b"),
        Battle("mandalorian-wars", "battle-of-malachor-v", "Battle of Malachor V", "3960 BBY", "#64748b"),
        Battle("mandalorian-wars", "battle-of-onderon-mandalorian-wars", "Battle of Onderon (Mandalorian Wars)", "3962 BBY", "#334155"),
        Battle("mandalorian-wars", "battle-of-serroco", "Battle of Serroco", "3963 BBY", "#64748b"),
        Battle("mandalorian-wars", "battle-of-telos-iv", "Battle of Telos IV", "3958 BBY", "#94a3b8"),
        Battle("mandalorian-wars", "battle-of-vanquo", "Battle of Vanquo", "3963 BBY", "#94a3b8"),
        Battle("mandalorian-wars", "devastation-of-cathar", "Devastation of Cathar", "3973 BBY", "#334155"),
        Battle("mandalorian-wars", "final-confrontation-at-malachor-v", "Final Confrontation at Malachor V", "3960 BBY", "#334155"),
        Battle("mandalorian-wars", "mandalorian-siege-of-taris", "Mandalorian Siege of Taris", "3962 BBY", "#52525b"),
        Battle("mandalorian-wars", "raid-on-cathar-survivors", "Raid on Cathar Survivors", "3963 BBY", "#475569"),
        Battle("mandalorian-wars", "siege-of-rhen-var", "Siege of Rhen Var", "3964 BBY", "#475569"),
        Battle("mandalorian-wars", "siege-of-tar-is", "Siege of Taris", "3962 BBY", "#71717a"),

        // Great Sith War
        Battle("great-sith-war", "assault-on-ossus-library", "Assault on the Ossus Great Library", "3996 BBY", "#ef4444"),
        Battle("great-sith-war", "battle-of-coruscant-great-sith-war", "Battle of Coruscant (Great Sith War)", "3996 BBY", "#b91c1c"),
        Battle("great-sith-war", "battle-of-foerost", "Battle of Foerost", "3996 BBY", "#dc2626"),
        Battle("great-sith-war", "battle-of-kemplex-nine", "Battle of Kemplex IX", "3996 BBY", "#ef4444"),
        Battle("great-sith-war", "battle-of-ossus", "Battle of Ossus", "3996 BBY", "#dc2626"),
        Battle("great-sith-war", "battle-of-yavin-4-exar-kun", "Battle of Yavin 4 (Exar Kun)", "3997 BBY", "#991b1b"),
        Battle("great-sith-war", "battle-of-cyax-system", "Battle of the Cyax System", "3996 BBY", "#dc2626"),
        Battle("great-sith-war", "duel-on-ossus", "Duel on Ossus", "3996 BBY", "#f87171"),
        Battle("great-sith-war", "duel-on-yavin-4-great-sith-war", "Duel on Yavin 4 (Great Sith War)", "3997 BBY", "#f87171"),
        Battle("great-sith-war", "invasion-of-korriban-great-sith-war", "Invasion of Korriban (Great Sith War)", "3996 BBY", "#b91c1c"),
        Battle("great-sith-war", "krath-coup-of-empress-teta", "Krath Coup of Empress Teta", "3997 BBY", "#991b1b"),
        Battle("great-sith-war", "sith-bombardment-of-ambria", "Sith Bombardment of Ambria", "3996 BBY", "#7f1d1d"),
        Battle("great-sith-war", "sith-invasion-of-ossus", "Sith Invasion of Ossus", "3996 BBY", "#7f1d1d"),

        // Great Galactic War
        Battle("great-galactic-war", "battle-of-alderaan-great-galactic-war", "Battle of Alderaan (Great Galactic War)", "3667 BBY", "#dc2626"),
        Battle("great-galactic-war", "battle-of-ilum-great-galactic-war", "Battle of Ilum (Great Galactic War)", "3665 BBY", "#ef4444"),
        Battle("great-galactic-war", "battle-of-manaan-great-galactic-war", "Battle of Manaan (Great Galactic War)", "3667 BBY", "#b91c1c"),
        Battle("great-galactic-war", "battle-of-quesh-great-galactic-war", "Battle of Quesh (Great Galactic War)", "3643 BBY", "#991b1b"),
        Battle("great-galactic-war", "battle-of-tython-great-galactic-war", "Battle of Tython (Great Galactic War)", "3660 BBY", "#ef4444"),
        Battle("great-galactic-war", "battle-of-voss", "Battle of Voss", "3645 BBY", "#dc2626"),
        Battle("great-galactic-war", "invasion-of-ord-mantell", "Invasion of Ord Mantell", "3665 BBY", "#7f1d1d"),
        Battle("great-galactic-war", "recapture-of-korriban", "Recapture of Korriban", "3681 BBY", "#991b1b"),
        Battle("great-galactic-war", "sacking-of-coruscant", "Sacking of Coruscant", "3653 BBY", "#b91c1c"),
        Battle("great-galactic-war", "siege-of-balmorra", "Siege of Balmorra", "3667 BBY", "#f87171"),
        Battle("great-galactic-war", "siege-of-nal-hutta-great-galactic-war", "Siege of Nal Hutta (Great Galactic War)", "3668 BBY", "#dc2626"),
        Battle("great-galactic-war", "sith-assault-on-dromund-kaas", "Sith Assault on Dromund Kaas", "3679 BBY", "#f87171"),
        Battle("great-galactic-war", "sith-invasion-of-taris", "Sith Invasion of Taris", "3683 BBY", "#b91c1c"),
        Battle("great-galactic-war", "sith-victory-at-ziost", "Sith Victory at Ziost", "3685 BBY", "#7f1d1d"),

        // Stark Hyperspace War
        Battle("stark-hyperspace-war", "battle-of-primus-goluud", "Battle of Primus Goluud", "44 BBY", "#fb923c"),
        Battle("stark-hyperspace-war", "battle-of-qika", "Battle of Qika", "44 BBY", "#ea580c"),
        Battle("stark-hyperspace-war", "battle-of-troiken", "Battle of Troiken", "44 BBY", "#f97316"),
        Battle("stark-hyperspace-war", "blockade-of-thyferra", "Blockade of Thyferra", "44 BBY", "#fdba74"),
        Battle("stark-hyperspace-war", "coruscant-financial-crisis", "Coruscant Financial Crisis", "44 BBY", "#c2410c"),
        Battle("stark-hyperspace-war", "jedi-intervention-at-coruscant", "Jedi Intervention at Coruscant", "44 BBY", "#c2410c"),
        Battle("stark-hyperspace-war", "naval-battle-over-troiken", "Naval Battle over Troiken", "44 BBY", "#ea580c"),
        Battle("stark-hyperspace-war", "siege-of-formos", "Siege of Formos", "44 BBY", "#f97316"),
        Battle("stark-hyperspace-war", "stark-alliance-collapse", "Stark Alliance Collapse", "44 BBY", "#fdba74"),
        Battle("stark-hyperspace-war", "stark-hyperspace-ambush-at-taanab", "Stark Hyperspace Ambush at Taanab", "44 BBY", "#fb923c"),

        // Hundred-Year Darkness
        Battle("hundred-year-darkness", "battle-of-corbos", "Battle of Corbos", "6900 BBY", "#7c3aed"),
        Battle("hundred-year-darkness", "battle-of-korriban-ancient", "Battle of Korriban (Ancient)", "6900 BBY", "#8b5cf6"),
        Battle("hundred-year-darkness", "battle-of-tython", "Battle of Tython", "6950 BBY", "#8b5cf6"),
        Battle("hundred-year-darkness", "dark-jedi-uprising-on-coruscant", "Dark Jedi Uprising on Coruscant", "6950 BBY", "#5b21b6"),
        Battle("hundred-year-darkness", "duel-of-the-first-sith", "Duel of the First Sith Lords", "6900 BBY", "#a78bfa"),
        Battle("hundred-year-darkness", "exile-to-korriban", "Exile to Korriban", "6900 BBY", "#7c3aed"),
        Battle("hundred-year-darkness", "fall-of-the-dark-jedi", "Fall of the Dark Jedi", "6900 BBY", "#6d28d9"),
        Battle("hundred-year-darkness", "founding-of-the-sith-empire", "Founding of the Sith Empire", "6900 BBY", "#6d28d9"),
        Battle("hundred-year-darkness", "sith-exodus", "Sith Exodus", "6900 BBY", "#5b21b6"),
        Battle("hundred-year-darkness", "sith-temple-construction-on-korriban", "Sith Temple Construction on Korriban", "6899 BBY", "#a78bfa"),

        // New Sith Wars
        Battle("new-sith-wars", "battle-of-jabiim-new-sith-wars", "Battle of Jabiim (New Sith Wars)", "1032 BBY", "#b91c1c"),
        Battle("new-sith-wars", "battle-of-ruusan", "Battle of Ruusan", "1000 BBY", "#991b1b"),
        Battle("new-sith-wars", "fifth-battle-of-ruusan", "Fifth Battle of Ruusan", "1001 BBY", "#ef4444"),
        Battle("new-sith-wars", "first-battle-of-ruusan", "First Battle of Ruusan", "1010 BBY", "#991b1b"),
        Battle("new-sith-wars", "fourth-battle-of-ruusan", "Fourth Battle of Ruusan", "1001 BBY", "#dc2626"),
        Battle("new-sith-wars", "reformation-of-the-jedi-order", "Reformation of the Jedi Order", "1000 BBY", "#ef4444"),
        Battle("new-sith-wars", "rise-of-darth-bane", "Rise of Darth Bane", "1000 BBY", "#991b1b"),
        Battle("new-sith-wars", "second-battle-of-ruusan", "Second Battle of Ruusan", "1006 BBY", "#7f1d1d"),
        Battle("new-sith-wars", "seventh-battle-of-ruusan", "Seventh Battle of Ruusan", "1000 BBY", "#7f1d1d"),
        Battle("new-sith-wars", "sith-brotherhood-collapse", "Sith Brotherhood Collapse", "1000 BBY", "#dc2626"),
        Battle("new-sith-wars", "sith-lord-skirmish-on-tython", "Sith Lord Skirmish on Tython", "1018 BBY", "#7f1d1d"),
        Battle("new-sith-wars", "sixth-battle-of-ruusan", "Sixth Battle of Ruusan", "1000 BBY", "#450a0a"),
        Battle("new-sith-wars", "third-battle-of-ruusan", "Third Battle of Ruusan", "1002 BBY", "#b91c1c"),
        Battle("new-sith-wars", "thought-bomb-detonation", "Thought Bomb Detonation", "1000 BBY", "#450a0a"),

        // Cold War (First Order)
        Battle("cold-war", "assault-on-starkiller-base-trench", "Assault on Starkiller Base Trench", "34 ABY", "#7f1d1d"),
        Battle("cold-war", "attack-on-ahch-to", "Attack on Ahch-To", "34 ABY", "#dc2626"),
        Battle("cold-war", "battle-of-ajan-kloss", "Battle of Ajan Kloss", "35 ABY", "#ef4444"),
        Battle("cold-war", "battle-of-crait", "Battle of Crait", "34 ABY", "#991b1b"),
        Battle("cold-war", "battle-of-d-qar", "Battle of D'Qar", "34 ABY", "#7f1d1d"),
        Battle("cold-war", "battle-of-exegol", "Battle of Exegol", "35 ABY", "#dc2626"),
        Battle("cold-war", "battle-of-kef-bir", "Battle of Kef Bir", "35 ABY", "#ef4444"),
        Battle("cold-war", "battle-of-kijimi", "Battle of Kijimi", "35 ABY", "#b91c1c"),
        Battle("cold-war", "battle-of-ord-mantell-cold-war", "Battle of Ord Mantell (Cold War)", "34 ABY", "#dc2626"),
        Battle("cold-war", "battle-of-pasaana", "Battle of Pasaana", "35 ABY", "#991b1b"),
        Battle("cold-war", "battle-of-starkiller-base", "Battle of Starkiller Base", "34 ABY", "#b91c1c"),
        Battle("cold-war", "battle-of-takodana", "Battle of Takodana", "34 ABY", "#f87171"),
        Battle("cold-war", "destruction-of-hosnian-prime", "Destruction of Hosnian Prime", "34 ABY", "#ef4444"),
        Battle("cold-war", "siege-of-maz-kanatas-castle", "Siege of Maz Kanata's Castle", "34 ABY", "#f87171"),

        // Great War (SWTOR)
        Battle("great-war", "battle-of-alderaan-great-war", "Battle of Alderaan (Great War)", "3643 BBY", "#1d4ed8"),
        Battle("great-war", "battle-of-corellia", "Battle of Corellia", "3641 BBY", "#2563eb"),
        Battle("great-war", "battle-of-dantooine-great-war", "Battle of Dantooine (Great War)", "3642 BBY", "#60a5fa"),
        Battle("great-war", "battle-of-dromund-kaas-great-war", "Battle of Dromund Kaas (Great War)", "3641 BBY", "#3b82f6"),
        Battle("great-war", "battle-of-hoth-great-war", "Battle of Hoth (Great War)", "3642 BBY", "#1d4ed8"),
        Battle("great-war", "battle-of-ilum-great-war", "Battle of Ilum (Great War)", "3640 BBY", "#3b82f6"),
        Battle("great-war", "battle-of-makeb", "Battle of Makeb", "3638 BBY", "#60a5fa"),
        Battle("great-war", "battle-of-manaan-great-war", "Battle of Manaan (Great War)", "3641 BBY", "#2563eb"),
        Battle("great-war", "battle-of-nal-hutta-great-war", "Battle of Nal Hutta (Great War)", "3640 BBY", "#60a5fa"),
        Battle("great-war", "battle-of-ord-mantell-great-war", "Battle of Ord Mantell (Great War)", "3643 BBY", "#1e40af"),
        Battle("great-war", "battle-of-taris-great-war", "Battle of Taris (Great War)", "3642 BBY", "#2563eb"),
        Battle("great-war", "battle-of-voss-great-war", "Battle of Voss (Great War)", "3641 BBY", "#1d4ed8"),
        Battle("great-war", "battle-of-ziost-great-war", "Battle of Ziost (Great War)", "3636 BBY", "#93c5fd"),
        Battle("great-war", "fall-of-balmorra-great-war", "Fall of Balmorra (Great War)", "3642 BBY", "#93c5fd"),
        Battle("great-war", "siege-of-kaon", "Siege of Kaon", "3641 BBY", "#1e40af"),
        Battle("great-war", "siege-of-kaon-great-war", "Siege of Kaon (Great War)", "3641 BBY", "#3b82f6"),
    ];

    public static FamousBattle? GetBySlug(string slug) =>
        Battles.FirstOrDefault(battle => battle.Slug.Equals(slug, StringComparison.OrdinalIgnoreCase));

    public static IReadOnlyList<FamousBattle> GetByWar(string warSlug) =>
        Battles.Where(battle => battle.WarSlug.Equals(warSlug, StringComparison.OrdinalIgnoreCase))
            .OrderBy(battle => battle.Name)
            .ToList();

    public static IReadOnlyList<FamousBattle> All() => Battles;

    private static FamousBattle Battle(string warSlug, string slug, string name, string era, string color) =>
        new()
        {
            WarSlug = warSlug,
            Slug = slug,
            Name = name,
            Route = $"wars-conflicts/battles/{slug}",
            Era = era,
            Color = color
        };
}
