from sqlalchemy import String, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection import Base

class Task(Base):

  __tablename__ = "tasks"

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