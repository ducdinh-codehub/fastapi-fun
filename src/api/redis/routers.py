from fastapi import APIRouter
import httpx
import json 
from ..redis.models import Redis
routers = APIRouter()
redisCacheManager = Redis()

@routers.on_event("shutdown")
async def shutdown_event():
    await redisCacheManager.closeRedisCache()

@routers.get("/set-redis-cache/")
async def set_redis_cache():
    http_client = httpx.AsyncClient()

    value = await redisCacheManager.getItemRedisCache("test")

    if value is None:
        rsp = await http_client.get("https://65f14f71da8c6584131d5bb6.mockapi.io/api")
        value = json.dumps(rsp.json())
        redisCacheManager.setItemRedisCache("test", value)

    return {"message": "Set Redis Cache success"}

@routers.get("/get-redis-cache/")
async def get_redis_cache():

    value =  redisCacheManager.getItemRedisCache("test")

    return value

@routers.get("/get-all-keys-in-redis-cache/")
async def get_all_keys_in_redis_cache():

    value = redisCacheManager.getAllKeysInRedisCache()

    return value