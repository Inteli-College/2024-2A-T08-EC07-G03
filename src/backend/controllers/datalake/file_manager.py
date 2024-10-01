from pymongo import MongoClient
import gridfs
from fastapi import UploadFile, HTTPException

# Conectar ao pc do Lab
client = MongoClient("mongodb://10.32.0.12:27017/")
db = client["data_lake"]  # Nome do banco de dados
fs = gridfs.GridFS(db)

async def upload_file(file: UploadFile, new_filename: str):
    try:
        file_id = fs.put(file.file, filename=new_filename)
        return {"message": "Arquivo carregado com sucesso!", "file_id": str(file_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao carregar o arquivo: {str(e)}")

async def download_file(filename: str):
    file_data = fs.find_one({"filename": filename})
    if not file_data:
        raise HTTPException(status_code=404, detail="Arquivo não encontrado")
    
    if "csv" in filename:
        return {"filename": filename, "content": file_data.read().decode("utf-8")}
    else:
        return {"filename": filename, "content": file_data.read()}

async def list_files():
    files = []
    try:
        for file in fs.find():
            files.append({
                "filename": file.filename,
                "file_id": str(file._id),
                "size": file.length,
            })
            
    except Exception as e:
        print(f"Erro ao listar arquivos: {e}")  # Isso exibe o erro no console
        return {"error": str(e)}  # Retorna o erro como resposta

    return {"files": files}

async def list_databases():
    databases = client.list_database_names()
    return {"databases": databases}

# Apagar todos os arquivos
async def delete_all_files_datalake():
    for file in fs.find({}):
        fs.delete(file._id)
    return {"message": "Todos os arquivos foram apagados com sucesso!"}
