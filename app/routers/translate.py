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
    print("Request recebido do frontend:", request.dict())

    # Verificação de campos obrigatórios
    missing_fields = [f for f, v in request.dict().items() if v is None or v == ""]
    if missing_fields:
        detail = f"Campos obrigatórios ausentes ou vazios: {', '.join(missing_fields)}"
        logger.warning(detail)
        raise HTTPException(status_code=400, detail=detail)

    # Seleciona serviço do provider
    service = get_provider_service(request.model)
    if not service:
        detail = f"Modelo de IA inválido: {request.model}"
        logger.warning(detail)
        raise HTTPException(status_code=400, detail=detail)

    try:
        translated_code, explanation = await service.translate_code(
            code=request.code,
            from_lang=request.from_lang,
            to_lang=request.to_lang
        )

        # Limpa o código dos blocos ``` se necessário
        cleaned_code = clean_code_response(translated_code)

        return TranslationResponse(
            translated_code=cleaned_code,
            explanation=explanation
        )

    except Exception as e:
        logger.exception(f"Erro ao processar tradução: {e}")
        raise HTTPException(
            status_code=500,
            detail="Erro ao processar tradução. Tente novamente mais tarde."
        )
