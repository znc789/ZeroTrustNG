from typing import List

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Zero Trust Network Guardian"
    app_env: str = "development"
    app_debug: bool = True
    secret_key: str = "change-me-in-prod"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60
    postgres_url: str = "postgresql://postgres:postgres@localhost:5432/ztng"
    mongo_url: str = "mongodb://localhost:27017"
    redis_url: str = "redis://localhost:6379/0"
    elastic_url: str = "http://localhost:9200"
    api_prefix: str = "/api/v1"
    cors_origins: List[str] = Field(
        default_factory=lambda: ["http://localhost:3000", "http://127.0.0.1:3000"]
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


settings = Settings()
