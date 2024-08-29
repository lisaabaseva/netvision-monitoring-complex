import os

from pydantic_settings import BaseSettings
from typing import Any

from functools import cached_property


class Config(BaseSettings):
    """Класс Config Класс Config - это класс настроек, который наследуется от BaseSettings из pydantic_settings.
    Он предоставляет возможность конфигурировать приложение с помощью различных параметров.
    """

    TITLE: str = os.environ.get("FASTAPI_TITLE") or "CENSUS"
    VERSION: str = os.environ.get("FASTAPI_VERSION") or "0.0.1"
    OVERSEER_URL: str = os.environ.get("OVERSEER_URL") or "http://localhost:8001"
    CRON_INTERVAL: int = int(os.environ.get("CRON_INTERVAL") or 5)
    MAX_JOBS_INSTANCES: int = int(os.environ.get("MAX_JOBS_INSTANCES") or 3)
    DATABASE_URL: str = os.environ.get("DATASOURCE_URL") or "postgresql+pg8000://postgres:123@localhost:5432/census"
    FRONTEND_URL: str = os.environ.get("FRONTEND_URL") or "http://localhost:3000"
    SERVER: str = os.environ.get("SERVER") or "gunicorn"

    @cached_property
    def get_app_config(self) -> Any:
        return {
            "title": self.TITLE,
            "version": self.VERSION,
            "overseer_url": self.OVERSEER_URL,
            "cron_interval": self.CRON_INTERVAL,
            "max_jobs_instances": self.MAX_JOBS_INSTANCES,
            "database_url": self.DATABASE_URL,
            "server": self.SERVER
        }
