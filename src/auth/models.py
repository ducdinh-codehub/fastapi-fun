from sqlmodel import Field, SQLModel
class Auth(SQLModel, table=True):
    id: int = Field(primary_key=True, default=None, nullable=False, unique=True)
    user_id: int = Field(foreign_key="user.id", default=None, nullable=False, unique=True)
    account: str
    password: str
    created_at: str
    updated_at: str
