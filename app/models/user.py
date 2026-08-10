# Standard imports
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Enum, DateTime, func
from datetime import datetime


# Project imports
from app.models.base import Base
from app.domain.enums import UserType, Status




class UserModel(Base):

    __tablename__ = "users"

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
            String(128),
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
            Enum(Status),
            default=Status.ACTIVE, # Assign default python-side
            nullable=False
            )
    created_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            nullable=False,
            default=datetime.now,
            )
    updated_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            nullable=False,
            default=datetime.now,
            onupdate=datetime.now,
            )

    def __repr__(self) -> str:
        return f"<UserModel(id={self.id}, user_name='{self.user_name}', user_type='{self.user_type}')>"

    def __str__(self) -> str:
        return f"{self.display_name} (@{self.user_name})"
