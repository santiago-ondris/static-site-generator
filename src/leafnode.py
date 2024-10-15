from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        """
        Inicializa un nuevo nodo hoja HTML.

        :param tag: La etiqueta HTML (por ejemplo, 'p', 'a'). Puede ser None.
        :param value: El contenido del nodo HTML, debe ser proporcionado.
        :param props: Un diccionario de atributos HTML (por ejemplo, {'href': 'url'}). Opcional.
        """
        if value is None:
            raise ValueError("El valor debe estar presente para un nodo hoja.")
        
        # Debemos asegurarnos de no tener hijos, por lo que pasamos una lista vacía
        super().__init__(tag, value, children=None, props=props)

    def to_html(self):
        """
        Renderiza el nodo leaf como una cadena HTML.
        
        :return: Una cadena HTML que representa el nodo.
        :raise ValueError: Si el valor está ausente.
        """
        if self.value is None:
            raise ValueError("El nodo hoja no tiene un valor.")

        # Si no hay etiqueta, retornamos solo el valor como texto plano
        if self.tag is None:
            return self.value
        
        # Usamos props_to_html de HTMLNode para manejar atributos
        props_html = self.props_to_html()
        
        # Retornamos la etiqueta HTML con el valor encapsulado
        return f'<{self.tag}{props_html}>{self.value}</{self.tag}>'