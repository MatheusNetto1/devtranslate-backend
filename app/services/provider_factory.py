# app/services/provider_factory.py
from app.services import openai_service

def get_provider_service(provider_name: str):
    providers = {
        "openai": openai_service
        # Adicione outros aqui: "anthropic": anthropic_service, "gemini": gemini_service, etc.
    }
    return providers.get(provider_name.lower())