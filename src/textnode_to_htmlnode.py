from enum import Enum
from leafnode import LeafNode 

# Define el enum TextType
class TextType(Enum):
    TEXT = 1
    BOLD = 2
    ITALIC = 3
    CODE = 4
    LINK = 5
    IMAGE = 6

def text_node_to_html_node(text_node):
    """
    Convierte un TextNode en un LeafNode basado en el tipo de TextType.

    :param text_node: El TextNode a convertir.
    :return: Un LeafNode correspondiente al tipo de TextType.
    """
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        if not text_node.url:
            raise ValueError("El enlace debe tener una URL.")
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        if not text_node.url:
            raise ValueError("La imagen debe tener una URL.")
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError("Tipo de TextNode no soportado.")