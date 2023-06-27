import uuid
from abc import abstractmethod
from base64 import (
    b64encode,
    standard_b64decode,
    standard_b64encode,
    urlsafe_b64decode,
    urlsafe_b64encode,
)
from collections.abc import Callable, Generator
from datetime import datetime as _datetime
from datetime import timezone as _timezone
from typing import Any, Generic, Type, TypeVar, Union, cast
from uuid import UUID

from dateutil.parser import parse as parse_datetime

T = TypeVar("T")
StrT = TypeVar("StrT", bound="NonEmptyString")
IdT = TypeVar("IdT", bound="Id")


class Serializable(Generic[T]):
    @abstractmethod
    def serialize(self) -> T:
        raise NotImplementedError


class Id(UUID, Serializable[str]):
    r"""Id is a UUID4 type that can be used as a primary key.

    >>> from unittest.mock import patch
    >>> with patch("uuid.uuid4", return_value=UUID('cf57432e-809e-4353-adbd-9d5c0d733868')):
    ...     x = Id.generate()
    ...
    >>> x
    Id('z1dDLoCeQ1OtvZ1cDXM4aA')
    >>> x.bytes
    b'\xcfWC.\x80\x9eCS\xad\xbd\x9d\\\rs8h'
    >>> x.hex
    'cf57432e809e4353adbd9d5c0d733868'
    >>> x.int
    275603287559914445491632874575877060712
    >>> x == Id('cf57432e809e4353adbd9d5c0d733868')
    True
    >>> x == Id('z1dDLoCeQ1OtvZ1cDXM4aA')
    True
    >>> x == Id(275603287559914445491632874575877060712)
    True
    """

    def __init__(self, value: Union[str, UUID, bytes, int]) -> None:
        if isinstance(value, UUID):
            super(Id, self).__init__(value.hex)
            return
        if isinstance(value, int):
            super(Id, self).__init__(value.to_bytes(16, "big").hex())
            return
        if isinstance(value, bytes):
            super(Id, self).__init__(value.hex())
            return
        if len(value) == 22:
            super(Id, self).__init__(urlsafe_b64decode(value + "==").hex())
            return
        super(Id, self).__init__(value)

    @classmethod
    def generate(cls: Type[IdT]) -> IdT:
        return cls(uuid.uuid4().hex)

    @property
    def b64encoded(self) -> str:
        return urlsafe_b64encode(self.bytes).rstrip(b"=").decode("utf-8")

    def __str__(self) -> str:
        return self.b64encoded

    def serialize(self) -> str:
        return self.b64encoded

    @classmethod
    def __get_validators__(cls) -> Generator[Callable[[Any], "Id"], None, None]:
        yield cls.validate

    @classmethod
    def validate(cls, v: Any) -> "Id":
        if isinstance(v, cls):
            return v
        if isinstance(v, (UUID, bytes, str, int)):
            return cls(v)
        raise ValueError(f"Cannot convert {v} to {cls}")


class IdGenerator(Generic[IdT]):
    def __call__(self) -> IdT:
        return cast(IdT, Id.generate())


class ComponentId(Id):
    """
    ComponentId class

    >>> ComponentId("z1dDLoCeQ1OtvZ1cDXM4aA")
    ComponentId('z1dDLoCeQ1OtvZ1cDXM4aA')
    """


class WorkerId(ComponentId):
    """
    WorkerId class

    >>> WorkerId("z1dDLoCeQ1OtvZ1cDXM4aA")
    WorkerId('z1dDLoCeQ1OtvZ1cDXM4aA')
    """


class InterfaceId(ComponentId):
    """
    InterfaceId class

    >>> InterfaceId("z1dDLoCeQ1OtvZ1cDXM4aA")
    InterfaceId('z1dDLoCeQ1OtvZ1cDXM4aA')
    """


class TaskId(Id):
    """
    TaskId class

    >>> TaskId("z1dDLoCeQ1OtvZ1cDXM4aA")
    TaskId('z1dDLoCeQ1OtvZ1cDXM4aA')
    """


