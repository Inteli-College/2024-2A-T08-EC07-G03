from fastapi import APIRouter
from controllers import model
from pydantic import BaseModel

router = APIRouter()


# Classe que define a estrutura de dados de entrada
class KNRData(BaseModel):
    knr: str


# Definir a rota para o endpoint de previsão
@router.post("/predict")
def predict(input_data: KNRData):
    return model.predict(input_data.knr)
