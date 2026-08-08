# Project imports
from app.models.goal import Goal


class GoalRepository:

    def __init__(self, session):
        self.session = session

    def get_by_name(self, user_id, name):
        goal = self.session.query(Goal).where( Goal.user_id == user_id, Goal.name == name).first()
        return goal

    def create(self, goal):
        self.session.add(goal)
        return goal

    def delete(self, goal):
        self.session.delete(goal)
        return goal
