from typing import Protocol

class Embedder(Protocol):
    ## Interfce for embedding models
    dim: int
    def embed(self, texts: list[str])-> list[list[float]]:
        """
        Returns embeddings for the given list of texts.
        """
        ...
    
