from src.htmlnode import HtmlNode
from src.block_markdown import block_to_block_type, BlockType
from src.extract_words import (
    markdown_to_blocks,
)

def markdown_to_html(markdown: str) -> list[HtmlNode]:
    markdown_blocks = markdown_to_blocks(markdown)
    html_nodes = []

    for block in markdown_blocks:
        if block_to_block_type(block) == BlockType.HEADING:
            pass



def text_to_children(text: str) -> list[HTMLNode]:
    # 1. Convert text to inline TextNode objects
    text_nodes = text_to_textnodes(text)

    # 2. Map each TextNode to an HTMLNode (LeafNode) using text_node_to_html_node
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)

    return children
