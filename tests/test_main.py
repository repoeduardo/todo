from todo.main import app
from fastapi.testclient import TestClient
from http import HTTPStatus


def test_index_from_main():
    client = TestClient(app) # arrange

    response = client.get('/') # act

    assert response.status_code == HTTPStatus.OK # assert
    assert response.json() == {'current page' : 'index'} # assert