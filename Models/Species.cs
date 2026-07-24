namespace StarWars.Models;

public sealed class Species
{
    public required string Name { get; init; }
    public required string Slug { get; init; }
    public required string Route { get; init; }
    public required string Homeworld { get; init; }
    public required string Classification { get; init; }
    public required string Description { get; init; }
    public required string Color { get; init; }
    public required string Sources { get; init; }

    public string ImagePath => $"/images/species/{Slug}.png";
    public string SceneImagePath => $"/images/species/{Slug}-scene.png";
}
