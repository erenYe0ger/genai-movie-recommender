import numpy as np
from app.services.data_loader import load_movies, load_embeddings
from app.utils.similarity import cosine_similarity

# Load once at startup
MOVIES = load_movies()               # list of dicts
EMBEDS = load_embeddings()           # numpy array (N x D)

def get_top_k(vector, k=5):
    sims = np.dot(EMBEDS, vector)    # fast cosine since all normalized
    top_idx = np.argsort(sims)[::-1][:k]
    return top_idx.tolist()

def build_recommendations(indices):
    results = []
    for idx in indices:
        m = MOVIES[idx]
        results.append({
            "movie_id": m["id"],
            "title": m["title"],
            "overview": m.get("overview", "")
        })
    return results
