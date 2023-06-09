from abc import abstractmethod
from collections.abc import Sequence
from typing import Optional

from ..base import EntryPointMixin
from ..components import BaseShikijinComponent
from ..fields import ComponentName
from ..interfaces.base import BaseInterface
from ..loggers.base import BaseLogger
from ..types import BaseCapability


class BaseWorker(BaseShikijinComponent, EntryPointMixin):
    def __init__(self, interface: BaseInterface, logger: BaseLogger, name: Optional[ComponentName] = None):
        super(BaseWorker, self).__init__(logger=logger, name=name)
        self._interface = interface

    @property
    def interface(self) -> BaseInterface:
        return self._interface

    @property
    @abstractmethod
    def capabilities(self) -> Sequence[BaseCapability]:
        ...
