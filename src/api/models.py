
from pydantic import BaseModel

class CommonHeaders(BaseModel):
    Origin: str
    Authorization: str | None = None
    ContentType: str | None = "application/json"
