from fastapi import HTTPException
import pandas as pd
from joblib import load
from controllers.banco.supabase import create_supabase_client  # Para salvar no banco

model = load("model/modelo.pkl")
print(type(model))
print(model)

def buscar_dados_por_knr(knr):    
    df = pd.read_excel("dados.xlsx")
    dados = df[df["KNR"] == knr]    
    if dados.empty:
        raise ValueError(f"KNR {knr} não encontrado.")    

    features = dados[
        [
            "Nvezes1",
            "Nvezes2",
            "Nvezes718",
            "SomaTempo1",
            "SomaTempo2",
            "SomaTempo718",
        ]
    ].values    

    features = features.reshape(1, -1)    

    return features

def predict(knr: str):
    try:
        data = buscar_dados_por_knr(knr)
        print(data)
        
        # Fazer a predição com o modelo
        prediction = model.predict(data)
        print(type(prediction))  

        # Extrair o valor da predição
        prediction_value = int(prediction[0][0])  # Supondo que seja uma classificação binária

        status = "Tem falha" if prediction_value == 1 else "Não tem falha"

        # Salvar a predição no banco de dados
        supabase = create_supabase_client()
        supabase.from_("predictions").insert({
            "knr": knr,
            "prediction": prediction_value,
            "status": status,
        }).execute()

        return {"knr": knr, "prediction": prediction_value, "status": status}
    
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
