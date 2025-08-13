# app/services/provider_factory.py
from app.services import openai_service, claude_service, gemini_service

def get_provider_service(provider_name: str):
    # Normalizar nomes comuns para os providers corretos
    mapping = {
        "openai": "openai",
        "gpt-4": "openai",
        "gpt4": "openai",
        "claude": "claude",
        "anthropic": "claude",
        "gemini": "gemini",
        "google": "gemini",
    }

    normalized = mapping.get(provider_name.lower())
    
    providers = {
        "openai": openai_service,
        "claude": claude_service,
        "gemini": gemini_service,
    }

    return providers.get(normalized)
