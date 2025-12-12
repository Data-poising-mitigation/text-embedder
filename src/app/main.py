from fastapi import FastAPI
from app.core.config import settings
from app.api.routes import router as chunk_router

def create_app() -> FastAPI:
    """Create and configure FastAPI app
    

    Returns:
        FastAPI: Configured FastAPI application  """
    app = FastAPI(
        title=settings.app_name,
    )
    app.include_router(chunk_router)
    return app

app = create_app()