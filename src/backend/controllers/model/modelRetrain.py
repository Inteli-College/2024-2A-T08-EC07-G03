from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.model_selection import train_test_split
from controllers.datalake import upload_file
from controllers.DataWarehouse import download_file
from routers.crud import insert_model
from pydantic import BaseModel
from datetime import datetime
import pandas as pd
import numpy as np


class ModelTraining(BaseModel):
    model_name: str
    training_accuracy: float
    date: str 

async def retrainModel(name_file: str):
    try:
        
        file_content = await download_file(name_file)
            
        # Tranformar em um dataframe
        
        df = pd.read_csv(file_content['content'])
        
        # Selecionar apenas as colunas numéricas para normalização
        colunas_numericas = df.select_dtypes(include=['float64', 'int64']).columns

        # Instanciar o MinMaxScaler
        scaler = MinMaxScaler()

        # Aplicar o scaler para as colunas numéricas
        df[colunas_numericas] = scaler.fit_transform(df_final[colunas_numericas])
    
        # Converter as colunas SomaTempo1, SomaTempo2 e SomaTempo718 para o tipo time delta
        df['SomaTempo1'] = pd.to_timedelta(df['SomaTempo1'])
        df['SomaTempo2'] = pd.to_timedelta(df['SomaTempo2'])
        df['SomaTempo718'] = pd.to_timedelta(df['SomaTempo718'])
        
        df['SomaTempo1'] = df['SomaTempo1'].dt.total_seconds()
        df['SomaTempo2'] = df['SomaTempo2'].dt.total_seconds()
        df['SomaTempo718'] = df['SomaTempo718'].dt.total_seconds()
        
        X = dataset[['Nvezes1', 'Nvezes2', 'Nvezes718', 'SomaTempo1', 'SomaTempo2', 'SomaTempo718', 'TemFalhaRod']].values

        Y = dataset['TemFalhaRod'].values
        
        X = np.expand_dims(X, axis=1)
        
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
        
        model = Sequential()
        model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])))
        model.add(Dropout(0.2))
        model.add(LSTM(units=50, return_sequences=False))
        model.add(Dropout(0.2))
        model.add(Dense(units=1, activation='sigmoid'))
        
        
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

        # Treinando o modelo
        model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2)
        
        loss, accuracy = model.evaluate(X_test, y_test)
        print(f'Test Accuracy: {accuracy:.2f}')
        
        # Salvar o modelo
        model.save('model.h5')
        
        # Formatar o nome do modelo com a data
        model_name = f'model_{datetime.now().strftime("%Y-%m-%d")}'
        
        model_data = ModelTraining(model_name=model_name, training_accuracy=accuracy, date=datetime.now().strftime("%Y-%m-%d"))
        
        await insert_model(model_data)
        
        # Salvar os dados no datalake
        await upload_file(csv_file)
        
        return {"message": "Modelo treinado com sucesso"}
    
    except Exception as e:
        return {"message": f"Erro ao treinar o modelo: {str(e)}"}
    


    
    
        

    