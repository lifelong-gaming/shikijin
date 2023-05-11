from typing import Type

from shikijin.settings import GlobalSettings

from ..settings import BaseComponentSettings, S


class BaseLoggerSettings(BaseComponentSettings):
    name: str = "shikijin"

    @classmethod
    def from_global_settings(cls: Type[S], settings: GlobalSettings) -> S:
        return super().from_global_settings(settings)
