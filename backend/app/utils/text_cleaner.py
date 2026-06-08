import re


def clean_medical_text(text: str):

    text = re.sub(
        r"Sample questions for autonomous healthcare agent:.*?(?=Page \d+|$)",
        "",
        text,
        flags=re.DOTALL
    )

    text = re.sub(
        r"What key information.*?\?",
        "",
        text
    )

    text = re.sub(
        r"Summarize this page\.",
        "",
        text
    )

    text = re.sub(
        r"Extract medications or test values if present\.",
        "",
        text
    )

    text = re.sub(
        r"\n\s*\n+",
        "\n\n",
        text
    )

    return text.strip()