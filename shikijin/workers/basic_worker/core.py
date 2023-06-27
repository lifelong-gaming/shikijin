from collections.abc import Sequence
from typing import Optional

from ...fields import ComponentName
from ...interfaces.base import BaseInterface
from ...loggers.base import BaseLogger
from ...types import BaseCapability
from ..base import BaseWorker


class BasicWorker(BaseWorker):
    def __init__(
        self,
        capabilities: Sequence[BaseCapability],
        interface: BaseInterface,
        logger: BaseLogger,
        name: Optional[ComponentName] = None,
    ):
        super(BasicWorker, self).__init__(interface=interface, logger=logger, name=name)
        self._capabilities = capabilities

    def main(self) -> None:
        while True:
            t = self.interface.pickup_task(self.capabilities)
            try:
                assignment = self.interface.get_assignment(self.id, t)
                self.logger.info(f"start {t.id}")
                for next_task in t.run():
                    self.interface.add_task(next_task)
                self.interface.complete_assignment(assignment)
            except Exception as e:
                self.interface.abandon_assignment(assignment)
                self.logger.error(f"error in {self.name}({t.id}): {e}")

    @property
    def capabilities(self) -> Sequence[BaseCapability]:
        return self._capabilities
