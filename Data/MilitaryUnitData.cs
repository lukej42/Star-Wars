using StarWars.Models;

namespace StarWars.Data;

public static class MilitaryUnitData
{
    public static IReadOnlyList<MilitaryUnitFaction> Factions { get; } =
    [
        new()
        {
            Name = "Confederacy of Independent Systems",
            Slug = "confederacy-of-independent-systems",
            Route = "military-units/confederacy-of-independent-systems",
            Color = "#3ecfb2"
        },
        new()
        {
            Name = "First Order",
            Slug = "first-order",
            Route = "military-units/first-order",
            Color = "#b91c1c"
        },
        new()
        {
            Name = "Galactic Empire",
            Slug = "galactic-empire",
            Route = "military-units/galactic-empire",
            Color = "#9ca3af"
        },
        new()
        {
            Name = "Galactic Republic",
            Slug = "galactic-republic",
            Route = "military-units/galactic-republic",
            Color = "#4a90d9"
        },
        new()
        {
            Name = "Mandalorian",
            Slug = "mandalorian",
            Route = "military-units/mandalorian",
            Color = "#64748b"
        },
        new()
        {
            Name = "New Republic",
            Slug = "new-republic",
            Route = "military-units/new-republic",
            Color = "#ffd166"
        },
        new()
        {
            Name = "Other",
            Slug = "other",
            Route = "military-units/other",
            Color = "#84cc16"
        },
        new()
        {
            Name = "Rebel Alliance",
            Slug = "rebel-alliance",
            Route = "military-units/rebel-alliance",
            Color = "#e85d04"
        },
        new()
        {
            Name = "Resistance",
            Slug = "resistance",
            Route = "military-units/resistance",
            Color = "#f97316"
        }
    ];

    public static MilitaryUnitFaction? GetBySlug(string slug) =>
        Factions.FirstOrDefault(faction => faction.Slug.Equals(slug, StringComparison.OrdinalIgnoreCase));
}
