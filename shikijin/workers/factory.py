from typing import Optional

from ..components import BaseShikijinComponentFactory
from ..fields import ComponentName
from ..loggers.base import BaseLogger
from ..settings import GlobalSettings, WorkerType
from .base import BaseWorker
from .basic_worker.core import BasicWorker
from .basic_worker.settings import BasicWorkerSettings


class WorkerFactory(BaseShikijinComponentFactory[BaseWorker]):
    def __init__(self, logger: BaseLogger, name: Optional[ComponentName] = None):
        super(WorkerFactory, self).__init__(logger, name)

    def create(self, settings: GlobalSettings) -> BaseWorker:
        t = settings.worker_type
        if t == WorkerType.BASIC:
            s = BasicWorkerSettings.from_global_settings(settings=settings)
            self.log_info("creating worker")
            return BasicWorker(logger=self.logger, name=s.name)
        raise NotImplementedError()
