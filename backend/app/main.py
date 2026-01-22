from fastapi import FastAPI
from app.services.data_loader import load_movies

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
