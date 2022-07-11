from enum import IntEnum, Enum
from typing import Any, List, Union, Optional


class StyleType(Enum):
    CLASS = "."
    ID = "#"
    TAG = ""


class ColorType(IntEnum):
    CURRENT_COLOR = 0
    HEX = 1
    HEXA = 2
    RGB = 3
    RGBA = 4
    HSL = 5
    HSLA = 6
    NAMED = 7


class Color(object):
    __slots__ = ("color_type", "values")

    def __init__(self, color_type: ColorType, values: List[str]):
        self.color_type = color_type
        self.values = values

    def __str__(self) -> str:
        if self.color_type == ColorType.CURRENT_COLOR:
            return "currentcolor"
        elif self.color_type in (ColorType.HEX, ColorType.HEXA):
            return f"#{self.values[0]}"
        elif self.color_type in (ColorType.RGB, ColorType.RGBA):
            return f"rgb({', '.join(self.values)})"
        elif self.color_type == ColorType.HSL:
            return f"hsl({self.values[0]}, {self.values[1]}%, {self.values[2]}%)"
        elif self.color_type == ColorType.HSLA:
            return f"hsl({self.values[0]}, {self.values[1]}%, {self.values[2]}%, {self.values[3]})"
        elif self.color_type == ColorType.NAMED:
            return self.values[0]

    @classmethod
    def currentcolor(cls):
        return Color(ColorType.CURRENT_COLOR, [])

    @classmethod
    def hex(cls, hex: str):
        return Color(ColorType.HEX, [hex])

    @classmethod
    def hexa(cls, hexa: str):
        return Color(ColorType.HEXA, [hexa])

    @classmethod
    def rgb(cls, r: Union[int, str], g: Union[int, str], b: Union[int, str]):
        return Color(ColorType.RGB, [str(r), str(g), str(b)])
    
    @classmethod
    def rgba(cls, r: Union[int, str], g: Union[int, str], b: Union[int, str], a: Union[float, str]):
        return Color(ColorType.RGBA, [str(r), str(g), str(b), str(a)])

    @classmethod
    def hsl(cls, h: Union[int, str], s: Union[int, str], l: Union[int, str]):
        return Color(ColorType.RGB, [str(h), str(s), str(l)])

    @classmethod
    def hsla(cls, h: Union[int, str], s: Union[int, str], l: Union[int, str], a: Union[float, str]):
        return Color(ColorType.HSLA, [str(h), str(s), str(l), str(a)])

    @classmethod
    def named(cls, color_name: str):
        return Color(ColorType.NAMED, [str(color_name)])

    @classmethod
    @property
    def CURRENTCOLOR(cls):
        return Color.currentcolor()

    @classmethod
    @property
    def ALICE_BLUE(cls):
        return Color.hex("F0F8FF")

    @classmethod
    @property
    def ANTIQUE_WHITE(cls):
        return Color.hex("FAEBD7")

    @classmethod
    @property
    def AQUA(cls):
        return Color.hex("00FFFF")

    @classmethod
    @property
    def AQUAMARINE(cls):
        return Color.hex("7FFFD4")

    @classmethod
    @property
    def AZURE(cls):
        return Color.hex("F0FFFF")

    @classmethod
    @property
    def BEIGE(cls):
        return Color.hex("F5F5DC")

    @classmethod
    @property
    def BISQUE(cls):
        return Color.hex("FFE4C4")

    @classmethod
    @property
    def BLACK(cls):
        return Color.hex("000000")

    @classmethod
    @property
    def BLANCHED_ALMOND(cls):
        return Color.hex("FFEBCD")

    @classmethod
    @property
    def BLUE(cls):
        return Color.hex("0000FF")

    @classmethod
    @property
    def BLUE_VIOLET(cls):
        return Color.hex("8A2BE2")

    @classmethod
    @property
    def BROWN(cls):
        return Color.hex("A52A2A")

    @classmethod
    @property
    def BURLY_WOOD(cls):
        return Color.hex("DEB887")

    @classmethod
    @property
    def CADET_BLUE(cls):
        return Color.hex("5F9EA0")

    @classmethod
    @property
    def CHARTREUSE(cls):
        return Color.hex("7FFF00")

    @classmethod
    @property
    def CHOCOLATE(cls):
        return Color.hex("D2691E")

    @classmethod
    @property
    def CORAL(cls):
        return Color.hex("FF7F50")

    @classmethod
    @property
    def CORNFLOWER_BLUE(cls):
        return Color.hex("6495ED")

    @classmethod
    @property
    def CORNSILK(cls):
        return Color.hex("FFF8DC")

    @classmethod
    @property
    def CRIMSON(cls):
        return Color.hex("DC143C")

    @classmethod
    @property
    def CYAN(cls):
        return Color.hex("00FFFF")

    @classmethod
    @property
    def DARK_BLUE(cls):
        return Color.hex("00008B")

    @classmethod
    @property
    def DARK_CYAN(cls):
        return Color.hex("008B8B")

    @classmethod
    @property
    def DARK_GOLDEN_ROD(cls):
        return Color.hex("B8860B")

    @classmethod
    @property
    def DARK_GRAY(cls):
        return Color.hex("A9A9A9")

    @classmethod
    @property
    def DARK_GREY(cls):
        return Color.DARK_GRAY

    @classmethod
    @property
    def DARK_GREEN(cls):
        return Color.hex("006400")

    @classmethod
    @property
    def DARK_KHAKI(cls):
        return Color.hex("BDB76B")

    @classmethod
    @property
    def DARK_MAGENTA(cls):
        return Color.hex("8B008B")

    @classmethod
    @property
    def DARK_OLIVE_GREEN(cls):
        return Color.hex("556B2F")

    @classmethod
    @property
    def DARK_ORANGE(cls):
        return Color.hex("FF8C00")

    @classmethod
    @property
    def DARK_ORCHID(cls):
        return Color.hex("9932CC")

    @classmethod
    @property
    def DARK_RED(cls):
        return Color.hex("8B0000")

    @classmethod
    @property
    def DARK_SALMON(cls):
        return Color.hex("E9967A")

    @classmethod
    @property
    def DARK_SEA_GREEN(cls):
        return Color.hex("8FBC8F")

    @classmethod
    @property
    def DARK_SLATE_BLUE(cls):
        return Color.hex("483D8B")

    @classmethod
    @property
    def DARK_SLATE_GRAY(cls):
        return Color.hex("2F4F4F")

    @classmethod
    @property
    def DARK_SLATE_GREY(cls):
        return Color.DARK_SLATE_GRAY

    @classmethod
    @property
    def DARK_TURQUOISE(cls):
        return Color.hex("00CED1")

    @classmethod
    @property
    def DARK_VIOLET(cls):
        return Color.hex("9400D3")

    @classmethod
    @property
    def DEEP_PINK(cls):
        return Color.hex("FF1493")

    @classmethod
    @property
    def DEEP_SKY_BLUE(cls):
        return Color.hex("00BFFF")

    @classmethod
    @property
    def DIM_GRAY(cls):
        return Color.hex("696969")

    @classmethod
    @property
    def DIM_GREY(cls):
        return Color.DIM_GRAY

    @classmethod
    @property
    def DODGER_BLUE(cls):
        return Color.hex("1E90FF")

    @classmethod
    @property
    def FIRE_BRIK(cls):
        return Color.hex("B22222")

    @classmethod
    @property
    def FLORAL_WHITE(cls):
        return Color.hex("FFFAF0")

    @classmethod
    @property
    def FOREST_GREEN(cls):
        return Color.hex("228B22")

    @classmethod
    @property
    def FUCHSIA(cls):
        return Color.hex("FF00FF")

    @classmethod
    @property
    def GAINSBORO(cls):
        return Color.hex("DCDCDC")

    @classmethod
    @property
    def GHOST_WHITE(cls):
        return Color.hex("F0F8FF")

    @classmethod
    @property
    def GOLD(cls):
        return Color.hex("FFD700")

    @classmethod
    @property
    def GOLDEN_ROD(cls):
        return Color.hex("DAA520")

    @classmethod
    @property
    def GRAY(cls):
        return Color.hex("808080")

    @classmethod
    @property
    def GREY(cls):
        return Color.GRAY

    @classmethod
    @property
    def GREEN(cls):
        return Color.hex("008000")

    @classmethod
    @property
    def GREEN_YELLOW(cls):
        return Color.hex("ADFF2F")

    @classmethod
    @property
    def HONEY_DEW(cls):
        return Color.hex("F0FFF0")

    @classmethod
    @property
    def HOT_PINK(cls):
        return Color.hex("FF69B4")

    @classmethod
    @property
    def INDIAN_RED(cls):
        return Color.hex("CD5C5C")

    @classmethod
    @property
    def INDIGO(cls):
        return Color.hex("4B0082")

    @classmethod
    @property
    def IVORY(cls):
        return Color.hex("FFFFF0")

    @classmethod
    @property
    def KHAKI(cls):
        return Color.hex("F0E68C")

    @classmethod
    @property
    def LAVENDER(cls):
        return Color.hex("E6E6FA")

    @classmethod
    @property
    def LAVENDER_BLUSH(cls):
        return Color.hex("FFF0F5")

    @classmethod
    @property
    def LAWN_GREEN(cls):
        return Color.hex("7CFC00")

    @classmethod
    @property
    def LEMON_CHIFFON(cls):
        return Color.hex("FFFACD")

    @classmethod
    @property
    def LIGHT_BLUE(cls):
        return Color.hex("ADD8E6")

    @classmethod
    @property
    def LIGHT_CORAL(cls):
        return Color.hex("F08080")

    @classmethod
    @property
    def LIGHT_CYAN(cls):
        return Color.hex("E0FFFF")

    @classmethod
    @property
    def LIGHT_GOLDEN_ROD_YELLOW(cls):
        return Color.hex("FAFAD2")

    @classmethod
    @property
    def LIGHT_GRAY(cls):
        return Color.hex("D3D3D3")

    @classmethod
    @property
    def LIGHT_GREY(cls):
        return Color.LIGHT_GRAY

    @classmethod
    @property
    def LIGHT_GREEN(cls):
        return Color.hex("90EE90")

    @classmethod
    @property
    def LIGHT_PINK(cls):
        return Color.hex("FFB6C1")

    @classmethod
    @property
    def LIGHT_SALMON(cls):
        return Color.hex("FFA07A")

    @classmethod
    @property
    def LIGHT_SEA_GREEN(cls):
        return Color.hex("20B2AA")

    @classmethod
    @property
    def LIGHT_SKY_BLUE(cls):
        return Color.hex("87CEFA")

    @classmethod
    @property
    def LIGHT_SLATE_GRAY(cls):
        return Color.hex("778899")

    @classmethod
    @property
    def LIGHT_SLATE_GREY(cls):
        return Color.LIGHT_SLATE_GRAY

    @classmethod
    @property
    def LIGHT_STEEL_BLUE(cls):
        return Color.hex("B0C4DE")

    @classmethod
    @property
    def LIGHT_YELLOW(cls):
        return Color.hex("FFFFE0")

    @classmethod
    @property
    def LIME(cls):
        return Color.hex("00FF00")

    @classmethod
    @property
    def LIME_GREEN(cls):
        return Color.hex("32CD32")

    @classmethod
    @property
    def LINEN(cls):
        return Color.hex("FAF0E6")

    @classmethod
    @property
    def MAGENTA(cls):
        return Color.hex("FF00FF")

    @classmethod
    @property
    def MAROON(cls):
        return Color.hex("800000")

    @classmethod
    @property
    def MEDIUM_AQUA_MARINE(cls):
        return Color.hex("66CDAA")

    @classmethod
    @property
    def MEDIUM_BLUE(cls):
        return Color.hex("0000CD")

    @classmethod
    @property
    def MEDIUM_ORCHID(cls):
        return Color.hex("BA55D3")

    @classmethod
    @property
    def MEDIUM_PURPLE(cls):
        return Color.hex("9370DB")

    @classmethod
    @property
    def MEDIUM_SEA_GREEN(cls):
        return Color.hex("3CB371")

    @classmethod
    @property
    def MEDIUM_SLATE_BLUE(cls):
        return Color.hex("7B68EE")

    @classmethod
    @property
    def MEDIUM_SPRING_GREEN(cls):
        return Color.hex("00FA9A")

    @classmethod
    @property
    def MEDIUM_TURQUOISE(cls):
        return Color.hex("48D1CC")

    @classmethod
    @property
    def MEDIUM_VIOLET_RED(cls):
        return Color.hex("C71585")

    @classmethod
    @property
    def MIDNIGHT_BLUE(cls):
        return Color.hex("191970")

    @classmethod
    @property
    def MINT_CREAM(cls):
        return Color.hex("F5FFFA")

    @classmethod
    @property
    def MISTY_ROSE(cls):
        return Color.hex("FFE4E1")

    @classmethod
    @property
    def MOCCASIN(cls):
        return Color.hex("FFE4B5")

    @classmethod
    @property
    def NAVAJO_WHITE(cls):
        return Color.hex("FFDEAD")

    @classmethod
    @property
    def NAVY(cls):
        return Color.hex("000080")

    @classmethod
    @property
    def OLD_LACE(cls):
        return Color.hex("FDF5E6")

    @classmethod
    @property
    def OLIVE(cls):
        return Color.hex("808000")

    @classmethod
    @property
    def OLIVE_DRAB(cls):
        return Color.hex("6B8E23")

    @classmethod
    @property
    def ORANGE(cls):
        return Color.hex("FFA500")

    @classmethod
    @property
    def ORANGE_RED(cls):
        return Color.hex("FF4500")

    @classmethod
    @property
    def ORCHID(cls):
        return Color.hex("DA70D6")

    @classmethod
    @property
    def PALE_GOLDEN_ROD(cls):
        return Color.hex("EEE8AA")

    @classmethod
    @property
    def PALE_GREEN(cls):
        return Color.hex("98FB98")

    @classmethod
    @property
    def PALE_TURQUOISE(cls):
        return Color.hex("AFEEEE")

    @classmethod
    @property
    def PALE_VIOLET_RED(cls):
        return Color.hex("DB7093")

    @classmethod
    @property
    def PAPAYA_WHIP(cls):
        return Color.hex("FFEFD5")

    @classmethod
    @property
    def PEACH_PUFF(cls):
        return Color.hex("FFDAB9")

    @classmethod
    @property
    def PERU(cls):
        return Color.hex("CD853F")

    @classmethod
    @property
    def PINK(cls):
        return Color.hex("FFC0CB")

    @classmethod
    @property
    def PLUM(cls):
        return Color.hex("DDA0DD")

    @classmethod
    @property
    def POWDER_BLUE(cls):
        return Color.hex("B0E0E6")

    @classmethod
    @property
    def PURPLE(cls):
        return Color.hex("800080")

    @classmethod
    @property
    def REBECCA_PURPLE(cls):
        return Color.hex("663399")

    @classmethod
    @property
    def RED(cls):
        return Color.hex("FF0000")

    @classmethod
    @property
    def ROSY_BROWN(cls):
        return Color.hex("BC8F8F")

    @classmethod
    @property
    def ROYAL_BLUE(cls):
        return Color.hex("4169E1")

    @classmethod
    @property
    def SADDLE_BROWN(cls):
        return Color.hex("8B4513")

    @classmethod
    @property
    def SALMON(cls):
        return Color.hex("FA8072")

    @classmethod
    @property
    def SANDY_BROWN(cls):
        return Color.hex("F4A460")

    @classmethod
    @property
    def SEA_GREEN(cls):
        return Color.hex("2E8B57")

    @classmethod
    @property
    def SEA_SHELL(cls):
        return Color.hex("FFF5EE")

    @classmethod
    @property
    def SIENNA(cls):
        return Color.hex("A0522D")

    @classmethod
    @property
    def SILVER(cls):
        return Color.hex("C0C0C0")

    @classmethod
    @property
    def SKY_BLUE(cls):
        return Color.hex("87CEEB")

    @classmethod
    @property
    def SLATE_BLUE(cls):
        return Color.hex("6A5ACD")

    @classmethod
    @property
    def SLATE_GRAY(cls):
        return Color.hex("708090")

    @classmethod
    @property
    def SLATE_GREY(cls):
        return Color.SLATE_GRAY

    @classmethod
    @property
    def SNOW(cls):
        return Color.hex("FFFAFA")

    @classmethod
    @property
    def SPRING_GREEN(cls):
        return Color.hex("00FF7F")

    @classmethod
    @property
    def STEEL_BLUE(cls):
        return Color.hex("4682B4")

    @classmethod
    @property
    def TAN(cls):
        return Color.hex("D2B48C")

    @classmethod
    @property
    def TEAL(cls):
        return Color.hex("008080")

    @classmethod
    @property
    def THISTLE(cls):
        return Color.hex("D8BFD8")

    @classmethod
    @property
    def TOMATO(cls):
        return Color.hex("FF6347")

    @classmethod
    @property
    def TURQUOISE(cls):
        return Color.hex("40E0D0")

    @classmethod
    @property
    def VIOLET(cls):
        return Color.hex("EE82EE")

    @classmethod
    @property
    def WHEAT(cls):
        return Color.hex("F5DEB3")

    @classmethod
    @property
    def WHITE(cls):
        return Color.hex("FFFFFF")

    @classmethod
    @property
    def WHITE_SMOKE(cls):
        return Color.hex("F5F5F5")

    @classmethod
    @property
    def YELLOW(cls):
        return Color.hex("FFFF00")

    @classmethod
    @property
    def YELLOW_GREEN(cls):
        return Color.hex("9ACD32")


