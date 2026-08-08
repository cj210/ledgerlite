# Standard imports
from sqlalchemy.orm import sessionmaker

# Project imports
from app.database.engine import engine


SessionLocal = sessionmaker(engine)
