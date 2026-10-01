import re

from src.textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type is not TextType:
            new_nodes.append(node)
            continue

        text = node.text
        target_words = styled_words(text, delimiter)
        if len(target_words) <= 0:
            raise ValueError("Matching closing delimiter is not found")

        split_words = text.split(delimiter)
        for word in split_words:
            if word in target_words:
                new_nodes.append(TextNode(word, text_type))
            else:
                new_nodes.append(TextNode(word, TextType.PLAIN_TEXT))

    return new_nodes


def styled_words(text: str, delimiter: str) -> list[str]:
    d = re.escape(delimiter)
    return re.findall(rf"{d}([^{d}]+){d}", text)
