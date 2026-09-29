import unittest

from src.htmlnode import LeafNode, ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_nested_parents(self):
        grand_grand_child_node = LeafNode(tag="span", value="child")
        grandchild_node = ParentNode(tag="b", children=[grand_grand_child_node])
        child_node = ParentNode(tag="p", children=[grandchild_node])
        parent_node = ParentNode(tag="div", children=[child_node])

        self.assertEqual(
            parent_node.to_html(),
            "<div><p><b><span>child</span></b></p></div>"
        )

    def test_to_html_with_props_attached_to_nodes(self):
        grand_grand_child_node = LeafNode(tag="span", value="child")
        grandchild_node = ParentNode(
            tag="b",
            children=[grand_grand_child_node],
            props={
                "class": "grand-child"
            }
        )
        child_node = ParentNode(tag="p", children=[grandchild_node])
        parent_node = ParentNode(
            tag="div",
            children=[child_node],
            props={"id": "intro-section", "class": "hero-wrapper", "data-author": "ghost"}
        )

        expected_html_str = (
            '<div id="intro-section" class="hero-wrapper" data-author="ghost">'
            '<p><b class="grand-child"><span>child</span></b></p>'
            '</div>'
        )

        self.assertEqual(
            parent_node.to_html(),
            expected_html_str
        )
