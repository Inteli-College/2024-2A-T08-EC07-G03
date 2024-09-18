from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from supabase import Client, create_client
from fastapi.responses import JSONResponse
from pymongo import MongoClient
import uvicorn
import requests
import httpx
import os


api_url: str = 'https://jhmlmzvzxtzbqxifoilb.supabase.co'
key: str = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpobWxtenZ6eHR6YnF4aWZvaWxiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjU1NjU0OTQsImV4cCI6MjA0MTE0MTQ5NH0.aVGsLYbW-4a21NTLWmG4NwC72_2V37AQ8NCJ78-LH-M'

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

client = MongoClient("mongodb://10.32.0.12:27017/", serverSelectionTimeoutMS = 2000)

supabase: Client = create_client(api_url, key)

@app.get("/index")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/healthcheck_services")
async def healthcheck_services():
    backend = await healthcheck_backend()
    datalake = await healthcheck_datalake()
    database = await healthcheck_database()
    frontend = await healthcheck_frontend()
    
    print(backend, datalake, database, frontend)
    
    return JSONResponse({
        "backend": backend,
        "datalake": datalake,
        "database": database,
        "frontend": frontend
    })

# Função para chamar healthcheck do backend
async def healthcheck_backend():
    try:
        async with httpx.AsyncClient() as client_http:
            response = await client_http.get("http://localhost:8000/health", timeout=2)
            if response.status_code == 200:
                return True
            else:
                return False
    except:
        return False

# Função para chamar healthcheck do datalake
async def healthcheck_datalake():
    try:
        client.admin.command('ping')
        return True
    except:
        return False
    
# Função para chamar healthcheck do banco de dados
async def healthcheck_database():
    try:
        supabase.table("model_training").select("*").limit(1).execute()
        return True
    except:
        return False
    
# Função para chamar healthcheck do frontend
async def healthcheck_frontend():
    try:
        async with httpx.AsyncClient() as client_http:
            response = await client_http.get("http://localhost:8002/health", timeout=2)
            if response.status_code == 200:
                return True
            else:
                return False
    except:
        return False


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
