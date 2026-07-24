namespace StarWars.Models;

public sealed class Droid
{
    public required string Name { get; init; }
    public required string Slug { get; init; }
    public required string Route { get; init; }
    public required string DroidType { get; init; }
    public required string Manufacturer { get; init; }
    public required string Description { get; init; }
    public required string Color { get; init; }
    public required string Sources { get; init; }

    public string ImagePath => $"/images/droids/{Slug}.png";
    public string SceneImagePath => $"/images/droids/{Slug}-scene.png";
}
