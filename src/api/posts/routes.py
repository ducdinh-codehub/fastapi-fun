from typing_extensions import Annotated
from fastapi import APIRouter, Depends, Header, status, HTTPException
from models import Response

from ..models import CommonHeaders

routers = APIRouter()

@routers.get("/", response_model=Response, summary="Get posts")
async def get_posts():
    response = Response(status="success", status_code=status.HTTP_200_OK, message="Get Posts")
    return response



