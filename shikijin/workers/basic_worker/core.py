from typing import Optional

from shikijin.fields import ComponentName
from shikijin.loggers.base import BaseLogger

from ..base import BaseWorker


class BasicWorker(BaseWorker):
    def __init__(self, logger: BaseLogger, name: Optional[ComponentName] = None):
        super(BasicWorker, self).__init__(logger=logger, name=name)

    def main(self) -> None:
        print(f"hello this is {self.name}")

        return super().main()
