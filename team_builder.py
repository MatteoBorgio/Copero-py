import json

from team import Team


def load_teams(filename: str) -> list[Team]:
    teams = []

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    for team_data in data:
        team = Team(
            team_data["name"],
            team_data["league"],
            team_data["country"],
            team_data["tier"],
            team_data["rating"],
        )
        teams.append(team)

    return teams


teams = load_teams("teams.json")
