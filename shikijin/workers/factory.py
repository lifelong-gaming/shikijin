from ..base import BaseFactory
from .settings import BaseWorkerSettings
from .base import BaseWorker


class WorkerFactory(BaseFactory[BaseWorkerSettings, BaseWorker]):
    def create(self, settings: BaseWorkerSettings) -> BaseWorker:
        ...
