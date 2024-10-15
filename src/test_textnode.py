import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        node3 = TextNode("xGringo", "italic")
        node4 = TextNode("xViejo", "None")
        node5 = TextNode("None", "regular")
        self.assertEqual(node, node2)  # node and node2 are expected to be equal
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node, node4)
        self.assertNotEqual(node, node5)


if __name__ == "__main__":
    unittest.main()