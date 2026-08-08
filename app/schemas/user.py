# Standard imports
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Project imports
from app.domain.enums import UserType

class UserBase(BaseModel):
    user_name: str
    display_name: str
    user_type: UserType
    description: Optional[str] = None
    email: Optional[EmailStr] = None
    mobile: Optional[str] = None


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    display_name: Optional[str] = None
    user_type: Optional[UserType] = None
    description: Optional[str] = None
    email: Optional[EmailStr] = None
    mobile: Optional[str] = None

class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
