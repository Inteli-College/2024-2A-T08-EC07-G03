import joblib
import pandas as pd
from fastapi import HTTPException  
import numpy as np

model = joblib.load("/home/arual/Documentos/Github/faculdade/2024-2A-T08-EC07-G03/src/backend/controllers/model/modelo.joblib")

def buscar_dados_por_knr(knr):
    df = pd.read_excel("dados.xlsx")

    dados = df[df["KNR"] == knr]

    if dados.empty:
        raise ValueError(f"KNR {knr} não encontrado.")

    dados["KNR"] = 0

    # Ajuste para garantir que você está extraindo exatamente 7 características
    features = dados[
        [
            "MODELO",
            "COR",
            "MOTOR",
            "ESTACAO",
            "USUARIO",
            "HALLE",
            "FALHA"
        ]
    ].values

    # Adiciona uma dimensão extra para corresponder à forma esperada
    features = np.expand_dims(features, axis=1)

    return features

def make_prediction(knr: str):  
    try:
        data = buscar_dados_por_knr(knr)
        print(data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    try:
        prediction = model.predict(data)
        print(type(prediction))
        return {"knr": knr, "prediction": int(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
