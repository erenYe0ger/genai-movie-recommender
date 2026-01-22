import requests
import os
from dotenv import load_dotenv


load_dotenv()


TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_MOVIE_URL = "https://api.themoviedb.org/3/movie/{id}?append_to_response=credits,keywords"

def fetch_tmdb_movie(tmdb_id: int):
    """
    Fetch metadata for a movie using TMDB API.
    Example return:
    {
      "id": 550,
      "title": "Fight Club",
      "overview": "...",
      "genres": ["Drama"],
      "keywords": ["alter ego", "violence"],
      "cast": ["Brad Pitt", "Edward Norton"],
      "director": "David Fincher"
    }
    """
    if not TMDB_API_KEY:
        return None

    url = TMDB_MOVIE_URL.format(id=tmdb_id)
    params = {"api_key": TMDB_API_KEY}

    r = requests.get(url, params=params)
    if r.status_code != 200:
        return None

    data = r.json()

    # Extract essential fields
    genres = [g["name"] for g in data.get("genres", [])]
    keywords = [k["name"] for k in data.get("keywords", {}).get("keywords", [])]
    cast = [c["name"] for c in data.get("credits", {}).get("cast", [])[:5]]  # top 5 actors

    crew = data.get("credits", {}).get("crew", [])
    director = next((c["name"] for c in crew if c.get("job") == "Director"), None)

    return {
        "id": data.get("id"),
        "title": data.get("title"),
        "overview": data.get("overview", ""),
        "genres": genres,
        "keywords": keywords,
        "cast": cast,
        "director": director
    }
