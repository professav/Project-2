import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from typing import List
import numpy as np
from fuzzywuzzy import fuzz, process
import pyarrow.parquet as pq
import pickle
import sys


# load game review data and create pivot table
game_pivot = pq.read_table('data/game_pivot.parquet', thrift_container_size_limit=(999000000), thrift_string_size_limit=(999000000)).to_pandas()

# create a nearest neighbors model
model_knn = pickle.load(open('models/knn.pkl', 'rb'))

# method for getting vectors from a dataframe and a list of game titles
def get_vectors(df: pd.DataFrame, game_titles: List[str]) -> np.ndarray:
    vectors = []
    for title in game_titles:
        vectors.append(df.loc[title].values)
    return np.array(vectors)

# method for getting recommendations
def get_recommendations(game_titles: List[str], model: NearestNeighbors = model_knn,
    df: pd.DataFrame = game_pivot, n_neighbors: int = 5) -> List[str]:
    vectors = get_vectors(game_pivot, game_titles)
    avg_vector = np.mean(vectors, axis=0).reshape(1, -1)
    x_neighbors = n_neighbors + len(game_titles)
    distances, indices = model.kneighbors(avg_vector, n_neighbors=x_neighbors)
    recommendations = [df.index[i] for i in indices.flatten()]
    
    filtered_recommendations = [game for game in recommendations if game not in game_titles][:n_neighbors]
    
    return filtered_recommendations

# method for getting likely game titles using fuzzy matching
def get_likely_titles(game_title: str, df: pd.DataFrame = game_pivot, threshold: int = 80) -> List[str]:
    # return the title if it is an exact match
    if game_title in df.index.values:
        return [game_title]
    
    # otherwise, use fuzzy matching
    likely_titles = []
    for title in df.index.values.tolist():
        ratio = fuzz.ratio(game_title.lower(), title.lower())
        ratio = max(ratio, fuzz.partial_ratio(game_title.lower(), title.lower()))
        if ratio >= threshold:
            likely_titles.append(title)
    return likely_titles