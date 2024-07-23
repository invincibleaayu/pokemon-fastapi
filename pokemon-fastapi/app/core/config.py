from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = Field(..., alias="API_V1_STR")
    DATABASE_URL: str = Field(..., alias="DATABASE_URL")
    POKEAPI_URL: str = Field(..., alias="POKEAPI_URL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
