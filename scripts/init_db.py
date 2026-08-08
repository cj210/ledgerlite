from app.models.base import Base
from app.models.user import User
from app.models.category import Category
from app.models.goal import Goal
from app.models.tag import Tag
from app.models.financial_record import FinancialRecord
from app.database.engine import engine


Base.metadata.create_all(engine)



