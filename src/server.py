from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from src.routes import tasks_router, oauth_router, person_router
from src.repositories import TaskRepository, PersonRepository
from src.database.database import Base, engine

def create_app() -> FastAPI:
    Base.metadata.create_all(bind=engine)

    app = FastAPI()
    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(oauth_router)
    app.include_router(tasks_router)
    app.include_router(person_router)

    return app

app = create_app()
