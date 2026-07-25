using StarWars.Models;

namespace StarWars.Data;

public static class TheForceTopicData
{
    public static TheForceTopic ConflictBetweenLightAndDark { get; } = new()
    {
        Name = "Conflict between Light & Dark side",
        Slug = "conflict-between-light-and-dark-side",
        Route = "the-force/conflict-between-light-and-dark-side",
        Color = "#a855f7"
    };

    public static IReadOnlyList<TheForceTopic> Topics { get; } =
    [
        new()
        {
            Name = "Lightsaber Forms",
            Slug = "lightsaber-forms",
            Route = "the-force/lightsaber-forms",
            Color = "#60a5fa"
        },
        new()
        {
            Name = "Kyber Crystals",
            Slug = "kyber-crystals",
            Route = "the-force/kyber-crystals",
            Color = "#22d3ee"
        },
        new()
        {
            Name = "Force Creatures",
            Slug = "force-creatures",
            Route = "the-force/force-creatures",
            Color = "#a78bfa"
        },
        new()
        {
            Name = "Jedi Code",
            Slug = "jedi-code",
            Route = "the-force/jedi-code",
            Color = "#22c55e"
        },
        new()
        {
            Name = "Sith Code",
            Slug = "sith-code",
            Route = "the-force/sith-code",
            Color = "#dc2626"
        },
        new()
        {
            Name = "Force Philosophy",
            Slug = "force-philosophy",
            Route = "the-force/force-philosophy",
            Color = "#eab308"
        },
        new()
        {
            Name = "Ancient Force Orders",
            Slug = "ancient-force-orders",
            Route = "the-force/ancient-force-orders",
            Color = "#f97316"
        }
    ];

    public static TheForceTopic? GetBySlug(string slug) =>
        ConflictBetweenLightAndDark.Slug.Equals(slug, StringComparison.OrdinalIgnoreCase)
            ? ConflictBetweenLightAndDark
            : Topics.FirstOrDefault(topic => topic.Slug.Equals(slug, StringComparison.OrdinalIgnoreCase));
}
