from fastapi import APIRouter, Depends, status, HTTPException

from ..identityPlant.models import IdentifyPlantsRequest
from ..identityPlant.services import identifyPlants

routers = APIRouter()

@routers.post("/image-searching-plants/")
async def image_searching_plants(item: IdentifyPlantsRequest):
    """
    Searching plant information through images:
    - **inputImage**: Input image Base64 string
    - **create_at**: The moment when user upload image to server
    - **owner**: The account sending image
    - **switchModeFlag**:
        "0": "Call this function seperately",
        "1": "Call this function from the other function" 
    """
    rsp = identifyPlants(item)

    return {"message": "Identify Plants"}
@routers.post("/insert-image/")
async def insert_image(item: IdentifyPlantsRequest):
    """
    Searching plant information through images:
    - **inputImage**: Input image Base64 string
    - **create_at**: The moment when user upload image to server
    - **owner**: The account sending image
    """

    
    rsp = identifyPlants(item)

    return {"message": "Identify Plants"}