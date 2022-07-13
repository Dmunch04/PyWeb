from enum import Enum
from typing import List, Union, Optional, Tuple

from pyweb.css.color import Color
from pyweb.css.unit import Angle, Length, RelativeLengthUnit
from pyweb.css.position import Position


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
        return f"{str(self.color)}{(' ' + str(self.degree)) if self.degree else ''}{(' ' + str(self.end)) if self.end else ''}"


class ColorStop(object):
    __slots__ = ("color", "stop_one", "stop_two")

    # TODO: allow for length along the gradient's axis (https://developer.mozilla.org/en-US/docs/Web/CSS/gradient/linear-gradient#values)
    # TODO: is allowing for int for the stops correct?
    def __init__(
        self,
        color: Color,
        stop_one: Optional[Union[Length, int]] = None,
        stop_two: Optional[Union[Length, int]] = None,
    ):
        self.color = color
        self.stop_one = stop_one
        self.stop_two = stop_two

        if self.stop_one is not None and isinstance(self.stop_one, Length):
            if not self.stop_one.unit == RelativeLengthUnit.PERCENT:
                raise Exception("color stop value must be a percent value")

        if self.stop_two is not None and isinstance(self.stop_two, Length):
            if not self.stop_two.unit == RelativeLengthUnit.PERCENT:
                raise Exception("color stop value must be a percent value")

    def __str__(self) -> str:
        return f"{str(self.color)}{(' ' + str(self.stop_one)) if self.stop_one is not None else ''}{(' ' + str(self.stop_two)) if self.stop_two is not None else ''}"


class ColorHint(object):
    __slots__ = ("percent",)

    # TODO: can you use other values than percent?
    def __init__(self, percent: Union[float, int]):
        self.percent = percent

    def __str__(self) -> str:
        return f"{str(self.percent)}%"


class CSSStartingPoint:
    pass


class HorizontalStartingPoint(CSSStartingPoint, Enum):
    LEFT = "left"
    RIGHT = "right"


class VerticalStartingPoint(CSSStartingPoint, Enum):
    TOP = "top"
    BOTTOM = "bottom"


class StartingPoint(object):
    __slots__ = ("k", "v")

    def __init__(
        self,
        k: Union[Angle, CSSStartingPoint, int],
        v: Optional[Union[Angle, CSSStartingPoint, int]] = None,
    ):
        self.k = k
        self.v = v

        if isinstance(self.k, CSSStartingPoint):
            if v is not None:
                if not isinstance(self.v, CSSStartingPoint):
                    raise Exception("both starting point values must be of same type")
                elif isinstance(self.k, HorizontalStartingPoint) and type(
                    self.k
                ) == type(self.v):
                    raise Exception("both values cannot be horizontal values")
                elif isinstance(self.k, VerticalStartingPoint) and type(self.k) == type(
                    self.v
                ):
                    raise Exception("both values cannot be vertical values")
                self.v = str(self.v.value)
            self.k = str(self.k.value)
        elif v is not None and not type(self.k) == type(self.v):
            raise Exception("both starting point values must be of same type")

    def __str__(self) -> str:
        return f"{str(self.k)}{(' ' + str(self.v)) if self.v is not None else ''}"


class RadialShape(Enum):
    CIRCLE = "circle"
    ELLIPSE = "ellipse"


class RadialSize(Enum):
    CLOSEST_SIDE = "closest-side"
    CLOSEST_CORNER = "closest-corner"
    FARTHEST_SIDE = "farthest-side"
    FARTHEST_CORNER = "farthest-corner"


class GradientConic(CSSGradient):
    """
    Conic gradients transition colors progressively around a circle.
    """

    __slots__ = ("colors", "from_angle", "at_pos", "repeating")

    def __init__(
        self,
        colors: List[ColorDegree],
        from_angle: Optional[Angle] = None,
        at_pos: Optional[StartingPoint] = None,
        repeating: bool = False,
    ):
        self.colors = colors
        self.from_angle = from_angle
        self.at_pos = at_pos
        self.repeating = repeating

    def __str__(self) -> str:
        from_at_str = ""
        if self.from_angle:
            from_at_str += "from " + str(self.from_angle)
        if self.at_pos:
            from_at_str += " at " + str(self.at_pos)

        from_at_str = from_at_str.strip()

        colors_str = ", ".join([str(color) for color in self.colors])

        return (
            (
                f"repeating-conic-gradient({(from_at_str + ', ') if from_at_str else ''}{colors_str})"
            )
            if self.repeating
            else (
                f"conic-gradient({(from_at_str + ', ') if from_at_str else ''}{colors_str})"
            )
        )


class GradientLinear(CSSGradient):
    """
    Linear gradients transition colors progressively along an imaginary line.
    """

    __slots__ = ("colors", "direction", "repeating")

    def __init__(
        self,
        colors: Tuple[ColorStop, ColorHint],
        direction: Optional[Union[StartingPoint, Angle]] = None,
        repeating: bool = False,
    ):
        self.colors = colors
        self.direction = direction
        self.repeating = repeating

    def __str__(self) -> str:
        direction_str = ""
        if self.direction is not None:
            if isinstance(self.direction, StartingPoint):
                direction_str += "to "
            direction_str += str(self.direction) + ", "

        return (
            (
                f"repeating-linear-gradient({direction_str if direction_str else ''}{', '.join([str(stop) for stop in self.colors])})"
            )
            if self.repeating
            else (
                f"linear-gradient({direction_str if direction_str else ''}{', '.join([str(stop) for stop in self.colors])})"
            )
        )


# TODO: maybe redo unit/length + percent system so it makes it easier to differantiate between length and percentage
# sources:
#   - https://developer.mozilla.org/en-US/docs/Web/CSS/gradient/radial-gradient#values
#   - https://developer.mozilla.org/en-US/docs/Web/CSS/length
class GradientRadial(CSSGradient):
    """
    Radial gradients transition colors progressively from a center point (origin).
    """

    __slots__ = ("colors", "position", "shape", "size", "repeating")

    def __init__(
        self,
        colors: List[Union[ColorStop, ColorHint]],
        position: Optional[Position] = None,
        shape: Optional[RadialShape] = None,
        size: Optional[Union[RadialSize, Length]] = None,
        repeating: bool = False,
    ):
        self.colors = colors
        self.position = position
        self.shape = shape
        self.size = size
        self.repeating = repeating

    def __str__(self) -> str:
        init_str = ""
        if self.shape is not None:
            init_str += self.shape.value + " "
        if self.size is not None:
            if isinstance(self.size, RadialSize):
                init_str += self.size.value + " "
            else:
                init_str += str(self.size) + " "
        if self.position is not None:
            if init_str:
                init_str += "at "
            init_str += str(self.position) + " "

        return (
            (
                f"repeating-radial-gradient({init_str.strip()}, {', '.join([str(stop) for stop in self.colors])})"
            )
            if self.repeating
            else (
                f"radial-gradient({init_str.strip()}, {', '.join([str(stop) for stop in self.colors])})"
            )
        )
