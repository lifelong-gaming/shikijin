from logging import FileHandler, LogRecord, StreamHandler
from typing import Optional

from pythonjsonlogger.jsonlogger import JsonFormatter

from ..base import BaseLogger
from ..types import logger_level_type


class Formatter(JsonFormatter):
    default_time_format = "%s"


class BasicLogger(BaseLogger):
    def __init__(self, name: str, level: logger_level_type = 0, file_path: Optional[str] = None) -> None:
        super(BasicLogger, self).__init__(name, level)
        formatter = Formatter(fmt="%(asctime)s %(levelname)s", json_ensure_ascii=False)
        stream_handler = StreamHandler()
        stream_handler.setLevel(self.level)
        stream_handler.setFormatter(formatter)
        self.addHandler(stream_handler)

        if file_path is not None:
            file_handler = FileHandler(file_path)
            file_handler.setLevel(self.level)
            file_handler.setFormatter(formatter)
            self.addHandler(file_handler)
