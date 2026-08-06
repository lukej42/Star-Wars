using StarWars.Data;
using StarWars.Models;

namespace StarWars.Services;

public static class OrganizationLinks
{
    public static ProfileLinkItem? FromParentFaction(string? factionSlug, string? label)
    {
        if (string.IsNullOrWhiteSpace(factionSlug))
        {
            return null;
        }

        var faction = FactionData.GetBySlug(factionSlug.Trim());
        if (faction is null)
        {
            return null;
        }

        return new ProfileLinkItem
        {
            Label = "Member of",
            Value = string.IsNullOrWhiteSpace(label) ? faction.Name : label,
            Route = faction.Route
        };
    }

    public static ProfileLinkItem? FromParentOrganization(string? organizationSlug)
    {
        if (string.IsNullOrWhiteSpace(organizationSlug))
        {
            return null;
        }

        var organization = OrganizationData.GetBySlug(organizationSlug.Trim());
        if (organization is null)
        {
            return null;
        }

        return new ProfileLinkItem
        {
            Label = "Parent organization",
            Value = organization.Name,
            Route = organization.Route
        };
    }

    public static ProfileLinkItem ToLink(Organization organization) =>
        new()
        {
            Label = organization.Name,
            Value = organization.Name,
            Route = organization.Route
        };
}
