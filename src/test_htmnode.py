import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_props(self):
        """
        Prueba que los atributos HTML se conviertan correctamente en una cadena 
        cuando el nodo tiene atributos.
        """
        node = HTMLNode("a", "", None, {"href": "https://www.google.com", "target": "_blank"})
        # Verifica que los atributos se formateen correctamente
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_props_to_html_without_props(self):
        """
        Verifica que los atributos HTML se conviertan en una cadena vacía 
        cuando no hay atributos.
        """
        node = HTMLNode("p", "", None, {})
        # Espera una cadena vacía ya que no hay atributos
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        """
        Prueba que `__repr__` devuelva una representación precisa del nodo HTML.
        """
        node = HTMLNode("a", "Click me!", None, {"href": "https://www.example.com"})
        expected = 'HTMLNode(tag=a, value=Click me!, children=None, props={\'href\': \'https://www.example.com\'})'
        # Compara la salida de __repr__ con la representación esperada
        self.assertEqual(repr(node), expected)

if __name__ == '__main__':
    unittest.main()

