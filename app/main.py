# app/main.py
from dotenv import load_dotenv
load_dotenv()  # carregar antes de qualquer import que use variáveis de ambiente

import os
print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import translate

app = FastAPI(title="DevTranslate API")

# CORS para permitir acesso do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas
app.include_router(translate.router)