# app/services/openai_service.py
import os
from openai import AsyncOpenAI
from app.utils.prompt_builder import build_translation_prompt

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def translate_code(code: str, from_lang: str, to_lang: str) -> str:
    prompt = build_translation_prompt(code, from_lang, to_lang)
    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content
