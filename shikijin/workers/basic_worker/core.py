from typing import Optional

from ...fields import ComponentName
from ...interfaces.base import BaseInterface
from ...loggers.base import BaseLogger
from ..base import BaseWorker


class BasicWorker(BaseWorker):
    def __init__(self, interface: BaseInterface, logger: BaseLogger, name: Optional[ComponentName] = None):
        super(BasicWorker, self).__init__(interface=interface, logger=logger, name=name)

    def main(self) -> None:
        while True:
            t = self.interface.pickup_task(self.capabilities)
            try:
                self.interface.signup_task(self.id, t)
                self.logger.info(f"start {t.id}")
                for next_task in t.run():
                    self.interface.add_task(next_task)
            except Exception as e:
                self.logger.error(f"error in {self.name}({t.id}): {e}")
            finally:
                self.interface.signoff_task(self.id, t)
        return super().main()
