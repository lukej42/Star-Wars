namespace StarWars.Models;

public sealed class Settlement
{
    public required string Name { get; init; }
    public required string Slug { get; init; }
    public required string Route { get; init; }
    public required string Planet { get; init; }
    public required string SettlementType { get; init; }
    public required string Description { get; init; }
    public required string Color { get; init; }
    public required string Sources { get; init; }

    public string ImagePath => $"/images/settlements/{Slug}.svg";
    public string SceneImagePath => $"/images/settlements/{Slug}-scene.svg";
}
