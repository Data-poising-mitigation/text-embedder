from fastapi import FastAPI
from app.core.config import settings
from app.api.routes import router as embed_router

def create_app() -> FastAPI:
    """Create and configure FastAPI app
    

    Returns:
        FastAPI: Configured FastAPI application  """
    app = FastAPI(
        title=settings.app_name,
    )
    app.include_router(embed_router)
    
    @app.get("/health", status_code=200)
    def health_check():
        """Health check endpoint to verify the service is running."""
        return {"status": "ok", "service": settings.app_name}
    
    return app

app = create_app()