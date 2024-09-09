from fastapi import APIRouter, HTTPException
from controllers.model import make_prediction
from pydantic import BaseModel

router = APIRouter()

class KNRData(BaseModel):
    knr: str

@router.post("/predict")
def predict(input_data: KNRData):
    try:
        result = make_prediction(input_data.knr)
        return {"prediction": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
