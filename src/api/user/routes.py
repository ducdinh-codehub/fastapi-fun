from typing_extensions import Annotated
from fastapi import APIRouter, Depends, status, HTTPException, Header

from ..user.models import CreateUserRequest
from ..user.services import createUser
from ..models import CommonHeaders

routers = APIRouter()

@routers.get("/")
async def get_users():
    return {"message": "Get Users"}

@routers.post("/create-user/")
async def get_users(Item: CreateUserRequest):
    rsp = createUser(Item)
    print("rsp", rsp)
    return {"message": "Get Users"}

