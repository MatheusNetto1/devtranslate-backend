# app/services/openai_service.py
import os
import re
from openai import AsyncOpenAI
from app.utils.prompt_builder import build_gpt_translation_prompt

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def translate_code(code: str, from_lang: str, to_lang: str) -> tuple[str, str]:
    prompt = build_gpt_translation_prompt(code, from_lang, to_lang)

    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
    )

    text = response.choices[0].message.content

    # Separar código traduzido da explicação
    match = re.search(r"```(?:\w+)?\n([\s\S]*?)\n```", text)
    translated_code = match.group(1).strip() if match else text.strip()

    explanation = re.sub(r"```[\s\S]*?```", "", text).strip()

    return translated_code, explanation
