from fastapi import APIRouter, HTTPException, UploadFile, File
from controllers.model import predict_failure
from pydantic import BaseModel
import pandas as pd


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

@router.post("/retrain")
async def retrain(file: UploadFile = File(...), save_new_model: bool = True):
    try:
        # Verifica se o arquivo é um CSV
        if file.content_type != 'text/csv':
            raise HTTPException(status_code=400, detail="O arquivo deve ser um CSV.")

        # Carrega o arquivo CSV em um DataFrame
        contents = await file.read()
        df = pd.read_csv(pd.io.common.BytesIO(contents))

        # Chama a função de retreinamento do modelo com os dados fornecidos
        retrain_model(df, save_new_model)

        if save_new_model:
            return {"detail": "Modelo retreinado e salvo com sucesso."}
        else:
            return {"detail": "Novo modelo descartado. Modelo antigo restaurado com sucesso."}

    except pd.errors.EmptyDataError:
        raise HTTPException(status_code=400, detail="O arquivo CSV está vazio ou inválido.")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao retreinar o modelo: {str(e)}")
