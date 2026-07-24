namespace StarWars.Models;

public sealed class Ship
{
    public required string Name { get; init; }
    public required string Slug { get; init; }
    public required string Route { get; init; }
    public required string Class { get; init; }
    public required string Description { get; init; }
    public required string ProductionCount { get; init; }
    public required string Era { get; init; }
    public required string Color { get; init; }

    public string ImagePath => $"/images/ships/{Slug}.png";
    public string SceneImagePath => $"/images/ships/{Slug}-scene.png";
}
