from fastapi import FastAPI

from app.routes import auth_routes
from app.database.connection import Base, engine


# Import models so SQLAlchemy knows about them
from app.models.user_model import User
from app.models.refresh_token_model import RefreshToken

app = FastAPI(
    title="Task Manager API",
    version="1.0.0"
)

Base.metadata

app.include_router(
    auth_routes.router
)


@app.get("/")
def home():
    return {
        "message": "Task Manager API is running"
    }