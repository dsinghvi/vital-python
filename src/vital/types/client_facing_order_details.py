# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .client_facing_at_home_phlebotomy_order_details import ClientFacingAtHomePhlebotomyOrderDetails
from .client_facing_test_kit_order_details import ClientFacingTestKitOrderDetails
from .client_facing_walk_in_order_details import ClientFacingWalkInOrderDetails


class ClientFacingOrderDetails_WalkInTest(ClientFacingWalkInOrderDetails):
    type: typing_extensions.Literal["walk_in_test"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ClientFacingOrderDetails_Testkit(ClientFacingTestKitOrderDetails):
    type: typing_extensions.Literal["testkit"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ClientFacingOrderDetails_AtHomePhlebotomy(ClientFacingAtHomePhlebotomyOrderDetails):
    type: typing_extensions.Literal["at_home_phlebotomy"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


ClientFacingOrderDetails = typing.Union[
    ClientFacingOrderDetails_WalkInTest, ClientFacingOrderDetails_Testkit, ClientFacingOrderDetails_AtHomePhlebotomy
]