namespace StarWars.Models;

public enum ForceSide
{
    Light,
    Dark
}

public sealed class ForcePower
{
    public required string Name { get; init; }
    public required string Slug { get; init; }
    public required string Route { get; init; }
    public required ForceSide Side { get; init; }
    public required string Category { get; init; }
    public required string Difficulty { get; init; }
    public required string Description { get; init; }
    public required string Color { get; init; }
    public required string Sources { get; init; }

    public string ImagePath => $"/images/force-powers/{Slug}.png";
    public string SceneImagePath => $"/images/force-powers/{Slug}-scene.png";
}
