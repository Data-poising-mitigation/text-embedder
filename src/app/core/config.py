from pydantic import BaseModel

class Settings(BaseModel):
    app_name: str = "Chunking Service"

settings = Settings()