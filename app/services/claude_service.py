# app/services/claude_service.py
import os
import anthropic
from app.utils.prompt_builder import build_translation_prompt

client = anthropic.AsyncAnthropic(api_key=os.getenv("CLAUDE_API_KEY"))

async def translate_code(code: str, from_lang: str, to_lang: str) -> str:
    prompt = build_translation_prompt(code, from_lang, to_lang)
    response = await client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text
