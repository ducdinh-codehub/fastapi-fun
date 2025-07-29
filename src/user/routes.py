from fastapi import APIRouter, Depends, status, HTTPException

from user.models import CreateUserRequest
from user.services import createUser

routers = APIRouter()

@routers.get("/users/", tags=["Users"])
async def get_users():
    return {"message": "Get Users"}

@routers.post("/users/create-user/", tags=["Users"])
async def get_users(Item: CreateUserRequest):
    rsp = createUser(Item)
    print("rsp", rsp)
    return {"message": "Get Users"}

