from app.models.base import Base

from app.models.user import User
from app.models.category import Category
from app.models.tag import Tag
from app.models.goal import Goal
from app.models.financial_record import FinancialRecord


for table in Base.metadata.sorted_tables:
    print(f"\nTABLE: {table.name}")

    for column in table.columns:
        print(
            f"  {column.name}: "
            f"type={column.type}, "
            f"nullable={column.nullable}, "
            f"primary_key={column.primary_key}"
        )

    for constraint in table.constraints:
        print(f"  CONSTRAINT: {constraint}")

    for foreign_key in table.foreign_keys:
        print(
            f"  FK: {foreign_key.parent.name}"
            f" -> {foreign_key.target_fullname}"
        )
