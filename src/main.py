from fastapi import Depends, FastAPI
import config
from database import Database
from typing_extensions import Annotated
from functools import lru_cache
from fastapi.security import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
from api.main import routers
from api.models import CommonHeaders

@lru_cache
def get_settings():
    return config.Settings()

settings = get_settings()

initDB = Database()
api_key_scheme = APIKeyHeader(name="Authorization", scheme_name="APIKey")

app = FastAPI(
    title=settings.app_name,
    description="This is backend system for Smart Agricultural App.",
    summary="For more information, please contact dinhduc4work@gmail.com",
    version=settings.app_version,
)

origins = [
    settings.backend_cors_origins,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    #allow_headers=["*"],
)

app.include_router(routers)
