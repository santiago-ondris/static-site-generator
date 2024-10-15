from leafnode import LeafNode


def test_leaf_node():
    # Prueba con una etiqueta y atributos
    node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    assert node.to_html() == '<a href="https://www.google.com">Click me!</a>'

    # Prueba sin etiqueta
    text_node = LeafNode(None, "Raw text content")
    assert text_node.to_html() == "Raw text content"

    # Prueba para verificar que el ValueError se lanza cuando no hay valor
    try:
        invalid_node = LeafNode("p", None)
    except ValueError as e:
        assert str(e) == "El valor debe estar presente para un nodo hoja."