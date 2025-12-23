from sentence_transformers import SentenceTransformer

_MODEL_ID = "sentence-transformers/all-MiniLM-L6-v2"
_model: SentenceTransformer | None = None

def _get_model() -> SentenceTransformer:
    """Load and return the specified SentenceTransformer model.

    Args:
        model_name (str): The name of the model to load.
    Returns:
        SentenceTransformer: The loaded embedding model.
    """
    global _model
    if _model is None:
        _model = SentenceTransformer(_MODEL_ID)
    
    return _model

class MiniLML6V2:
    """Wrapper for the 'all-minilm-l6-v2' embedding model."""
    def __init__(self):
        model = _get_model()
        self.dim: int = model.get_sentence_embedding_dimension()

    def embed(self, texts: list[str]) -> list[list[float]]:
        """Generate embeddings for a list of texts.

        Args:
            texts (list[str]): List of input texts to embed.
        Returns:
            list[list[float]]: List of embedding vectors.
        """
        model = _get_model()
        embeddings = model.encode(texts, convert_to_numpy=True, normalize_embeddings=True)
        return embeddings.tolist()
    