from pydantic import BaseModel
from sqlmodel import Field, SQLModel
from typing import Generic, TypeVar, Optional, Any

T = TypeVar("T")
class User(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None, nullable=False, unique=True)
    name: str | None = None
    full_name: str | None = None
    email: str | None = None
    phone: str | None = None
    age: int
    created_at: str
    updated_at: str
    image_avatar: str | None = None
    hash_email: int 
    is_locked: bool | None = False
    description: str | None = None

class CreateUserRequest(BaseModel):
    name: str | None = None
    full_name: str | None = None
    email: str | None = None
    phone: str | None = None
    age: int
    created_at: str
    updated_at: str
    image_avatar: str | None = None

class CreateUserResponse(BaseModel):
    user_id: int| None = None
    message: str | None = None
    code: int | None = None

class FilterUserItem(BaseModel):
    name: str | None = None
    full_name: str | None = None
    email: str | None = None
    phone: str | None = None
    age: int | None = None
    created_at: str | None = None
    updated_at: str | None = None

class GetUserResponse(BaseModel):
    message: str | None = None
    code: int | None = None
    data: Optional[T] = None
