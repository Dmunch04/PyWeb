from enum import IntEnum, Enum
from typing import Union


class LengthFontUnit(IntEnum):
    CAP = 0
    CH = 1
    EM = 2
    EX = 3
    IC = 4
    LH = 5
    REM = 6
    RLH = 7


class LengthFont(object):
    __slots__ = ("length", "unit")

    def __init__(self, length: Union[int, float], unit: LengthFontUnit):
        self.length = length
        self.unit = unit

    def __str__(self) -> str:
        return f"{str(self.length)}{self.unit.name.lower()}"


class ViewportSize(Enum):
    SMALL = "s"
    LARGE = "l"
    DYNAMIC = "d"
    DEFAULT = ""


class LengthViewportUnit(IntEnum):
    VH = 0
    VW = 1
    VMAX = 2
    VMIN = 3
    VB = 4
    VI = 5


class LengthViewport(object):
    __slots__ = ("length", "unit", "viewport")

    def __init__(self, length: Union[int, float], unit: LengthViewportUnit, viewport: ViewportSize):
        self.length = length
        self.unit = unit
        self.viewport = viewport

    def __str__(self) -> str:
        return f"{str(self.length)}{self.viewport.value}{self.unit.name.lower()}"


class LengthContainerQueryUnit(IntEnum):
    CQW = 0
    CQH = 1
    CQI = 2
    CQB = 3
    CQMIN = 4
    CQMAX = 5


class LengthContainerQuery(object):
    __slots__ = ("length", "unit")

    def __init__(self, length: Union[int, float], unit: LengthContainerQueryUnit):
        self.length = length
        self.unit = unit

    def __str__(self) -> str:
        return f"{str(self.length)}{self.unit.name.lower()}"


class LengthAbsoluteUnit(IntEnum):
    PX = 0
    CM = 1
    MM = 2
    Q = 3
    IN = 4
    PC = 5
    PT = 6


class LengthAbsolute(object):
    __slots__ = ("length", "unit")

    def __init__(self, length: Union[int, float], unit: LengthAbsoluteUnit):
        self.length = length
        self.unit = unit

    def __str__(self) -> str:
        name: str = self.unit.name
        if name != "Q":
            name = name.lower()

        return f"{str(self.length)}{name}"


LengthTypes = Union[LengthFont, LengthViewport, LengthContainerQuery, LengthAbsolute]
LengthUnits = Union[LengthFontUnit, LengthViewportUnit, LengthContainerQueryUnit, LengthAbsoluteUnit]


class Length(object):
    __slots__ = ("length", "unit")

    def __init__(self, length: Union[int, float], unit: Un):


class Percentage(object):
    __slots__ = "value"

    def __init__(self, value: Union[int, float]):
        self.value = value

    def __str__(self):
        return f"{str(self.value)}%"



LengthPercentage = Union[Length, Percentage]
