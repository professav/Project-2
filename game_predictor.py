from typing import Union, List
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.put("/predict/")
def update_game_recommendation(game_list: List[str]):
    return {"game_list": game_list}
