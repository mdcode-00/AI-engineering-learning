from fastapi import FastAPI
from app.routers import task_routes

app = FastAPI(
   title="Task Manager API",
    description="A modular task management backend",
    version="1.0.0"
)

app.include_router(task_routes.router)

@app.get("/")
def home():
    return {
        "message": "Task Manager API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }