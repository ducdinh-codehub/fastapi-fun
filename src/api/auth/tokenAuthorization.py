from ..redis.models import Redis
from fastapi import Request, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
import config
from jwt.exceptions import InvalidTokenError

SECRET_KEY = config.Settings().secret_key
ALGORITHM = config.Settings().algorithm
EXPIRE_TOKEN_TIME = config.Settings().access_token_expire_minutes
redis = Redis()

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True, scheme_name="APIKey (Bearer)", description = None):
        super(JWTBearer, self).__init__(auto_error=auto_error, scheme_name=scheme_name, description=description)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            # Check revoke token
            
            decode_jwt_jti = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM]).get("jti")
            print("CHECK REVOKE", decode_jwt_jti)
            is_jti_exist = redis.getItemRedisCache(key="jti"+decode_jwt_jti)

            if is_jti_exist:
                raise HTTPException(status_code=403, detail="Invalid token or token has been revoked.")

            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(jwtoken, SECRET_KEY, algorithms=[ALGORITHM])
            username = payload.get("sub")
            if username is None:
                raise credentials_exception
        except InvalidTokenError:
            raise credentials_exception

        return "AUTHEN TOKEN"
    
    