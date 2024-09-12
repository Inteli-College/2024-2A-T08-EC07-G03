from fastapi import APIRouter, HTTPException
from controllers.model import predict
from pydantic import BaseModel

router = APIRouter()

class KNRData(BaseModel):
    knr: str

@router.post("/predict")
def predict(input_data: KNRData):
    try:
        # Fazer a predição usando o KNR fornecido
        result = predict(input_data.knr)
        
        if result is None:
            raise HTTPException(status_code=404, detail="KNR não encontrado ou predição inválida.")
        
        return {"knr": input_data.knr, "prediction": result}
    
    except ValueError as e:
        # Lançar uma exceção para KNR não encontrado
        raise HTTPException(status_code=404, detail=str(e))
    
    except Exception as e:
        # Tratar qualquer outra exceção inesperada
        raise HTTPException(status_code=500, detail=f"Erro ao fazer a predição: {str(e)}")
