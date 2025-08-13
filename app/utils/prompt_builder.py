# app/utils/prompt_builder.py
def build_translation_prompt(code: str, from_lang: str, to_lang: str) -> str:
    return (
        f"Traduza o código abaixo de {from_lang} para {to_lang}, "
        "mantendo a funcionalidade e estilo:\n\n"
        f"```{from_lang}\n{code}\n```"
    )