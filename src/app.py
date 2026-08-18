from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from src.schema import Message, Userdb, UserList, UserPublic, UserSchema

app = FastAPI(title='Little API')

db = []


# Aqui estou solicitando a pagina padrao (GET : /)
# onde '/' e pagina padrao e retorna uma mensagem
@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root() -> dict:
    return {'msg': 'Hello world'}


# Recebe todos os dados do Schema e nao e
# interessante retornar a senha no Payload
@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_users(user: UserSchema) -> Userdb:
    user_with_id = Userdb(**user.model_dump(), id=len(db) + 1)

    db.append(user_with_id)

    return user_with_id


@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users() -> dict:
    return {'users': db}


@app.put(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def update_user(user_id: int, user: UserSchema) -> UserSchema:
    user_with_id = Userdb(**user.model_dump(), id=user_id)

    if user_id < 1 or user_id > len(db):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    db[user_id - 1] = user_with_id

    return user_with_id


@app.delete(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(db):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    return db.pop(user_id - 1)
