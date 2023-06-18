from typing import Optional

from ...fields import ComponentName
from ...interfaces.base import BaseInterface
from ...loggers.base import BaseLogger
from ..base import BaseWorker


class BasicWorker(BaseWorker):
    def __init__(self, interface: BaseInterface, logger: BaseLogger, name: Optional[ComponentName] = None):
        super(BasicWorker, self).__init__(interface=interface, logger=logger, name=name)

    def main(self) -> None:
        print(f"hello this is {self.name}")

        return super().main()
