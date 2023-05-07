from abc import ABCMeta, abstractmethod
from typing import TypeVar, Generic, Optional
from .settings import GlobalSettings
from .loggers.base import BaseLogger
from .types import ComponentName

T = TypeVar("T", bound="BaseComponent")


class EntryPointMixin(metaclass=ABCMeta):
    @abstractmethod
    def main(self) -> None:
        ...


class BaseComponent(metaclass=ABCMeta):
    def __init__(self, name: Optional[ComponentName] = None):
        self._name = name if name else ComponentName(self.__class__.__name__)

    @property
    def name(self) -> ComponentName:
        return self._name


class BaseShikijinComponent(BaseComponent, metaclass=ABCMeta):
    def __init__(self, logger: BaseLogger, name: Optional[ComponentName] = None):
        super(self, BaseShikijinComponent).__init__(name=name)
        self._logger = logger

    @property
    def logger(self) -> BaseLogger:
        return self._logger


class BaseFactory(Generic[T], metaclass=ABCMeta):
    @abstractmethod
    def create(self, settings: GlobalSettings) -> T:
        ...


class BaseShikijinComponentFactory(BaseShikijinComponent, BaseFactory[T], metaclass=ABCMeta):
    ...
