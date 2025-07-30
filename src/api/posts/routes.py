from typing_extensions import Annotated
from fastapi import APIRouter, Depends, Header, status, HTTPException

from api.models import CommonHeaders

routers = APIRouter()

@routers.get("/")
async def get_posts():
    return {"message": "Get Posts"}



