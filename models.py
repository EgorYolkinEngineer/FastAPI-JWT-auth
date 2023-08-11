from pydantic import BaseModel
from utils.tools import generate_nickname


class JWTData(BaseModel):
    info: str
    username: str = generate_nickname()


class LoginData(BaseModel):
    username: str
    password: str


class RegisterData(BaseModel):
    username: str
    password: str
    name: str
    surname: str
    age: int
