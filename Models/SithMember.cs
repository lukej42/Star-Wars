namespace StarWars.Models;

public sealed class SithMember
{
    public required string Name { get; init; }
    public required string Slug { get; init; }
    public required string Route { get; init; }
    public required string Title { get; init; }
    public required string Description { get; init; }
    public required string Color { get; init; }

    public string ImagePath => $"/images/sith/{Slug}.png";
    public string SceneImagePath => $"/images/sith/{Slug}-scene.png";
}
