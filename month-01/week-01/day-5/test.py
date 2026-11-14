from pydantic import BaseModel, Field

class Task(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)

try:
    task = Task(title="")
    print(task)
except Exception as e:
    print(e)