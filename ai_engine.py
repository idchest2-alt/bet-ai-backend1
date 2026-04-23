def calculate_team_strength(matches):
    goals = 0
    wins = 0

    for m in matches:
        goals += m["goals_for"]
        if m["goals_for"] > m["goals_against"]:
            wins += 1

    avg_goals = goals / len(matches) if matches else 0

    return {
        "form": wins,
        "avg_goals": avg_goals,
        "strength": wins * 2 + avg_goals
    }


def predict_match(home_stats, away_stats):
    home_score = home_stats["strength"]
    away_score = away_stats["strength"]

    if home_score > away_score:
        return "Home Win"
    elif away_score > home_score:
        return "Away Win"
    else:
        return "Draw"