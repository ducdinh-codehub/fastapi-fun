from fastapi import APIRouter, Depends, status, HTTPException

routers = APIRouter()

@routers.get("/users/", tags=["Users"])
async def get_users():
    return {"message": "Get Users"}