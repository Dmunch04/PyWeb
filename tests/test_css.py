from pyweb.css import Color, Length, RelativeLengthUnit


def test_css_color():
    print(Color.ALICE_BLUE.values)
    print(str(Length(7, RelativeLengthUnit.REM)))
