
from typing import Any
from api.redis.models import Redis

redisCacheManager = Redis()

async def getItemRedisCache(key: str) -> Any:
    value = redisCacheManager.getItemRedisCache(key)
    return value

async def setItemRedisCache(key: str, value : Any):
    redisCacheManager.setItemRedisCache(key, value)

async def delItemsInRedisCache(keyList: list):
    redisCacheManager.delItemsInRedisCache(keyList)

async def flushAllRedisCache():
    redisCacheManager.flushAllRedisCache()

async def closeRedisCache():
    redisCacheManager.closeRedisCache()