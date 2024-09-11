from fastapi import APIRouter, HTTPException
from controllers.banco.supabase import create_supabase_client 
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

supabase = create_supabase_client()

class ModelTraining(BaseModel):
    model_name: str
    training_accuracy: float
    date: str

@router.post("/insert_model_training")
def insert_model(input_data: ModelTraining):
    # Valida o formato da data
    try:
        date_formatted = datetime.strptime(input_data.date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Data inválida. O formato correto é YYYY-MM-DD")

    # Valida o campo de accuracy
    if not (0 <= input_data.training_accuracy <= 1):
        raise HTTPException(status_code=400, detail="Accuracy deve estar entre 0 e 1")

    date_as_string = date_formatted.strftime("%Y-%m-%d %H:%M:%S")

    try:
        # Inserir os dados no banco
        model = supabase.from_("model_training")\
            .insert({
                "model_name": input_data.model_name,
                "training_accuracy": input_data.training_accuracy,
                "date": date_as_string 
            })\
            .execute()

        if model.data:
            return {"message": "Model created successfully"}
        else:
            raise HTTPException(status_code=500, detail="Model creation failed")

    except Exception as e:
        # Tratar possíveis erros inesperados
        raise HTTPException(status_code=500, detail=str(e))
