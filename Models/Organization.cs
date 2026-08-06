namespace StarWars.Models;

public sealed class Organization
{
    public required string Name { get; init; }
    public required string Slug { get; init; }
    public required string Route { get; init; }
    public required string Group { get; init; }
    public required string Description { get; init; }
    public required string Color { get; init; }
    public string? ParentFactionSlug { get; init; }
    public string? ParentFactionLabel { get; init; }
    public string? ParentOrganizationSlug { get; init; }
    public bool IsCategoryHub { get; init; }

    public string ImagePath => $"/images/organizations/{Slug}.webp";
    public string SceneImagePath => $"/images/organizations/{Slug}-scene.webp";
}
