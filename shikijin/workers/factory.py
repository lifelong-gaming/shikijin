from ..base import BaseShikijinComponentFactory
from ..fields import ComponentName
from ..loggers.base import BaseLogger
from ..settings import GlobalSettings, WorkerType
from .base import BaseWorker
from .basic_worker.core import BasicWorker
from .basic_worker.settings import BasicWorkerSettings


class WorkerFactory(BaseShikijinComponentFactory[BaseWorker]):
    def __init__(self, logger: BaseLogger, name: ComponentName | None = None):
        super().__init__(logger, name)

    def create(self, settings: GlobalSettings) -> BaseWorker:
        t = settings.worker_type
        if t == WorkerType.BASIC:
            s = BasicWorkerSettings.from_global_settings(settings=settings)
            return BasicWorker(settings=s, logger=self.logger)
