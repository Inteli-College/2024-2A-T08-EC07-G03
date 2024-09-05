from fastapi import APIRouter
from controllers import banco
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()


# Initialize supabase client
supabase = banco.create_supabase_client()

class ModelTraining(BaseModel):
    model_name : str
    training_accuracy : float
    date : str

@router.post("/insert_model_training")
def insert_model(input_data: ModelTraining):
    # Converter a string da data para o formato datetime
    try:
        date_formatted = datetime.strptime(input_data.date, "%Y-%m-%d")  # Verificar formato da data
    except ValueError:
        return {"message": "Data inválida. O formato correto é YYYY-MM-DD"}

    # Converter a data para uma string antes de inserir
    date_as_string = date_formatted.strftime("%Y-%m-%d %H:%M:%S")  # Formatar como string

    model = supabase.from_("model_training")\
        .insert({
            "model_name": input_data.model_name,
            "training_accuracy": input_data.training_accuracy,
            "date": date_as_string  # Inserir data como string formatada
        })\
        .execute()

    if model:
        return {"message": "Model created successfully"}
    else:
        return {"message": "Model creation failed"}
