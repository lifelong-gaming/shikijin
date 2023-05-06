from collections.abc import Callable, Generator
from typing import Any


class ComponentName(str):
    """
    ComponentName is a string that is not empty.

    This class is used to validate the name of a component.

    Example:
        >>> from pydantic import BaseModel
        >>> class ComponentNameTester(BaseModel):
        ...     name: ComponentName
        >>> ComponentNameTester(name="foo")
        ComponentNameTester(name=ComponentName('foo'))
        >>> ComponentNameTester(name="")
        Traceback (most recent call last):
         ...
        pydantic.error_wrappers.ValidationError: 1 validation error for ComponentNameTester
        name
          empty string (type=value_error)
        >>> ComponentNameTester(name=1)
        Traceback (most recent call last):
         ...
        pydantic.error_wrappers.ValidationError: 1 validation error for ComponentNameTester
        name
          string required (type=type_error)

    """

    @classmethod
    def __get_validators__(self) -> Generator[Callable[[Any], "ComponentName"], None, None]:
        yield self._validate

    @classmethod
    def _validate(cls, v: Any) -> "ComponentName":
        if not isinstance(v, str):
            raise TypeError("string required")
        if len(v) == 0:
            raise ValueError("empty string")
        return cls(v)

    def __repr__(self) -> str:
        return f"ComponentName({super().__repr__()})"
