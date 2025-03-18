from todo.main import app
from fastapi.testclient import TestClient
import pytest

@pytest.fixture
def client():
    return TestClient(app) # arrange