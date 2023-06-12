import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator


DATABASE_URL = os.environ["DATABASE_URL"]


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
