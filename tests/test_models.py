from todo.models import User

def test_create_user():
    user = User(username='test', password='secret', email='test@mail.com')
    assert user.password == 'secret'