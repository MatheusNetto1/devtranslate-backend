# app/schemas/translation.py
from pydantic import BaseModel, Field

class TranslationRequest(BaseModel):
    code: str = Field(..., description="Código-fonte original")
    from_lang: str = Field(..., alias="from", description="Linguagem de origem")
    to_lang: str = Field(..., alias="to", description="Linguagem de destino")
    model: str = Field(..., description="Modelo de IA a ser usado (openai, claude, gemini)")

    # Configuração compatível com Pydantic v2
    model_config = {
        "populate_by_name": True
    }

class TranslationResponse(BaseModel):
    translated_code: str
    explanation: str