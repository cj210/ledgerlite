from app.database.connection import get_connection


def get_db():
    return get_connection()



