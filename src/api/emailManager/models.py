from pydantic import BaseModel
from sqlmodel import Field, SQLModel

class EmailManager(SQLModel, table=True): 
    id: int | None = Field(primary_key=True, default=None, nullable=False, unique=True)
    content: str
    created_at: str
    updated_at: str
    owner: str
    sending_status: bool
    receiver_email: str
    receiver_name: str
    error_sending: str | None = None

class SendingEmailRequest(BaseModel):
    email_receiver: str
    client_name: str
    created_at: str
    updated_at: str
