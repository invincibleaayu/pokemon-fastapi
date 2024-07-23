from pydantic import BaseSettings, AnyHttpUrl, Field
from typing import List


class Settings(BaseSettings):
    api_v1_str: str = Field(..., alias="API_V1_STR")
    is_debug: bool = Field(..., alias="IS_DEBUG")
    project_port: int = Field(..., alias="PROJECT_PORT")
    backend_cors_origins: List[AnyHttpUrl] = Field(..., alias="BACKEND_CORS_ORIGINS")
    app_host: str = Field(..., alias="APP_HOST")
    database_url: str = Field(..., alias="DATABASE_URL")
    pokeapi_url: str = Field(..., alias="POKEAPI_URL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
