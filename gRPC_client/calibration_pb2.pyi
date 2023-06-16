from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

ALICE: Link
BOB: Link
BOTH: Link
DESCRIPTOR: _descriptor.FileDescriptor
MOD: EndNodeCalibrationType
MPN: EndNodeCalibrationType

class BoostIntensityCalibrationReply(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: ResponseStatus
    def __init__(self, status: _Optional[_Union[ResponseStatus, _Mapping]] = ...) -> None: ...

class BoostIntensityCalibrationRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CalibrateModulatorsReply(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: ResponseStatus
    def __init__(self, status: _Optional[_Union[ResponseStatus, _Mapping]] = ...) -> None: ...

class CalibrateModulatorsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CalibrateMpnReply(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: ResponseStatus
    def __init__(self, status: _Optional[_Union[ResponseStatus, _Mapping]] = ...) -> None: ...

class CalibrateMpnRequest(_message.Message):
    __slots__ = ["attn2_default", "coeffs0", "coeffs1", "multiplication_factor"]
    ATTN2_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    COEFFS0_FIELD_NUMBER: _ClassVar[int]
    COEFFS1_FIELD_NUMBER: _ClassVar[int]
    MULTIPLICATION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    attn2_default: float
    coeffs0: float
    coeffs1: float
    multiplication_factor: float
    def __init__(self, coeffs0: _Optional[float] = ..., coeffs1: _Optional[float] = ..., attn2_default: _Optional[float] = ..., multiplication_factor: _Optional[float] = ...) -> None: ...

class GetCalibrationIntervalsReply(_message.Message):
    __slots__ = ["interval", "status"]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    interval: float
    status: ResponseStatus
    def __init__(self, status: _Optional[_Union[ResponseStatus, _Mapping]] = ..., interval: _Optional[float] = ...) -> None: ...

class GetCalibrationIntervalsRequest(_message.Message):
    __slots__ = ["calib_type"]
    CALIB_TYPE_FIELD_NUMBER: _ClassVar[int]
    calib_type: EndNodeCalibrationType
    def __init__(self, calib_type: _Optional[_Union[EndNodeCalibrationType, str]] = ...) -> None: ...

class ResponseStatus(_message.Message):
    __slots__ = ["code", "reason", "success"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    code: int
    reason: str
    success: bool
    def __init__(self, success: bool = ..., code: _Optional[int] = ..., reason: _Optional[str] = ...) -> None: ...

class SetCalibrationIntervalsReply(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: ResponseStatus
    def __init__(self, status: _Optional[_Union[ResponseStatus, _Mapping]] = ...) -> None: ...

class SetCalibrationIntervalsRequest(_message.Message):
    __slots__ = ["calib_type", "interval"]
    CALIB_TYPE_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    calib_type: EndNodeCalibrationType
    interval: float
    def __init__(self, calib_type: _Optional[_Union[EndNodeCalibrationType, str]] = ..., interval: _Optional[float] = ...) -> None: ...

class Link(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class EndNodeCalibrationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
