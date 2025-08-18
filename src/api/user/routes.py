from typing_extensions import Annotated
from fastapi import APIRouter, Depends, status, HTTPException, Header
from models import Response

from ..user.models import CreateUserRequest, FilterUserItem
from ..user.services import createUser, getUser
from ..models import CommonHeaders


routers = APIRouter()

@routers.get("/", response_model=Response, summary="Get users")
async def get_users(
        name: str | None = None, 
        full_name: str | None = None,
        email: str | None = None,
        phone: str | None = None,
        age: int | None = None,
        created_at: str | None = None,
        updated_at: str | None = None
    ):
    filter = FilterUserItem(name=name, full_name=full_name, email=email, phone=phone, age=age, created_at=created_at, updated_at=updated_at)
    response = Response(status="success", status_code=status.HTTP_200_OK, message="Get Users")
    rst = getUser(filter)
    response.data = rst.data
    return response

@routers.post("/create-user/", response_model=Response, summary="Create user")
async def create_users(Item: CreateUserRequest):
    response = Response(status="success", status_code=status.HTTP_200_OK, message="Create Users")
    rsp = createUser(Item)
    response.status = "success" if rsp.code is not status.HTTP_200_OK else "error"
    response.status_code = rsp.code
    response.message = rsp.message
    response.data = {
        "user_id": rsp.user_id,
    }

    return response

