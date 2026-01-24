import json
import pickle
from pathlib import Path

BASE = Path(__file__).resolve().parents[3]

MOVIES_PATH = BASE / "data" / "clean" / "movies.json"
EMBEDDINGS_PATH = BASE / "models" / "movie_embeddings.pkl"
MOVIE_IDS_PATH = BASE / "models" / "movie_ids.pkl"

def load_movies():
    with open(MOVIES_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def load_embeddings():
    with open(EMBEDDINGS_PATH, "rb") as f:
        return pickle.load(f)

def load_movie_ids():
    with open(MOVIE_IDS_PATH, "rb") as f:
        return pickle.load(f)