class URL(object):
    __slots__ = ("url",)

    def __init__(self, url: str):
        self.url = url

    def __str__(self) -> str:
        return f"url({self.url})"


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
    PERCENT = 9 # %


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


class BaseProperty(Enum):
    INITIAL = "initial"
    INHERIT = "inherit"


class AccentColor(Enum):
    AUTO = "auto"
    INITIAL = "initial"
    INHERIT = "inherit"


class ContentAlignment(Enum):
    STRETCH = "stretch"
    CENTER = "center"
    FLEX_START = "flex-start"
    FLEX_END = "flex-end"
    SPACE_BETWEEN = "space-between"
    SPACE_AROUND = "space-around"
    SPACE_EVENLY = "space-evenly"
    INITIAL = "initial"
    INHERIT = "inherit"


class ItemAlignment(Enum):
    STRETCH = "stretch"
    CENTER = "center"
    FLEX_START = "flex-start"
    FLEX_END = "flex-end"
    BASELINE = "baseline"
    INITIAL = "initial"
    INHERIT = "inherit"


class SelfAlignment(Enum):
    AUTO = "auto"
    STRETCH = "stretch"
    CENTER = "center"
    FLEX_START = "flex-start"
    FLEX_END = "flex-end"
    BASELINE = "baseline"
    INITIAL = "initial"
    INHERIT = "inherit"


