from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.embedding import embed_text
from app.services.recommender import get_top_k, build_recommendations
from app.services.data_loader import load_movie_ids, load_embeddings
from app.services.tmdb import get_poster_url
from app.services.explainer import generate_explanation

router = APIRouter()

MOVIE_IDS = load_movie_ids()      # dict: movie_id -> row index
EMBEDS = load_embeddings()        # numpy array


class RecommendRequest(BaseModel):
    selected_movie_id: int | None = None
    user_prompt: str | None = ""


@router.post("/recommend")
def recommend(req: RecommendRequest):
    if not req.selected_movie_id and not req.user_prompt:
        raise HTTPException(400, "Provide movie or text")

    vectors = []

    # Text input
    if req.user_prompt:
        text_vec = embed_text(req.user_prompt)
        vectors.append(text_vec)

    # Movie selected -> lookup embedding
    if req.selected_movie_id:
        if req.selected_movie_id not in MOVIE_IDS:
            raise HTTPException(404, "Movie ID not found")

        movie_row_index = MOVIE_IDS[req.selected_movie_id]
        movie_vec = EMBEDS[movie_row_index]
        vectors.append(movie_vec)

    # Combine (mean)
    final_vec = sum(vectors) / len(vectors)

    # Get best matches
    indices = get_top_k(final_vec, k=5)
    recs = build_recommendations(indices)

    # Add posters + explanation
    for r in recs:
        r["poster_url"] = get_poster_url(r["movie_id"]) or ""
        r["why"] = generate_explanation(
            user_prompt=req.user_prompt or "",
            title=r["title"],
            overview=r["overview"],
        )

    return recs
