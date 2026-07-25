using StarWars.Models;

namespace StarWars.Data;

public static class WarConflictData
{
    public static IReadOnlyList<WarConflict> Conflicts { get; } =
    [
        new()
        {
            Name = "Clone Wars",
            Slug = "clone-wars",
            Route = "wars-conflicts/clone-wars",
            Color = "#3ecfb2"
        },
        new()
        {
            Name = "Galactic Civil War",
            Slug = "galactic-civil-war",
            Route = "wars-conflicts/galactic-civil-war",
            Color = "#ffd166"
        }
    ];

    public static WarConflict? GetBySlug(string slug) =>
        Conflicts.FirstOrDefault(conflict => conflict.Slug.Equals(slug, StringComparison.OrdinalIgnoreCase));
}
