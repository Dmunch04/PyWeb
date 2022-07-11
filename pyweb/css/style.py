from enum import Enum
from typing import Any, List, Union, Dict, NoReturn

from pyweb.css.animation import *
from pyweb.css.backdropfilter import *
from pyweb.css.color import *
from pyweb.css.gradient import *
from pyweb.css.unit import *


class StyleType(Enum):
    CLASS = "."
    ID = "#"
    TAG = ""


class URL(object):
    __slots__ = ("url",)

    def __init__(self, url: str):
        self.url = url

    def __str__(self) -> str:
        return f"url(\"{self.url}\")"


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
    def __init__(self, name: str, style_type: StyleType):
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
        self.animation_timing_function: Union[
            AnimationTimingFunction, CSSAnimation
        ] = None
        self.backdrop_filter: Union[
            BackdropFilter, Union[CSSBackdropFilter, List[CSSBackdropFilter]]
        ] = None
        self.backface_visibility: BackfaceVisibility = None
        self.background: Union[BaseProperty, str, Background] = None
        self.background_attachment: BackgroundAttachment = None
        self.background_blend_mode: BackgroundBlendMode = None
        self.background_clip: BackgroundClip = None
        self.background_color: Color = None
        self.background_image: Union[
            BackgroundImage, URL, List[URL], CSSGradient
        ] = None
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

    def get_fields(self) -> Dict[str, Any]:
        fields = {}
        for slot in self.__fields:
            if self.__getattribute__(slot):
                name = slot.replace("_", "-")

                if name in (
                    "charset",
                    "font-face",
                    "font-feature-values",
                    "import",
                    "keyframes",
                    "media",
                ):
                    name = "@" + name

                value = self.__getattribute__(slot)

                if isinstance(value, Enum):
                    value = value.value

                fields[name] = value

        return fields

    def get_str(self) -> str:
        template = "{style_type}{name} {{\n{fields}\n}}"

        fields = []
        for field, value in self.get_fields().items():
            fields.append(f"\t{field}: {value};")

        return template.format(
            style_type=self.style_type.value, name=self.name, fields="\n".join(fields)
        )

    def get_inline_fields_str(self) -> str:
        fields = []
        for field, value in self.get_fields().items():
            fields.append(f"{field}:{value};")

        return "".join(fields)

    def get_inline_str(self) -> str:
        template = "{style_type}{name}{{{fields}}}"

        return template.format(
            style_type=self.style_type.value,
            name=self.name,
            fields=self.get_inline_fields_str(),
        )

    def __str__(self) -> str:
        return self.get_inline_str()

    __fields = (
        "accent_color",
        "align_content",
        "align_items",
        "align_self",
        "all",
        "animation",
        "animation_delay",
        "animation_direction",
        "animation_duration",
        "animation_fill_mode",
        "animation_iteration_count",
        "animation_name",
        "animation_play_state",
        "animation_timing_function",
        "backdrop_filter",
        "backface_visibility",
        "background",
        "background_attachment",
        "background_blend_mode",
        "background_clip",
        "background_color",
        "background_image",
        "background_origin",
        "background_position",
        "background_repeat",
        "background_size",
        "border",
        "border_bottom",
        "border_bottom_color",
        "border_bottom_left_radius",
        "border_bottom_right_radius",
        "border_bottom_style",
        "border_bottom_width",
        "border_collapse",
        "border_color",
        "border_image",
        "border_image_outset",
        "border_image_repeat",
        "border_image_slice",
        "border_image_source",
        "border_image_width",
        "border_left",
        "border_left_color",
        "border_left_style",
        "border_left_width",
        "border_radius",
        "border_right",
        "border_right_color",
        "border_right_style",
        "border_right_width",
        "border_spacing",
        "border_style",
        "border_top",
        "border_top_color",
        "border_top_left_radius",
        "border_top_right_radius",
        "border_top_style",
        "border_top_width",
        "border_width",
        "bottom",
        "box_decoration_break",
        "box_shadow",
        "box_sizing",
        "break_after",
        "break_before",
        "break_inside",
        "caption_side",
        "caret_color",
        "charset",
        "clear",
        "clip",
        "color",
        "column_count",
        "column_fill",
        "column_gap",
        "column_rule",
        "column_rule_color",
        "column_rule_style",
        "column_rule_width",
        "column_span",
        "column_width",
        "columns",
        "content",
        "counter_increment",
        "counter_reset",
        "cursor",
        "direction",
        "display",
        "empty_cells",
        "filter",
        "flex",
        "flex_basis",
        "flex_direction",
        "flex_flow",
        "flex_grow",
        "flex_shrink",
        "flex_wrap",
        "float",
        "font",
        "font_face",
        "font_family",
        "font_feature_settings",
        "font_feature_values",
        "font_kerning",
        "font_language_override",
        "font_size",
        "font_size_adjust",
        "font_stretch",
        "font_style",
        "font_synthesis",
        "font_variant",
        "font_variant_alternates",
        "font_variant_caps",
        "font_variant_east_asian",
        "font_variant_ligatures",
        "font_variant_numeric",
        "font_variant_position",
        "font_weight",
        "gap",
        "grid",
        "grid_area",
        "grid_auto_columns",
        "grid_auto_flow",
        "grid_auto_rows",
        "grid_column",
        "grid_column_end",
        "grid_column_gap",
        "grid_column_start",
        "grid_gap",
        "grid_row",
        "grid_row_end",
        "grid_row_gap",
        "grid_row_start",
        "grid_template",
        "grid_template_areas",
        "grid_template_columns",
        "grid_template_rows",
        "hanging_punctuation",
        "height",
        "hyphens",
        "image_rendering",
        "import_",
        "isolation",
        "justify_content",
        "keyframes",
        "left",
        "letter_spacing",
        "line_break",
        "line_height",
        "list_style",
        "list_style_image",
        "list_style_position",
        "list_style_type",
        "margin",
        "margin_bottom",
        "margin_left",
        "margin_right",
        "margin_top",
        "mask",
        "mask_clip",
        "mask_composite",
        "mask_image",
        "mask_mode",
        "mask_origin",
        "mask_position",
        "mask_repeat",
        "mask_size",
        "mask_type",
        "max_height",
        "max_width",
        "media",
        "min_height",
        "min_width",
        "mix_blend_mode",
        "object_fit",
        "object_position",
        "opacity",
        "order",
        "orphans",
        "outline",
        "outline_color",
        "outline_offset",
        "outline_style",
        "outline_width",
        "overflow",
        "overflow_wrap",
        "overflow_x",
        "overflow_y",
        "padding",
        "padding_bottom",
        "padding_left",
        "padding_right",
        "padding_top",
        "page_break_after",
        "page_break_before",
        "page_break_inside",
        "perspective",
        "perspective_origin",
        "pointer_events",
        "position",
        "quotes",
        "resize",
        "right",
        "row_gap",
        "scroll_behaviour",
        "tab_size",
        "table_layout",
        "text_align",
        "text_align_last",
        "text_combine_upright",
        "text_decoration",
        "text_decoration_color",
        "text_decoration_line",
        "text_decoration_style",
        "text_decoration_thickness",
        "text_emphasis",
        "text_indent",
        "text_justify",
        "text_orientation",
        "text_overflow",
        "text_shadow",
        "text_transform",
        "text_underline_position",
        "top",
        "transform",
        "transform_origin",
        "transform_style",
        "transition",
        "transition_delay",
        "transition_duration",
        "transition_property",
        "transition_timing_function",
        "unicode_bidi",
        "user_select",
        "vertical_align",
        "visibility",
        "white_space",
        "widows",
        "width",
        "word_break",
        "word_spacing",
        "word_wrap",
        "writing_mode",
        "z_index",
    )

    def inject_field(self, field: str, value: str) -> NoReturn:
        if not field in self.__fields:
            raise Exception("cannot inject value into non existing css field")

        self.__setattr__(field, value)
