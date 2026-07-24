using StarWars.Models;

namespace StarWars.Data;

public static class TimelineData
{
    public const int ChartMinYear = -40;
    public const int ChartMaxYear = 26000;

    public static IReadOnlyList<TimelineEra> Eras { get; } =
    [
        new()
        {
            Name = "Major Events",
            Slug = "major-events",
            Route = "timelines/major-events",
            DateRange = "25,000 BBY – 35 ABY",
            EraLabel = "Cross-era turning points",
            Description = "The defining moments that reshaped the galaxy — from the founding of the Republic and the Ruusan Reformations to the Battle of Yavin, Order 66, Endor, and the fall of the First Order.",
            Color = "#f59e0b",
            ChartStart = 25000,
            ChartEnd = -35,
            ShowOnChart = false
        },
        new()
        {
            Name = "Republic Era",
            Slug = "republic-era",
            Route = "timelines/republic-era",
            DateRange = "25,000 BBY – 19 BBY",
            EraLabel = "Galactic Republic",
            Description = "More than twenty-five millennia of democratic union — from the early expansion of the Core Worlds through the Ruusan Reformations, the Jedi's golden age, and the slow corruption that Palpatine exploited to end the Republic forever.",
            Color = "#4a90d9",
            ChartStart = 25000,
            ChartEnd = 19
        },
        new()
        {
            Name = "High Republic",
            Slug = "high-republic",
            Route = "timelines/high-republic",
            DateRange = "500 BBY – 100 BBY",
            EraLabel = "Age of the High Republic",
            Description = "A zenith of Jedi idealism and Republic optimism — Starlight Beacons, frontier exploration, and a galaxy confident in peace — until the Nihil and the Drengir revealed how fragile that light could be.",
            Color = "#22c55e",
            ChartStart = 500,
            ChartEnd = 100
        },
        new()
        {
            Name = "Clone Wars",
            Slug = "clone-wars",
            Route = "timelines/clone-wars",
            DateRange = "22 BBY – 19 BBY",
            EraLabel = "Clone Wars",
            Description = "Three years of galactic civil war that consumed the Outer Rim, militarized the Jedi, and delivered the Republic into Palpatine's hands — ending with Order 66 and the birth of the Empire.",
            Color = "#3ecfb2",
            ChartStart = 22,
            ChartEnd = 19
        },
        new()
        {
            Name = "Imperial Era",
            Slug = "imperial-era",
            Route = "timelines/imperial-era",
            DateRange = "19 BBY – 5 ABY",
            EraLabel = "Galactic Empire",
            Description = "Two decades of authoritarian rule under Emperor Palpatine — the Jedi Purge, the Death Star, rebellion in the shadows, and the chain of victories that culminated at Endor and Jakku.",
            Color = "#9ca3af",
            ChartStart = 19,
            ChartEnd = -5
        },
        new()
        {
            Name = "New Republic",
            Slug = "new-republic",
            Route = "timelines/new-republic",
            DateRange = "4 ABY – 34 ABY",
            EraLabel = "New Republic",
            Description = "Thirty years of restored democracy after Endor — demilitarization, Senate politics, Imperial remnants, and the hidden rise of the First Order until Starkiller Base destroyed Hosnian Prime.",
            Color = "#ffd166",
            ChartStart = -4,
            ChartEnd = -34
        },
        new()
        {
            Name = "First Order Era",
            Slug = "first-order-era",
            Route = "timelines/first-order-era",
            DateRange = "28 ABY – 35 ABY",
            EraLabel = "First Order / Resistance",
            Description = "The final crisis of the Skywalker saga — Leia's Resistance, Kylo Ren's First Order, Starkiller Base, and the battle at Exegol that rallied the galaxy against Palpatine's return.",
            Color = "#b91c1c",
            ChartStart = -28,
            ChartEnd = -35
        },
        new()
        {
            Name = "Legends Timeline",
            Slug = "legends-timeline",
            Route = "timelines/legends-timeline",
            DateRange = "25,053 BBY – 138 ABY",
            EraLabel = "Star Wars Legends (EU)",
            Description = "The pre-2014 Expanded Universe — Tales of the Jedi, Old Republic games, Thrawn novels, New Jedi Order, Legacy comics, and decades of parallel storytelling now preserved as Legends.",
            Color = "#8b5cf6",
            ChartStart = 25053,
            ChartEnd = -138,
            ShowOnChart = false
        }
    ];

    public static IReadOnlyList<TimelineEra> ChartEras =>
        Eras.Where(era => era.ShowOnChart).OrderByDescending(era => era.ChartStart).ToList();

    public static TimelineEra? GetBySlug(string slug) =>
        Eras.FirstOrDefault(era => era.Slug.Equals(slug, StringComparison.OrdinalIgnoreCase));
}
