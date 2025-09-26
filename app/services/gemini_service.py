# app/services/gemini_service.py
import os
import google.generativeai as genai
from app.utils.prompt_builder import build_gemini_translation_prompt
import re

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

async def translate_code(code: str, from_lang: str, to_lang: str) -> tuple[str, str]:
    prompt = build_gemini_translation_prompt(code, from_lang, to_lang)
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = await model.generate_content_async(prompt)

    text = response.text

    # Separar código traduzido da explicação
    match = re.search(r"```(?:\w+)?\n([\s\S]*?)\n```", text)
    translated_code = match.group(1).strip() if match else text.strip()

    explanation = re.sub(r"```[\s\S]*?```", "", text).strip()

    return translated_code, explanation