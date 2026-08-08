# Standard imports
from sqlalchemy import ForeignKey, String, Enum, Numeric, Date, CheckConstraint, Integer, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from decimal import Decimal
from datetime import date, datetime


# Project imports
from app.domain.enums import RecordType, Frequency
from app.models.base import Base





class FinancialRecord(Base):

    __tablename__ = "financial_records"

    __table_args__ = (
                CheckConstraint("due_month >= 1 AND due_month <= 12", name="check_due_month_range",),
                CheckConstraint("due_on >= 1 AND due_on <= 31", name="check_due_on_range",)

            )

    
    id: Mapped[int] = mapped_column(primary_key=True,)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False,)
    user: Mapped["User"] = relationship(back_populates="financial_records")
    category_id: Mapped[int | None] = mapped_column(ForeignKey("categories.id", ondelete="SET NULL"), nullable=True,)
    category: Mapped["Category | None"] = relationship(back_populates="financial_records")
    goal_id: Mapped[int | None] = mapped_column(ForeignKey("goals.id", ondelete="SET NULL"), nullable=True,)
    goal: Mapped["Goal | None"] = relationship(back_populates="financial_records")
    tag_id: Mapped[int | None] = mapped_column(ForeignKey("tags.id", ondelete="SET NULL"), nullable=True,)
    tag: Mapped["Tag | None"] = relationship(back_populates="financial_records")
    record_type: Mapped[RecordType] = mapped_column(Enum(RecordType), nullable=False,)
    frequency: Mapped[Frequency | None] = mapped_column(Enum(Frequency), nullable=True,)
    amount: Mapped[Decimal] = mapped_column(Numeric(10,2), nullable=False,)
    transaction_date: Mapped[date] = mapped_column(Date,)
    recorded_date: Mapped[date] = mapped_column(Date, default=date.today,)
    end_date: Mapped[date | None] = mapped_column(Date, nullable=True,)
    is_fixed: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False,)
    name: Mapped[str] = mapped_column(String(80), nullable=False,)
    description: Mapped[str | None] = mapped_column(String(300), nullable=True,)
    due_month: Mapped[int | None] = mapped_column(Integer, nullable=True,)
    due_on: Mapped[int | None] = mapped_column(Integer, nullable=True,)

    created_at: Mapped[datetime] = mapped_column(
                                                DateTime,
                                                default=datetime.now,
                                                )
    updated_at: Mapped[datetime] = mapped_column(
                                                DateTime,
                                                default=datetime.now,
                                                onupdate=datetime.now,
                                                )
