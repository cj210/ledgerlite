# Standard imports
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, DateTime, UniqueConstraint
from datetime import datetime
from typing import List

# Project imports
from app.models.base import Base


class Goal(Base):

    __tablename__ = "goals"

    __table_args__ = (
            UniqueConstraint(
                "user_id",
                "name",
                ),
            )
    id: Mapped[int] = mapped_column(primary_key=True,)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False,) 
    user: Mapped["User"] = relationship(back_populates="goals",)
    name: Mapped[str] = mapped_column(String(50), nullable=False,)
    description: Mapped[str | None] = mapped_column(String(300), nullable=True,)
    created_at: Mapped[datetime] = mapped_column(
            DateTime,
            default=datetime.now,
            )
    updated_at: Mapped[datetime] = mapped_column(
            DateTime,
            default=datetime.now,
            onupdate=datetime.now,
            )

    financial_records: Mapped[List["FinancialRecord"]] = relationship(back_populates="goal")
