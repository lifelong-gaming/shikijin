from ..components import BaseShikijinComponentFactory
from ..settings import GlobalSettings, InterfaceType
from .base import BaseInterface
from .basic_interface.core import BasicInterface
from .basic_interface.settings import BasicInterfaceSettings


class InterfaceFactory(BaseShikijinComponentFactory[BaseInterface]):
    def create(self, settings: GlobalSettings) -> BaseInterface:
        t = settings.interface_type
        if t == InterfaceType.BASIC:
            self.log_info("creating interface")
            self.log_info(f"interface settings: {settings.interface_settings}")
            s = BasicInterfaceSettings.from_global_settings(settings=settings)
            return BasicInterface(name=s.name)
