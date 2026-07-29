namespace StarWars.Models;

public sealed class ChronicleEntry
{
    public required string Name { get; init; }
    public required string Slug { get; init; }
    public required string Route { get; init; }
    public required string Color { get; init; }
    public string EraLabel { get; init; } = string.Empty;
    public string Description { get; init; } = string.Empty;
    public string DateRange { get; init; } = string.Empty;
    public string SceneImagePath => $"/images/chronicles/{Slug}-scene.webp";
}
