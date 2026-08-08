# Project imports
from app.models.financial_record import FinancialRecord

class FinancialRecordRepository:

    def __init__(self, session):
        self.session = session

    def get_by_category(self, user_id, category_id):
        records = self.session.query(FinancialRecord).where(FinancialRecord.user_id == user_id, FinancialRecord.category_id == category_id,).all()
        return records

    def get_by_goal(self, user_id, goal_id):
        records = self.session.query(FinancialRecord).where(FinancialRecord.user_id == user_id, FinancialRecord.goal_id == goal_id,).all()
        return records

    def get_by_tag(self, user_id, tag_id):
        records = self.session.query(FinancialRecord).where(FinancialRecord.user_id == user_id, FinancialRecord.tag_id == tag_id,).all()
        return records

    def get_by_date_range(self, user_id, start_date, end_date):
        records = self.session.query(FinancialRecord).where(
                FinancialRecord.user_id == user_id,
                FinancialRecord.recorded_date >= start_date,
                FinancialRecord.recorded_date <= end_date).all()
        return records

    def create(self, record):
        self.session.add(record)
        return record

    def delete(self, financial_record):
        self.session.delete(financial_record)
        return financial_record
