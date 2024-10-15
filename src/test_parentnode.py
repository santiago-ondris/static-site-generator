from leafnode import LeafNode
from parentnode import ParentNode


def test_parent_node():
    # Nodo padre con hijos válidos
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
    assert node.to_html() == "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"

    # Prueba para verificar que se lanza ValueError sin etiqueta
    try:
        invalid_node = ParentNode(None, [LeafNode("b", "text")])
    except ValueError as e:
        assert str(e) == "El nodo padre debe tener una etiqueta."

    # Prueba para verificar que se lanza ValueError sin hijos
    try:
        invalid_node = ParentNode("div", [])
    except ValueError as e:
        assert str(e) == "El nodo padre debe tener al menos un hijo."