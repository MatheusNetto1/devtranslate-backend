# app/utils/formatters.py
def clean_code_response(response: str) -> str:
    """
    Remove marcações de bloco de código (```lang ... ```) da resposta.
    """
    if response.startswith("```"):
        lines = response.split("\n")
        # Remove a primeira e a última linha se forem blocos de código
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines[-1].startswith("```"):
            lines = lines[:-1]
        return "\n".join(lines).strip()
    return response.strip()