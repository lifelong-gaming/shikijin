from abc import ABCMeta, abstractmethod
from typing import Generic, Optional, TypeVar

from .fields import ComponentId, ComponentName
from .settings import GlobalSettings

T = TypeVar("T", bound="BaseComponent")


class EntryPointMixin(metaclass=ABCMeta):
    @abstractmethod
    def main(self) -> None:
        ...


class BaseComponent(metaclass=ABCMeta):
    def __init__(self, name: Optional[ComponentName] = None, component_id: Optional[ComponentId] = None):
        self._name = name if name else ComponentName(self.__class__.__name__)
        self._id = component_id if component_id else ComponentId.generate()

    @property
    def name(self) -> ComponentName:
        return self._name

    @property
    def id(self) -> ComponentId:
        return self._id


class BaseFactory(Generic[T], metaclass=ABCMeta):
    @abstractmethod
    def create(self, settings: GlobalSettings) -> T:
        ...
