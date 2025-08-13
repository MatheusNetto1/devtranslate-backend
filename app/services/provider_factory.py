# app/services/provider_factory.py
from app.services import openai_service, claude_service, gemini_service

def get_provider_service(provider_name: str):
    providers = {
        "openai": openai_service,
        "claude": claude_service,
        "gemini": gemini_service,
    }
    return providers.get(provider_name.lower())
