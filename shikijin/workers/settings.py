from typing import Type, Union

from ..fields import ComponentName
from ..settings import BaseComponentSettings, GlobalSettings, S


class BaseWorkerSettings(BaseComponentSettings):
    name: Union[ComponentName, None] = None

    @classmethod
    def from_global_settings(cls: Type[S], settings: GlobalSettings) -> S:
        if "name" in settings.worker_settings:
            return cls(name=ComponentName(settings.worker_settings["name"]))
        return cls()
