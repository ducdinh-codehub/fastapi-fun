from fastapi import APIRouter
import httpx
import json 
from api.redis.models import Redis
import api.redis.services as services
routers = APIRouter()

@routers.on_event("shutdown")
async def shutdown_event():
    await services.closeRedisCache()

@routers.get("/set-redis-cache/")
async def set_redis_cache():
    http_client = httpx.AsyncClient()

    value = await services.getItemRedisCache("test")

    if value is None:
        rsp = await http_client.get("https://65f14f71da8c6584131d5bb6.mockapi.io/api")
        value = json.dumps(rsp.json())
        await services.setItemRedisCache("test", value)

    return {"message": "Set Redis Cache success"}

@routers.get("/get-redis-cache/")
async def get_redis_cache():

    value = await services.getItemRedisCache("test")

    return value