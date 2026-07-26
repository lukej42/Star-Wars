namespace StarWars.Models;

public sealed class MilitaryUnit
{
    public required string Name { get; init; }
    public required string Slug { get; init; }
    public required string FactionSlug { get; init; }
    public required MilitaryUnitBranch Branch { get; init; }
    public required string UnitType { get; init; }
    public string? NavyClass { get; init; }
    public required string Description { get; init; }
    public required string Color { get; init; }
    public IReadOnlyList<string> RelatedUnitSlugs { get; init; } = [];

    public string BranchSlug => Branch == MilitaryUnitBranch.Army ? "army" : "navy";

    public string Route => $"military-units/{FactionSlug}/{BranchSlug}/{Slug}";

    public string HeroImagePath => $"/images/military-units/{FactionSlug}-{BranchSlug}-{Slug}-hero.webp";
}
