from fastapi import FastAPI , HTTPException
from pydantic import BaseModel

app = FastAPI(
  title="Task Manager Api",
  description="My first FastApi application",
  version="0.162.4"
)

@app.get("/")
def home():
  return {"message": "Welcome to my FastApi application!"}

@app.get("/health")
def health_check():
  return {"status": "healthy"}


tasks = [
    {
        "id": 1,
        "title": "Learn Python",
        "description": "Practice Python basics",
        "priority": "high"
    },
    {
        "id": 2,
        "title": "Learn FastAPI",
        "description": "Build REST APIs",
        "priority": "medium"
    }
]

valid_priorities = ["low", "medium", "high"]

class TaskCreate(BaseModel):
    title: str
    description: str
    priority: str = "medium"

@app.get("/tasks")
def get_tasks():
   return {"message": "Here are your tasks!", "tasks": tasks}

@app.get("/tasks/{task_id}")
def get_task_by_id(task_id: int):
  for task in tasks:
    if task["id"] == task_id:
       return task

  raise HTTPException(status_code=404,
        detail="Task not found")
  

@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):

  if task.priority not in valid_priorities:
    raise HTTPException(status_code=400,
            detail="Invalid priority. Use low, medium or high")
  new_task = {
    "id": max((t["id"] for t in tasks), default=0) + 1,
    "title": task.title,
    "description": task.description,
    "priority": task.priority
}
  tasks.append(new_task)
  return {"message": "Task created successfully!" , "task": new_task}

# @app.put("/tasks/{task_id}")
# def update_task(task_id: int):
#   if 0 <= task_id < len(tasks):
#     raise HTTPException(400, "id not define")

#   for task in tasks:
#     if task["id"] != task_id:
#       raise HTTPException(400, "id not define")

#   return {"message": f"Task {task_id} updated successfully!"}

# @app.patch("/tasks/{task_id}")
# def partial_update_task(task_id: int):
#   return {"message": f"Task {task_id} partially updated successfully!"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
  for task in tasks:
    if task["id"] == task_id:
      tasks.remove(task)
      return {"message": f"Task {task_id} deleted successfully!"}

  raise HTTPException( status_code=404,
        detail="Task not found")
    
  

