import os

from dotenv import load_dotenv

from groq import Groq

import google.generativeai as genai

load_dotenv()


# ===================================
# GROQ CONFIG
# ===================================

groq_client = Groq(
    api_key=os.getenv(
        "GROQ_API_KEY"
    )
)

GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "llama3-8b-8192"
)


# ===================================
# GEMINI CONFIG
# ===================================

genai.configure(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)

gemini_model = genai.GenerativeModel(
    "gemini-1.5-flash"
)


# ===================================
# GROQ RESPONSE
# ===================================

def generate_with_groq(
    prompt: str
):

    completion = (
        groq_client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3
        )
    )

    return (
        completion
        .choices[0]
        .message
        .content
    )


# ===================================
# GEMINI RESPONSE
# ===================================

def generate_with_gemini(
    prompt: str
):

    response = (
        gemini_model.generate_content(
            prompt
        )
    )

    return response.text


# ===================================
# MAIN ROUTER
# ===================================

def generate_response(
    prompt: str
):

    try:

        print(
            "\nUSING GROQ\n"
        )

        return generate_with_groq(
            prompt
        )

    except Exception as groq_error:

        print(
            f"\nGROQ FAILED: {groq_error}"
        )

        try:

            print(
                "\nUSING GEMINI FALLBACK\n"
            )

            return generate_with_gemini(
                prompt
            )

        except Exception as gemini_error:

            print(
                f"\nGEMINI FAILED: {gemini_error}"
            )

            return """
I am temporarily unable to generate a response.

Please try again in a few moments.
"""