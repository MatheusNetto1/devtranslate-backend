# app/schemas/models.py
from pydantic import BaseModel

class TranslationRequest(BaseModel):
    code: str
    from_lang: str
    to_lang: str
    model: str

class TranslationResponse(BaseModel):
    translated_code: str