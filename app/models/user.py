# Standard imports
from sqlalchemy import String, Enum, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import List


# Project imports
from app.models.base import Base
from app.domain.enums import UserType, Status


class User(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(
            String(20),
            unique=True, 
            nullable=False,
            )
    display_name: Mapped[str] = mapped_column(
            String(30),
            nullable=False,
            )
    user_type: Mapped[UserType] = mapped_column(
            Enum(UserType),
            nullable=False,
            )
    status: Mapped[Status] = mapped_column(
            Enum(Status),
            nullable=False,
            )
    description: Mapped[str | None] = mapped_column(
            String(150),
            nullable=True,
            )
    password_hash: Mapped[str] = mapped_column(
            nullable=False,
            )
    email: Mapped[str | None] = mapped_column(
            String(254),
            unique=True,
            nullable=True,
            )
    mobile: Mapped[str | None] = mapped_column(
            String(10),
            unique=True,
            nullable=True,
            )
    created_at: Mapped[datetime] = mapped_column(
            DateTime,
            default=datetime.now,
            )
    updated_at: Mapped[datetime] = mapped_column(
            DateTime,
            default=datetime.now,
            onupdate=datetime.now,
            )
    categories: Mapped[List["Category"]] = relationship(back_populates="user")
    tags: Mapped[List["Tag"]] = relationship(back_populates="user")
    goals: Mapped[List["Goal"]] = relationship(back_populates="user")
    financial_records: Mapped[List["FinancialRecord"]] = relationship(back_populates="user")
