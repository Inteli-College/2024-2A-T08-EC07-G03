import pandas as pd
from tensorflow.keras.models import load_model
import os
import shutil

# Caminhos para o data lake e modelos
DATA_LAKE_PATH = "df_combined_final_monstro.csv"
MODEL_PATH = "modelo2.h5"
BACKUP_MODEL_PATH = "modelo2.h5"

def retrain_model(new_data: pd.DataFrame, save_new_model: bool):
    """
    Função para retreinar o modelo, combinando novos dados com o data lake, 
    e permitindo escolher entre salvar ou descartar o novo modelo treinado.
    
    Args:
        new_data (pd.DataFrame): Novo conjunto de dados em formato de DataFrame.
        save_new_model (bool): Se True, salva o novo modelo treinado; se False, restaura o modelo antigo.
        
    Returns:
        None
    """
    # Verificar se o data lake existe
    if os.path.exists(DATA_LAKE_PATH):
        # Carregar o data lake existente
        data_lake = pd.read_csv(DATA_LAKE_PATH)
        # Concatenar os novos dados ao data lake
        combined_data = pd.concat([data_lake, new_data], ignore_index=True)
    else:
        # Se o data lake não existir, usar apenas os novos dados
        combined_data = new_data

    # Salvar os dados atualizados no data lake
    combined_data.to_csv(DATA_LAKE_PATH, index=False)

    # Criar um backup do modelo atual antes do retreinamento
    if os.path.exists(MODEL_PATH):
        shutil.copy(MODEL_PATH, BACKUP_MODEL_PATH)

    # Carregar o modelo retreinado
    model = load_model(MODEL_PATH)

    # INSERIR CÓDIGO DE RETREINO AQ

    # Se o usuário escolher salvar o novo modelo
    if save_new_model:
        # Salvar o novo modelo treinado
        model.save(MODEL_PATH)
        print("Novo modelo salvo com sucesso.")
    else:
        # Restaurar o modelo antigo
        if os.path.exists(BACKUP_MODEL_PATH):
            shutil.copy(BACKUP_MODEL_PATH, MODEL_PATH)
        print("Modelo antigo restaurado com sucesso.")
