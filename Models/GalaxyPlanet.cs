namespace StarWars.Models;

public sealed class GalaxyPlanet
{
    public required string Name { get; init; }
    public required string Slug { get; init; }
    public required string Route { get; init; }
    public required string Region { get; init; }
    public required string Description { get; init; }
    public required double X { get; init; }
    public required double Y { get; init; }
    public required string Color { get; init; }
    public string? ImagePath { get; init; }

    public string DisplayImagePath => ImagePath ?? $"/images/planets/{Slug}.svg";

    public string BackgroundImagePath => ImagePath ?? $"/images/planets/{Slug}-space.png";
}
