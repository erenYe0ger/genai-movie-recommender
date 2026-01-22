import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
DATA_PATH = PROJECT_ROOT / "data" / "clean" / "movies.json"

def load_movies():
    """
    Loads final cleaned movies.
    Example:
    [{"id": 19995, "title": "Avatar", ...}, ...]
    """
    if not DATA_PATH.exists():
        return []

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
