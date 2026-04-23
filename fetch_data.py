import requests

API_KEY = "PASTE_API_KEY"

def get_today_matches():
    url = "https://v3.football.api-sports.io/fixtures"
    headers = {"x-apisports-key": API_KEY}
    params = {}

    res = requests.get(url, headers=headers, params=params)
    data = res.json()

    matches = []

    for m in data["response"][:10]:
        matches.append({
            "home": m["teams"]["home"]["name"],
            "away": m["teams"]["away"]["name"]
        })

    return matches


def get_team_stats(team_id):
    url = f"https://v3.football.api-sports.io/fixtures?team={team_id}&last=5"
    headers = {"x-apisports-key": API_KEY}

    res = requests.get(url, headers=headers)
    data = res.json()

    stats = []

    for m in data["response"]:
        is_home = m["teams"]["home"]["id"] == team_id

        stats.append({
            "goals_for": m["goals"]["home"] if is_home else m["goals"]["away"],
            "goals_against": m["goals"]["away"] if is_home else m["goals"]["home"]
        })

    return stats