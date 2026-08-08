# Project imports
from app.models.tag import Tag


class TagRepository:

    def __init__(self, session):
        self.session = session

    def get_by_name(self, user_id, name):
        tag = self.session.query(Tag).where(Tag.user_id == user_id, Tag.name == name).first()
        return tag

    def create(self, tag):
        self.session.add(tag)
        return tag
        
    def delete(self, tag):
        self.session.delete(tag)
        return tag
