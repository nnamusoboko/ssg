import unittest

from src.textnode import TextNode, TextType, text_node_to_html_node
from src.extract_words import split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)

        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)

        self.assertNotEqual(node, node2)

    def test_not_eq_with_url(self):
        node1 = TextNode("This is a text node", TextType.BOLD_TEXT, None)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT, "https://image.com/image1")

        self.assertNotEqual(node1, node2)


class TestTextNodeToHtml(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        text_node = TextNode("This is an image", TextType.IMAGE, "https://image.com/image1")
        html_node = text_node_to_html_node(text_node)

        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://image.com/image1", "alt": "This is an image"}
        )


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_plain_text(self):
        node = TextNode("My name is **Nelson** and i love programming", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        actual_types = [node.text_type for node in new_nodes]

        expected_nodes = [
            TextNode("My name is ", TextType.PLAIN_TEXT, None),
            TextNode("Nelson", TextType.BOLD_TEXT, None),
            TextNode(" and i love programming", TextType.PLAIN_TEXT, None)
        ]

        self.assertEqual(new_nodes, expected_nodes)
        self.assertIn(TextType.BOLD_TEXT, actual_types)

    def test_split_styled_text_contains_bold_text(self):
        node = TextNode("I love **building** toy projects", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        actual_types = [node.text_type for node in new_nodes]

        self.assertIn(TextType.BOLD_TEXT, actual_types)

    def test_split_styled_text_contains_multiple_bold_text(self):
        node = TextNode("I love **building** toy **projects**", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)

        expected_nodes = [
            TextNode("I love ", TextType.PLAIN_TEXT, None),
            TextNode("building", TextType.BOLD_TEXT, None),
            TextNode(" toy ", TextType.PLAIN_TEXT, None),
            TextNode("projects", TextType.BOLD_TEXT, None),
        ]

        self.assertEqual(new_nodes, expected_nodes)

    def test_split_styled_text_contains_italic_text(self):
        node = TextNode("I love _building_ toy projects", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)
        actual_types = [node.text_type for node in new_nodes]

        self.assertIn(TextType.ITALIC_TEXT, actual_types)


    if  __name__ == "__main__":
        unittest.main()
