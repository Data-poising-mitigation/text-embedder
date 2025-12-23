from dataclasses import dataclass

from app.core.config import settings
from app.schema.schemas import EmbedResponse
from app.models.factory import get_embedder

class LimitExceededError(Exception):
    """Custom exception for exceeding limits."""
    
@dataclass(frozen=True)
class Limits:
    max_texts: int
    max_chars_per_text: int
    
def _validate_limits(texts: list[str], limits: Limits) -> None:
    """
    Validate that the provided texts adhere to the specified limits.
    """
    if len(texts) > limits.max_texts:
        raise LimitExceededError(f"Number of texts ({len(texts)}) exceeds the maximum allowed ({limits.max_texts}).")
    
    total = 0
    for i, t in enumerate(texts):
        length = len(t)
        if length > limits.max_chars_per_text:
            raise LimitExceededError(f"Text at index {i} exceeds the maximum character limit of {limits.max_chars_per_text} (length: {length}).")
        total += length
    
    
class EmbedService:
    def __init__(self) -> None:
        self._limits = Limits(
            max_texts=getattr(settings, "MAX_TEXTS_PER_REQUEST", 64),
            max_chars_per_text=getattr(settings, "MAX_CHARS_PER_TEXT", 8000),
        )
        
    def embed(self, texts: list[str], model_name: str | None ) -> EmbedResponse:
        """
        Generate embeddings for the provided texts using the specified model.
        
        Args:
            texts (list[str]): List of input texts to embed.
            model_name (str | None): Name of the embedding model to use. Defaults to None.
        Returns:
            EmbedResponse: The response containing embeddings and model info.
        """
        model = (model_name or "").strip() or getattr(settings, "DEFAULT_MODEL", "all-minilm-l6-v2")
        
        _validate_limits(texts, self._limits)
        
        embedder = get_embedder(model)
        vectors = embedder.embed(texts)
        
        return EmbedResponse(
            model=model,
            dim=embedder.dim,
            embeddings=vectors,
        )