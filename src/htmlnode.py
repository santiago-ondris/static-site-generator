class HTMLNode:
    def __init__(self, tag, value, children, props):
        """
        Inicializa un nuevo nodo HTML.

        :param tag: La etiqueta HTML (por ejemplo, 'div', 'a').
        :param value: El contenido del nodo HTML (puede ser texto dentro del nodo).
        :param children: Una lista de nodos hijos. Puede ser None si no hay hijos.
        :param props: Un diccionario de atributos HTML (por ejemplo, {'href': 'url'}).
        """
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        """
        Método abstracto, debe ser implementado para generar la representación HTML del nodo.
        """
        raise NotImplementedError    

    def props_to_html(self):
        """
        Convierte los atributos del nodo en una cadena HTML.

        :return: Una cadena de atributos formateados para HTML.
        """
        if not self.props:
            return ""
        # Convierte cada par clave-valor en la forma ' key="value"'
        return ''.join(f' {key}="{value}"' for key, value in self.props.items())
    
    def __repr__(self):
        """
        Devuelve una representación en cadena del nodo HTML, útil para depuración.

        :return: Una representación de cadena del nodo con sus atributos.
        """
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
