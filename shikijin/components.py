from abc import ABCMeta
from typing import Optional

from .base import BaseComponent, BaseFactory, T
from .fields import ComponentName
from .loggers.base import BaseLogger


class BaseShikijinComponent(BaseComponent, metaclass=ABCMeta):
    def __init__(self, logger: BaseLogger, name: Optional[ComponentName] = None):
        super(BaseShikijinComponent, self).__init__(name=name)
        self._logger = logger

    @property
    def logger(self) -> BaseLogger:
        return self._logger

    def log_info(self, message: str) -> None:
        self.logger.info({"component_name": self.name, "message": message})


class BaseShikijinComponentFactory(BaseShikijinComponent, BaseFactory[T], metaclass=ABCMeta):
    ...
