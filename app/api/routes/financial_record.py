# Standard imports
from fastapi import APIRouter, status
from datetime import date, datetime

# Project imports
from app.domain.enums import RecordType
from app.schemas.financial_record import FinancialRecordResponse, FinancialRecordCreate

# Thirdparty imports
from decimal import Decimal

financial_record_router = APIRouter()


@financial_record_router.post("/financial_records", response_model = FinancialRecordResponse, status_code = status.HTTP_201_CREATED)
def create_financial_record(financial_record: FinancialRecordCreate):

    response = FinancialRecordResponse(**financial_record.model_dump(),id = 10, user_id = 15, recorded_date = date.today(),
                                       created_at = datetime.now(), updated_at = datetime.now())
    return response


@financial_record_router.get("/financial_records/{record_id}", response_model = FinancialRecordResponse)
def get_financial_record(record_id: int):

    response = FinancialRecordResponse(
            record_type = RecordType.EXPENSE,
            name = "Swiggy order for Lunch",
            amount = Decimal("222.22"),
            transaction_date = date.today(),
            id = record_id,
            user_id = 31, 
            recorded_date = date.today(),
            created_at = datetime.now(),
            updated_at = datetime.now())

    return response

    

