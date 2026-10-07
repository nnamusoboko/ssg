import unittest

from src.extract_words import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)
from src.textnode import TextNode, TextType, text_node_to_html_node


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

    def test_split_styled_text_contains_code_text(self):
        node = TextNode("I love `building` toy projects", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        actual_types = [node.text_type for node in new_nodes]

        self.assertIn(TextType.CODE_TEXT, actual_types)


class TestLinkAndImageExtract(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "![alt text](image.jpg)"
        images = extract_markdown_images(text)
        self.assertEqual(images, [("alt text", "image.jpg")])

    def test_extract_markdown_links(self):
        text = "[alt text](link.com)"
        links = extract_markdown_links(text)
        self.assertEqual(links, [("alt text", "link.com")])

    def test_split_nodes_image(self):
        node = TextNode("![alt text](image.jpg)", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_image([node])
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text_type, TextType.IMAGE)
        self.assertEqual(new_nodes[0].text, "alt text")
        self.assertEqual(new_nodes[0].url, "image.jpg")

    def test_split_nodes_image_with_mixed_text(self):
        node = TextNode(
            "This is text with images ![personal mascot](./mascot.jpeg) and ![image2](./assets/image2.jpeg)",
            TextType.PLAIN_TEXT
        )
        new_nodes = split_nodes_image([node])
        expected_nodes = [
            TextNode("This is text with images ", TextType.PLAIN_TEXT),
            TextNode("personal mascot", TextType.IMAGE, "./mascot.jpeg"),
            TextNode(" and ", TextType.PLAIN_TEXT),
            TextNode("image2", TextType.IMAGE, "./assets/image2.jpeg")
        ]

        self.assertEqual(len(new_nodes), len(expected_nodes))
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_link(self):
        node = TextNode("[alt text](link.com)", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_link([node])
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text_type, TextType.LINK)
        self.assertEqual(new_nodes[0].text, "alt text")
        self.assertEqual(new_nodes[0].url, "link.com")

    def test_split_nodes_link_with_mixed_text(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.PLAIN_TEXT
        )
        new_nodes = split_nodes_link([node])
        expected_nodes = [
            TextNode("This is text with a link ", TextType.PLAIN_TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.PLAIN_TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
        ]

        self.assertEqual(len(new_nodes), len(expected_nodes))
        self.assertEqual(new_nodes, expected_nodes)


class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **bold** and _italic_ and `code`"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 6)
        self.assertEqual(nodes[0].text_type, TextType.PLAIN_TEXT)
        self.assertEqual(nodes[1].text_type, TextType.BOLD_TEXT)
        self.assertEqual(nodes[2].text_type, TextType.PLAIN_TEXT)
        self.assertEqual(nodes[3].text_type, TextType.ITALIC_TEXT)
        self.assertEqual(nodes[4].text_type, TextType.PLAIN_TEXT)


if  __name__ == "__main__":
    unittest.main()
