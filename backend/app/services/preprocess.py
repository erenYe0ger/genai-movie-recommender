import pandas as pd
from pathlib import Path
import json

RAW_PATH = Path("data/raw/")
OUTPUT_PATH = Path("data/clean_movies.json")

def load_raw_movielens():
    """
    Loads raw MovieLens movies CSV.
    Example return shape:
    DataFrame with columns like:
    movieId | title | genres | ...
    """
    file = RAW_PATH / "movies.csv"
    if not file.exists():
        return pd.DataFrame()  # example: empty df

    return pd.read_csv(file)  # example df with ~60k rows


def preprocess_movies(df):
    """
    Basic placeholder cleaning.
    Example output:
    [
      {
        "movie_id": 1,
        "title": "Toy Story",
        "overview": "",
        "genres": ["Animation","Children","Comedy"]
      },
      ...
    ]
    """
    movies = []
    for _, row in df.iterrows():
        movies.append({
            "movie_id": int(row["movieId"]),
            "title": row["title"],
            "overview": "",   # placeholder, TMDB fetch later
            "genres": str(row["genres"]).split("|") if "genres" in row else []
        })

    return movies  # example: [{"movie_id":1,"title":"Toy Story","genres":[...]}, ...]


def save_clean_movies(movies):
    """
    Saves cleaned list into JSON file.
    Example input shape:
    [{"movie_id": 1, "title": "Toy Story"}, ...]
    """
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(movies, f, indent=2)
