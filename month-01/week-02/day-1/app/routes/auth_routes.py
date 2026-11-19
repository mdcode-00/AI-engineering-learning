from fastapi import (
  APIRouter,
  Depends,
  HTTPException,
  status
)

from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session


from app.database.connection import get_db

from app.schemas.user_schemas import (
  UserCreate,
  UserResponse,
  TokenResponse,
  RefreshRequest,
  LogoutRequest
)

from app.services.auth_services import (
  register_user,
  authenticate_user,
  issue_token,
  refresh_token,
  revoke_refresh_token
)

from app.dependencies.auth import get_current_user

from app.models.user_model import User


router = APIRouter(
  prefix="/auth",
  tags=["Authentication"]
)

# Register

@router.post(
  "/register",
  response_model=UserResponse,
  status_code=status.HTTP_201_CREATED
)
def register(user_data: UserCreate, db:Session = Depends(get_db)):
  user = register_user(
    db,
    user_data.email,
    user_data.password
  )

  if not user:
    raise HTTPException(
      status_code=409,
      detail="Email already registered"
    )

  return user


@router.post(
  "/login",
  response_model=TokenResponse
)
def login(
  form_data: OAuth2PasswordRequestForm = Depends(),
  db: Session = Depends(get_db)
):

  user = authenticate_user(
    db,
    form_data.username,
    form_data.password
  )

  if not user:
    raise HTTPException(
      status_code=401,
      detail="Invalid email or password"
    )
  return issue_token(db, user)

# Refresh Token

@router.post(
  "/refresh",
  response_model=TokenResponse
)
def refresh(
  request: RefreshRequest,
  db: Session = Depends(get_db)
):
  tokens = refresh_token(
    db, request.refresh_token
  )

  if not tokens:
    raise HTTPException(
      status_code=401,
      detail="Invalid or expired refresh token"
    )
  return tokens


@router.post("/logout")
def logout(
  request: LogoutRequest,
  db: Session = Depends(get_db)
):
  revoked = revoke_refresh_token(
    db,
    request.refresh_token
  )

  if not revoked:
    raise HTTPException(
      status_code=401,
      detail="Invalid refresh token"
    )
  return {
    "message": "Logged out successfully"
  }


# CURRENT USER

@router.get(
    "/me",
    response_model=UserResponse
)
def get_me(
    current_user: User = Depends(get_current_user)
):

    return current_user