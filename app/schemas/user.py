# Standard imports
from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr, Field

# Project imports
from app.domain.enums import UserType


class UserBase(BaseModel):
    user_name: str = Field(
        ...,
        min_length=3,
        max_length=20,
        pattern=r"^[a-zA-Z0-9_]+$",
        description="Unique username consisting of letters, numbers, or underscores.",
    )
    display_name: str = Field(..., min_length=1, max_length=30)
    user_type: UserType = Field(default=UserType.INDIVIDUAL)
    description: str | None = Field(default=None, max_length=150)
    email: EmailStr | None = Field(default=None, max_length=255)
    mobile: str | None = Field(
        default=None,
        pattern=r"^\d{10}$",
        description="10-digit phone number.",
    )


class UserCreate(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        description="Plain text password supplied by client.",
    )


class UserUpdate(BaseModel):
    display_name: str | None = Field(default=None, min_length=1, max_length=30)
    user_type: UserType | None = Field(default=None)
    description: str | None = Field(default=None, max_length=150)
    email: EmailStr | None = Field(default=None, max_length=255)
    mobile: str | None = Field(default=None, pattern=r"^\d{10}$")


class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    # Allows Pydantic to read ORM attributes directly from SQLAlchemy models
    model_config = ConfigDict(from_attributes=True)
