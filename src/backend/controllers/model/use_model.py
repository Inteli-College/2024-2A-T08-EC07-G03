from fastapi import HTTPException
import joblib
import pandas as pd


model = joblib.load("modelo.joblib")

print(type(model))
print(model)


def buscar_dados_por_knr(knr):

    df = pd.read_excel("dados.xlsx")

    dados = df[df["KNR"] == knr]

    if dados.empty:
        raise ValueError(f"KNR {knr} não encontrado.")

    dados["KNR"] = 0

    features = dados[
        [
            "KNR",
            "MODELO",
            "COR",
            "MOTOR",
            "ESTACAO",
            "USUARIO",
            "HALLE",
            "FALHA",
            "DATA_x",
            "NAME",
            "ID",
            "STATUS",
            "UNIT",
            "VALUE_ID",
            "VALUE",
            "DATA_y",
        ]
    ].values

    features = features.reshape(1, -1)

    return features


def predict(knr: str):
    try:
        data = buscar_dados_por_knr(knr)
        print(data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    prediction = model.predict(data)
    print(type(prediction))

    return {"knr": knr, "prediction": int(prediction[0])}
