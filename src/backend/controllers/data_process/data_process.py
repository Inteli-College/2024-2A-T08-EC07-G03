from datetime import datetime
from pydantic import BaseModel
import pandas as pd
import numpy as np
import io
from  controllers.datalake.file_manager import download_file
from routers.crud import insert_data_entries

class NewEntries(BaseModel):
    date: datetime
    nvezes1: int
    nvezes2: int
    nvezes718: int
    somatempo1: int
    somatempo2: int
    somatempo718: int

async def build_feature_prediction(knr):
    # Pegar os dados do arquivo
    print("Estou no processo de predição")
    
    file_data = await download_file("df_combined_final_monstro.csv")
    
    file_content = file_data["content"]

    # Transformar em CSV e depois transformar em DataFrame
    file_data = pd.read_csv(io.StringIO(file_content))
    
    # Pegar só os dados do KNR  
    file_data = file_data[file_data["KNR"] == knr]
    
    # Converter o timedelta para segundos
    file_data["SomaTempo1"] = pd.to_timedelta(file_data["SomaTempo1"]).dt.total_seconds()
    file_data["SomaTempo2"] = pd.to_timedelta(file_data["SomaTempo2"]).dt.total_seconds()
    file_data["SomaTempo718"] = pd.to_timedelta(file_data["SomaTempo718"]).dt.total_seconds()

    print(file_data.values)
    
    # Montar dicionario para enviar para o banco de dados
    db_data = {
        "date": datetime.now(),
        "nvezes1": file_data["Nvezes1"].values[0],
        "nvezes2": file_data["Nvezes2"].values[0],
        "nvezes718": file_data["Nvezes718"].values[0],
        "somatempo1": file_data["SomaTempo1"].values[0],
        "somatempo2": file_data["SomaTempo2"].values[0],
        "somatempo718": file_data["SomaTempo718"].values[0],
    }
    
    db_data_pydantic = NewEntries(**db_data)
    
    insert_data_entries(db_data_pydantic)

    
    file_data = file_data[
        [
            "Nvezes1",
            "Nvezes2",
            "Nvezes718",
            "SomaTempo1",
            "SomaTempo2",
            "SomaTempo718",
        ]
    ].values

    # Add um valor aleatório que indica o TemFalhaRod
    file_data = np.hstack((file_data, np.random.rand(file_data.shape[0], 1))) # TIRAR ISSO DEPOIS !!!!GAMBIARA!!!!
        
    # Reshape para o formato que o Keras espera
    file_data = file_data.reshape(1, 1, -1)  # (1, 1, 7)
    
    return file_data

