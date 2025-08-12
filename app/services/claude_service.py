# app/services/claude_service.py
import os
import httpx

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
ANTHROPIC_API_URL = "https://api.anthropic.com/v1/messages"

async def translate_with_claude(code: str, from_lang: str, to_lang: str) -> str:
    prompt = f"Traduza o seguinte código de {from_lang} para {to_lang}:\n\n{code}"

    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(
            ANTHROPIC_API_URL,
            headers={
                "x-api-key": ANTHROPIC_API_KEY,
                "Content-Type": "application/json",
                "anthropic-version": "2023-06-01"
            },
            json={
                "model": "claude-3-opus-20240229",
                "max_tokens": 1000,
                "messages": [{"role": "user", "content": prompt}]
            }
        )
        response.raise_for_status()
        data = response.json()
        return data["content"][0]["text"].strip()