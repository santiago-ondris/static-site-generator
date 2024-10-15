from textnode import TextNode
from textnode_to_htmlnode import TextType, text_node_to_html_node


def test_text_node_to_html_node():
    # Esto probará todo el rango de TextType con ejemplos básicos
    text_node = TextNode("Este es un texto simple", TextType.TEXT)
    assert text_node_to_html_node(text_node).to_html() == "Este es un texto simple"

    bold_node = TextNode("Bold text", TextType.BOLD)
    assert text_node_to_html_node(bold_node).to_html() == "<b>Bold text</b>"

    italic_node = TextNode("Italic text", TextType.ITALIC)
    assert text_node_to_html_node(italic_node).to_html() == "<i>Italic text</i>"

    code_node = TextNode("Code snippet", TextType.CODE)
    assert text_node_to_html_node(code_node).to_html() == "<code>Code snippet</code>"

    link_node = TextNode("Google", TextType.LINK, url="https://www.google.com")
    assert text_node_to_html_node(link_node).to_html() == '<a href="https://www.google.com">Google</a>'

    image_node = TextNode("Example Image", TextType.IMAGE, url="https://example.com/image.png")
    assert text_node_to_html_node(image_node).to_html() == '<img src="https://example.com/image.png" alt="Example Image"/>'

    # Prueba para un tipo no soportado
    try:
        unsupported_node = TextNode("Unsupported text", None)
        text_node_to_html_node(unsupported_node)
    except ValueError as e:
        assert str(e) == "Tipo de TextNode no soportado."