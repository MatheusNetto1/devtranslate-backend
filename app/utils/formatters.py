# app/utils/formatters.py
import re

def clean_code_response(response: str) -> str:
    """Extrai apenas o código de dentro de blocos ``` se existir."""
    if not response:
        return ""
    match = re.search(r"```(?:\w+)?\n([\s\S]*?)\n```", response)
    return match.group(1).strip() if match else response.strip()
