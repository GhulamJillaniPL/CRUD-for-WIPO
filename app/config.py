from pydantic import BaseSettings

class Settings(BaseSettings):
    wipo_api_key: str
    wipo_api_secret: str
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()
