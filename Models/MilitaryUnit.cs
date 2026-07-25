namespace StarWars.Models;

public sealed class MilitaryUnit
{
    public required string Name { get; init; }
    public required string Slug { get; init; }
    public required string FactionSlug { get; init; }
    public required string UnitType { get; init; }
    public required string Description { get; init; }
    public required string Color { get; init; }

    public string Route => $"military-units/{FactionSlug}/{Slug}";
    public string HeroImagePath => $"/images/military-units/{FactionSlug}-{Slug}-hero.webp";
}
