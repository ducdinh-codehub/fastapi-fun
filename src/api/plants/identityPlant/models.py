from pydantic import BaseModel
from sqlmodel import Field, SQLModel


switchModeFlagData = {
    "0": "Call this function seperately",
    "1": "Call this function from the other function" 
}

class IdentifyPlantsRequest(BaseModel):
    inputImage: str
    created_at: str
    updated_at: str
    switchModeFlag: str = "0"
    owner: str

class ImageInforaStorage(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None, nullable=False, unique=True, index=True)
    inputImageBase64: str
    created_at: str
    updated_at: str
    owner: str
    switchModeFlag: str
    error: str | None = None

