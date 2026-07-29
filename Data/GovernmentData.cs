using StarWars.Models;

namespace StarWars.Data;

public static class GovernmentData
{
    public static IReadOnlyList<Government> Governments { get; } =
    [
        new()
        {
            Name = "Je'daii Order",
            Slug = "jedaii-order",
            Route = "governments/jedaii-order",
            Era = "Pre-Republic",
            Color = "#8b5cf6",
            Description = "The ancient Force-balanced society of Tython's Temples, governing Je'daii adepts before the Jedi and Sith orders diverged.",
        },
        new()
        {
            Name = "Dark Council",
            Slug = "dark-council",
            Route = "governments/dark-council",
            Era = "Sith Empire",
            Color = "#991b1b",
            Description = "The ruling council of Sith Lords that administered the reconstituted Sith Empire from Dromund Kaas under the Sith Emperor's direction.",
        },
        new()
        {
            Name = "Galactic Senate",
            Slug = "galactic-senate",
            Route = "governments/galactic-senate",
            Era = "Galactic Republic",
            Color = "#4a90d9",
            Description = "The democratic legislature of the Galactic Republic, seated on Coruscant and led by the elected Supreme Chancellor.",
        },
        new()
        {
            Name = "Imperial Ruling Council",
            Slug = "imperial-ruling-council",
            Route = "governments/imperial-ruling-council",
            Era = "Galactic Empire",
            Color = "#64748b",
            Description = "The advisory and administrative body that executed Emperor Palpatine's will across the Imperial bureaucracy and military.",
        },
        new()
        {
            Name = "Alliance Civil Government",
            Slug = "alliance-civil-government",
            Route = "governments/alliance-civil-government",
            Era = "Rebel Alliance",
            Color = "#dc2626",
            Description = "The political structure of the Rebel Alliance, coordinating member worlds and military operations against the Empire.",
        },
        new()
        {
            Name = "New Republic Senate",
            Slug = "new-republic-senate",
            Route = "governments/new-republic-senate",
            Era = "New Republic",
            Color = "#ffd166",
            Description = "The restored democratic senate of the New Republic, rebuilding galactic governance after the Empire's defeat at Endor.",
        },
        new()
        {
            Name = "First Order Supreme Council",
            Slug = "first-order-supreme-council",
            Route = "governments/first-order-supreme-council",
            Era = "First Order",
            Color = "#1e293b",
            Description = "The senior command structure of the First Order, directing military expansion from the Unknown Regions under the Supreme Leader.",
        },
        new()
        {
            Name = "Jedi High Council",
            Slug = "jedi-council",
            Route = "governments/jedi-council",
            Era = "New Jedi Order",
            Color = "#38bdf8",
            Description = "The governing circle of the restored Jedi Order, guiding training and galactic stewardship after the fall of the Sith.",
        },
    ];

    public static Government? GetBySlug(string slug) =>
        Governments.FirstOrDefault(g => g.Slug.Equals(slug, StringComparison.OrdinalIgnoreCase));
}
