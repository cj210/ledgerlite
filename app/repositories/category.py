# Project imports
from app.models.category import Category


class CategoryRepository:

    def __init__(self, session):
        self.session = session

    def get_by_name(self, user_id, name):
        category = self.session.query(Category).where(Category.user_id == user_id, Category.name == name).first()
        return category
        
    def create(self, category):
        self.session.add(category)
        return category

    def delete(self, category):
        self.session.delete(category)
        return category
