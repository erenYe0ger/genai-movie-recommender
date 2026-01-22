import json
from pathlib import Path

DATA_PATH = Path("data/clean_movies.json")

def load_movies():
    """
    Loads movie records into memory if file exists.
    Example return structure:
    [
        {
            "movie_id": 1,
            "title": "Interstellar",
            "overview": "A team travels through a wormhole...",
            "genres": ["Adventure", "Drama", "Sci-Fi"]
        },
        ...
    ]
    """
    if not DATA_PATH.exists():
        return []  # example: []

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        movies = json.load(f)

    return movies  # example: [{"movie_id":1,"title":"Interstellar",...}, ...]
