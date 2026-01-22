from fastapi import FastAPI
from dotenv import load_dotenv
from app.services.data_loader import load_movies

load_dotenv()
app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}  # example -> {"status": "ok"}

@app.get("/movies")
def get_movies():
    """
    Returns movies from cleaned data.
    Example:
    [{"id": 19995, "title": "Avatar", ...}, ...]
    """
    return load_movies()
