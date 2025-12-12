from fastapi import APIRouter, HTTPException, status
from app.core.config import settings
from app.schema.shemas import ChunkResponseModel, ChunkRequestModel

router = APIRouter(prefix="/chunk", tags=["Chunk"])

@router.post("", response_model=ChunkResponseModel)