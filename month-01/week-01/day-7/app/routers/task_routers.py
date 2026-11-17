from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 

from app.database.connection import get_db

from app.schemas.task_schema import (
  TaskCreate,
  TaskUpdate,
  TaskResponse
)

from app.services import task_service


router = APIRouter(
  prefix='/tasks',
  tags=["Tasks"]
)

# Create Task
@router.post("/", response_model=TaskResponse)
def create_task(
  task: TaskCreate,
  db: Session = Depends(get_db)
):
  return task_service.create_task(db, task)

# get All tasks

@router.get("/", response_model=list[TaskResponse])
def get_all_tasks(
  db: Session = Depends(get_db)
):
  return task_service.get_all_tasks(db)

# get task by id
@router.get("/{task_id}", response_model=TaskResponse)
def get_task_by_id(
  task_id:int,
  db:Session = Depends(get_db)
):
  task = task_service.get_task_by_id(db, task_id)

  if task is None:
    raise HTTPException(
      status_code=404,
      detail=f"Task with id {task_id} not found"
    )
  return task

# update task
@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(
  task_id:int,
  task_data: TaskUpdate,
  db: Session = Depends(get_db)
):

  task = task_service.update_task(db, task_id, task_data)

  if task is None:
    raise HTTPException(
      status_code=404,
      detail=f"Task with id {task_id} not found"
    )
  return task

# delete task
@router.delete("/{task_id}")
def delete_task(
  task_id:int,
  db:Session = Depends(get_db)
):
  task = task_service.delete_task(db,task_id)

  if task is None:
    raise HTTPException(
      status_code=404,
      detail=f"Task with id {task_id} not found"
    )

  return {"message": f"Task with id {task_id} has been deleted successfully."}

