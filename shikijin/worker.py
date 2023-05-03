from .base import BaseShikijinObject, ExecutableMixin


class ShikijinWorker(BaseShikijinObject, ExecutableMixin):
    def execute(self) -> None:
        raise NotImplementedError()
