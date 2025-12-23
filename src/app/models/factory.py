from typing import Dict

from app.core.config import settings
from app.models.base import Embedder
from app.models.minilm_l6_v2 import MiniLML6V2

_SUPPORTED_MODELS = {
    "all-minilm-l6-v2": MiniLML6V2,
}

_instance_cache: Dict[str, Embedder] = {}

def get_embedder(model_name: str) -> Embedder:
    """
    Get an instance of the specified embedding model.
    Args:
        model_name (str): The name of the embedding model.
    Returns:
        Embedder: An instance of the requested embedding model.
    """
    model_name = (model_name or "").strip() or settings.DEFAULT_MODEL
    
    # Only allow models specificied in config
    if model_name not in settings.ALLOWED_MODELS:
        raise ValueError(f"Model '{model_name}' is not supported.")
    
    if model_name not in _SUPPORTED_MODELS:
        raise ValueError(f"Model '{model_name}' is not recognized.")
    
    if model_name not in _instance_cache:
        _instance_cache[model_name] = _SUPPORTED_MODELS[model_name]()
    
    return _instance_cache[model_name]