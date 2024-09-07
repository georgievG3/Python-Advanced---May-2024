def team_lineup(*args):
    result = {}

    for name, country in args:
        if country not in result:
            result[country] = []
        result[country].append(name)

    sorted_result = sorted(result.items(), key=lambda x: (-len(x[1]), x[0]))

    output = []
    for country, players in sorted_result:
        output.append(f"{country}:")
        for player in players:
            output.append(f"  -{player}")

    return "\n".join(output)


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))





