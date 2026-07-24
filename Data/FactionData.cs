using StarWars.Models;

namespace StarWars.Data;

public static class FactionData
{
    public static IReadOnlyList<Faction> Factions { get; } =
    [
        new()
        {
            Name = "Republic",
            Slug = "republic",
            Route = "factions/republic",
            Era = "Galactic Republic",
            YearsActive = "1,000 BBY – 19 BBY",
            Capital = "Coruscant",
            Government = "Federal democratic republic",
            Description = "For a millennium the Galactic Republic united thousands of star systems under the Senate on Coruscant, with the Jedi Order serving as guardians of peace. Wealth and corruption slowly hollowed its institutions until the Clone Wars fractured the galaxy. Chancellor Palpatine's emergency powers and the war's devastation gave him the pretext to declare the Jedi enemies of the state and reorganize the Republic into the Galactic Empire.",
            Color = "#4a90d9"
        },
        new()
        {
            Name = "Confederacy",
            Slug = "confederacy",
            Route = "factions/confederacy",
            Era = "Confederacy of Independent Systems",
            YearsActive = "24 BBY – 19 BBY",
            Capital = "Raxus Secundus",
            Government = "Confederacy of sovereign systems and megacorporations",
            Description = "Born from decades of grievance against Coruscant's taxation and bureaucracy, the Confederacy united disaffected worlds, Trade Federation interests, and the Banking Clan under Count Dooku. Publicly framed as a fight for self-determination, the movement was secretly bankrolled and directed by Darth Sidious to weaken the Republic. Its droid armies ravaged the Outer Rim until the Clone Wars ended with the Confederacy's collapse and the rise of the Empire.",
            Color = "#3ecfb2"
        },
        new()
        {
            Name = "Empire",
            Slug = "empire",
            Route = "factions/empire",
            Era = "Galactic Empire",
            YearsActive = "19 BBY – 5 ABY",
            Capital = "Coruscant (Imperial Center)",
            Government = "Authoritarian fascist galactic hegemony",
            Description = "Proclaimed by Emperor Palpatine at the end of the Clone Wars, the Galactic Empire replaced democracy with rule by fear. The Imperial Navy, stormtrooper legions, and ISB enforced compliance from the Core to the Rim, while the Death Star embodied the doctrine of terror. Resistance simmered for years before the Rebel Alliance destroyed both Death Stars, leading to the Emperor's death and the Empire's fragmentation at Jakku.",
            Color = "#9ca3af"
        },
        new()
        {
            Name = "Rebel Alliance",
            Slug = "rebel-alliance",
            Route = "factions/rebel-alliance",
            Era = "Alliance to Restore the Republic",
            YearsActive = "2 BBY – 4 ABY",
            Capital = "Mobile (Dantooine, Yavin 4, Hoth, and others)",
            Government = "Coalition of rebel cells and allied worlds",
            Description = "What began as scattered cells of dissidents, senators, and freedom fighters coalesced into the Alliance to Restore the Republic under Mon Mothma's leadership. Supported by Alderaan, Chandrila, and countless hidden bases, the Rebellion struck decisive blows at Scarif, Yavin, and Endor. Though outgunned, its pilots, spies, and soldiers proved that a determined few could topple tyranny and spark the birth of the New Republic.",
            Color = "#e85d04"
        },
        new()
        {
            Name = "New Republic",
            Slug = "new-republic",
            Route = "factions/new-republic",
            Era = "New Republic",
            YearsActive = "4 ABY – 34 ABY",
            Capital = "Chandrila, then Hosnian Prime",
            Government = "Democratic federal republic",
            Description = "Founded in the wake of Endor, the New Republic restored the Senate and sought to dismantle Imperial war machines through demilitarization and diplomacy. Mon Mothma's vision of a peaceful galaxy faced constant pressure from Imperial remnants, warlords, and eventually the First Order. For three decades it held, until the Hosnian system was annihilated by Starkiller Base, shattering the Republic's leadership in a single strike.",
            Color = "#ffd166"
        },
        new()
        {
            Name = "Hutts",
            Slug = "hutts",
            Route = "factions/hutts",
            Era = "Hutt Cartel",
            YearsActive = "c. 15,000 BBY – present",
            Capital = "Nal Hutta / Nar Shaddaa",
            Government = "Criminal kajidic clans and syndicate councils",
            Description = "The Hutts built one of the galaxy's oldest power structures not through fleets or senates but through contracts, bribes, and violence. From palaces on Tatooine to dens on Nar Shaddaa, kajidic families controlled smuggling lanes, slavery, gambling, and bounty hunting. Even the Empire and Republic often tolerated Hutt influence in the Outer Rim, trading stability for a share of the Cartel's shadow economy.",
            Color = "#84cc16"
        },
        new()
        {
            Name = "Sith Empire",
            Slug = "sith-empire",
            Route = "factions/sith-empire",
            Era = "Sith Empire",
            YearsActive = "c. 6,900 BBY – 3,641 BBY",
            Capital = "Korriban, Dromund Kaas, and Ziost",
            Government = "Dark-side theocratic empire ruled by the Sith Emperor",
            Description = "Ancient Sith Lords exiled from the Jedi Order forged empires on Korriban and Dromund Kaas, waging wars that reshaped the galaxy long before the Republic knew their name. From Naga Sadow's invasions to Exar Kun's rebellion and eventually Tenebrae's immortal reign as Vitiate, Sith empires rose on conquest, betrayal, and the dark side. Their legacy endured in hidden tombs, forgotten fleets, and the Rule of Two that would one day destroy the Republic from within.",
            Color = "#dc2626"
        },
        new()
        {
            Name = "First Order",
            Slug = "first-order",
            Route = "factions/first-order",
            Era = "First Order",
            YearsActive = "21 ABY – 35 ABY",
            Capital = "Starkiller Base / mobile command",
            Government = "Military dictatorship and dark-side theocracy",
            Description = "Born from Imperial exiles in the Unknown Regions, the First Order rebuilt Palpatine's doctrine in secret — stormtrooper legions raised from childhood, Resurgent-class dreadnoughts, and Starkiller Base. It annihilated the Hosnian system and nearly crushed the Resistance before Palpatine's hidden fleet on Exegol was defeated.",
            Color = "#b91c1c"
        },
        new()
        {
            Name = "Resistance",
            Slug = "resistance",
            Route = "factions/resistance",
            Era = "Resistance",
            YearsActive = "28 ABY – 35 ABY",
            Capital = "Mobile (D'Qar, Crait, Ajan Kloss, and others)",
            Government = "Private militia under Leia Organa's command",
            Description = "When the New Republic ignored warnings about the First Order, Leia Organa formed the Resistance — pilots, spies, and soldiers fighting without Senate backing. Outgunned and hunted from base to base, they destroyed Starkiller Base and rallied the galaxy at Exegol to finish what the Rebellion started.",
            Color = "#f97316"
        },
        new()
        {
            Name = "Mandalorians",
            Slug = "mandalorians",
            Route = "factions/mandalorians",
            Era = "Mandalorian culture and clans",
            YearsActive = "c. 7,000 BBY – present",
            Capital = "Mandalore (historical; clans scattered after the Purge)",
            Government = "Warrior clans united by the Creed and the Darksaber",
            Description = "Forged in beskar and clan loyalty, Mandalorians have been crusaders, mercenaries, and protectors across millennia. From the Mandalorian-Jedi wars to the Great Purge and Din Djarin's quest to reclaim Mandalore, their armor and Creed outlasted empires that tried to erase them.",
            Color = "#64748b"
        },
        new()
        {
            Name = "Trade Federation",
            Slug = "trade-federation",
            Route = "factions/trade-federation",
            Era = "Trade Federation",
            YearsActive = "c. 350 BBY – 19 BBY",
            Capital = "Corporate fleet (Lucrehulk command ships)",
            Government = "Neimoidian corporate directorate with private droid army",
            Description = "The Trade Federation turned commerce into conquest — blockading Naboo, fielding battle droids by the millions, and bankrolling the Separatist Alliance. Its Neimoidian viceroys wielded Senate influence and Lucrehulk battleships until Darth Vader eliminated its leadership on Mustafar.",
            Color = "#7c3aed"
        }
    ];

    public static Faction? GetBySlug(string slug) =>
        Factions.FirstOrDefault(faction => faction.Slug.Equals(slug, StringComparison.OrdinalIgnoreCase));
}
