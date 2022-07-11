from enum import IntEnum
from typing import List, Union


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
            return f"hsla({self.values[0]}, {self.values[1]}%, {self.values[2]}%, {self.values[3]})"
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
    def rgba(
        cls,
        r: Union[int, str],
        g: Union[int, str],
        b: Union[int, str],
        a: Union[float, str],
    ):
        return Color(ColorType.RGBA, [str(r), str(g), str(b), str(a)])

    @classmethod
    def hsl(cls, h: Union[int, str], s: Union[int, str], l: Union[int, str]):
        return Color(ColorType.RGB, [str(h), str(s), str(l)])

    @classmethod
    def hsla(
        cls,
        h: Union[int, str],
        s: Union[int, str],
        l: Union[int, str],
        a: Union[float, str],
    ):
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
