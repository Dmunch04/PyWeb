import os
from enum import Enum, IntEnum
from collections import namedtuple


Position = namedtuple("Position", ("x", "y"))


class TextType(Enum):
    H1 = "h1"
    H2 = "h2"
    H3 = "h3"
    H4 = "h4"
    H5 = "h5"
    H6 = "h6"
    P = "p"


class CSSStyleType(Enum):
    CLASS = "."
    ID = "#"
    TAG = ""


class CSSFieldValueType(IntEnum):
    Number = 0
    String = 1
    Keyword = 2

class CSSField(object):
    __slots__ = ("name", "value", "value_type")

    def __init__(self, name, value, value_type):
        self.name = name
        self.value = value
        self.value_type = value_type

    def __str__(self):
        value = str(self.value)
        #if self.value_type == CSSFieldValueType.String:
            #value = f"\"{value}\""

        return f"{self.name}: {value};"


class Color(object):
    __slots__ = ("r", "g", "b", "a")

    def __init__(self, r, g, b, a=1):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    @staticmethod
    def from_hex(hex):
        import re

        if re.match(r"^#([A-Fa-f0-9]{3}){1,2}$", hex):
            hex = hex[1:].split(" ")[0]
            rgb = tuple(int(hex[i : i + 2], 16) for i in (0, 2, 4))
            return Color(rgb[0], rgb[1], rgb[2])

        raise Exception("Bad Hex")

    def to_hex_string(self):
        return "#%02x%02x%02x" % (self.r, self.g, self.b)


class CSSStyle(object):
    __slots__ = ("name", "style_type", "fields")

    def __init__(self, name, style_type=CSSStyleType.CLASS, fields=[]):
        self.name = name
        self.style_type = style_type
        self.fields = fields

    def add_field(self, field: CSSField):
        self.fields.append(field)
        return self

    def remove_field(self, field_name):
        print("implement")
        return self

    def __str__(self):
        fields = [str(field) for field in self.fields]
        return self.style_type.value + self.name + "{" + "".join(fields) + "}"


class HTMLElementStyle(object):
    @classmethod
    def get_css(cls):
        raise NotImplementedError

    @classmethod
    def get_inline_css(cls):
        raise NotImplementedError


class TextStyle(HTMLElementStyle):
    __slots__ = ("name", "font", "size", "color", "css")

    def __init__(
        self, name, font="Sans-Serif", size=16, color=Color.from_hex("#000000")
    ):
        self.name = name
        self.font = font
        self.size = size
        self.color = color

        self.css = CSSStyle(
            name,
            CSSStyleType.TAG,
            [
                CSSField("font-family", font, CSSFieldValueType.String),
                CSSField("font-size", str(size), CSSFieldValueType.Number),
                CSSField("color", color.to_hex_string(), CSSFieldValueType.String),
            ],
        )

    def get_css(self):
        return self.css

    def get_inline_css(self):
        css = [str(field) for field in self.css.fields]

        return "".join(css)


class ButtonStyle(HTMLElementStyle):
    __slots__ = ("name", "text_style", "width", "height", "color", "css")

    def __init__(self, name, text_style=None, width=100, height=80, color=Color.from_hex("#ffffff")):
        self.name = name
        self.text_style = text_style
        self.width = width
        self.height = height
        self.color = color

        self.css = CSSStyle(
            name,
            CSSStyleType.TAG,
            [
                CSSField("width", str(width), CSSFieldValueType.Number),
                CSSField("height", str(height), CSSFieldValueType.Number),
                CSSField("background-color", color.to_hex_string(), CSSFieldValueType.String),
            ],
        )

    def get_css(self):
        return self.css

    def get_inline_css(self):
        css = ""
        for name, value in self.css.fields.items():
            css += f"{name}:{value};"

        return css


class HTMLElement(object):
    @classmethod
    def to_html(cls):
        raise NotImplementedError


