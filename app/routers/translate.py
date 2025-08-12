# app/routers/translate.py
from fastapi import APIRouter, HTTPException
from app.schemas.translate_schema import TranslateRequest, TranslateResponse
from app.services.provider_factory import get_provider_service

router = APIRouter()

@router.post("/translate", response_model=TranslateResponse)
async def translate_code(payload: TranslateRequest):
    provider_service = get_provider_service(payload.provider)

    if not provider_service:
        raise HTTPException(status_code=400, detail="Provedor de IA inválido ou não suportado.")

    try:
        translated_code = await provider_service.translate(
            source_lang=payload.source_lang,
            target_lang=payload.target_lang,
            model=payload.model,
            code=payload.code
        )
        return TranslateResponse(
            translated_code=translated_code,
            provider=payload.provider,
            model=payload.model
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))