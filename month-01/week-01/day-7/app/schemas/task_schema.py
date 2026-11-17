from pydantic import BaseModel, ConfigDict , Field

# create Schema
class TaskCreate(BaseModel):
  title: str = Field(..., min_length=1, max_length=100)
  priority: str = "medium"
  completed: bool = False


# update Schema
class TaskUpdate(BaseModel):

  title: str | None = Field(default=None, min_length=1,
  max_length=100)
  priority: str | None = None
  completed: bool | None = None

class TaskResponse(BaseModel):
  model_config = ConfigDict(from_attributes=True)

  id: int
  title:str
  priority:str
  completed: bool
  
