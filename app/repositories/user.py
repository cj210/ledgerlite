# Project imports
from app.models.user import User


class UserRepository():

    def __init__(self, session):
        self.session = session

    def get_by_id(self, user_id):
        user = self.session.query(User).filter(User.id == user_id).first()
        return user

    def get_by_user_name(self, user_name):
        user = self.session.query(User).filter(User.user_name == user_name).first()
        return user

    def create(self, user):
        self.session.add(user)
        return user
