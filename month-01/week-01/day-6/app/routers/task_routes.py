from fastapi import APIRouter, HTTPException, status

from app.schemas.task_schema import Taskcreate, TaskUpdate
from app.services import task_services


router = APIRouter(
  prefix='/task',
  tags=["Tasks"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_task(task: Taskcreate):
  return task_services.create_task(task.model_dump())



@router.get("/",status_code=status.HTTP_200_OK)
def get_all_task():
  return task_services.get_all_task()



@router.get("/{task_id}", status_code=status.HTTP_200_OK)
def get_task_by_id(task_id:int):
  task = task_services.get_task_by_id(task_id)
  if task is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
  return task


@router.patch("/{task_id}", status_code=status.HTTP_200_OK)
def update_task(task_id:int, updated_task:TaskUpdate):
  task = task_services.update_task(task_id, updated_task.model_dump())

  if task is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
  return task



@router.delete("/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(task_id:int):
  deleted_task = task_services.delete_task(task_id)

  if deleted_task is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
  return deleted_task
