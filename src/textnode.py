from enum import Enum

from src.htmlnode import LeafNode


class TextType(Enum):
    PLAIN_TEXT = "plain"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: object, /) -> bool:
        if not isinstance(other, TextNode):
            return False

        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    leaf_node: LeafNode

    match text_node.text_type:
        case TextType.PLAIN_TEXT:
            leaf_node = LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD_TEXT:
            leaf_node = LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC_TEXT:
            leaf_node = LeafNode(tag="i", value=text_node.text)
        case TextType.CODE_TEXT:
            leaf_node = LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            if text_node.url is None:
                raise ValueError("Link node has no url")
            leaf_node = LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
        case TextType.IMAGE:
            if text_node.url is None:
                raise ValueError("Image node has no url")
            leaf_node = LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError("Unsupported text node type")

    return leaf_node
