from sqlalchemy import String, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from app.database.connection import Base

class User(Base):

  __tablename__ = "tasks"


owner_id: Mapped[int] = mapped_column(
  ForeignKey("users.id"),
  nullable=False,
  index=True
)

id: Mapped[int] = mapped_column(
    Integer,
    primary_key=True,
    index=True
  )

title: Mapped[str] = mapped_column(
    String(100),
    index=True
  )

priority: Mapped[str] = mapped_column(
    String,
    default="medium",
    nullable=False
  )

completed: Mapped[bool] = mapped_column(
    Boolean,
    default=False,
    nullable=False
  )

