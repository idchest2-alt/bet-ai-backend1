from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

teams = {
    "Arsenal": {"form": [1,1,0,1,1], "goals": 2.1},
    "Chelsea": {"form": [0,0,1,0,1], "goals": 1.3},
    "Barcelona": {"form": [1,1,1,1,1], "goals": 2.5},
    "Madrid": {"form": [1,1,1,0,1], "goals": 2.2},
}

def form_score(f):
    return sum(f)/len(f)

def analyze(team1, team2):
    t1 = teams.get(team1)
    t2 = teams.get(team2)

    f1 = form_score(t1["form"])
    f2 = form_score(t2["form"])

    s1 = f1*2 + t1["goals"]
    s2 = f2*2 + t2["goals"]

    if s1 > s2:
        winner = team1
    elif s2 > s1:
        winner = team2
    else:
        winner = "Draw"

    confidence = round(abs(s1 - s2) * 20, 1)
    odds = round(1.5 + (2.5 - abs(s1 - s2)), 2)

    return {
        "team1": team1,
        "team2": team2,
        "prediction": winner,
        "odds": odds,
        "confidence": confidence,
        "analysis": f"{team1} form: {f1:.2f}, {team2} form: {f2:.2f}"
    }

@app.get("/today")
def today():
    matches = [
        ("Arsenal","Chelsea"),
        ("Barcelona","Madrid"),
        ("Chelsea","Madrid"),
        ("Arsenal","Barcelona"),
    ]

    return [analyze(t1,t2) for t1,t2 in matches]