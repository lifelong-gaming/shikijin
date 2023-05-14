from abc import ABCMeta, abstractmethod
from typing import Generic, Optional, TypeVar

from .fields import ComponentName
from .settings import GlobalSettings

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


class BaseFactory(Generic[T], metaclass=ABCMeta):
    @abstractmethod
    def create(self, settings: GlobalSettings) -> T:
        ...
