# Standard imports
from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, timezone
from sqlalchemy import DateTime, Enum, String, func

# Project imports
from app.domain.enums import Status, UserType
from app.models.base import Base


class User(Base):
    __tablename__ = "users"

    def __repr__(self) -> str:
        return (
            f"<User(Table Name: {self.__tablename__} "
            f"Record: id={self.id}, user_name='{self.user_name}', user_type='{self.user_type}')>"
        )

    def __str__(self) -> str:
        return f"{self.display_name} (@{self.user_name})"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )
    
    user_name: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False,
    )

    display_name: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )
    
    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    user_type: Mapped[UserType] = mapped_column(
        Enum(UserType, native_enum=False, length=20),
        nullable=False,
        default=UserType.INDIVIDUAL,
    )

    description: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
    )

    email: Mapped[str | None] = mapped_column(
        String(255),
        unique=True,
        nullable=True,
    )

    mobile: Mapped[str | None] = mapped_column(
        String(10),
        unique=True,
        nullable=True,
    )

    status: Mapped[Status] = mapped_column(
        Enum(Status, native_enum=False, length=20),
        default=Status.ACTIVE,
        nullable=False,
    )
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        server_default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        server_default=func.now(),
    )

    categories: Mapped[List["Category"]] = relationship( back_populates="user")
    goals: Mapped[List["Goal"]] = relationship( back_populates="user")
    tags: Mapped[List["Tag"]] = relationship( back_populates="user")
    financial_records: Mapped[List["FinancialRecord"]] = relationship( back_populates="user")

