# app/services/gemini_service.py
import os
import httpx

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

async def translate_with_gemini(code: str, from_lang: str, to_lang: str) -> str:
    prompt = f"Traduza o seguinte código de {from_lang} para {to_lang}:\n\n{code}"

    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(
            f"{GEMINI_API_URL}?key={GEMINI_API_KEY}",
            json={
                "contents": [
                    {"parts": [{"text": prompt}]}
                ]
            }
        )
        response.raise_for_status()
        data = response.json()
        return data["candidates"][0]["content"]["parts"][0]["text"].strip()