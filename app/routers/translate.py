# app/routers/translate.py
from fastapi import APIRouter, HTTPException
from app.schemas.translation import TranslationRequest, TranslationResponse
from app.services.provider_factory import get_provider_service
from app.utils.formatters import clean_code_response
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/translate", response_model=TranslationResponse)
async def translate_code(request: TranslationRequest):
    service = get_provider_service(request.model)
    
    if not service:
        raise HTTPException(status_code=400, detail="Modelo de IA inválido.")

    try:
        translated_code = await service.translate_code(
            code=request.code,
            from_lang=request.from_lang,
            to_lang=request.to_lang
        )
        cleaned_code = clean_code_response(translated_code)
        return TranslationResponse(translated_code=cleaned_code)
    except Exception as e:
        logger.exception(f"Erro na tradução: {e}")
        raise HTTPException(
            status_code=500,
            detail="Erro ao processar tradução. Tente novamente mais tarde."
        )