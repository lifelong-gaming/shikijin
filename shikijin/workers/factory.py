from ..base import BaseShikijinComponentFactory
from .settings import BaseWorkerSettings
from .base import BaseWorker


class WorkerFactory(BaseShikijinComponentFactory[BaseWorker]):
    def create(self, settings: BaseWorkerSettings) -> BaseWorker:
        ...
