from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , DeclarativeBase

# database_url
DATABASE_URL = "sqlite:///./test.db"

# create engine
engine = create_engine(
  DATABASE_URL, connect_args={"check_same_thread":False}
)

# create session
SessionLocal = sessionmaker(
  autocommit=False,
  autoflush=False,
  bind=engine
)

#create declarative base

class Base(DeclarativeBase):
  pass

def get_db():
  db = SessionLocal()

  try: 
    yield db
  finally:
    db.close()

