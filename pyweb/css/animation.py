from typing import Union, Optional

from pyweb.css.style import (
    BaseProperty,
    AnimationName,
    AnimationTimingFunction,
    AnimationIterationCount,
    AnimationDirection,
    AnimationFillMode,
    AnimationPlayState,
)
from pyweb.css.unit import Time


class CSSAnimation(object):
    @classmethod
    @property
    def value(self) -> str:
        return self.__str__()


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

    def __init__(
        self,
        a: Union[float, int],
        b: Union[float, int],
        c: Union[float, int],
        d: Union[float, int],
    ):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self) -> str:
        return f"cubic-bezier({str(self.a)},{self.b},{self.c},{self.d})"


class Animation(object):
    __slots__ = (
        "name",
        "duration",
        "timing_function",
        "delay",
        "iteration_count",
        "direction",
        "fill_mode",
        "play_state",
    )

    def __init__(
        self,
        name: Optional[Union[AnimationName, str]] = None,
        duration: Optional[Union[BaseProperty, Time]] = "1s",
        timing_function: Optional[Union[AnimationTimingFunction, CSSAnimation]] = None,
        delay: Optional[Union[BaseProperty, Time]] = None,
        iteration_count: Optional[Union[AnimationIterationCount, str]] = None,
        direction: Optional[AnimationDirection] = None,
        fill_mode: Optional[AnimationFillMode] = None,
        play_state: Optional[AnimationPlayState] = None,
    ):
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
