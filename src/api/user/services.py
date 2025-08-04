from fastapi import HTTPException, status
from database import Database
from sqlmodel import Session, select

from api.user.models import CreateUserResponse, User

engine = Database().engine


def validateData(data):
    exception_empty_field = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="You cannot leave required field empty, please check full name, name, email again !!!",
    )

    exception_duplicate_user = HTTPException(
        status_code=status.HTTP_406_NOT_ACCEPTABLE,
        detail="Your information is already exist, please check again !!!",
    )

    if data.name is None or data.full_name is None or data.email is None:
        raise exception_empty_field
    
    #rsp = checkUserExist(data.name, data.full_name, data.email, data.phone)

    '''
    if rsp is not None:
        raise exception_duplicate_user
    '''


def createUser(data) -> CreateUserResponse:
    validateData(data)
    user = User(name = data.name, full_name = data.full_name, email = data.email, phone = data.phone, age = data.age, created_at = data.created_at, updated_at = data.updated_at, image_avatar = data.image_avatar, hash_email=data.hash_email)
    
    try:
        session =  Session(engine)
        session.add(user)
        session.commit()
        response = CreateUserResponse(user_id = user.id, message = "User created successfully", code = 200)
    except Exception as e:
        response = CreateUserResponse(user_id = None, message = f"User created fail error: {e}", code = status.HTTP_400_BAD_REQUEST)
    return response

def checkUserExist(name: str, full_name: str, email: str, phone: str):
    session = Session(engine)
    statement = select(User).where(User.name == name).where(User.full_name == full_name).where(User.email == email).where(User.phone == phone)
    results = session.exec(statement)
    
    return results.first()

