

from fastapi import HTTPException,status
from sqlmodel import Session
from api.plants.identityPlant.models import IdentifyPlantsRequest, ImageInforaStorage
from database import Database
from utility import processInput
from api.plants.identityPlant.models import switchModeFlagData

engine = Database().engine

def validateData(data: IdentifyPlantsRequest):
    exception = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Input image, created date and owner fields are empty, please check one of those field again !!!",
        headers={"WWW-Authenticate": "Bearer"},
    )
    print("data.inputImage", data.inputImage)
    if len(data.inputImage) <= 0 or len(data.created_at) <= 0 or len(data.owner) <= 0:
        raise exception

def identifyPlants(item: IdentifyPlantsRequest):
    validateData(item)
    processInput(item.inputImage)
    item.switchModeFlag = "1"
    insertImageData(item)
    return {"message": "Identify Plants"}

def insertImageData(item: IdentifyPlantsRequest):
    if(switchModeFlagData[item.switchModeFlag] == switchModeFlagData["0"]):
        validateData(item)
    image = ImageInforaStorage(inputImageBase64 = item.inputImage, created_at = item.created_at, updated_at = item.updated_at, owner = item.owner, switchModeFlag = item.switchModeFlag)
    
    session = Session(engine)
    session.add(image)
    session.commit()
    
    '''
        try:
            session = Session(engine)
            session.add(image)
            session.commit()
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=e,
                headers={"WWW-Authenticate": "Bearer"},
            )
    '''
    return {"message": "Insert Image into Storage success"}