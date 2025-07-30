from pydantic import BaseModel
from sqlmodel import Field, SQLModel

from api.user.models import CreateUserRequest
class Auth(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None, nullable=False, unique=True, index=True)
    user_id: int | None = Field(foreign_key="user.id", default=None, nullable=False, unique=True)
    username: str
    password: str # hash value
    created_at: str
    updated_at: str

class TokenData(BaseModel):
    username: str | None = None

class Item(BaseModel):
    account: str
    password: str

class Response(BaseModel):
    message: str
    code: int
    access_token: str
    token_type: str
class Token(BaseModel):
    access_token: str
    token_type: str

class CreateAccountRequest(CreateUserRequest):
    username: str
    password: str
    created_at: str
    updated_at: str

