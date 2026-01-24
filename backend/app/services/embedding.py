from sentence_transformers import SentenceTransformer

# Load BGE-large once at app startup
model = SentenceTransformer("BAAI/bge-large-en")

def embed_text(text: str):
    """
    Returns a normalized embedding vector for the input text.
    If text is empty/None, returns None.
    """
    if not text:
        return None

    vec = model.encode(text, normalize_embeddings=True)
    return vec
