from typing_extensions import Annotated
from fastapi import APIRouter, Depends, status, HTTPException, Header

from api.user.models import CreateUserRequest
from api.user.services import createUser
from api.models import CommonHeaders

routers = APIRouter()

@routers.get("/")
async def get_users():
    return {"message": "Get Users"}

@routers.post("/create-user/")
async def get_users(Item: CreateUserRequest):
    rsp = createUser(Item)
    print("rsp", rsp)
    return {"message": "Get Users"}

