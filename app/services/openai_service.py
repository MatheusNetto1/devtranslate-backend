# app/services/openai_service.py
import os
import httpx
from dotenv import load_dotenv
from app.utils.formatters import clean_code_response

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"

if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY não encontrada. Configure no arquivo .env")

async def translate(source_lang: str, target_lang: str, model: str, code: str) -> str:
    prompt = (
        f"Traduza o seguinte código de {source_lang} para {target_lang}, "
        f"mantendo a lógica e boas práticas:\n\n{code}"
    )

    async with httpx.AsyncClient(timeout=60.0) as client:
        response = await client.post(
            OPENAI_API_URL,
            headers={
                "Authorization": f"Bearer {OPENAI_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": model,
                "messages": [
                    {"role": "system", "content": "Você é um tradutor de código."},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0
            }
        )

    if response.status_code != 200:
        raise RuntimeError(f"Erro da API OpenAI: {response.text}")

    data = response.json()
    raw_code = data["choices"][0]["message"]["content"]
    return clean_code_response(raw_code)
