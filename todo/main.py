from fastapi import FastAPI, HTTPException
from http import HTTPStatus
from todo.schemas import Message, UserSchema, UserPublic, UserDB, UserList

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

@app.get('/users', response_model=UserList)
def read_user():
    return {'users': database}

@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):

    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='USER NOT FOUND'
        )
    
    user_with_id = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id
    return user_with_id

@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):

    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='USER NOT FOUND'
        )
    
    del database[user_id - 1]
    return {'message': 'USER DELETED'}