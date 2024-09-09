from fastapi import APIRouter
from controllers.banco.supabase import create_supabase_client 
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

# Initialize supabase client
supabase = create_supabase_client()

class ModelTraining(BaseModel):
    model_name: str
    training_accuracy: float
    date: str

@router.post("/insert_model_training")
def insert_model(input_data: ModelTraining):
    # Converter a string da data para o formato datetime
    try:
        date_formatted = datetime.strptime(input_data.date, "%Y-%m-%d")
    except ValueError:
        return {"message": "Data inválida. O formato correto é YYYY-MM-DD"}

    # Converter a data para uma string antes de inserir
    date_as_string = date_formatted.strftime("%Y-%m-%d %H:%M:%S")

    # Inserir os dados no banco
    model = supabase.from_("model_training")\
        .insert({
            "model_name": input_data.model_name,
            "training_accuracy": input_data.training_accuracy,
            "date": date_as_string 
        })\
        .execute()

    # Checar se a operação foi bem-sucedida
    if model.data:
        return {"message": "Model created successfully"}
    else:
        return {"message": "Model creation failed"}
