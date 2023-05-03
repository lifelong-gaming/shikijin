from abc import ABCMeta, abstractmethod
from typing import TypeVar, Generic
from .settings import GlobalSettings

T = TypeVar("T", bound="BaseShikijinComponent")


class ExecutableMixin(metaclass=ABCMeta):
    @abstractmethod
    def execute(self) -> None:
        ...


class BaseShikijinComponent(metaclass=ABCMeta):
    ...


class BaseFactory(Generic[T], metaclass=ABCMeta):
    @abstractmethod
    def create(self, settings: GlobalSettings) -> T:
        ...
