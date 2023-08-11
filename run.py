from fastapi import FastAPI

from routes.user import user_router
from routes.jwt import jwt_router

app = FastAPI()
app.include_router(jwt_router)
app.include_router(user_router)
