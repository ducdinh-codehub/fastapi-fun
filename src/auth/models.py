from pydantic import BaseModel
from sqlmodel import Field, SQLModel
class Auth(SQLModel, table=True):
    id: int = Field(primary_key=True, default=None, nullable=False, unique=True)
    user_id: int = Field(foreign_key="user.id", default=None, nullable=False, unique=True)
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
