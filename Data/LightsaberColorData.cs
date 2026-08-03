namespace StarWars.Data;

public static class LightsaberColorData
{
    public static string? GetGlowPath(string category, string slug)
    {
        var color = GetColor(category, slug);
        return color is null ? null : $"/images/lightsaber-glow/{color}.gif?v=2";
    }

    public static string? GetColor(string category, string slug)
    {
        if (!category.Equals("jedi", StringComparison.OrdinalIgnoreCase)
            && !category.Equals("sith", StringComparison.OrdinalIgnoreCase))
        {
            return null;
        }

        if (category.Equals("sith", StringComparison.OrdinalIgnoreCase))
        {
            return "red";
        }

        return JediColors.TryGetValue(slug, out var color) ? color : "blue";
    }

    private static readonly Dictionary<string, string> JediColors = new(StringComparer.OrdinalIgnoreCase)
    {
        ["yoda"] = "green",
        ["qui-gon-jinn"] = "green",
        ["kit-fisto"] = "green",
        ["luke-skywalker"] = "green",
        ["depa-billaba"] = "green",
        ["luminara-unduli"] = "green",
        ["jolee-bindo"] = "green",
        ["kanan-jarrus"] = "green",
        ["ezra-bridger"] = "green",
        ["grogu"] = "green",
        ["mace-windu"] = "purple",
        ["ahsoka-tano"] = "white",
        ["anakin-skywalker"] = "blue",
        ["obi-wan-kenobi"] = "blue",
        ["revan"] = "blue",
        ["bastila-shan"] = "yellow",
    };
}
