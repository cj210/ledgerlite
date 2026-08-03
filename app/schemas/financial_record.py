
from datetime import date, datetime
from decimal import Decimal
from typing import Optional
from app.domain.enums import RecordType, Frequency
from pydantic import BaseModel


class FinancialRecordBase(BaseModel):
    record_type: RecordType
    name: str
    amount: Decimal
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
    amount: Optional[Decimal] = None
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



