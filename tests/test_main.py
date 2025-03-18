from tests.conftest import client
from http import HTTPStatus

def test_index(client):

    response = client.get('/') # act

    assert response.status_code == HTTPStatus.OK # assert
    assert response.json() == {'message' : 'hello world'} # assert

def test_create_user(client):

    response = client.post('/users', json={
        'username' : 'testusername',
        'email': 'test@test.com',
        'password': 'password'
    }) # act

    assert response.status_code == HTTPStatus.CREATED # assert
    assert response.json() == {
        'username' : 'testusername',
        'email': 'test@test.com',
        'id': 1
    } # assert 

def test_read_user(client):

    response = client.get('/users') # act

    assert response.status_code == HTTPStatus.OK # assert
    assert response.json() == {'users': [
        {
            'username' : 'testusername',
            'email': 'test@test.com',
            'id': 1
        }
    ]}