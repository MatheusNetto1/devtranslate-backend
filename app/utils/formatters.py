# app/utils/formatters.py
import re

def clean_code_response(response: str) -> str:
    """Extrai apenas o código do primeiro bloco ``` e ignora mensagens de introdução."""
    if not response:
        return ""

    # Extrai todos os blocos de código
    matches = re.findall(r"```(?:\w+)?\n([\s\S]*?)\n```", response)
    if matches:
        # Retorna o primeiro bloco de código sem linhas de introdução típicas
        code_lines = matches[0].splitlines()
        # Remove linhas iniciais que começam com frases comuns de introdução
        filtered_lines = [line for line in code_lines if not re.match(r'^\s*(Aqui|Mudanças|Segue).*', line)]
        return "\n".join(filtered_lines).strip()
    
    return response.strip()
