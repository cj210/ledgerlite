import sqlite3
from app.core.config import settings


def get_connection():
    return sqlite3.connect(settings.database_name)
