from typing import Union

from pyweb.css.unit import Length, Angle
from pyweb.css.color import Color


class CSSBackdropFilter(object):
    @classmethod
    @property
    def value(self) -> str: return self.__str__()


class BackdropFilterBlur(CSSBackdropFilter):
    __slots__ = ("length",)

    def __init__(self, length: Length):
        self.length = length

    def __str__(self) -> str:
        return f"blur({str(self.length)})"


class BackdropFilterBrightness(CSSBackdropFilter):
    __slots__ = ("value", "is_percent")

    def __init__(self, value: Union[float, int], is_percent: bool):
        self.value = value
        self.is_percent = is_percent

    def __str__(self) -> str:
        return f"brightness({str(self.value)}{'%' if self.is_percent else ''})"


class BackdropFilterContrast(CSSBackdropFilter):
    __slots__ = ("value", "is_percent")

    def __init__(self, value: Union[float, int], is_percent: bool):
        self.value = value
        self.is_percent = is_percent

    def __str__(self) -> str:
        return f"contrast({str(self.value)}{'%' if self.is_percent else ''})"


class BackdropFilterGrayscale(CSSBackdropFilter):
    __slots__ = ("value", "is_percent")

    def __init__(self, value: Union[float, int], is_percent: bool):
        self.value = value
        self.is_percent = is_percent

    def __str__(self) -> str:
        return f"grayscale({str(self.value)}{'%' if self.is_percent else ''})"


class BackdropFilterHueRotate(CSSBackdropFilter):
    __slots__ = ("angle",)

    def __init__(self, angle: Angle):
        self.angle = angle

    def __str__(self) -> str:
        return f"hue-rotate({str(self.angle)})"


class BackdropFilterInvert(CSSBackdropFilter):
    __slots__ = ("value", "is_percent")

    def __init__(self, value: Union[float, int], is_percent: bool):
        self.value = value
        self.is_percent = is_percent

    def __str__(self) -> str:
        return f"invert({str(self.value)}{'%' if self.is_percent else ''})"


class BackdropFilterOpacity(CSSBackdropFilter):
    __slots__ = ("value", "is_percent")

    def __init__(self, value: Union[float, int], is_percent: bool):
        self.value = value
        self.is_percent = is_percent

    def __str__(self) -> str:
        return f"opacity({str(self.value)}{'%' if self.is_percent else ''})"


class BackdropFilterSaturate(CSSBackdropFilter):
    __slots__ = ("value", "is_percent")

    def __init__(self, value: Union[float, int], is_percent: bool):
        self.value = value
        self.is_percent = is_percent

    def __str__(self) -> str:
        return f"saturate({str(self.value)}{'%' if self.is_percent else ''})"


class BackdropFilterSepia(CSSBackdropFilter):
    __slots__ = ("value", "is_percent")

    def __init__(self, value: Union[float, int], is_percent: bool):
        self.value = value
        self.is_percent = is_percent

    def __str__(self) -> str:
        return f"sepia({str(self.value)}{'%' if self.is_percent else ''})"


class BackdropFilterDropShadow(CSSBackdropFilter):
    __slots__ = ("offset_x", "offset_y", "blur_radius", "color")

    def __init__(self, offset_x: Length, offset_y: Length, blur_radius: Length = None, color: Color = None):
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.blur_radius = blur_radius
        self.color = color

    def __str__(self) -> str:
        lengths = [str(self.offset_x), str(self.offset_y)]
        if self.blur_radius:
            lengths.append(str(self.blur_radius))

        return f"drop-shadow({' '.join(lengths)} {str(self.color) if self.color else ''})"