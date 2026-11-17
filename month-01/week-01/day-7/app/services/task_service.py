from sqlalchemy.orm import Session

from app.models.task_model import Task
from app.schemas.task_schema import TaskCreate , TaskUpdate


# create

def create_task(db: Session, task:TaskCreate):
  new_task = Task(
    title=task.title,
    priority=task.priority,
    completed=task.completed
  )

  db.add(new_task)
  db.commit()
  db.refresh(new_task)

  return new_task

# read All

def get_all_tasks(db:Session):
  return db.query(Task).all()

# READ BY ID
def get_task_by_id(db: Session, task_id: int):

    return db.get(Task, task_id)



# Update
def update_task(db:Session, task_id: int, task_data:TaskUpdate):
  task = db.get(Task, task_id)

  if task is None:
    return None

  update_date = task_data.model_dump(exclude_unset=True)

  for key, value in update_date.items():
    setattr(task,key,value)

  db.commit()
  db.refresh(task)

  return task

# Delete

def delete_task(db:Session, task_id: int):

  task = db.get(Task, task_id)

  if task is None:
    return None

  db.delete(task)
  db.commit()

  return task