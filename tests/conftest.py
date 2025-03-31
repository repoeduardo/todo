from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from todo.main import app
from todo.models import table_registry
from fastapi.testclient import TestClient
import pytest

@pytest.fixture
def client():
    return TestClient(app) # arrange

@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    table_registry.metadata.create_all(engine)

    # context manager
    with Session(engine) as session:
        yield session # yield return session before destroy the registry

    table_registry.metadata.drop_all(engine)