from fastapi import FastAPI


from app.database.connection import engine, Base
from app.models.task_model import Task


from app.routers import task_routers

# create database table 
Base.metadata.create_all(bind=engine)

app = FastAPI(
  title="Task Management API",
  version="0.163.1"
)

# request router
app.include_router(task_routers.router)

app.get("/")
def home():
  return {"message": "Welcome to Task Management API"}