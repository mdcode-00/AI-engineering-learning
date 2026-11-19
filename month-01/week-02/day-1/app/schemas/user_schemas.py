from pydantic import BaseModel, Field


class UserCreate(BaseModel):
  email: str = Field(min_length=5, max_length=255)
  password: str = Field(min_length=8, max_length=128)


class UserResponse(BaseModel):
  id: int
  email: str

  model_config = {"from_attributes": True}

class TokenResponse(BaseModel):
  access_token: str
  refresh_token: str
  token_type: str = "bearer"

  
class RefreshRequest(BaseModel):
    refresh_token: str


class LogoutRequest(BaseModel):
    refresh_token: str