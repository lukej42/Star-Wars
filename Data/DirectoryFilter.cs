namespace StarWars.Data;

public static class DirectoryFilter
{
    public static bool Matches(string query, params string?[] fields)
    {
        if (string.IsNullOrWhiteSpace(query))
        {
            return true;
        }

        var terms = query.Trim().Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);

        return terms.All(term =>
            fields.Any(field =>
                field?.Contains(term, StringComparison.OrdinalIgnoreCase) == true));
    }
}
