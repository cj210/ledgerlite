# Stadard imports
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from fastapi.testclient import TestClient


# Project imports
from app.models.user import User
from app.main import ledger
from app.database.session import get_db
from app.models.category import Category
from app.models.goal import Goal
from app.models.tag import Tag
from app.models.financial_record import FinancialRecord
from app.models.base import Base


test_engine = create_engine(
        'sqlite:///:memory:',
        connect_args={"check_same_thread": False},
        poolclass=StaticPool
        )

Base.metadata.create_all(test_engine)

SessionLocalTest = sessionmaker(
        bind=test_engine,
        autoflush=False,
        )

@pytest.fixture
def test_db():

    session = SessionLocalTest()

    yield session

    session.close()

@pytest.fixture
def client(test_db):

    def override_get_db():
        yield test_db

    ledger.dependency_overrides[get_db] = override_get_db
    
    yield TestClient(ledger)
    
    ledger.dependency_overrides.clear()