class All(Enum):
    INITIAL = "initial"
    INHERIT = "inherit"
    UNSET = "unset"


class AnimationDirection(Enum):
    NORMAL = "normal"
    REVERSE = "reverse"
    ALTERNATE = "alternate"
    ALTERNATE_REVERSE = "alternate-reverse"
    INITIAL = "initial"
    INHERIT = "inherit"


class AnimationFillMode(Enum):
    NONE = "none"
    FORWARDS = "forwards"
    BACKWARDS = "backwards"
    BOTH = "both"
    INITIAL = "initial"
    INHERIT = "inherit"


class AnimationIterationCount(Enum):
    INFINITE = "infinite"
    INITIAL = "initial"
    INHERIT = "inherit"


class AnimationName(Enum):
    NONE = "none"
    INITIAL = "initial"
    INHERIT = "inherit"


class AnimationPlayState(Enum):
    PAUSED = "paused"
    RUNNING = "running"
    INITIAL = "initial"
    INHERIT = "inherit"


class AnimationTimingFunction(Enum):
    LINEAR = "linear"
    EASE = "ease"
    EASE_IN = "ease-in"
    EASE_OUT = "ease-out"
    EASE_IN_OUT = "ease-in-out"
    STEP_START = "step-start"
    STEP_END = "step-end"
    INITIAL = "initial"
    INHERIT = "inherit"


