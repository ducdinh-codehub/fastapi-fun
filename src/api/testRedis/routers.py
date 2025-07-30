from fastapi import APIRouter, Depends, status, HTTPException, FastAPI
import redis
import httpx
import json 

routers = APIRouter()


rd = redis.Redis(host="localhost", port=6379, db=0)

@routers.on_event("shutdown")
async def shutdown_event():
    await rd.close()

@routers.get("/test/")
async def test_redis():
    http_client = httpx.AsyncClient()

    value = rd.get("test")

    if value is None:
        rsp = await http_client.get("https://65f14f71da8c6584131d5bb6.mockapi.io/api")
        value = json.dumps(rsp.json())
        rd.set("test", value)

    return value