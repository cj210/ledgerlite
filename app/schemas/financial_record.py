# Standard imports
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime
from decimal import Decimal


# Project imports
from app.domain.enums import RecordType, Frequency


class FinancialRecordBase(BaseModel):
    record_type: RecordType
    name: str
    amount: Decimal = Field(gt=0, decimal_places=2)
    transaction_date: date
    category_id: Optional[int] = None
    description: Optional[str] = None
    frequency: Optional[Frequency] = None
    is_fixed: Optional[bool] = None
    due_day: Optional[int] = None
    end_date: Optional[date] = None
    tag_id: Optional[int] = None
    goal_id: Optional[int] = None


class FinancialRecordCreate(FinancialRecordBase):
    pass


class FinancialRecordUpdate(BaseModel):
    record_type: Optional[RecordType] = None
    name: Optional[str] = None
    amount: Optional[Decimal] = Field(default=None, gt=0, decimal_places=2)
    transaction_date: Optional[date] = None
    category_id: Optional[int] = None
    description: Optional[str] = None
    frequency: Optional[Frequency] = None
    is_fixed: Optional[bool] = None
    due_day: Optional[int] = None
    end_date: Optional[date] = None
    tag_id: Optional[int] = None
    goal_id: Optional[int] = None


class FinancialRecordResponse(FinancialRecordBase):
    id: int
    user_id: int
    recorded_date: date
    created_at: datetime
    updated_at: datetime



