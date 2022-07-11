from enum import IntEnum, Enum
from typing import Union


# TODO: maybe collect all length units into one instead?
class CSSLengthUnit:
    pass


class AbsoluteLengthUnit(CSSLengthUnit, IntEnum):
    CM = 0
    MM = 1
    IN = 2
    PX = 3
    PT = 4
    PC = 5


class RelativeLengthUnit(CSSLengthUnit, IntEnum):
    EM = 0
    EX = 1
    CH = 2
    REM = 4
    VW = 5
    VH = 6
    VMIN = 7
    VMAX = 8
    PERCENT = 9  # %


class Length(object):
    __slots__ = ("length", "unit")

    def __init__(self, length: Union[float, int], unit: CSSLengthUnit):
        self.length = length
        self.unit = unit

    def __str__(self) -> str:
        return f"{str(self.length)}{'%' if self.unit == RelativeLengthUnit.PERCENT else self.unit.name.lower()}"


class AngleUnit(IntEnum):
    DEG = 0
    GRAD = 1
    RAD = 2
    TURN = 4


class Angle(object):
    __slots__ = ("angle", "unit")

    # TODO: is float allowed for angles?
    def __init__(self, angle: Union[float, int], unit: AngleUnit):
        self.angle = angle
        self.unit = unit

    def __str__(self) -> str:
        return f"{str(self.angle)}{self.unit.name.lower()}"


class TimeUnit(Enum):
    SECONDS = "s"
    MILLISECONDS = "ms"


class Time(object):
    __slots__ = ("value", "unit")

    def __init__(self, value: Union[float, int], unit: TimeUnit):
        self.value = value
        self.unit = unit

    def __str__(self) -> str:
        return f"{str(self.value)}{self.unit.value}"
