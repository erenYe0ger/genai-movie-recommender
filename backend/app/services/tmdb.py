import requests

TMDB_API_KEY = "YOUR_API_KEY"  # replace later

def get_poster_url(movie_id: int):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"
    r = requests.get(url)
    if r.status_code != 200:
        return None

    data = r.json()
    poster_path = data.get("poster_path")
    if not poster_path:
        return None

    return f"https://image.tmdb.org/t/p/w500{poster_path}"
