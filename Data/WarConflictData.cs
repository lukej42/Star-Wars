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
        },
        new()
        {
            Name = "Mandalorian Wars",
            Slug = "mandalorian-wars",
            Route = "wars-conflicts/mandalorian-wars",
            Color = "#64748b"
        },
        new()
        {
            Name = "Great Sith War",
            Slug = "great-sith-war",
            Route = "wars-conflicts/great-sith-war",
            Color = "#dc2626"
        },
        new()
        {
            Name = "Great Galactic War",
            Slug = "great-galactic-war",
            Route = "wars-conflicts/great-galactic-war",
            Color = "#b91c1c"
        },
        new()
        {
            Name = "Stark Hyperspace War",
            Slug = "stark-hyperspace-war",
            Route = "wars-conflicts/stark-hyperspace-war",
            Color = "#f97316"
        },
        new()
        {
            Name = "Hundred-Year Darkness",
            Slug = "hundred-year-darkness",
            Route = "wars-conflicts/hundred-year-darkness",
            Color = "#7c3aed"
        },
        new()
        {
            Name = "New Sith Wars",
            Slug = "new-sith-wars",
            Route = "wars-conflicts/new-sith-wars",
            Color = "#991b1b"
        },
        new()
        {
            Name = "Cold War (First Order)",
            Slug = "cold-war",
            Route = "wars-conflicts/cold-war",
            Color = "#ef4444"
        },
        new()
        {
            Name = "Great War (SWTOR)",
            Slug = "great-war",
            Route = "wars-conflicts/great-war",
            Color = "#2563eb"
        }
    ];

    public static WarConflict? GetBySlug(string slug) =>
        Conflicts.FirstOrDefault(conflict => conflict.Slug.Equals(slug, StringComparison.OrdinalIgnoreCase));
}
