# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AppointmentServiceType(str, enum.Enum):
    """
    An enumeration.
    """

    APPOINTMENT_READY = "appointment-ready"
    APPOINTMENT_REQUEST = "appointment-request"

    def visit(
        self, appointment_ready: typing.Callable[[], T_Result], appointment_request: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is AppointmentServiceType.APPOINTMENT_READY:
            return appointment_ready()
        if self is AppointmentServiceType.APPOINTMENT_REQUEST:
            return appointment_request()