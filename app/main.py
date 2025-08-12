# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import translate

app = FastAPI(title="DevTranslate Backend", version="1.0.0")

# Configuração do CORS (ajuste o domínio do frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # frontend local
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas
app.include_router(translate.router, prefix="/api", tags=["Tradução"])

@app.get("/")
def root():
    return {"message": "DevTranslate API is running"}