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
        }
    ];

    public static Faction? GetBySlug(string slug) =>
        Factions.FirstOrDefault(faction => faction.Slug.Equals(slug, StringComparison.OrdinalIgnoreCase));
}
