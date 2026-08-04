from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class GoalBase(BaseModel):

    name: str
    description: Optional[str] = None


class GoalCreate(GoalBase):

    pass


class GoalUpdate(BaseModel):

    name: Optional[str] = None
    description: Optional[str] = None


class GoalResponse(GoalBase):

    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
