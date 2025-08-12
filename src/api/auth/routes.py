from datetime import timedelta
from api.auth.tokenAuthorization import JWTBearer
from fastapi import APIRouter, Depends, Header, status, HTTPException
from ..auth.services import checkAccountExist as sv_checkAccountExist, createAccount, logOut
from ..auth.services import createAccessToken as sv_getToken
from pydantic import (
    BaseModel,
)   
from typing import Any, Annotated
from fastapi.security import OAuth2PasswordRequestForm

from ..auth.models import CreateAccountRequest, Response
from ..user.models import CreateUserResponse
from ..models import CommonHeaders

routers = APIRouter()

@routers.post("/login/", response_model=Response, summary="Login to system")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    """
    LOGIN TO SYSTEM:
    - **account**: each user must have an account to login
    - **password**: password for each account
    """

    rsp = sv_checkAccountExist(form_data.username, form_data.password)

    if rsp == "Error":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = sv_getToken(
        data={"sub": form_data.username}
    )
    
    return {"message": "Login Success", "code": status.HTTP_200_OK, "access_token": access_token, "token_type": "bearer"}

@routers.post("/create-account/", summary="Create account")
async def create_account(Item: CreateAccountRequest) -> CreateUserResponse:
    response = await createAccount(Item)

    if response.code is not status.HTTP_200_OK:
        raise HTTPException(
            status_code=response.code,
            detail=response.message,
        )
    return response

@routers.post("/logout/", summary="Logout")
async def logout_account(token: dict=Depends(JWTBearer())):
    await logOut(token)


    return "logout"
