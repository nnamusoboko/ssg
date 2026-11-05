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


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        original_text = node.text

        image_links = extract_markdown_images(original_text)
        if not image_links:
            new_nodes.append(node)
            continue

        for text, url in image_links:
            image_link_markdown = f"![{text}]({url})"
            sections = original_text.split(image_link_markdown, 1)

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.PLAIN_TEXT))

            new_nodes.append(TextNode(text, TextType.IMAGE, url))
            original_text = sections[1]

        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.PLAIN_TEXT))

    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        original_text = node.text

        link_links = extract_markdown_links(original_text)
        if not link_links:
            new_nodes.append(node)
            continue

        for text, url in link_links:
            link_link_markdown = f"[{text}]({url})"
            sections = original_text.split(link_link_markdown, 1)

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.PLAIN_TEXT))
            new_nodes.append(TextNode(text, TextType.LINK, url))
            original_text = sections[1]

        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.PLAIN_TEXT))
    return new_nodes


delimiter_map = {
    TextType.BOLD_TEXT: "**",
    TextType.ITALIC_TEXT: "_",
    TextType.CODE_TEXT: "`",
}

def text_to_textnodes(text: str) -> list[TextNode]:
    new_nodes = split_nodes_image([TextNode(text, TextType.PLAIN_TEXT)])
    new_nodes = split_nodes_link(new_nodes)
    for text_type, delimiter in delimiter_map.items():
        new_nodes = split_nodes_delimiter(new_nodes, delimiter, text_type)
    return new_nodes

def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    block_list = []
    for block in blocks:
        stripped = block.strip()
        if stripped:
            block_list.append(stripped)

    return block_list
