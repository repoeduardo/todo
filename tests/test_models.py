from todo.models import User
from sqlalchemy import  select

def test_create_user(session):
   
    user = User(username='test', password='secret', email='test@mail.com')
    session.add(user)
    session.commit()
    #session.refresh(user)
    user_obj = session.scalar(
        select(User).where(User.email == 'test@mail.com')
    )

    assert user_obj.username == 'test'