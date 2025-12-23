from fastapi import APIRouter, HTTPException, status, Query
from app.core.config import settings
from app.schema.schemas import EmbedRequest, EmbedResponse
from app.services.embed_service import EmbedService, LimitExceededError

router = APIRouter()

_embed_service = EmbedService()

@router.post("/embed", response_model=EmbedResponse, status_code=status.HTTP_200_OK)
def embed(req: EmbedRequest) -> EmbedResponse:
    """
    Generate embeddings for the provided texts using the specified model.
    Args:
        req (EmbedRequest): The embedding request containing texts and optional model name.

    Returns:
        EmbedResponse: The response containing embeddings and model info.
    """
    try:
        response = _embed_service.embed(texts=req.texts, model_name=req.model)
        return response
    except LimitExceededError as e:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=str(e),
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )