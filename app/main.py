from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import TranslationRequest, TranslationResponse
from services.openai_service import translate_with_gpt4
from services.claude_service import translate_with_claude
from services.gemini_service import translate_with_gemini

app = FastAPI(title="DevTranslate API")

# Permitir acesso do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # depois podemos restringir para o domínio do frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/translate", response_model=TranslationResponse)
async def translate_code(request: TranslationRequest):
    try:
        if request.model == "GPT-4":
            translated = await translate_with_gpt4(request.code, request.from_lang, request.to_lang)
        elif request.model == "Claude":
            translated = await translate_with_claude(request.code, request.from_lang, request.to_lang)
        elif request.model == "Gemini":
            translated = await translate_with_gemini(request.code, request.from_lang, request.to_lang)
        else:
            raise HTTPException(status_code=400, detail="Modelo inválido.")

        return TranslationResponse(translated_code=translated)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))