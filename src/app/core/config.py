from pydantic import BaseModel

class Settings(BaseModel):
    app_name: str = "Chunking Service"
    
    DEFAULT_MODEL: str = "all-minilm-l6-v2"
    ALLOWED_MODELS: list[str] = [
        "all-minilm-l6-v2",
    ]
    MAX_TEXTS_PER_REQUEST: int = 64
    MAX_CHARS_PER_TEXT: int = 8000

settings = Settings()