from groq import Groq

from app.core.config import settings

client = Groq(
    api_key=settings.GROQ_API_KEY
)


def generate_response(prompt: str):

    completion = client.chat.completions.create(

        model=settings.GROQ_MODEL,

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.3,

        max_tokens=500
    )

    return completion.choices[0].message.content


def stream_response(prompt: str):

    stream = client.chat.completions.create(

        model=settings.GROQ_MODEL,

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.3,

        max_tokens=500,

        stream=True
    )

    for chunk in stream:

        content = chunk.choices[0].delta.content

        if content:

            yield content