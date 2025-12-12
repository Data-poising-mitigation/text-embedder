from fastapi import FastAPI
from app.core.config import settings

def create_app() -> FastAPI:
    """Create and configure FastAPI app
    

    Returns:
        FastAPI: Configured FastAPI application  """
    app = FastAPI(
        title=settings.app_name,
        
        
    )
    return app

app = create_app()