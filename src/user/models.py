from sqlmodel import Field, SQLModel
class User(SQLModel, table=True):
    id: int = Field(primary_key=True, default=None, nullable=False, unique=True)
    name: str | None = None
    full_name: str | None = None
    email: str | None = None
    phone: str | None = None
    age: int
    created_at: str
    updated_at: str
    image_avatar: str | None = None