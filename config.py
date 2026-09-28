ROLES = {
    "LB": {"goal_ratio": 0.1, "assist_ration": 0.3},
    "DC": {"goal_ratio": 0.05, "assist_ratio": 0.03},
    "RB": {"goal_ratio": 0.1, "assist_ratio": 0.3},
    "CDM": {"goal_ratio": 0.04, "assist_ratio": 0.04},
    "CM": {"goal_ratio": 0.15, "assist_ratio": 0.35},
    "LM": {"goal_ratio": 0.15, "assist_ratio": 0.4},
    "RM": {"goal_ratio": 0.15, "assist_ratio": 0.4},
    "COC": {"goal_ratio": 0.3, "assist_ratio": 0.5},
    "RW": {"goal_ratio": 0.35, "assist_ratio": 0.5},
    "LW": {"goal_ratio": 0.35, "assist_ratio": 0.5},
    "AT": {"goal_ratio": 0.4, "assist_ratio": 0.5},
    "ATT": {"goal_ratio": 0.7, "assist_ratio": 0.3},
}

LEAGUE_RATIO = {
    "Serie A": 1,
    "Serie B": 1.3,
    "Premier League": 0.9,
    "EFL Championship": 1.2,
    "La Liga": 1,
    "Segunda División": 1.4,
    "Bundesliga": 1.1,
    "2. Bundesliga": 1.5,
    "Ligue 1": 1.1,
    "Ligue 2": 1.5,
    "Primeira Liga": 1.2,
    "Liga Portugal 2": 1.6,
    "Eredivisie": 1.2,
    "Eerste Divisie": 1.6,
}

FOOT = ["RIGHT", "LEFT", "BOTH"]
