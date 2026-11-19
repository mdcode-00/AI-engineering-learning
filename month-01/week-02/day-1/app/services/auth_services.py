from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone

from app.models.refresh_token_model import RefreshToken
from app.models.user_model import User
from app.core.security import ( hash_password,
    verify_password,
    create_access_token,
    create_refresh_token,
    hash_refresh_token)

from app.core.config import REFRESH_TOKEN_EXPIRE_DAYS

def register_user(db:Session, email: str, password: str):
  existing_user = (
    db.query(User)
    .filter(User.email == email)
    .first()
  )

  if existing_user: 
    return None

  user = User(
    email=email,
    hash_password=hash_password(password)
  )
  try:
   db.add(user)
   db.commit()
   db.refresh(user)
   
   return user
  except Exception:
    db.rollback()
    raise

def authenticate_user(
    db: Session,
    email: str,
    password: str
): 
  user = db.query(User).filter(
    User.email == email
  ).first()

  if not user:
    return None

  if not verify_password(
    password,
    user.hash_password
  ):
    return None

  return user


def issue_token(db: Session, user: User):

  access_token = create_access_token(user.id)

  refresh_token = create_refresh_token()

  token_record = RefreshToken(
    user_id=user.id,
    token_hash= hash_refresh_token(refresh_token),
    expires_at=datetime.now(timezone.utc) + timedelta(
      days=REFRESH_TOKEN_EXPIRE_DAYS
    )
  )

  try: 
    db.add(token_record)
    db.commit()

    return {
      "access_token": access_token,
      "refresh_token": refresh_token,
      "token_type": "bearer"
    }
  except Exception:
    db.rollback()
    raise

def refresh_token(
    db:Session,
    raw_token: str
):
  token_hash = hash_refresh_token(raw_token)

  record = db.query(RefreshToken).filter(
    RefreshToken.token_hash == token_hash
  ).with_for_update().first()

  if not record:
    return None

  now = datetime.now(timezone.utc)

  expires_at = record.expires_at

  if expires_at.tzinfo is None:
    expires_at = expires_at.replace(
      tzinfo=timezone.utc
    )

  if record.revoked or expires_at <= now:
    return None

  user = db.query(User).filter(
        User.id == record.user_id
    ).first()

  if not user:
        return None

# Revoke old refresh token.

  record.revoked = True

# Issue replacement tokens.
  new_access_token = create_access_token(user.id)
  new_refresh_token = create_refresh_token()

  new_record = RefreshToken(
        user_id=user.id,
        token_hash=hash_refresh_token(new_refresh_token),
        expires_at=now + timedelta(
            days=REFRESH_TOKEN_EXPIRE_DAYS
        )
    )

  try:
        db.add(new_record)
        db.commit()

        return {
            "access_token": new_access_token,
            "refresh_token": new_refresh_token,
            "token_type": "bearer"
        }

  except Exception:
        db.rollback()
        raise



def revoke_refresh_token(
    db: Session,
    raw_token: str
):

    token_hash = hash_refresh_token(raw_token)

    record = db.query(RefreshToken).filter(
        RefreshToken.token_hash == token_hash
    ).with_for_update().first()

    if not record or record.revoked:
        return False

    record.revoked = True
    db.commit()

    return True