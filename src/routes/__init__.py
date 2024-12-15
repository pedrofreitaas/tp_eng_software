from src.routes.tasks import router as tasks_router
from src.routes.oauth import router as oauth_router
from src.routes.person import router as person_router

__all__ = ("tasks_router", "oauth_router", "person_router")