class BackdropFilter(Enum):
    NONE = "none"
    INITIAL = "initial"
    INHERIT = "inherit"


class BackfaceVisibility(Enum):
    VISIBLE = "visible"
    HIDDEN = "hidden"
    INITIAL = "initial"
    INHERIT = "inherit"


class BackgroundAttachment(Enum):
    SCROLL = "scroll"
    FIXED = "fixed"
    LOCAL = "local"
    INITIAL = "initial"
    INHERIT = "inherit"


class BackgroundBlendMode(Enum):
    NORMAL = "normal"
    MULTIPLY = "multiply"
    SCREEN = "screen"
    OVERLAY = "overlay"
    DARKEN = "darken"
    LIGHTEN = "lighten"
    COLOR_DODGE = "color-dodge"
    SATURATION = "saturation"
    COLOR = "color"
    LUMINOSITY = "luminosity"


class BackgroundClip(Enum):
    BORDER_BOX = "border-box"
    PADDING_BOX = "padding-box"
    CONTENT_BOX = "content-box"
    INITIAL = "initial"
    INHERIT = "inherit"


class BackgroundImage(Enum):
    NONE = "none"
    INITIAL = "initial"
    INHERIT = "inherit"


class Style(object):
    def __init__(self, name, style_type):
        self.name = name
        self.style_type = style_type

        # src: https://www.w3schools.com/cssref/
        self.accent_color: Union[AccentColor, Color] = None
        self.align_content: ContentAlignment = None
        self.align_items: ItemAlignment = None
        self.align_self: SelfAlignment = None
        self.all: All = None
        self.animation: Union[BaseProperty, str, Animation] = None
        self.animation_delay: Union[BaseProperty, Time] = None
        self.animation_direction: AnimationDirection = None
        self.animation_duration: Union[BaseProperty, Time] = None
        self.animation_fill_mode: AnimationFillMode = None
        self.animation_iteration_count: Union[AnimationIterationCount, int] = None
        self.animation_name: Union[AnimationName, str] = None
        self.animation_play_state: AnimationPlayState = None
        self.animation_timing_function: Union[AnimationTimingFunction, CSSAnimation] = None
        self.backdrop_filter: Union[BackdropFilter, Union[CSSBackdropFilter, List[CSSBackdropFilter]]] = None
        self.backface_visibility: BackfaceVisibility = None
        self.background: Union[BaseProperty, str, Background] = None
        self.background_attachment: BackgroundAttachment = None
        self.background_blend_mode: BackgroundBlendMode = None
        self.background_clip: BackgroundClip = None
        self.background_color: Color = None
        self.background_image: Union[BackgroundImage, URL, List[URL], CSSGradient] = None
        self.background_origin = None
        self.background_position = None
        self.background_repeat = None
        self.background_size = None
        self.border = None
        self.border_bottom = None
        self.border_bottom_color = None
        self.border_bottom_left_radius = None
        self.border_bottom_right_radius = None
        self.border_bottom_style = None
        self.border_bottom_width = None
        self.border_collapse = None
        self.border_color = None
        self.border_image = None
        self.border_image_outset = None
        self.border_image_repeat = None
        self.border_image_slice = None
        self.border_image_source = None
        self.border_image_width = None
        self.border_left = None
        self.border_left_color = None
        self.border_left_style = None
        self.border_left_width = None
        self.border_radius = None
        self.border_right = None
        self.border_right_color = None
        self.border_right_style = None
        self.border_right_width = None
        self.border_spacing = None
        self.border_style = None
        self.border_top = None
        self.border_top_color = None
        self.border_top_left_radius = None
        self.border_top_right_radius = None
        self.border_top_style = None
        self.border_top_width = None
        self.border_width = None
        self.bottom = None
        self.box_decoration_break = None
        self.box_shadow = None
        self.box_sizing = None
        self.break_after = None
        self.break_before = None
        self.break_inside = None
        self.caption_side = None
        self.caret_color = None
        self.charset = None
        self.clear = None
        self.clip = None
        self.color = None
        self.column_count = None
        self.column_fill = None
        self.column_gap = None
        self.column_rule = None
        self.column_rule_color = None
        self.column_rule_style = None
        self.column_rule_width = None
        self.column_span = None
        self.column_width = None
        self.columns = None
        self.content = None
        self.counter_increment = None
        self.counter_reset = None
        self.cursor = None
        self.direction = None
        self.display = None
        self.empty_cells = None
        self.filter = None
        self.flex = None
        self.flex_basis = None
        self.flex_direction = None
        self.flex_flow = None
        self.flex_grow = None
        self.flex_shrink = None
        self.flex_wrap = None
        self.float = None
        self.font = None
        self.font_face = None
        self.font_family = None
        self.font_feature_settings = None
        self.font_feature_values = None
        self.font_kerning = None
        self.font_language_override = None
        self.font_size = None
        self.font_size_adjust = None
        self.font_stretch = None
        self.font_style = None
        self.font_synthesis = None
        self.font_variant = None
        self.font_variant_alternates = None
        self.font_variant_caps = None
        self.font_variant_east_asian = None
        self.font_variant_ligatures = None
        self.font_variant_numeric = None
        self.font_variant_position = None
        self.font_weight = None
        self.gap = None
        self.grid = None
        self.grid_area = None
        self.grid_auto_columns = None
        self.grid_auto_flow = None
        self.grid_auto_rows = None
        self.grid_column = None
        self.grid_column_end = None
        self.grid_column_gap = None
        self.grid_column_start = None
        self.grid_gap = None
        self.grid_row = None
        self.grid_row_end = None
        self.grid_row_gap = None
        self.grid_row_start = None
        self.grid_template = None
        self.grid_template_areas = None
        self.grid_template_columns = None
        self.grid_template_rows = None
        self.hanging_punctuation = None
        self.height = None
        self.hyphens = None
        self.image_rendering = None
        self.import_ = None
        self.isolation = None
        self.justify_content = None
        self.keyframes = None
        self.left = None
        self.letter_spacing = None
        self.line_break = None
        self.line_height = None
        self.list_style = None
        self.list_style_image = None
        self.list_style_position = None
        self.list_style_type = None
        self.margin = None
        self.margin_bottom = None
        self.margin_left = None
        self.margin_right = None
        self.margin_top = None
        self.mask = None
        self.mask_clip = None
        self.mask_composite = None
        self.mask_image = None
        self.mask_mode = None
        self.mask_origin = None
        self.mask_position = None
        self.mask_repeat = None
        self.mask_size = None
        self.mask_type = None
        self.max_height = None
        self.max_width = None
        self.media = None
        self.min_height = None
        self.min_width = None
        self.mix_blend_mode = None
        self.object_fit = None
        self.object_position = None
        self.opacity = None
        self.order = None
        self.orphans = None
        self.outline = None
        self.outline_color = None
        self.outline_offset = None
        self.outline_style = None
        self.outline_width = None
        self.overflow = None
        self.overflow_wrap = None
        self.overflow_x = None
        self.overflow_y = None
        self.padding = None
        self.padding_bottom = None
        self.padding_left = None
        self.padding_right = None
        self.padding_top = None
        self.page_break_after = None
        self.page_break_before = None
        self.page_break_inside = None
        self.perspective = None
        self.perspective_origin = None
        self.pointer_events = None
        self.position = None
        self.quotes = None
        self.resize = None
        self.right = None
        self.row_gap = None
        self.scroll_behaviour = None
        self.tab_size = None
        self.table_layout = None
        self.text_align = None
        self.text_align_last = None
        self.text_combine_upright = None
        self.text_decoration = None
        self.text_decoration_color = None
        self.text_decoration_line = None
        self.text_decoration_style = None
        self.text_decoration_thickness = None
        self.text_emphasis = None
        self.text_indent = None
        self.text_justify = None
        self.text_orientation = None
        self.text_overflow = None
        self.text_shadow = None
        self.text_transform = None
        self.text_underline_position = None
        self.top = None
        self.transform = None
        self.transform_origin = None
        self.transform_style = None
        self.transition = None
        self.transition_delay = None
        self.transition_duration = None
        self.transition_property = None
        self.transition_timing_function = None
        self.unicode_bidi = None
        self.user_select = None
        self.vertical_align = None
        self.visibility = None
        self.white_space = None
        self.widows = None
        self.width = None
        self.word_break = None
        self.word_spacing = None
        self.word_wrap = None
        self.writing_mode = None
        self.z_index = None

    def get_fields(self):
        fields = {}
        for slot in self.__fields:
            if self.__getattribute__(slot):
                name = slot.replace("_", "-")

                if name in ("charset", "font-face", "font-feature-values", "import", "keyframes", "media"):
                    name = "@" + name

                value = self.__getattribute__(slot)

                if isinstance(value, Enum):
                    value = value.value

                fields[name] = value

        return fields

    def get_str(self):
        template = "{style_type}{name} {{\n{fields}\n}}"

        fields = []
        for field, value in self.get_fields().items():
            fields.append(f"\t{field}: {value};")

        return template.format(
            style_type=self.style_type.value,
            name=self.name,
            fields="\n".join(fields)
        )

    def get_inline_fields_str(self):
        fields = []
        for field, value in self.get_fields().items():
            fields.append(f"{field}:{value};")

        return "".join(fields)

    def get_inline_str(self):
        template = "{style_type}{name}{{{fields}}}"

        return template.format(
            style_type=self.style_type.value,
            name=self.name,
            fields=self.get_inline_fields_str()
        )

    def __str__(self):
        return self.get_inline_str()

    __fields = ("accent_color", "align_content", "align_items", "align_self", "all", "animation", "animation_delay", "animation_direction", "animation_duration", "animation_fill_mode", "animation_iteration_count", "animation_name", "animation_play_state", "animation_timing_function", "backdrop_filter", "backface_visibility", "background", "background_attachment", "background_blend_mode", "background_clip", "background_color", "background_image", "background_origin", "background_position", "background_repeat", "background_size", "border", "border_bottom", "border_bottom_color", "border_bottom_left_radius", "border_bottom_right_radius", "border_bottom_style", "border_bottom_width", "border_collapse", "border_color", "border_image", "border_image_outset", "border_image_repeat", "border_image_slice", "border_image_source", "border_image_width", "border_left", "border_left_color", "border_left_style", "border_left_width", "border_radius", "border_right", "border_right_color", "border_right_style", "border_right_width", "border_spacing", "border_style", "border_top", "border_top_color", "border_top_left_radius", "border_top_right_radius", "border_top_style", "border_top_width", "border_width", "bottom", "box_decoration_break", "box_shadow", "box_sizing", "break_after", "break_before", "break_inside", "caption_side", "caret_color", "charset", "clear", "clip", "color", "column_count", "column_fill", "column_gap", "column_rule", "column_rule_color", "column_rule_style", "column_rule_width", "column_span", "column_width", "columns", "content", "counter_increment", "counter_reset", "cursor", "direction", "display", "empty_cells", "filter", "flex", "flex_basis", "flex_direction", "flex_flow", "flex_grow", "flex_shrink", "flex_wrap", "float", "font", "font_face", "font_family", "font_feature_settings", "font_feature_values", "font_kerning", "font_language_override", "font_size", "font_size_adjust", "font_stretch", "font_style", "font_synthesis", "font_variant", "font_variant_alternates", "font_variant_caps", "font_variant_east_asian", "font_variant_ligatures", "font_variant_numeric", "font_variant_position", "font_weight", "gap", "grid", "grid_area", "grid_auto_columns", "grid_auto_flow", "grid_auto_rows", "grid_column", "grid_column_end", "grid_column_gap", "grid_column_start", "grid_gap", "grid_row", "grid_row_end", "grid_row_gap", "grid_row_start", "grid_template", "grid_template_areas", "grid_template_columns", "grid_template_rows", "hanging_punctuation", "height", "hyphens", "image_rendering", "import_", "isolation", "justify_content", "keyframes", "left", "letter_spacing", "line_break", "line_height", "list_style", "list_style_image", "list_style_position", "list_style_type", "margin", "margin_bottom", "margin_left", "margin_right", "margin_top", "mask", "mask_clip", "mask_composite", "mask_image", "mask_mode", "mask_origin", "mask_position", "mask_repeat", "mask_size", "mask_type", "max_height", "max_width", "media", "min_height", "min_width", "mix_blend_mode", "object_fit", "object_position", "opacity", "order", "orphans", "outline", "outline_color", "outline_offset", "outline_style", "outline_width", "overflow", "overflow_wrap", "overflow_x", "overflow_y", "padding", "padding_bottom", "padding_left", "padding_right", "padding_top", "page_break_after", "page_break_before", "page_break_inside", "perspective", "perspective_origin", "pointer_events", "position", "quotes", "resize", "right", "row_gap", "scroll_behaviour", "tab_size", "table_layout", "text_align", "text_align_last", "text_combine_upright", "text_decoration", "text_decoration_color", "text_decoration_line", "text_decoration_style", "text_decoration_thickness", "text_emphasis", "text_indent", "text_justify", "text_orientation", "text_overflow", "text_shadow", "text_transform", "text_underline_position", "top", "transform", "transform_origin", "transform_style", "transition", "transition_delay", "transition_duration", "transition_property", "transition_timing_function", "unicode_bidi", "user_select", "vertical_align", "visibility", "white_space", "widows", "width", "word_break", "word_spacing", "word_wrap", "writing_mode", "z_index")

    def inject_field(self, field: str, value: str):
        if not field in self.__fields:
            raise Exception("cannot inject value into non existing css field")

        self.__setattr__(field, value)


