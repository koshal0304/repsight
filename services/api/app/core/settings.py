"""The only module that reads environment variables (05 §5.2); names follow 02 Appendix A."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # `.env` holds every service's variables (05 §4.5); each field arrives with its first user.
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    celery_broker_url: str = "redis://localhost:6379/1"


settings = Settings()
