from fastapi import APIRouter, Depends, status, HTTPException

routers = APIRouter()

@routers.get("/posts/", tags=["Posts"])
async def get_posts():
    return {"message": "Get Posts"}



