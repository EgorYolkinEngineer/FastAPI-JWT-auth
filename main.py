from fastapi import FastAPI, HTTPException
from fastapi import status, Header, Depends
from utils.tools import create_jwt
from jose import jwt, JWTError
from settings import SECRET_KEY
from settings import ALGORITHM
from models import JWTData

app = FastAPI()


async def validate_authorization(authorization: str = Header()):
    if authorization is None or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization")
    try:
        payload = jwt.decode(authorization.split('Bearer ')[1], SECRET_KEY,
                             algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail='Invalid authentication token'
        )


@app.get('/auth/jwt/get/')
async def get_jwt(jwt_data: JWTData):
    """ Get JWT with username and info. """

    data_dict = jwt_data.dict()

    token = create_jwt(data_dict)

    return {
        'token': token
    }


@app.post('/auth/jwt/verify/')
async def verify_jwt(authorization: str = Depends(validate_authorization)):
    """ Check JWT. """

    return authorization
