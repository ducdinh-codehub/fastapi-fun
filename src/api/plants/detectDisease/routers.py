from fastapi import APIRouter, Depends, status, HTTPException

from api.plants.identityPlant.models import IdentifyPlantsRequest

routers = APIRouter()

@routers.get("/image-diagnose-disease/")
async def image_diagnose_disease(item: IdentifyPlantsRequest):
    """
    Searching plant information through images:
    - **inputImage**: Input image Base64 string
    """
    return {"message": "Detect Disease"}