from fastapi import APIRouter, Depends
from api.auth.tokenAuthorization import JWTBearer
import api.auth.routes as auth
from database import Database
import api.posts.routes as posts
import api.user.routes as user
import api.emailManager.routes as email
import api.redis.routers as testRedis
import api.rabbitmq.routers as rabbitmq

routers = APIRouter()
initDB = Database()

@routers.get("/", tags=["Root"])
async def root():
    initDB.init_db()
    return {"message": "This is welcome page for Smart Agricultural BE system."}

routers.include_router(auth.routers, prefix="/auth", tags=["Auth"])
routers.include_router(posts.routers, prefix="/posts", tags=["Posts"], dependencies=[Depends(JWTBearer())])
routers.include_router(user.routers, prefix="/users", tags=["Users"], dependencies=[Depends(JWTBearer())])
routers.include_router(email.routers, prefix="/email", tags=["Email"], dependencies=[Depends(JWTBearer())])
routers.include_router(testRedis.routers, prefix="/redis", tags=["Redis"], dependencies=[Depends(JWTBearer())])
routers.include_router(rabbitmq.routers, prefix="/rabbitmq", tags=["RabbitMQ"], dependencies=[Depends(JWTBearer())])

