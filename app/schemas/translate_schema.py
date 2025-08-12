# app/schemas/translate_schema.py
from pydantic import BaseModel, Field

class TranslateRequest(BaseModel):
    source_lang: str = Field(..., example="JavaScript")
    target_lang: str = Field(..., example="Python")
    model: str = Field(..., example="gpt-4")
    provider: str = Field(..., example="openai")
    code: str = Field(..., example="console.log('Hello World');")

class TranslateResponse(BaseModel):
    translated_code: str
    provider: str
    model: str