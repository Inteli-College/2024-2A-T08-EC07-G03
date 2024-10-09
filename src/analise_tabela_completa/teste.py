import pandas as pd
import joblib

csv_file_path = "teste_falha.csv"
novos_dados = pd.read_csv(csv_file_path)

novos_dados = novos_dados.drop(
    columns=["KNR", "MOD", "FALHAS_ROD", "TROCA_PECA", "REPINT"]
)


rf_model = joblib.load("falhaROD.pkl")


predicao = rf_model.predict(novos_dados)

print("Previsão:", predicao)
