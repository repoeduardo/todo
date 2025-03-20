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

def test_update_user(client):

    response = client.put('/users/1', json={
            'password': '123',
            'username' : 'test_update_username',
            'email': 'test_update@test.com',
            'id': 1
    }) #act

    assert response.json() == {
            'username' : 'test_update_username',
            'email': 'test_update@test.com',
            'id': 1
    }# assert

def test_delete_user(client):

    response = client.delete('/users/1') #act

    assert response.json() == {'message': 'USER DELETED'} #assert