from fastapi import FastAPI
from app.services.data_loader import load_movies
from app.services.preprocess import load_raw_movielens, preprocess_movies, save_clean_movies

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
    Triggers raw → clean processing.
    Returns count of processed movies.
    Example return:
    {"processed": 60000}
    """
    df = load_raw_movielens()
    cleaned = preprocess_movies(df)
    save_clean_movies(cleaned)
    return {"processed": len(cleaned)}  # example: {"processed": 60000}