class HTMLText(HTMLElement):
    __slots__ = ("text", "style", "text_type", "position", "link", "class_", "id_")

    def __init__(self, text, style, text_type, position, link, class_, id_):
        self.text = text
        self.style = style
        self.text_type = text_type
        self.position = position
        self.link = link
        self.class_ = class_
        self.id_ = id_

        if isinstance(class_, list) or isinstance(class_, tuple):
            self.classes = class_
        elif isinstance(class_, str):
            self.classes = class_.split(" ")
        else:
            raise ValueError

        if isinstance(id_, list) or isinstance(id_, tuple):
            self.ids = id_
        elif isinstance(id_, str):
            self.ids = id_.split(" ")
        else:
            raise ValueError

    def to_html(self):
        template = """<{text_type} {attrs}>{text}</{text_type}>"""
        attrs = {}

        if not self.link is None:
            text = """<a href="{link}">{text}</a>""".format(
                link=self.link,
                text=self.text,
            )
        else:
            text = self.text

        if self.style:
            attrs["style"] = self.style.get_inline_css()

        if self.class_:
            attrs["class"] = self.class_

        if self.id_:
            attrs["id"] = self.id_

        attr_str = ""
        for attr, value in attrs.items():
            attr_str += f"{attr}=\"{value}\" "

        attr_str = attr_str[0:-1]
        
        html = template.format(
            text_type=self.text_type.value,
            attrs=attr_str,
            text=text,
        )

        return html


class HTMLButton(HTMLElement):
    __slots__ = ("text", "style", "position", "size", "link", "class_", "id_")

    def __init__(self, text, style, position, size, link, class_, id_):
        self.text = text
        self.style = style
        self.position = position
        self.size = size
        self.link = link
        self.class_ = class_
        self.id_ = id_

        if isinstance(class_, list) or isinstance(class_, tuple):
            self.classes = class_
        elif isinstance(class_, str):
            self.classes = class_.split(" ")
        else:
            raise ValueError

        if isinstance(id_, list) or isinstance(id_, tuple):
            self.ids = id_
        elif isinstance(id_, str):
            self.ids = id_.split(" ")
        else:
            raise ValueError

    def to_html(self):
        template = """<form action={link}><input style="{style}" class="{class_}" id="{id_}" type="submit" value="{text}"></input></form>"""
        
        html = template.format(
            link=self.link,
            style=f"top:{self.position[0]};left:{self.position[1]};",
            class_=" ".join(self.classes),
            id_=" ".join(self.ids),
            text=self.text,
        )

        return html


class HTMLImage(HTMLElement):
    def to_html(self):
        pass


class PageStyle(object):
    __slots__ = ("background_color", "favicon", "h1", "h2", "h3", "h4", "h5", "h6", "p")

    def __init__(
        self,
        background_color=Color.from_hex("#ffffff"),
        favicon="",
        h1=TextStyle(TextType.H1, size=32),
        h2=TextStyle(TextType.H2, size=24),
        h3=TextStyle(TextType.H3, size=18.72),
        h4=TextStyle(TextType.H4, size=16),
        h5=TextStyle(TextType.H5, size=13.28),
        h6=TextStyle(TextType.H6, size=12),
        p=TextStyle(TextType.P, size=16, color=Color.from_hex("#212121")),
    ):
        self.background_color = background_color
        self.favicon = favicon
        self.h1 = h1
        self.h2 = h2
        self.h3 = h3
        self.h4 = h4
        self.h5 = h5
        self.h6 = h6
        self.p = p

    def get_text_style(self, text_type):
        if text_type == TextType.H1:
            return self.h1
        elif text_type == TextType.H2:
            return self.h2
        elif text_type == TextType.H3:
            return self.h3
        elif text_type == TextType.H4:
            return self.h4
        elif text_type == TextType.H5:
            return self.h5
        elif text_type == TextType.H6:
            return self.h6
        elif text_type == TextType.P:
            return self.p


class Page(object):
    def __init__(
        self, filename, out_path="/", title="Untitled", page_style=PageStyle()
    ):
        self.filename = filename
        self.out_path = out_path
        self.save_path = os.path.join(out_path, filename)

        self.elements = []
        self.classes = []

        self.title = title
        self.page_style = page_style

    def add_text(self, text, position, text_type=TextType.P, class_="", id_=""):
        self.elements.append(HTMLText(
            text,
            self.page_style.get_text_style(text_type),
            text_type,
            position,
            None,
            class_,
            id_
        ))

    def add_linked_text(
        self, text, position, text_type=TextType.P, class_="", id_="", link="#"
    ):
        self.elements.append(HTMLText(
            text,
            self.page_style.get_text_style(text_type),
            text_type,
            position,
            link,
            class_,
            id_
        ))

    def add_button(self, text, position, style=None, size=(80, 50), class_="", id_="", link="#"):
        self.elements.append(HTMLButton(
            text,
            style,
            position,
            size,
            link,
            class_,
            id_
        ))

    def write(self):
        for element in self.elements:
            print(element.to_html())
