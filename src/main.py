from fastapi import Depends, FastAPI
import config
from database import init_db
from typing_extensions import Annotated
from functools import lru_cache
import auth.routes as auth
from fastapi.security import APIKeyHeader


api_key_scheme = APIKeyHeader(name="Authorization", scheme_name="APIKey")

app = FastAPI()
app.include_router(auth.routers)

@lru_cache
def get_settings():
    return config.Settings()

@app.get("/", tags=["Root"])
async def root():
    init_db()
    return {"message": "Hello World"}

@app.get("/appinfor", tags=["Root"])
async def info(settings: Annotated[config.Settings, Depends(get_settings)], token: Annotated[str, Depends(api_key_scheme)]):
    return {
        "app_name": settings.app_name,
        "app_version": settings.app_version,
        }