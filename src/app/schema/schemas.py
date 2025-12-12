from pydantic import BaseModel, Field
from typing import List

class ChunkRequestModel(BaseModel):
    text: str = Field(..., description="The text to be chunked")
    chunk_size: int = Field(..., description="The size of each chunk")
    overlap: int = Field(0, description="The number of overlapping characters between chunks")
    
class ChunkResponseModel(BaseModel):
    chunks: List[str] = Field(..., description="The list of text chunks generated from the input text")
    
class Chunk(BaseModel):
    id: int = Field(..., description="The unique identifier for the chunk")
    content: str = Field(..., description="The content of the chunk")