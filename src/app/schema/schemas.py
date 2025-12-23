from pydantic import BaseModel, Field, field_validator
from typing import List


class EmbedRequest(BaseModel):
    model: str = Field(..., description="The embedding model to use.")
    texts: List[str] = Field(..., description="A list of texts to be embedded.")

    @field_validator("texts")
    @classmethod
    def validate_texts(cls, v: List[str]) -> List[str]:
        """
        Validate that the texts list is not empty and does not contain only whitespace strings.
        """
        if not v:
            raise ValueError("The texts list must not be empty.")

        cleaned = [text.strip() for text in v if text and text.strip()]
        if not cleaned:
            raise ValueError("The texts list must not be empty after removing whitespace-only items.")
        return cleaned


class EmbedResponse(BaseModel):
    model: str = Field(..., description="The embedding model used.")
    dim: int = Field(..., description="The dimensionality of the embedding vectors.")
    embeddings: List[List[float]] = Field(..., description="Embedding vectors for each input text.")
