from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str

    GROQ_API_KEY: str

    GROQ_MODEL: str

    GEMINI_API_KEY: str = ""

    DEBUG: bool = True

    class Config:

        env_file = ".env"

        extra = "ignore"


settings = Settings()