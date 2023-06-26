from collections.abc import Sequence

from ...types import BaseCapability
from ..settings import BaseWorkerSettings


class BasicWorkerSettings(BaseWorkerSettings):
    capabilities: Sequence[BaseCapability]
