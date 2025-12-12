from fastapi import APIRouter, HTTPException, status, Query
from app.core.config import settings
from app.schema.schemas import ChunkResponseModel, ChunkRequestModel
from app.services.base import get_chunker_for_strategy, ChunkingError

router = APIRouter(prefix="/chunk", tags=["Chunk"])

@router.post("", response_model=ChunkResponseModel)
async def chunk_document(
    payload: ChunkRequestModel,
    strategy: str = Query("fixed_size", description="Chunking strategy to use"),
):
    chunker = get_chunker_for_strategy(strategy)
    if not chunker:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unsupported chunking strategy: {strategy}",
        )
    try:
        chunks = chunker.chunk(payload.text, payload.chunk_size, payload.overlap)
    except ChunkingError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    return ChunkResponseModel(chunks=chunks)