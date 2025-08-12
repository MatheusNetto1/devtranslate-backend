# app/services/openai_service.py
import os
import httpx

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"

async def translate_with_gpt4(code: str, from_lang: str, to_lang: str) -> str:
    prompt = f"Traduza o seguinte código de {from_lang} para {to_lang}:\n\n{code}"

    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(
            OPENAI_API_URL,
            headers={
                "Authorization": f"Bearer {OPENAI_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-4",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0
            }
        )
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()
