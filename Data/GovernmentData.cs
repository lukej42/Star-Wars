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
        new()
        {
            Name = "Separatist Parliament",
            Slug = "separatist-parliament",
            Route = "governments/separatist-parliament",
            Era = "Confederacy of Independent Systems",
            Color = "#3ecfb2",
            Description = "The legislative assembly of the Confederacy of Independent Systems, seated on Raxus Secundus and coordinating secessionist worlds and corporate sponsors.",
        },
        new()
        {
            Name = "Hutt Grand Council",
            Slug = "hutt-grand-council",
            Route = "governments/hutt-grand-council",
            Era = "Hutt Cartel",
            Color = "#84cc16",
            Description = "The council of Hutt kajidic elders that arbitrates clan disputes, trade routes, and syndicate policy across Nal Hutta and the wider Cartel.",
        },
        new()
        {
            Name = "Resistance High Command",
            Slug = "resistance-high-command",
            Route = "governments/resistance-high-command",
            Era = "Resistance",
            Color = "#f97316",
            Description = "The military-political leadership of the Resistance, coordinating cells, fleet assets, and intelligence operations against the First Order without Senate backing.",
        },
        new()
        {
            Name = "Mandalorian Clans",
            Slug = "mandalorian-clans",
            Route = "governments/mandalorian-clans",
            Era = "Mandalorian culture",
            Color = "#64748b",
            Description = "The decentralized council of Mandalorian warrior clans united by the Creed, the Darksaber, and the office of Mand'alor.",
        },
        new()
        {
            Name = "Trade Federation Directorate",
            Slug = "trade-federation-directorate",
            Route = "governments/trade-federation-directorate",
            Era = "Trade Federation",
            Color = "#7c3aed",
            Description = "The Neimoidian corporate directorate that governed Trade Federation commerce, blockades, and private droid armies from Lucrehulk command ships.",
        },
    ];

    public static Government? GetBySlug(string slug) =>
        Governments.FirstOrDefault(g => g.Slug.Equals(slug, StringComparison.OrdinalIgnoreCase));
}
