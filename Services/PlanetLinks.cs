using StarWars.Data;
using StarWars.Models;

namespace StarWars.Services;

public static class PlanetLinks
{
    public static ProfileLinkItem? FromSlug(string? planetSlug)
    {
        if (string.IsNullOrWhiteSpace(planetSlug))
        {
            return null;
        }

        var planet = GalaxyData.GetBySlug(planetSlug.Trim());
        return planet is null ? null : ToLink(planet);
    }

    public static ProfileLinkItem? FromName(string? planetName)
    {
        if (string.IsNullOrWhiteSpace(planetName))
        {
            return null;
        }

        foreach (var part in planetName.Split(';', '/', ',', '·'))
        {
            var trimmed = part.Trim();
            if (trimmed.Length == 0)
            {
                continue;
            }

            var link = ResolveName(trimmed);
            if (link is not null)
            {
                return link;
            }
        }

        return null;
    }

    private static ProfileLinkItem? ResolveName(string name)
    {
        var normalized = Normalize(name);
        var planet = GalaxyData.Planets.FirstOrDefault(p =>
            Normalize(p.Name) == normalized || Normalize(p.Slug) == normalized.Replace(' ', '-'));

        if (planet is not null)
        {
            return ToLink(planet);
        }

        planet = GalaxyData.Planets.FirstOrDefault(p =>
        {
            var planetNorm = Normalize(p.Name);
            return planetNorm.Contains(normalized, StringComparison.Ordinal)
                || normalized.Contains(planetNorm, StringComparison.Ordinal);
        });

        return planet is null ? null : ToLink(planet);
    }

    private static ProfileLinkItem ToLink(GalaxyPlanet planet) =>
        new()
        {
            Label = planet.Name,
            Value = planet.Name,
            Route = planet.Route
        };

    private static string Normalize(string value) =>
        new string(value.ToLowerInvariant()
            .Where(ch => char.IsLetterOrDigit(ch) || char.IsWhiteSpace(ch))
            .ToArray())
            .Replace("  ", " ")
            .Trim();
}
