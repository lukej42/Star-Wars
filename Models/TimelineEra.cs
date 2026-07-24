namespace StarWars.Models;

public sealed class TimelineEra
{
    public required string Name { get; init; }
    public required string Slug { get; init; }
    public required string Route { get; init; }
    public required string DateRange { get; init; }
    public required string EraLabel { get; init; }
    public required string Description { get; init; }
    public required string Color { get; init; }

    /// <summary>Start of era in chart coordinates: positive = BBY, negative = ABY.</summary>
    public int ChartStart { get; init; }

    /// <summary>End of era in chart coordinates: positive = BBY, negative = ABY.</summary>
    public int ChartEnd { get; init; }

    public bool ShowOnChart { get; init; } = true;

    public string SceneImagePath => $"/images/timelines/{Slug}-scene.png";
}
