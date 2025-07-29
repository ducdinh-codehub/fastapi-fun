from datetime import timedelta
from fastapi import APIRouter, Depends, status, HTTPException
from auth.services import checkUserExist as sv_checkUserExist
from auth.services import createAccessToken as sv_getToken
from pydantic import (
    BaseModel,
)   
from typing import Any, Annotated
from fastapi.security import OAuth2PasswordRequestForm
import config

from auth.models import Response

routers = APIRouter()

@routers.post("/auth/login/", response_model=Response, summary="Login to system", tags=["Auth"])
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    """
    LOGIN TO SYSTEM:
    - **account**: each user must have an account to login
    - **password**: password for each account
    """

    rsp = sv_checkUserExist(form_data.username, form_data.password)

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
