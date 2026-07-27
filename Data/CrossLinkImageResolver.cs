using StarWars.Models;

namespace StarWars.Data;

public static class CrossLinkImageResolver
{
    private static readonly Dictionary<string, string> DirectoryImages = new(StringComparer.OrdinalIgnoreCase)
    {
        ["all-planets"] = "/images/planets/planets-directory-hero.webp",
        ["all-characters"] = "/images/characters/characters-directory-hero.webp",
        ["all-jedi"] = "/images/jedi/jedi-directory-hero.webp",
        ["all-sith"] = "/images/sith/sith-directory-hero.webp",
        ["all-ships"] = "/images/ships/ships-directory-hero.webp",
        ["all-species"] = "/images/species/species-directory-hero.webp",
        ["all-factions"] = "/images/factions/factions-directory-hero.webp",
        ["all-cities-settlements"] = "/images/settlements/cities-settlements-directory-hero.webp",
        ["all-droids"] = "/images/droids/droids-directory-hero.webp",
        ["all-bounty-hunters"] = "/images/bounty-hunters/bounty-hunters-directory-hero.webp",
        ["all-military-units"] = "/images/military-units/military-units-directory-hero.webp",
        ["all-force-powers"] = "/images/force-powers/force-powers-all-hero.webp",
        ["all-light-side-powers"] = "/images/force-powers/force-powers-light-side-hero.webp",
        ["all-dark-side-powers"] = "/images/force-powers/force-powers-dark-side-hero.webp",
        ["galaxy-map"] = "/images/planets/planets-directory-hero.webp",
        ["timelines"] = "/images/timelines/timelines-directory-hero.webp",
        ["wars-conflicts"] = "/images/wars-conflicts/wars-conflicts-directory-hero.webp",
        ["the-force"] = "/images/the-force/light-dark-conflict-scene.webp",
    };

    public static string? Resolve(string route)
    {
        if (string.IsNullOrWhiteSpace(route))
        {
            return null;
        }

        var normalized = route.Trim().TrimStart('/');

        if (DirectoryImages.TryGetValue(normalized, out var directoryImage))
        {
            return directoryImage;
        }

        var segments = normalized.Split('/', StringSplitOptions.RemoveEmptyEntries);
        if (segments.Length == 0)
        {
            return null;
        }

        if (segments[0] == "planet" && segments.Length >= 2)
        {
            return $"/images/planets/{segments[1]}-hero.webp";
        }

        var legacyPlanet = GalaxyData.GetBySlug(segments[0]);
        if (legacyPlanet is not null && segments.Length == 1)
        {
            return legacyPlanet.HeroImagePath;
        }

        return segments[0] switch
        {
            "characters" when segments.Length >= 2 => $"/images/characters/{segments[1]}.webp",
            "jedi" when segments.Length >= 2 => $"/images/jedi/{segments[1]}.webp",
            "sith" when segments.Length >= 2 => $"/images/sith/{segments[1]}.webp",
            "ships" when segments.Length >= 2 => $"/images/ships/{segments[1]}.webp",
            "species" when segments.Length >= 2 => $"/images/species/{segments[1]}.webp",
            "factions" when segments.Length >= 2 => $"/images/factions/{segments[1]}.svg",
            "settlements" when segments.Length >= 2 => $"/images/settlements/{segments[1]}.webp",
            "bounty-hunters" when segments.Length >= 2 => $"/images/bounty-hunters/{segments[1]}.webp",
            "droids" when segments.Length >= 2 => $"/images/droids/{segments[1]}.webp",
            "force-powers" when segments.Length >= 2 => $"/images/force-powers/{segments[1]}.webp",
            "wars-conflicts" when segments is ["wars-conflicts", var warSlug] => $"/images/wars-conflicts/{warSlug}-hero.webp",
            "wars-conflicts" when segments is ["wars-conflicts", "battles", var battleSlug] => $"/images/wars-conflicts/battles/{battleSlug}-hero.webp",
            "the-force" when segments is ["the-force", "lightsaber-forms", var formSlug] => $"/images/the-force/lightsaber-forms/{formSlug}-hero.webp",
            "military-units" => ResolveMilitaryUnitImage(segments),
            _ => null
        };
    }

    private static string? ResolveMilitaryUnitImage(string[] segments)
    {
        if (segments.Length == 2)
        {
            return $"/images/military-units/{segments[1]}-hero.webp";
        }

        if (segments.Length >= 4)
        {
            return $"/images/military-units/{segments[1]}-{segments[2]}-{segments[3]}-hero.webp";
        }

        return null;
    }
}
