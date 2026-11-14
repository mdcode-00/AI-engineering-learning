from pydantic import BaseModel, Field
from typing import Literal

class TaskCreate(BaseModel):
  title: str = Field(...,min_length=3,max_length=100 ,)
  priority: Literal['low', 'high', 'medium'] = 'medium'
  completed: bool = False


class Task_update(BaseModel):
  title: str | None = Field(
    default=None,
    min_length=3,
    max_length=100  
  )

  priority: Literal["low", "high", "medium"] | None = None

  completed: bool| None = None