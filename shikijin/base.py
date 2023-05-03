from abc import ABCMeta, abstractmethod

class ExecutableMixin(metaclass=ABCMeta):
    @abstractmethod
    def execute(self) -> None:
        ...

class BaseShikijinObject:
    ...
