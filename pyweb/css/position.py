from enum import Enum
from typing import Union, Optional

from pyweb.css.unit import Length, RelativeLengthUnit


class CSSPosition(Enum):
    LEFT = "left"
    RIGHT = "right"
    TOP = "top"
    BOTTOM = "bottom"
    CENTER = "center"


class Position(object):
    __slots__ = ("x", "y")

    def __init__(
        self,
        x: Union[CSSPosition, Length],
        y: Union[Optional[CSSPosition], Length] = None,
    ):
        self.x = x
        self.y = y

        if self.y is None:
            if isinstance(self.x, CSSPosition):
                self.y = CSSPosition.CENTER
            elif isinstance(self.x, Length):
                self.y = Length(50, RelativeLengthUnit.PERCENT)

        if isinstance(self.x, CSSPosition):
            if (str(self.x.value), (str(self.y.value))) not in (
                ("left", "top"),
                ("left", "center"),
                ("left", "bottom"),
                ("right", "top"),
                ("right", "center"),
                ("right", "bottom"),
                ("center", "top"),
                ("center", "center"),
                ("center", "bottom"),
            ):
                raise Exception(
                    f"invalid css position match: {str(self.x.value)} {str(self.y.value)}"
                )

    def __str__(self) -> str:
        return f"{str(self.x.value) if isinstance(self.x, CSSPosition) else str(self.x)} {str(self.y.value) if isinstance(self.y, CSSPosition) else str(self.y)}"
