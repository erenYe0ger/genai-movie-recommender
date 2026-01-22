from fastapi import FastAPI
from app.services.data_loader import load_movies
from app.services.preprocess import load_links, load_raw_movielens, preprocess_movies, save_clean_movies
from app.services.tmdb import fetch_tmdb_movie
from dotenv import load_dotenv
from app.services.preprocess import (
    load_raw_movielens,
    load_links,
    preprocess_movies,
    enrich_with_tmdb,
    save_clean_movies
)


load_dotenv()


app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}  # example: {"status": "ok"}

@app.get("/movies")
def get_movies():
    """
    Returns list of movies (empty for now until data loaded).
    Example return:
    [{"movie_id": 1, "title": "Interstellar", ...}, ...]
    """
    movies = load_movies()
    return movies


@app.post("/preprocess")
def run_preprocess():
    """
    Processes MovieLens + TMDB and saves final JSON.
    Example return: {"processed": 62000}
    """
    df = load_raw_movielens()
    link_map = load_links()
    base = preprocess_movies(df, link_map)
    enriched = enrich_with_tmdb(base)
    save_clean_movies(enriched)
    return {"processed": len(enriched)}  # example: {"processed": 62423}



@app.get("/test_tmdb/{tmdb_id}")
def test_tmdb(tmdb_id: int):
    """
    Fetch single movie from TMDB.
    Example return:
    {
      "id": 550,
      "title": "Fight Club",
      "genres": ["Drama"],
      "cast": ["Brad Pitt", "Edward Norton"],
      ...
    }
    """
    data = fetch_tmdb_movie(tmdb_id)
    return data 
