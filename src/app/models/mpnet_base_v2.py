from sentence_transformers import SentenceTransformer

_MODEL_ID = "sentence-transformers/all-mpnet-base-v2"
_model: SentenceTransformer | None = None


def _get_model() -> SentenceTransformer:
    """Load and return the specified SentenceTransformer model."""
    global _model
    if _model is None:
        _model = SentenceTransformer(_MODEL_ID)
    return _model


class MpnetBaseV2:
    """Wrapper for the 'all-mpnet-base-v2' embedding model."""

    def __init__(self) -> None:
        model = _get_model()
        self.dim: int = model.get_sentence_embedding_dimension()

    def embed(self, texts: list[str]) -> list[list[float]]:
        """Generate embeddings for a list of texts."""
        model = _get_model()
        embeddings = model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )
        return embeddings.tolist()

