from ..settings import GlobalSettings
from .base import BaseLogger


class LoggerFactory:
    def create(self, settings: GlobalSettings) -> BaseLogger:
        raise NotImplementedError()
