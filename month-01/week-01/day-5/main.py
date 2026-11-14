from fastapi import FastAPI
from schemas import TaskCreate , Task_update

app = FastAPI()

@app.get("/")
def home():
  return {"message": "Welcome to my FastApi application!"}

tasks = []

@app.post('/task')
def Post_task(task: TaskCreate):

  newtask = {
    "id": len(tasks)+1,
    "title": task.title,
    "priority": task.priority,
    "completed": task.completed
  }

  tasks.append(newtask)
  return {"message": "Task created successfully",
          "task": newtask}

@app.get('/task/{task_id}')
def get_task(task_id: int):
  for t in tasks:
    if t["id"] == task_id:
      return t
  return {"message": "Task not found"}

@app.patch('/task/{task_id}')
def Post_task(task: Task_update , task_id: int):
  for t in tasks:
    if t["id"] == task_id:
     t["title"] = task.title
     t["priority"] = task.priority
     t["completed"] = task.completed
     return {"message": "Task updated successfully",
          "task": t }
  return {"message": "Task not found"}

@app.delete('/task/{task_id}')
def delete_data(task_id: int):
  for t in tasks:
    if t["id"] == task_id:
      tasks.remove(t)
      return {"message": "task deleted successfully"}
  return {"message": "Task not found"}


@app.get("/tasks")
def get_all_task():
  return tasks