from fastapi import APIRouter, UploadFile, File
from controllers.DataWarehouse import upload_file, download_file, list_files, list_databases

router = APIRouter()

# Rota de upload de arquivo
@router.post("/upload")
async def upload_file_warehouse(file: UploadFile = File(...)):
    return await upload_file(file)

# Rota para recuperar arquivo pelo nome
@router.get("/download/{filename}")
async def download_file_warehouse(filename: str):
    return await download_file(filename)

# Rota para listar todos os arquivos
@router.get("/list")
async def list_files_warehouse():
    return await list_files()

# Rota para listar todos os bancos de dados
@router.get("/databases")
async def list_database_warehouse():
    return await list_databases()


