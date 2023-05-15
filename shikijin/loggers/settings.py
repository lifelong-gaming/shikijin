from typing import Type

from shikijin.settings import GlobalSettings

from ..settings import BaseComponentSettings, S
from .types import logger_level_type


class BaseLoggerSettings(BaseComponentSettings):
    name: str = "shikijin"
    level: logger_level_type

    @classmethod
    def from_global_settings(cls: Type[S], settings: GlobalSettings) -> S:
        return super().from_global_settings(settings)
