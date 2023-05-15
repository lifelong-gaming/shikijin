from logging import INFO
from typing import Optional

from shikijin.settings import GlobalSettings

from ..settings import BaseLoggerSettings


class BasicLoggerSettings(BaseLoggerSettings):
    file_path: Optional[str] = None

    @classmethod
    def from_global_settings(cls, settings: GlobalSettings) -> "BasicLoggerSettings":
        return BasicLoggerSettings(
            name=settings.logger_settings.get("name", "shikijin"),
            level=settings.logger_settings.get("level", INFO),
            file_path=settings.logger_settings.get("file_path", None),
        )
