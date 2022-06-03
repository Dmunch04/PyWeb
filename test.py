from pyweb import pyweb


if __name__ == "__main__":
    color = pyweb.Color.from_hex("#fbafff")
    print(color.r)
    print(color.g)
    print(color.b)
    print(color.a)
    print(color.to_hex_string())

    page = pyweb.Page("index")

    page.add_text("MUNCHII", pyweb.Position(100, 100), text_type=pyweb.TextType.H1)
    page.add_linked_text("OTHER SITE", pyweb.Position(75, 75))
    page.add_button("CONTACT", pyweb.Position(50, 50))

    style = pyweb.CSSStyle("yeet")
    style.add_field("color", "black")
    print(str(style))

    page.write()
