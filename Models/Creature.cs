namespace StarWars.Models;

public sealed class Creature
{
    public required string Name { get; init; }
    public required string Slug { get; init; }
    public required string Route { get; init; }
    public required string Habitat { get; init; }
    public required string Homeworld { get; init; }
    public required string Description { get; init; }
    public required string Color { get; init; }

    public string ImagePath => $"/images/creatures/{Slug}.webp";
    public string SceneImagePath => $"/images/creatures/{Slug}-scene.webp";
}
