# Standard imports
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TagBase(BaseModel):

    name: str
    description: Optional[str] = None


class TagCreate(TagBase):

    pass


class TagUpdate(BaseModel):
    
    name: Optional[str] = None
    description: Optional[str] = None


class TagResponse(TagBase):

    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
