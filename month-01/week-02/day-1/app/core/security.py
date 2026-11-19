from datetime import datetime, timedelta, timezone

import jwt
from pwdlib import PasswordHash
import uuid
import secrets
import hashlib

from app.core.config import (
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    REFRESH_TOKEN_EXPIRE_DAYS
)



password_hash = PasswordHash.recommended()


# PASSWORD HASHING

def hash_password(password: str) -> str:
  return password_hash.hash(password)

def verify_password(
    plain_password:str,
    hashed_password:str
) -> bool:
  return password_hash.verify(plain_password,hashed_password)


# ACCESS TOKEN

def create_access_token(user_id:int) -> str:
  expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

  payload = {
    "sub": str(user_id),
    "exp": expire,
    "type": "access"
  }
  return jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)

# DECODE ACCESS TOKEN

def decode_access_token(token: str):
  payload = jwt.decode(
    token,SECRET_KEY,algorithms=[ALGORITHM]
  )
  if payload.get("type") != "access":
    raise ValueError("Invalid token type")
  return payload



# REFRESH TOKEN

def create_refresh_token() -> str:
    return secrets.token_urlsafe(64)


# HASH REFRESH TOKEN BEFORE DATABASE STORAGE

def hash_refresh_token(token: str) -> str:
    return hashlib.sha256(
        token.encode()
    ).hexdigest()

