from enum import Enum


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


class BackgroundOrigin(Enum):
    PADDING_BOX = "padding-box"
    BORDER_BOX = "border-box"
    CONTENT_BOX = "content-box"
    INITIAL = "initial"
    INHERIT = "inherit"


class BackgroundRepeat(Enum):
    REPEAT = "repeat"
    REPEAT_X = "repeat-x"
    REPEAT_Y = "repeat-y"
    NO_REPEAT = "no-repeat"
    SPACE = "space"
    ROUND = "round"
    INITIAL = "initial"
    INHERIT = "inherit"


class BackgroundSize(Enum):
    AUTO = "auto"
    COVER = "cover"
    CONTAIN = "contain"
    INITIAL = "initial"
    INHERIT = "inherit"
