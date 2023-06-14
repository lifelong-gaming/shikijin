from typing import Union

from ..fields import ComponentName
from ..settings import BaseComponentSettings, GlobalSettings


class BaseInterfaceSettings(BaseComponentSettings):
    name: Union[ComponentName, None] = None

    @classmethod
    def from_global_settings(cls, settings: GlobalSettings) -> "BaseInterfaceSettings":
        if "name" in settings.interface_settings:
            return BaseInterfaceSettings(name=ComponentName(settings.interface_settings["name"]))
        return BaseInterfaceSettings()
