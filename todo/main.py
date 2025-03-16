from fastapi import FastAPI
from http import HTTPStatus
from todo.schemas import Message, UserSchema, UserPublic, UserDB

app = FastAPI()

database = [] #provisional

@app.get('/', response_model=Message, status_code=HTTPStatus.OK)
def index():
    return {'message' : 'hello world'}

@app.post('/users', response_model=UserPublic, status_code=HTTPStatus.CREATED)
def create_user(user: UserSchema):

    user_with_id = UserDB(
        id = len(database) + 1,
        **user.model_dump()
    )

    database.append(user_with_id)
    print(database)
    return user_with_id