import os

from pydantic_settings import BaseSettings
from typing import Any

from functools import cached_property


class Config(BaseSettings):
    TITLE: str = os.environ.get("FASTAPI_TITLE") or "OVERSEER"
    VERSION: str = os.environ.get("FASTAPI_VERSION") or "0.0.1"
    CENSUS_URL: str = os.environ.get("CENSUS_URL") or "http://localhost:8000"
    CAMERA_CHECK_PROTOCOL: str = os.environ.get("CAMERA_CHECK_PROTOCOL") or "http://"
    AUTHENTICATION_TIMEOUT: float = float(os.environ.get("AUTHENTICATION_TIMEOUT") or 3)
    CAMERA_CHECK_TIMEOUT: float = float(os.environ.get("CAMERA_CHECK_TIMEOUT") or 1)
    GET_CAMERAS_TIMEOUT: float = float(os.environ.get("GET_CAMERAS_TIMEOUT") or 3)

    @cached_property
    def get_app_config(self) -> Any:
        return {
            "title": self.TITLE,
            "version": self.VERSION,
            "census_url": self.CENSUS_URL,
            "camera_check_protocol": self.CAMERA_CHECK_PROTOCOL,
            "authentication_timeout": self.AUTHENTICATION_TIMEOUT,
            "camera_check_timeout": self.CAMERA_CHECK_TIMEOUT,
            "get_cameras_timeout": self.GET_CAMERAS_TIMEOUT
        }
