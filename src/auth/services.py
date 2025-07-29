
from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from typing_extensions import Annotated
from sqlmodel import Session, select
from auth.exceptions import login_exception
import hashlib
from auth.models import Auth, CreateAccountRequest
import config
from database import Database
from datetime import datetime, timedelta, timezone
import jwt
from jwt.exceptions import InvalidTokenError
from auth.models import Auth
from user.models import CreateUserResponse, User
from user.services import createUser

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

def checkAccountExist(user_account: str, user_password: str):
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
    
def validateAccount(username: str, password: str):
    exception_duplicate_account = HTTPException(
        status_code=status.HTTP_406_NOT_ACCEPTABLE,
        detail="Your current account is already exist, please check again !!!",
    )
    
    rsp = checkAccountExist(username, password)

    if rsp is "Success":
        raise exception_duplicate_account
    
def createAccount(data : CreateAccountRequest) -> CreateUserResponse:
    user = User(name = data.name, full_name = data.full_name, email = data.email, phone = data.phone, age = data.age, created_at = data.created_at, updated_at = data.updated_at, image_avatar = data.image_avatar)
    response = createUser(user)

    if(response.code is not status.HTTP_200_OK):
        return response

    hashpassword = hashlib.md5(data.password.encode()).hexdigest()

    validateAccount(data.username, hashpassword)

    try:
        acc = Auth(user_id = response.user_id, username = data.username, password = hashpassword, created_at = data.created_at, updated_at = data.updated_at)
        session = Session(engine)
        session.add(acc)
        session.commit()
        response = CreateUserResponse(user_id = response.user_id, message = "User created successfully", code = 200)
    except Exception as e:
        response = CreateUserResponse(user_id = None, message = f"User created fail error: {e}", code = status.HTTP_400_BAD_REQUEST)

    return response