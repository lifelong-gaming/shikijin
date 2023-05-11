from collections.abc import Mapping
from typing import AbstractSet, Any, Dict, Optional, Union

from humps import camelize
from pydantic import BaseModel as _BaseModel
from pydantic import Field

from .fields import Id, Serializable, Timestamp


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


class BaseEntity(BaseType):
    id: Id = Field(default_factory=Id.generate)
    created_at: Timestamp = Field(default_factory=Timestamp.now)
    updated_at: Timestamp = Field(default_factory=Timestamp.now)


class BaseTask(BaseEntity):
    ...


class Capability(BaseType):
    ...
