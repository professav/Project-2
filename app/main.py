from typing import Union, List
from fastapi import FastAPI
from game_matching import get_likely_titles, get_recommendations

app = FastAPI()

@app.get("/")
def read_root():
    return {"Status": "Working"}

@app.put("/predict/")
def update_game_recommendation(game_list: List[str], num_recommendations: int = 5):
    likely_titles = []
    for game in game_list:
        likely_titles += get_likely_titles(game)

    recommendations = get_recommendations(likely_titles, n_neighbors = num_recommendations)

    return {"match_list": likely_titles, "recommendation_list": recommendations}