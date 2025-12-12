from typing import List, Optional
from dataclasses import dataclass

class ChunkingError(Exception):
    pass

@dataclass
class Chunker:
    def chunk(self, text: str, chunk_size: int, overlap: int = 0) -> List[str]:
        raise NotImplementedError("Chunk method must be implemented by subclasses")

class FixedSizeChunker(Chunker):
    def chunk(self, text: str, chunk_size: int, overlap: int = 0) -> List[str]:
        if overlap >= chunk_size:
            raise ChunkingError("Overlap must be smaller than chunk size")
        chunks = []
        start = 0
        idx = 0
        while start < len(text):
            end = min(start + chunk_size, len(text))
            chunks.append({"id": idx, "content": text[start:end]})
            idx += 1
            start = end - overlap
        return chunks
    
def get_chunker_for_strategy(name: str) -> Optional[Chunker]:
    if name == "fixed_size":
        return FixedSizeChunker()
    return None