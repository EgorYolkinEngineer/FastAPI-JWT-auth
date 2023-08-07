from pydantic import BaseModel
from utils.tools import generate_nickname


class JWTData(BaseModel):
    info: str
    username: str = generate_nickname()
