from pydantic import BaseModel , Field
from typing import Literal

class Taskcreate(BaseModel):
  title: str = Field(..., min_length=1, max_length=100)
  priority: Literal["low","medium","high"] = "medium"
  completed: bool = False


class TaskUpdate(BaseModel):
  title : str | None = Field(default=None, min_length=3,max_length=100)
  priority: Literal["low","medium","high"] | None = None
  completed: bool | None = None