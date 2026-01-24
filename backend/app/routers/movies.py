from fastapi import APIRouter
import json
from pathlib import Path

router = APIRouter()

# Path to movies.json (adjust if needed)
MOVIES_PATH = Path(__file__).resolve().parents[3] / "data" / "clean" / "movies.json"

@router.get("/movies")
def get_movies():
    with open(MOVIES_PATH, "r", encoding="utf-8") as f:
        movies = json.load(f)

    # Return only needed fields
    dropdown_movies = sorted(
        (
            {"id": str(m["id"]), "title": m["title"]}
            for m in movies
        ),
        key=lambda x: x["title"].lower()
    )


    return dropdown_movies
