# app/utils/prompt_builder.py
def build_gpt_translation_prompt(code: str, from_lang: str, to_lang: str) -> str:
    return (
        f"Traduza o código abaixo de {from_lang} para {to_lang}. "
        "Não escreva mensagens de introdução como 'Aqui está o código…' ou 'Mudanças feitas…'. "
        "Forneça apenas o código traduzido dentro de um bloco de código e, em seguida, "
        "toda explicação detalhada fora do bloco de código.\n\n"
        f"```{from_lang}\n{code}\n```"
    )

def build_gemini_translation_prompt(code: str, from_lang: str, to_lang: str) -> str:
    return (
        f"Traduza o código abaixo de {from_lang} para {to_lang}, "
        "mantendo a funcionalidade e o estilo da linguagem de destino. "
        "Após a tradução, forneça uma breve explicação das mudanças feitas e "
        "por que elas seguem a lógica da linguagem traduzida.\n\n"
        f"```{from_lang}\n{code}\n```"
    )

def build_translation_prompt(code: str, from_lang: str, to_lang: str) -> str:
    return (
        f"Traduza o código abaixo de {from_lang} para {to_lang}, "
        "mantendo a funcionalidade e o estilo da linguagem de destino. "
        "Não inclua comentários no código. "
        "Toda explicação detalhada sobre as mudanças deve ser fornecida separadamente, "
        "fora do bloco de código.\n\n"
        f"```{from_lang}\n{code}\n```"
    )