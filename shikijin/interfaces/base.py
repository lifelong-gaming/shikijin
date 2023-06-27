from abc import ABCMeta, abstractmethod
from collections.abc import Sequence

from ..components import BaseShikijinComponent
from ..fields import ComponentId, Id
from ..types import Assignment, BaseCapability, BaseTask, Blob


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
    def pickup_task(self, capabilities: Sequence[BaseCapability]) -> BaseTask:
        ...

    @abstractmethod
    def get_assignment(self, worker_id: ComponentId, task: BaseTask) -> Assignment:
        ...

    @abstractmethod
    def complete_assignment(self, assignment: Assignment) -> None:
        ...

    @abstractmethod
    def abandon_assignment(self, assignment: Assignment) -> None:
        ...
