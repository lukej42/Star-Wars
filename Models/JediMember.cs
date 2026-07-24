namespace StarWars.Models;

public sealed class JediMember
{
    public required string Name { get; init; }
    public required string Slug { get; init; }
    public required string Route { get; init; }
    public required string Rank { get; init; }
    public required string Description { get; init; }
    public required string Color { get; init; }

    public string ImagePath => $"/images/jedi/{Slug}.png";
    public string SceneImagePath => $"/images/jedi/{Slug}-scene.png";
}