class AssignmentId(Id):
    """
    AssignmentId class

    >>> AssignmentId("z1dDLoCeQ1OtvZ1cDXM4aA")
    AssignmentId('z1dDLoCeQ1OtvZ1cDXM4aA')
    """


class CapabilityId(Id):
    """
    CapabilityId class

    >>> CapabilityId("z1dDLoCeQ1OtvZ1cDXM4aA")
    CapabilityId('z1dDLoCeQ1OtvZ1cDXM4aA')
    """


class BlobId(Id):
    """
    BlobId class

    >>> BlobId("z1dDLoCeQ1OtvZ1cDXM4aA")
    BlobId('z1dDLoCeQ1OtvZ1cDXM4aA')
    """


class UserId(str):
    ...


class Timestamp(int):
    """
    Timestamp class
    >>> a = Timestamp(1674397764479000)
    >>> a
    Timestamp(1674397764479000)
    >>> a.milliseconds
    1674397764479
    >>> a.microseconds
    1674397764479000
    >>> a.datetime
    datetime.datetime(2023, 1, 22, 14, 29, 24, 479000, tzinfo=datetime.timezone.utc)
    >>> dt = a.datetime
    >>> ts = dt.timestamp()
    >>> Timestamp(dt)
    Timestamp(1674397764479000)
    >>> Timestamp(ts)
    Timestamp(1674397764479000)
    >>> Timestamp("2023-01-22T14:29:24.422Z")
    Timestamp(1674397764422000)
    >>> Timestamp("2023/02/12 12:21:12")
    Timestamp(1676172072000000)
    >>> Timestamp("invalid")
    Traceback (most recent call last):
      ...
    dateutil.parser._parser.ParserError: Unknown string format: invalid

    """

    def __new__(cls, value: Union[int, float, _datetime, str]) -> "Timestamp":
        if isinstance(value, _datetime):
            return super(Timestamp, cls).__new__(cls, int(value.timestamp() * 1000000))
        if isinstance(value, str):
            return super(Timestamp, cls).__new__(cls, int(parse_datetime(value).timestamp() * 1000000))
        if isinstance(value, float):
            return super(Timestamp, cls).__new__(cls, int(value * 1000000))
        return super(Timestamp, cls).__new__(cls, value)

    @classmethod
    def __get_validators__(cls) -> Generator[Callable[[Any], "Timestamp"], None, None]:
        yield cls.validate

    @classmethod
    def validate(cls, v: Any) -> "Timestamp":
        if isinstance(v, cls):
            return v
        if isinstance(v, (int, float, _datetime, str)):
            return cls(v)
        raise ValueError(f"Cannot convert {v} to {cls}")

    @property
    def milliseconds(self) -> int:
        """
        >>> a = Timestamp(1674365364479000)
        >>> a.milliseconds
        1674365364479
        """
        return int(self // 1000)

    @property
    def microseconds(self) -> int:
        """
        >>> a = Timestamp(1674365364479000)
        >>> a.microseconds
        1674365364479000
        """
        return int(self)

    @property
    def datetime(self) -> _datetime:
        """
        >>> a = Timestamp(1674397764479000)
        >>> a.datetime
        datetime.datetime(2023, 1, 22, 14, 29, 24, 479000, tzinfo=datetime.timezone.utc)
        """
        return _datetime.fromtimestamp(self / 1000000, tz=_timezone.utc)

    @classmethod
    def now(cls) -> "Timestamp":
        """
        >>> import freezegun
        >>> from datetime import timedelta, timezone
        >>> with freezegun.freeze_time(_datetime(2023, 1, 22, 14, 29, 23, 123321, tzinfo=_timezone.utc)):
        ...     Timestamp.now()
        Timestamp(1674397763123321)
        """
        return cls(_datetime.utcnow())

    def __repr__(self) -> str:
        return f"Timestamp({super(Timestamp, self).__repr__()})"


class Bytes(bytes, Serializable[str]):
    r"""
    >>> Bytes(b"hello")
    Bytes(b'hello')
    >>> Bytes("aGVsbG8=")
    Bytes(b'hello')
    >>> Bytes(123)
    Bytes(b'{')
    >>> Bytes(b"hello").hex()
    '68656c6c6f'
    >>> Bytes(b"hello").b64encoded
    'aGVsbG8='
    >>> Bytes(b"hello").urlsafe_b64encoded
    'aGVsbG8='
    """

    def __new__(cls, value: Union[bytes, str, int]) -> "Bytes":
        if isinstance(value, bytes):
            return super(Bytes, cls).__new__(cls, value)
        if isinstance(value, str):
            return super(Bytes, cls).__new__(cls, standard_b64decode(value))
        if isinstance(value, int):
            return super(Bytes, cls).__new__(cls, value.to_bytes((value.bit_length() + 7) // 8, "big"))
        raise ValueError(f"Cannot create Bytes from {value}")

    @property
    def b64encoded(self) -> str:
        return b64encode(self).decode("utf-8")

    @property
    def urlsafe_b64encoded(self) -> str:
        return urlsafe_b64encode(self).decode("utf-8")

    @property
    def standard_b64encoded(self) -> str:
        return standard_b64encode(self).decode("utf-8")

    def __repr__(self) -> str:
        return f"Bytes({super(Bytes, self).__repr__()})"

    @classmethod
    def __get_validators__(cls) -> Generator[Callable[[Any], "Bytes"], None, None]:
        yield cls.validate

    @classmethod
    def validate(cls, v: Any) -> "Bytes":
        if isinstance(v, cls):
            return v
        return cls(v)

    def serialize(self) -> str:
        return self.standard_b64encoded


class NonEmptyString(str):
    """
    Example:
        >>> from pydantic import BaseModel
        >>> class NonEmptyStringTester(BaseModel):
        ...     name: NonEmptyString
        >>> NonEmptyStringTester(name="foo")
        NonEmptyStringTester(name=NonEmptyString('foo'))
        >>> NonEmptyStringTester(name="")
        Traceback (most recent call last):
         ...
        pydantic.error_wrappers.ValidationError: 1 validation error for NonEmptyStringTester
        name
          empty string (type=value_error)
        >>> NonEmptyStringTester(name=1)
        Traceback (most recent call last):
         ...
        pydantic.error_wrappers.ValidationError: 1 validation error for NonEmptyStringTester
        name
          string required (type=type_error)
    """

    @classmethod
    def __get_validators__(cls: Type[StrT]) -> Generator[Callable[[Any], StrT], None, None]:
        yield cls._validate

    @classmethod
    def _validate(cls: Type[StrT], v: Any) -> StrT:
        if not isinstance(v, str):
            raise TypeError("string required")
        if len(v) == 0:
            raise ValueError("empty string")
        return cls(v)

    def __repr__(self) -> str:
        return f"NonEmptyString({super().__repr__()})"


class ComponentName(NonEmptyString):
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

    def __repr__(self) -> str:
        return f"ComponentName('{super().__str__()}')"


class TaskName(NonEmptyString):
    """
    TaskName is a string that is not empty.

    This class is used to validate the name of a task.

    Example:
        >>> from pydantic import BaseModel
        >>> class TaskNameTester(BaseModel):
        ...     name: TaskName
        >>> TaskNameTester(name="foo")
        TaskNameTester(name=TaskName('foo'))
        >>> TaskNameTester(name="")
        Traceback (most recent call last):
         ...
        pydantic.error_wrappers.ValidationError: 1 validation error for TaskNameTester
        name
          empty string (type=value_error)
        >>> TaskNameTester(name=1)
        Traceback (most recent call last):
         ...
        pydantic.error_wrappers.ValidationError: 1 validation error for TaskNameTester
        name
          string required (type=type_error)
    """

    def __repr__(self) -> str:
        return f"TaskName('{super().__str__()}')"
