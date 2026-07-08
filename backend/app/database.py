from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import DATABASE_URL

connect_args = {}
if DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args
)

<<<<<<< HEAD

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
=======
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
>>>>>>> 85e6ca36e4f95fd64aed5eee5d79d0f895d17ced

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()