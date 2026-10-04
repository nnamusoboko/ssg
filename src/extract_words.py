import re

from src.textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        split_words = text.split(delimiter)

        if len(split_words) % 2 == 0:
            raise ValueError("Matching closing delimiter is not found")

        for index, word in enumerate(split_words):
            if not word:
                continue

            if index % 2 == 0:
                new_nodes.append(TextNode(word, TextType.PLAIN_TEXT))
            else:
                new_nodes.append(TextNode(word, text_type))

    return new_nodes


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    pattern = r"!\[(.*?)\]\((.*?)\)"
    return re.findall(pattern, text)

def extract_markdown_links(text: str) -> list[tuple[str, str]]:
   pattern = r"\[(.*?)\]\((.*?)\)"
   return re.findall(pattern, text)
