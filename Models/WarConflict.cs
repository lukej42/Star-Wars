namespace StarWars.Models;

public sealed class WarConflict
{
    public required string Name { get; init; }
    public required string Slug { get; init; }
    public required string Route { get; init; }
    public required string Color { get; init; }

    public string HeroImagePath => $"/images/wars-conflicts/{Slug}-hero.webp";
}
