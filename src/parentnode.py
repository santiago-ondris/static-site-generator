from htmlnode import HTMLNode
from leafnode import LeafNode  

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        """
        Inicializa un nuevo nodo padre HTML.

        :param tag: La etiqueta HTML (por ejemplo, 'div', 'p'). No puede ser None.
        :param children: Lista de nodos hijos, al menos debe tener un elemento.
        :param props: Un diccionario de atributos HTML (por ejemplo, {'class': 'my-class'}). Opcional.
        """
        if tag is None:
            raise ValueError("El nodo padre debe tener una etiqueta.")

        if not children or len(children) == 0:
            raise ValueError("El nodo padre debe tener al menos un hijo.")
        
        # Dado que no necesitamos un valor para ParentNode, le pasamos None
        super().__init__(tag, value=None, children=children, props=props)

    def to_html(self):
        """
        Renderiza el nodo padre y sus hijos como una cadena HTML.

        :return: Una cadena HTML que representa el nodo y sus hijos.
        :raise ValueError: Si no hay una etiqueta o hijos.
        """
        if not self.children:
            raise ValueError("El nodo padre debe tener al menos un hijo.")
        
        # Generar HTML para cada hijo y concatenar
        children_html = ''.join(child.to_html() for child in self.children)
        
        # Usamos props_to_html de HTMLNode para manejar atributos
        props_html = self.props_to_html()
        
        return f'<{self.tag}{props_html}>{children_html}</{self.tag}>'