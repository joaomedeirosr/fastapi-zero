from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    msg: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    username: str
    email: EmailStr
    id: int


class Userdb(UserSchema):
    id: int


# Composicao users lista de UserPublic
class UserList(BaseModel):
    users: list[UserPublic]
