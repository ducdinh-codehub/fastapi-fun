from sqlmodel import Field, SQLModel
class Image:
    title_image: str
    list_image: []

class Posts(SQLModel, table=True):
    id: int = Field(primary_key=True, default=None, nullable=False, unique=True)
    title: str
    content: str
    created_at: str
    updated_at: str
    owner: str
    image_storage: str | None = None
