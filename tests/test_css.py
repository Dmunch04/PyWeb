from pyweb.css import *


def test_css_color():
    print(Color.ALICE_BLUE.values)
    print(str(Length(7, RelativeLengthUnit.REM)))
    print(str(Time(5, TimeUnit.MILLISECONDS)))
    print(str(Angle(180, AngleUnit.DEG)))

    style = Style("boobs", StyleType.CLASS)
    style.background_image = URL("billed.png")
    style.align_content = ContentAlignment.CENTER
    style.backface_visibility = BackfaceVisibility.HIDDEN

    print(GradientConic([
        ColorDegree(Color.named("red")),
        ColorDegree(Color.named("yellow")),
        ColorDegree(Color.named("rebeccapurple"))],
        Angle(90, AngleUnit.DEG),
        StartingPoint(Angle(60, AngleUnit.DEG), Angle(45, AngleUnit.DEG))
    ))

    print(GradientLinear([
        ColorStop(Color.named("red")),
        ColorHint(10),
        ColorStop(Color.named("blue"))],
        Angle(.25, AngleUnit.TURN)
    ))

    print(GradientLinear([
        ColorStop(Color.named("red"), 0, Length(50, RelativeLengthUnit.PERCENT)),
        ColorStop(Color.named("blue"), Length(50, RelativeLengthUnit.PERCENT), Length(100, RelativeLengthUnit.PERCENT))],
        Angle(45, AngleUnit.DEG)
    ))

    print(GradientLinear([
        ColorStop(Color.named("blue")),
        ColorStop(Color.named("red"))],
        StartingPoint(HorizontalStartingPoint.LEFT, VerticalStartingPoint.TOP)
    ))
