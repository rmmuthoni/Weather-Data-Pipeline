from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import HttpUrl, Field


# API Settings
class AppSettings(BaseSettings):
    API_URL: str
    AIRFLOW_UID: int # Will be ignored

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

API_URL = AppSettings().API_URL 