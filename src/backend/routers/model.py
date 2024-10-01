from fastapi import APIRouter, HTTPException, UploadFile, File
from controllers.model import predict_failure
from pydantic import BaseModel
import pandas as pd
import io

router = APIRouter()

class KNRData(BaseModel):
    knr: str

@router.post("/predict")
async def predict(input_data: KNRData):
    try:
        # Fazer a predição usando o KNR fornecido
        print(f"KNR: {input_data.knr}")
        result = await predict_failure(input_data.knr)
        
        if result is None:
            raise HTTPException(status_code=404, detail="KNR não encontrado ou predição inválida.")
        
        return {"knr": input_data.knr, "prediction": result}
    
    except ValueError as e:
        # Lançar uma exceção para KNR não encontrado
        raise HTTPException(status_code=404, detail=str(e))
    
    except Exception as e:
        # Tratar qualquer outra exceção inesperada
        raise HTTPException(status_code=500, detail=f"Erro ao fazer a predição: {str(e)}")

# Prever múltiplos KNRs a partir de um arquivo CSV
@router.post("/predict_batch")
async def predict_batch(file: UploadFile = File(...)):
    try:
        content = await file.read()
        df = pd.read_csv(io.BytesIO(content)) 
        
        # Fazer a predição para cada KNR no CSV
        knrs = df["knr"].tolist() 
        predictions = []
        for knr in knrs:
            prediction = await predict_failure(knr)
            predictions.append({"knr": knr, "prediction": prediction})
        
        return {"predictions": predictions}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar o CSV: {str(e)}")