class CSSAnimation(object):
    @classmethod
    @property
    def value(self) -> str: return self.__str__()


class AnimationSteps(CSSAnimation):
    """
    Specifies a stepping function, with two parameters. The first parameter specifies the number of intervals in the function.
    It must be a positive integer (greater than 0). The second parameter, which is optional, is either the value "start" or "end",
    and specifies the point at which the change of values occur within the interval. If the second parameter is omitted,
    it is given the value "end"
    """

    __slots__ = ("intervals", "changepoint")

    def __init__(self, intervals: int, changepoint: str = "end"):
        self.intervals = intervals

        if changepoint not in ("start", "end"):
            changepoint = "end"

        self.changepoint = changepoint

    def __str__(self) -> str:
        return f"steps({str(self.intervals)},{self.changepoint})"


class AnimationCubicBezier(CSSAnimation):
    """
    Define your own values in the cubic-bezier function
    Possible values are numeric values from 0 to 1
    """

    __slots__ = ("a", "b", "c", "d")

    def __init__(self, a: int, b: int, c: int, d: int):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self) -> str:
        return f"cubic-bezier({str(self.a)},{self.b},{self.c},{self.d})"


class Animation(object):
    __slots__ = ("name", "duration", "timing_function", "delay",
                 "iteration_count", "direction", "fill_mode", "play_state")

    def __init__(self, name: Union[AnimationName, str] = None, duration: Union[BaseProperty, str] = "1s", timing_function: Union[AnimationTimingFunction, CSSAnimation] = None, delay: Union[BaseProperty, str] = None, iteration_count: Union[AnimationIterationCount, str] = None, direction: AnimationDirection = None, fill_mode: AnimationFillMode = None, play_state: AnimationPlayState = None):
        self.name = name
        self.duration = duration
        self.timing_function = timing_function
        self.delay = delay
        self.iteration_count = iteration_count
        self.direction = direction
        self.fill_mode = fill_mode
        self.play_state = play_state

    def __str__(self) -> str:
        animation = ""

        if self.name:
            if isinstance(self.name, str):
                animation += self.name + " "
            else:
                animation += self.name.value + " "

        if self.duration:
            if isinstance(self.duration, str):
                animation += self.duration + " "
            else:
                animation += self.duration.value + " "

        if self.timing_function:
            animation += self.timing_function.value + " "

        if self.delay:
            if isinstance(self.delay, str):
                animation += self.delay + " "
            else:
                animation += self.delay.value + " "

        if self.iteration_count:
            if isinstance(self.iteration_count, str):
                animation += self.iteration_count + " "
            else:
                animation += self.iteration_count.value + " "

        if self.direction:
            animation += self.direction.value + " "

        if self.fill_mode:
            animation += self.fill_mode.value + " "

        if self.play_state:
            animation += self.play_state.value + " "

        return animation[0:-1]


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


class CSSGradient(object):
    @classmethod
    @property
    def value(self) -> str: return self.__str__()


class ColorDegree(object):
    __slots__ = ("color", "degree")

    def __init__(self, color: Color, degree: Union[Angle, Length] = None):
        self.color = color
        self.degree = degree

        if self.degree is not None:
            if not self.degree.unit == RelativeLengthUnit.PERCENT:
                raise Exception("color degree value must be an angle or percent value")

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

    def __init__(self, k: Union[Angle, CSSStartingPoint], v: Optional[Union[Angle, CSSStartingPoint]] = None):
        self.k = k
        self.v = v

        if isinstance(k, HorizontalStartingPoint) and isinstance(v, HorizontalStartingPoint):
            raise Exception("both values cannot be horizontal values")
        elif isinstance(k, VerticalStartingPoint) and isinstance(v, VerticalStartingPoint):
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
    def __init__(self, colors: List[ColorDegree], from_angle: Angle = None, at_pos = None):
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


class Background(object):
    pass

