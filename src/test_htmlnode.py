import unittest
from src.htmlnode import HtmlNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        node1 = HtmlNode("a", "click me", [], {
            "href": "https://www.google.com",
            "target": "_blank"
        })

        target = ' href="https://www.google.com" target="_blank"'
        result = node1.props_to_html()

        self.assertEqual(result, target)

    def test_props_to_html_on_eq_props(self):
        node1 = HtmlNode("a", "click me", [], {
            "href": "https://www.google.com",
            "target": "_blank"
        })
        node2 = HtmlNode("a", "click me", [], {
            "href": "https://www.google.com",
            "target": "_blank"
        })
        node1_result = node1.props_to_html()
        node2_result = node2.props_to_html()

        self.assertEqual(node1_result, node2_result)

    def test_prop_to_html_with_empty_props(self):
        node = HtmlNode("a", "click me", [], {})

        result = node.props_to_html()
        self.assertEqual(result, "")


if __name__ == "__name__":
    unittest.main()
