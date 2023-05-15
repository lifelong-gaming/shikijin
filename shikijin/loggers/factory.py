from ..settings import GlobalSettings, LoggerType
from .base import BaseLogger
from .basic_logger.core import BasicLogger
from .basic_logger.settings import BasicLoggerSettings


class LoggerFactory:
    def create(self, settings: GlobalSettings) -> BaseLogger:
        if settings.logger_type == LoggerType.BASIC:
            s = BasicLoggerSettings.from_global_settings(settings=settings)
            return BasicLogger(name=s.name, level=s.level, file_path=s.file_path)
        raise NotImplementedError()
