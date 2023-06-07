from abc import ABCMeta, abstractmethod
from ..components import BaseShikijinComponent
from ..fields import Id
from ..types import Blob


class BaseInterface(BaseShikijinComponent, metaclass=ABCMeta):
    @abstractmethod
    def get_blob(self, id: Id) -> Blob:
        ...

    @abstractmethod
    def save_blob(self, blob: Blob) -> None:
        ...
