from datetime import datetime

from sqlalchemy import (
  Integer,
  String,
  DateTime,
  ForeignKey
)


from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection import Base

class RefreshToken(Base):

  __tablename__ = "refresh_tokens"

  id: Mapped[int] = mapped_column(
    Integer,
    primary_key=True
  )

  user_id: Mapped[int] = mapped_column(
    ForeignKey("users.id"),
    nullable=False,
    index=True
  )

  token_hash: Mapped[str] = mapped_column(
    String(64),
    unique=True,
    nullable=False
  )

  expires_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True),
    nullable=False
  )

  revoked: Mapped[bool] = mapped_column(
    default=False,
    nullable=False
  )
