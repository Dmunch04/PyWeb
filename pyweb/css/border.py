from enum import Enum
from typing import Union, List, Optional

from pyweb.css.style_value import BaseProperty
from pyweb.css.unit import Length
from pyweb.css.color import Color


class BorderWidth(Enum):
    MEDIUM = "medium"
    THIN = "thin"
    THICK = "thick"
    INITIAL = "initial"
    INHERIT = "inherit"


class BorderStyle(Enum):
    NONE = "none"
    HIDDEN = "hidden"
    DOTTED = "dotted"
    DASHED = "dashed"
    SOLID = "solid"
    DOUBLE = "double"
    GROOVE = "groove"
    RIDGE = "ridge"
    INSET = "inset"
    OUTSET = "outset"
    INITIAL = "initial"
    INHERIT = "inherit"


class Border(object):
    __slots__ = ("width", "style", "color")

    def __init__(
        self,
        width: Optional[
            Union[BorderWidth, List[BorderWidth], Length, List[Length]]
        ] = None,
        style: Optional[Union[BorderStyle, List[BorderStyle]]] = None,
        color: Optional[Union[BaseProperty, Color, List[Color]]] = None,
    ):
        self.width = width
        self.style = style
        self.color = color

        if self.width is None and self.style is None and self.color is None:
            raise Exception("border must have at least 1 value")

    def __str__(self) -> str:
        init_str = ""
        if self.width is not None:
            if isinstance(self.width, list):
                widths = []
                list_type = None
                for width in self.width:
                    if list_type is None:
                        list_type = type(width)

                    if not isinstance(width, list_type):
                        raise Exception("width values must be same types")

                    if isinstance(width, BorderWidth):
                        widths.append(self.width.value)
                    elif isinstance(width, Length):
                        widths.append(str(self.width))
                    else:
                        raise Exception("width must be BorderWidth or a Length")
                init_str.append(" ".join(widths) + " ")
            elif isinstance(self.width, BorderWidth):
                init_str += self.width.value + " "
            elif isinstance(self.width, Length):
                init_str += str(self.width) + " "
            else:
                raise Exception("width must be BorderWidth, Length or a list of either")
        if self.style is not None:
            if isinstance(self.style, list):
                for style in self.style:
                    init_str += style.value + " "
            else:
                init_str += self.style.value + " "
        if self.color is not None:
            if isinstance(self.color, BaseProperty):
                init_str += self.color.value + " "
            elif isinstance(self.color, list):
                for color in self.color:
                    if not isinstance(color, Color):
                        raise Exception("colors list must only contain colors")

                    init_str += str(color) + " "
            else:
                init_str += str(self.color) + " "

        return init_str.strip()
