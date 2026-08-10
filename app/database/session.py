# Standard imports
from typing import Generator
from sqlalchemy.orm import Session, sessionmaker

# Project imports
from app.database.engine import engine


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db() -> Generator[Session, None, None]:

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
