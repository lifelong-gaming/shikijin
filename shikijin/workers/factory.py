from ..components import BaseShikijinComponentFactory
from ..interfaces.factory import InterfaceFactory
from ..settings import GlobalSettings, WorkerType
from .base import BaseWorker
from .basic_worker.core import BasicWorker
from .basic_worker.settings import BasicWorkerSettings


class WorkerFactory(BaseShikijinComponentFactory[BaseWorker]):
    def create(self, settings: GlobalSettings) -> BaseWorker:
        t = settings.worker_type
        if t == WorkerType.BASIC:
            s = BasicWorkerSettings.from_global_settings(settings=settings)
            self.log_info("creating worker")
            self.log_info(f"worker settings: {settings.worker_settings}")
            return BasicWorker(
                interface=InterfaceFactory(logger=self.logger).create(settings=settings),
                capabilities=s.capabilities,
                logger=self.logger,
                name=s.name,
            )
        raise NotImplementedError()
