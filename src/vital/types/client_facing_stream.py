# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ClientFacingStream(pydantic.BaseModel):
    cadence: typing.Optional[typing.List[float]]
    time: typing.Optional[typing.List[int]] = pydantic.Field(
        description="Corresponding time stamp in unix time for datapoint"
    )
    altitude: typing.Optional[typing.List[float]]
    velocity_smooth: typing.Optional[typing.List[float]]
    heartrate: typing.Optional[typing.List[int]]
    lat: typing.Optional[typing.List[float]]
    lng: typing.Optional[typing.List[float]]
    distance: typing.Optional[typing.List[float]]
    power: typing.Optional[typing.List[float]]
    resistance: typing.Optional[typing.List[float]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}