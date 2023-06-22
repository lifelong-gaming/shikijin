from abc import ABCMeta, abstractmethod

from ..components import BaseShikijinComponent
from ..fields import ComponentId, Id
from ..types import BaseTask, Blob


class BaseInterface(BaseShikijinComponent, metaclass=ABCMeta):
    @abstractmethod
    def get_blob(self, id: Id) -> Blob:
        ...

    @abstractmethod
    def save_blob(self, blob: Blob) -> None:
        ...

    @abstractmethod
    def add_task(self, task: BaseTask) -> None:
        ...

    @abstractmethod
    def get_task(self, id: Id) -> BaseTask:
        ...

    @abstractmethod
    def pickup_task(self) -> BaseTask:
        ...

    @abstractmethod
    def signup_task(self, worker_id: ComponentId, task: BaseTask) -> None:
        ...

    @abstractmethod
    def signoff_task(self, worker_id: ComponentId, task: BaseTask) -> None:
        ...
