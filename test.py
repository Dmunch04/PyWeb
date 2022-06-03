from pyweb import pyweb, css


if __name__ == "__main__":
    color = pyweb.Color.from_hex("#fbafff")
    print(color.r)
    print(color.g)
    print(color.b)
    print(color.a)
    print(color.to_hex_string())

    page = pyweb.Page("index")

    page.add_text("MUNCHII", pyweb.Position(100, 100), text_type=pyweb.TextType.H1, class_="yeet")
    page.add_linked_text("OTHER SITE", pyweb.Position(75, 75))
    page.add_button("CONTACT", pyweb.Position(50, 50))

    style = pyweb.CSSStyle("yeet")
    style.add_field(pyweb.CSSField("color", "black", pyweb.CSSFieldValueType.String))
    print(str(style))

    page.write()

    style2 = css.Style("div", css.StyleType.TAG)
    style2.accent_color = "rgb(1,1,1)"
    style2.align_content = css.ContentAlignment.CENTER

    anim = css.Animation("mymove", "5s", iteration_count=css.AnimationIterationCount.INFINITE)
    style2.animation = anim

    print(style2.get_str())
    print(style2.get_inline_str())
