from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 



# API Settings
class AppSettings(BaseSettings):
    API_URL: str
    AIRFLOW_UID: int # Will be ignored

    DATABASE_URL: str
    DATABASE_NAME: str
    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_USER: str
    DATABASE_PASSWORD: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

# Weather API URL
API_URL = AppSettings().API_URL 

# Database Settings
DATABASE_URL = AppSettings().DATABASE_URL.format(
    DATABASE_NAME=AppSettings().DATABASE_NAME,
    DATABASE_HOST=AppSettings().DATABASE_HOST,
    DATABASE_PORT=AppSettings().DATABASE_PORT,
    DATABASE_USER=AppSettings().DATABASE_USER,
    DATABASE_PASSWORD=AppSettings().DATABASE_PASSWORD
)

DATABASE_ENGINE = create_engine(DATABASE_URL, echo=True, connect_args={"sslmode": "require"})  # Create a SQLAlchemy engine for the database connection 
SESSION_LOCAL = sessionmaker(bind=DATABASE_ENGINE, autoflush=False, autocommit=False)  # Create a local session factory for the database connection
