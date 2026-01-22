import pandas as pd
from pathlib import Path
import json
from app.services.tmdb import fetch_tmdb_movie
import time

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


def enrich_with_tmdb(movies):
    """
    Takes basic movie list AND fills overview, genres, cast, director, keywords from TMDB.
    Example input item:
      {"movie_id": 1, "tmdb_id": 862, "title": "Toy Story", ...}

    Example output item:
      {
        "movie_id": 1,
        "tmdb_id": 862,
        "title": "Toy Story",
        "overview": "A cowboy doll is profoundly threatened...",
        "genres": ["Animation","Comedy","Family"],
        "keywords": ["toys","friendship"],
        "cast": ["Tom Hanks","Tim Allen"],
        "director": "John Lasseter"
      }
    """
    enriched = []

    for m in movies:
        tmdb_id = m.get("tmdb_id")
        if not tmdb_id:
            enriched.append(m)  # keep as is
            continue

        meta = fetch_tmdb_movie(tmdb_id)
        if meta:
            m.update(meta)  # merge TMDB fields into movie dict

        enriched.append(m)

        time.sleep(0.2)  # avoid rate limit

    return enriched  # example: list of enriched movie dicts