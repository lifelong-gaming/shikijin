from abc import ABCMeta
from typing import Optional

from .base import BaseComponent, BaseFactory, T
from .fields import ComponentId, ComponentName
from .loggers.base import BaseLogger


class BaseShikijinComponent(BaseComponent, metaclass=ABCMeta):
    def __init__(
        self, logger: BaseLogger, name: Optional[ComponentName] = None, component_id: Optional[ComponentId] = None
    ):
        super(BaseShikijinComponent, self).__init__(name=name, component_id=component_id)
        self._logger = logger

    @property
    def logger(self) -> BaseLogger:
        return self._logger

    def log_info(self, message: str) -> None:
        self.logger.info({"componentname": self.name, "message": message})

    def log_warning(self, message: str) -> None:
        self.logger.warning({"componentname": self.name, "message": message})

    def log_error(self, message: str) -> None:
        self.logger.error({"componentname": self.name, "message": message})

    def log_debug(self, message: str) -> None:
        self.logger.debug({"componentname": self.name, "message": message})


class BaseShikijinComponentFactory(BaseShikijinComponent, BaseFactory[T], metaclass=ABCMeta):
    ...
