# app/services/gemini_service.py
import os
import google.generativeai as genai
from app.utils.prompt_builder import build_translation_prompt

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

async def translate_code(code: str, from_lang: str, to_lang: str) -> str:
    prompt = build_translation_prompt(code, from_lang, to_lang)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = await model.generate_content_async(prompt)
    return response.text
