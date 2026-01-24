from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import movies

app = FastAPI(title="GenAI Movie Recommender API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(movies.router)

@app.get("/")
def root():
    return {"status": "ok", "message": "backend running"}
