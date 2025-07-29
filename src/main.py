from fastapi import Depends, FastAPI
import config
from database import Database
from typing_extensions import Annotated
from functools import lru_cache
import auth.routes as auth
import posts.routes as posts
import user.routes as user
from auth.services import authenToken
from fastapi.security import APIKeyHeader
from auth.tokenAuthorization import JWTBearer


@lru_cache
def get_settings():
    return config.Settings()

settings = get_settings()

initDB = Database()
api_key_scheme = APIKeyHeader(name="Authorization", scheme_name="APIKey")
app = FastAPI(
    title=settings.app_name,
    description="This is backend system for smart agricultural app.",
    summary="For more information, please visit https://github.com/ducdinh/smart-agricultural-app",
    version=settings.app_version,
)
app.include_router(auth.routers)
app.include_router(posts.routers, dependencies=[Depends(JWTBearer())])
app.include_router(user.routers, dependencies=[Depends(JWTBearer())])



@app.get("/", tags=["Root"])
async def root(token: Annotated[str, Depends(authenToken)]):
    initDB.init_db()
    return {"message": "Hello World"}

@app.get("/appinfor", tags=["Root"])
async def info(settings: Annotated[config.Settings, Depends(get_settings)], token: Annotated[str, Depends(api_key_scheme)]):
    return {
        "app_name": settings.app_name,
        "app_version": settings.app_version,
        }