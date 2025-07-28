from fastapi import APIRouter, Depends, status
from auth.services import login
from pydantic import (
    BaseModel,
)   
from typing import Any, Annotated
from fastapi.security import APIKeyHeader, OAuth2PasswordRequestForm

routers = APIRouter()

class Item(BaseModel):
    account: str
    password: str

class Response(BaseModel):
    message: str
    code: str

@routers.post("/auth/login/", response_model=Response, summary="Login to system", tags=["Auth"])
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    """
    LOGIN TO SYSTEM:
    - **account**: each user must have an account to login
    - **password**: password for each account
    """

    print(item,'item')
       
    account = item.account
    password = item.password
    
    print("Go there !!!")
    return {"message": "Login Success", "code": "200"}
