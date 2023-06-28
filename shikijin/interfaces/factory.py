from ..components import BaseShikijinComponentFactory
from ..settings import GlobalSettings, InterfaceType
from .base import BaseInterface
from .in_memory_interface.core import InMemoryInterface
from .in_memory_interface.settings import InMemoryInterfaceSettings


class InterfaceFactory(BaseShikijinComponentFactory[BaseInterface]):
    def create(self, settings: GlobalSettings) -> BaseInterface:
        t = settings.interface_type
        if t == InterfaceType.IN_MEMORY:
            self.log_info("creating interface")
            self.log_info(f"interface settings: {settings.interface_settings}")
            s = InMemoryInterfaceSettings.from_global_settings(settings=settings)
            return InMemoryInterface(logger=self.logger, name=s.name)
        raise ValueError(f"unknown interface type: {t}")
