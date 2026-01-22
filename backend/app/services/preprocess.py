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


def preprocess_movies(df, link_map):
    """
    Merges MovieLens movies with their tmdbId.
    Example output:
    [
      {
        "movie_id": 1,
        "tmdb_id": 862,
        "title": "Toy Story",
        "genres": ["Animation","Children","Comedy"],
        "overview": ""
      },
      ...
    ]
    """
    movies = []
    for _, row in df.iterrows():
        mid = int(row["movieId"])
        tmdb_id = link_map.get(mid)

        movies.append({
            "movie_id": mid,
            "tmdb_id": tmdb_id,  # example: 862
            "title": row["title"],
            "overview": "",  # will fill later
            "genres": str(row["genres"]).split("|") if "genres" in row else []
        })

    return movies  # example list of movie dicts



def save_clean_movies(movies):
    """
    Saves cleaned list into JSON file.
    Example input shape:
    [{"movie_id": 1, "title": "Toy Story"}, ...]
    """
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(movies, f, indent=2)


def load_links():
    """
    Loads links.csv which maps movieId -> tmdbId.
    Example return:
    {
      1: 862,
      2: 8844,
      3: 15602
    }
    """
    file = RAW_PATH / "links.csv"
    if not file.exists():
        return {}  # example: {}

    import pandas as pd
    df = pd.read_csv(file)
    mapping = {}

    for _, row in df.iterrows():
        if not pd.isna(row["tmdbId"]):
            mapping[int(row["movieId"])] = int(row["tmdbId"])

    return mapping  # example: {1: 862, 2: 8844}
