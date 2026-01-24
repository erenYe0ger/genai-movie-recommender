import numpy as np

def cosine_similarity(a, b):
    """
    Embeddings are already normalized.
    Cosine similarity = dot product.
    """
    return float(np.dot(a, b))
