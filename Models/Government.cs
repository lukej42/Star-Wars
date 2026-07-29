namespace StarWars.Models;

public sealed class Government
{
    public required string Name { get; init; }
    public required string Slug { get; init; }
    public required string Route { get; init; }
    public required string Color { get; init; }
    public string Era { get; init; } = string.Empty;
    public string Description { get; init; } = string.Empty;

    public string SceneImagePath => $"/images/governments/{Slug}-scene.webp";
}
