using StarWars.Models;

namespace StarWars.Data;

public static class ChroniclesData
{
    public const string GalacticHistoryRoute = "chronicles/galactic-history";

    public static IReadOnlyList<ChronicleEntry> Entries { get; } =
    [
        new()
        {
            Name = "Dawn of the Jedi",
            Slug = "dawn-of-the-jedi",
            Route = "chronicles/galactic-history/dawn-of-the-jedi",
            EraLabel = "Pre-Republic · Je'daii Order",
            Color = "#8b5cf6",
            DateRange = "c. 36,453 BBY – c. 25,000 BBY",
            Description = "The ancient era when Force-sensitive pioneers on Tython first codified Ashla and Bogan, forging the Je'daii Order and the philosophical roots of every Jedi and Sith tradition that followed."
        },
        new()
        {
            Name = "Sith Empire",
            Slug = "old-sith-empire",
            Route = "chronicles/galactic-history/old-sith-empire",
            EraLabel = "Sith Golden Age · Great Hyperspace War",
            Color = "#991b1b",
            DateRange = "c. 6,900 BBY – 5,000 BBY",
            Description = "The rise of Korriban's Sith Lords, Naga Sadow's invasion fleets, and the ancient Sith Empire's dominion over the Outer Rim before its shattering defeat and exile into the Unknown Regions."
        },
        new()
        {
            Name = "Old Republic",
            Slug = "old-republic",
            Route = "chronicles/galactic-history/old-republic",
            EraLabel = "Galactic Republic · Ruusan Reformations",
            Color = "#4a90d9",
            DateRange = "c. 25,000 BBY – c. 1,000 BBY",
            Description = "Millennia of democratic union from the founding of the Galactic Republic through the New Sith Wars, the Rule of Two, and the Ruusan Reformations that reshaped the Jedi Order."
        },
        new()
        {
            Name = "High Republic",
            Slug = "high-republic",
            Route = "chronicles/galactic-history/high-republic",
            EraLabel = "Age of the High Republic",
            Color = "#22c55e",
            DateRange = "c. 500 BBY – c. 100 BBY",
            Description = "A zenith of Jedi idealism and Republic expansion — Starlight Beacons, frontier exploration, and the Nihil marauders who tested whether the light could endure on the galactic frontier."
        },
        new()
        {
            Name = "Fall of the Republic",
            Slug = "fall-of-the-republic",
            Route = "chronicles/galactic-history/fall-of-the-republic",
            EraLabel = "Clone Wars · Order 66",
            Color = "#3ecfb2",
            DateRange = "32 BBY – 19 BBY",
            Description = "The final years of the Republic — Separatist secession, the Clone Wars, Palpatine's long con, and the Jedi Purge that ended a thousand generations of guardians in a single night."
        },
        new()
        {
            Name = "Reign of the Empire",
            Slug = "reign-of-the-empire",
            Route = "chronicles/galactic-history/reign-of-the-empire",
            EraLabel = "Galactic Empire · Dark Times",
            Color = "#9ca3af",
            DateRange = "19 BBY – 4 BBY",
            Description = "Two decades of authoritarian rule under Emperor Palpatine — the Inquisitorius, the Death Star, rebel cells in the shadows, and the machinery of fear that held the galaxy in iron grip."
        },
        new()
        {
            Name = "Age of Rebellion",
            Slug = "age-of-rebellion",
            Route = "chronicles/galactic-history/age-of-rebellion",
            EraLabel = "Rebel Alliance · Galactic Civil War",
            Color = "#dc2626",
            DateRange = "4 BBY – 4 ABY",
            Description = "The Rebel Alliance's fight against the Empire — from hidden bases on Dantooine and Yavin to the thawing of Hoth, the revelation at Cloud City, and the decisive victory at Endor."
        },
        new()
        {
            Name = "New Republic",
            Slug = "new-republic",
            Route = "chronicles/galactic-history/new-republic",
            EraLabel = "Restored Democracy · Imperial Remnants",
            Color = "#ffd166",
            DateRange = "4 ABY – 34 ABY",
            Description = "The restored Republic after Endor — demilitarization, Senate politics, the rise of the Resistance, and the hidden First Order preparing to strike from the Unknown Regions."
        },
        new()
        {
            Name = "Rise of the First Order",
            Slug = "rise-of-the-first-order",
            Route = "chronicles/galactic-history/rise-of-the-first-order",
            EraLabel = "First Order · Cold War",
            Color = "#1e293b",
            DateRange = "34 ABY – 35 ABY",
            Description = "The First Order's emergence from Imperial exile — Starkiller Base, the destruction of Hosnian Prime, and the desperate last stand of the Resistance on Crait and Exegol."
        },
        new()
        {
            Name = "New Jedi Order",
            Slug = "new-jedi-order",
            Route = "chronicles/galactic-history/new-jedi-order",
            EraLabel = "Restored Jedi · Dyad and Legacy",
            Color = "#38bdf8",
            DateRange = "4 ABY – onward",
            Description = "The rebirth of the Jedi after the Sith's final defeat — Luke's academy, its fall, Rey's journey, and the promise of a new generation carrying the Force into an uncertain future."
        }
    ];

    public static ChronicleEntry? GetBySlug(string slug) =>
        Entries.FirstOrDefault(entry => entry.Slug.Equals(slug, StringComparison.OrdinalIgnoreCase));
}
