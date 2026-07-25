namespace StarWars.Models;

public sealed class BountyHunter
{
    public required string Name { get; init; }
    public required string Slug { get; init; }
    public required string Route { get; init; }
    public required string Specialty { get; init; }
    public required string Homeworld { get; init; }
    public required string Description { get; init; }
    public required string Color { get; init; }
    public required string Sources { get; init; }

    public string ImagePath => $"/images/bounty-hunters/{Slug}.webp";
    public string SceneImagePath => $"/images/bounty-hunters/{Slug}-scene.webp";
}
