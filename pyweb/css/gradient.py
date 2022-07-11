from enum import Enum
from typing import List, Union, Optional

from pyweb.css.color import Color
from pyweb.css.unit import Angle, Length, RelativeLengthUnit


class CSSGradient(object):
    @classmethod
    @property
    def value(self) -> str:
        return self.__str__()


class ColorDegree(object):
    __slots__ = ("color", "degree", "end")

    def __init__(
        self,
        color: Color,
        degree: Optional[Union[Angle, Length]] = None,
        end: Optional[Union[Angle, Length]] = None,
    ):
        self.color = color
        self.degree = degree
        self.end = end

        if self.degree is not None:
            if (
                isinstance(self.degree, Length)
                and not self.degree.unit == RelativeLengthUnit.PERCENT
            ):
                raise Exception("color degree value must be an angle or percent value")

        if self.end is not None:
            if (
                isinstance(self.end, Length)
                and not self.end.unit == RelativeLengthUnit.PERCENT
            ):
                raise Exception("color end value must be an angle or percent value")

    def __str__(self) -> str:
        return f"{str(self.color)}{(' ' + str(self.degree)) if self.degree else ''}"


class CSSStartingPoint:
    pass


class HorizontalStartingPoint(Enum):
    LEFT = "left"
    RIGHT = "right"


class VerticalStartingPoint(Enum):
    TOP = "top"
    BOTTOM = "bottom"


class StartingPoint(object):
    __slots__ = ("k", "v")

    def __init__(
        self,
        k: Union[Angle, CSSStartingPoint],
        v: Optional[Union[Angle, CSSStartingPoint]] = None,
    ):
        self.k = k
        self.v = v

        if isinstance(k, HorizontalStartingPoint) and isinstance(
            v, HorizontalStartingPoint
        ):
            raise Exception("both values cannot be horizontal values")
        elif isinstance(k, VerticalStartingPoint) and isinstance(
            v, VerticalStartingPoint
        ):
            raise Exception("both values cannot be vertical values")

    def __str__(self) -> str:
        pass


# TODO: i think this gradient class is broken in the way it generates css
class GradientConic(CSSGradient):
    """
    Conic gradients transition colors progressively around a circle.
    """

    __slots__ = ("colors", "from_angle", "at_pos")

    # TODO: find type for at_pos (https://www.w3schools.com/cssref/func_conic-gradient.asp)
    def __init__(
        self, colors: List[ColorDegree], from_angle: Angle = None, at_pos=None
    ):
        self.colors = colors
        self.from_angle = from_angle
        self.at_pos = at_pos

    def __str__(self) -> str:
        return f"conic-gradient({('from ' + str(self.from_angle) + ', ') if self.from_angle else ''}{('at ' + str(self.at_pos) + ', ') if self.at_pos else ''}{', '.join(self.colors)})"


class GradientLinear(CSSGradient):
    """
    Linear gradients transition colors progressively along an imaginary line.
    """

    pass


class GradientRadial(CSSGradient):
    """
    Radial gradients transition colors progressively from a center point (origin).
    """

    pass
