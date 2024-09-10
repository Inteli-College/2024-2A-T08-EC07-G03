from fastapi import HTTPException
from keras.models import load_model
import pandas as pd

# Carregar o modelo salvo no formato .h5
model = load_model("modelo2.h5")
print(type(model))

print(model)

def buscar_dados_por_knr(knr):    
    
    df = pd.read_excel("dados.xlsx")
    dados = df[df["KNR"] == knr]    
    if dados.empty:
        raise ValueError(f"KNR {knr} não encontrado.")    
    
    # Selecionar as features e prepará-las para o modelo
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

    # O Keras espera um array NumPy, então as dimensões devem estar corretas
    features = features.reshape(1, -1)    
    
    return featuresdef 

def predict(knr: str):
    try:
        data = buscar_dados_por_knr(knr)
        print(data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))    
    
    # Fazer a predição com o modelo Keras
    prediction = model.predict(data)
    print(type(prediction))  

    # O Keras geralmente retorna a predição como uma matriz, então podemos precisar extrair o valor
    prediction_value = int(
        prediction[0][0]
    )  # Supondo que seja uma classificação binária    
    
    if prediction_value == 0:
        return {"knr": knr, "prediction": prediction_value, "status": "Não tem falha"}
    else:
        return {"knr": knr, "prediction": prediction_value, "status": "Tem falha"}