
from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from typing_extensions import Annotated
from sqlmodel import Session, select
from auth.exceptions import login_exception
import hashlib
from auth.models import Auth
import config
from database import Database
from datetime import datetime, timedelta, timezone
import jwt
from jwt.exceptions import InvalidTokenError

engine = Database().engine

oauth2_scheme = APIKeyHeader(name="Authorization", scheme_name="APIKey")
SECRET_KEY = config.Settings().secret_key
ALGORITHM = config.Settings().algorithm
EXPIRE_TOKEN_TIME = config.Settings().access_token_expire_minutes

def authenToken(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception

    return "AUTHEN TOKEN"

def createAccessToken(data: dict):
    to_encode = data.copy()
    expires_delta = timedelta(minutes=EXPIRE_TOKEN_TIME)
    
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def checkUserExist(user_account: str, user_password: str):
    is_user_found = False
    # Asuming user pasword is md5 hash
    hash_user_password = hashlib.md5(user_password.encode()).hexdigest()
    response =selectByUsernamePassword(user_account, hash_user_password)
    if response is None:
        is_user_found = False
    else:
        is_user_found = True

    return "Success" if is_user_found else  "Error"

def selectByUsernamePassword(username: str, password: str) -> Auth:
    with Session(engine) as session:
        statement = select(Auth).where(Auth.username == username).where(Auth.password == password)
        results = session.exec(statement)
        
        return results.first()