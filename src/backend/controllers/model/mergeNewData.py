import pandas as pd
from tensorflow.keras.models import load_model
from controllers.datalake import download_file, list_files
from controllers.DataWarehouse import upload_file
from datetime import datetime
import os
import shutil

        
# Processamento de dados cru para serem subidos no data warehouse

async def process_data_datawarehouse(name_files: list):
    
    dataframes = []
    
    # Puxar os arquivos do data lake
    
    for file in name_files:
        
        try:
            file_content = await download_file(file)
            
            df = pd.read_csv(file_content.decode('utf-8'))
            
            dataframes.append(df)
            
        except Exception as e:
            print(f"Erro ao baixar o arquivo {file}: {str(e)}")
            continue
        
    # PROCESSAMENTO DOS DADOS
    
    # Pegar o ultimo arquivo do data lake e ver quais KNR já estão na tabela antiga
    
    
    
    
    # Salvar arquivo final
    
    final_file = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_final.csv'
    
    df.to_csv(final_file, index=False)
    
    await upload_file(final_file)
    
    return final_file
    
    
    
    