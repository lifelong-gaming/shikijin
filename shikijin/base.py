from abc import ABCMeta, abstractmethod
from typing import TypeVar, Generic
from .settings import GlobalSettings
from .loggers.base import BaseLogger

T = TypeVar("T", bound="BaseShikijinComponent")


class EntryPointMixin(metaclass=ABCMeta):
    @abstractmethod
    def main(self) -> None:
        ...


class BaseComponent(metaclass=ABCMeta):
    ...


class BaseShikijinComponent(BaseComponent, metaclass=ABCMeta):
    def __init__(self, logger: BaseLogger):
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
