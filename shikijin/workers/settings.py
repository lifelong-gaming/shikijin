from typing import Union

from ..fields import ComponentName
from ..settings import BaseComponentSettings, GlobalSettings


class BaseWorkerSettings(BaseComponentSettings):
    name: Union[ComponentName, None] = None

    @classmethod
    def from_global_settings(cls, settings: GlobalSettings) -> "BaseWorkerSettings":
        if "name" in settings.worker_settings:
            return BaseWorkerSettings(name=ComponentName(settings.worker_settings["name"]))
        return BaseWorkerSettings()
