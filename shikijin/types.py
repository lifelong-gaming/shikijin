from collections.abc import Mapping, Sequence
from typing import AbstractSet, Any, Callable, Dict, Generic, Optional, Union

from humps import camelize
from pydantic import Field
from pydantic.generics import GenericModel as _BaseModel

from .fields import (
    AssignmentId,
    BlobId,
    Bytes,
    CapabilityId,
    IdGenerator,
    IdT,
    Serializable,
    TaskId,
    Timestamp,
    WorkerId,
)


class BaseType(_BaseModel):
    class Config:
        allow_mutation = False
        alias_generator = camelize
        allow_population_by_field_name = True

    def dict(
        self,
        *,
        include: Union[AbstractSet[Union[int, str]], Mapping[Union[int, str], Any], None] = None,
        exclude: Union[AbstractSet[Union[int, str]], Mapping[Union[int, str], Any], None] = None,
        by_alias: bool = True,
        skip_defaults: Optional[bool] = None,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
    ) -> Dict[str, Any]:
        return dict(
            (k, v.serialize() if isinstance(v, Serializable) else v)
            for k, v in super(BaseType, self)
            .dict(
                include=include,
                exclude=exclude,
                by_alias=by_alias,
                skip_defaults=skip_defaults,
                exclude_unset=exclude_unset,
                exclude_defaults=exclude_defaults,
                exclude_none=exclude_none,
            )
            .items()
        )

    def json(
        self,
        *,
        include: Union[AbstractSet[Union[int, str]], Mapping[Union[int, str], Any], None] = None,
        exclude: Union[AbstractSet[Union[int, str]], Mapping[Union[int, str], Any], None] = None,
        by_alias: bool = True,
        skip_defaults: bool | None = None,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
        encoder: Callable[[Any], Any] | None = None,
        models_as_dict: bool = True,
        **dumps_kwargs: Any,
    ) -> str:
        return super().json(
            include=include,
            exclude=exclude,
            by_alias=by_alias,
            skip_defaults=skip_defaults,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            encoder=encoder,
            models_as_dict=models_as_dict,
            **dumps_kwargs,
        )


class BaseEntity(BaseType, Generic[IdT]):
    id: IdT = Field(default_factory=IdGenerator[IdT]())
    created_at: Timestamp = Field(default_factory=Timestamp.now)
    updated_at: Timestamp = Field(default_factory=Timestamp.now)


class BaseTask(BaseEntity[TaskId]):
    ...


class Assignment(BaseEntity[AssignmentId]):
    worker_id: WorkerId
    task_id: TaskId


class BaseCapability(BaseEntity[CapabilityId]):
    ...


class Blob(BaseEntity[BlobId]):
    blob: Bytes
