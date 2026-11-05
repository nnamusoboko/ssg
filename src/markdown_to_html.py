from src.block_markdown import BlockType, block_to_block_type
from src.extract_words import markdown_to_blocks, text_to_textnodes
from src.htmlnode import HtmlNode, ParentNode
from src.textnode import TextNode, TextType, text_node_to_html_node


def markdown_to_html_node(markdown: str) -> ParentNode:
    children = [block_to_html_node(block) for block in markdown_to_blocks(markdown)]
    return ParentNode("div", children)


def block_to_html_node(block: str) -> ParentNode:
    match block_to_block_type(block):
        case BlockType.PARAGRAPH:
            return paragraph_to_html_node(block)
        case BlockType.HEADING:
            return heading_to_html_node(block)
        case BlockType.CODE:
            return code_to_html_node(block)
        case BlockType.QUOTE:
            return quote_to_html_node(block)
        case BlockType.UNORDERED_LIST:
            return unordered_list_to_html_node(block)
        case BlockType.ORDERED_LIST:
            return ordered_list_to_html_node(block)
        case _:
            raise ValueError("Unsupported block type")


def text_to_children(text: str) -> list[HtmlNode]:
    return [text_node_to_html_node(node) for node in text_to_textnodes(text)]


def paragraph_to_html_node(block: str) -> ParentNode:
    text = " ".join(block.split("\n"))
    return ParentNode("p", text_to_children(text))


def heading_to_html_node(block: str) -> ParentNode:
    level = len(block) - len(block.lstrip("#"))
    text = block[level + 1:]
    return ParentNode(f"h{level}", text_to_children(text))


def code_to_html_node(block: str) -> ParentNode:
    # Code is literal, so it skips inline markdown parsing.
    text = block[4:-3]
    code_child = text_node_to_html_node(TextNode(text, TextType.PLAIN_TEXT))
    return ParentNode("pre", [ParentNode("code", [code_child])])


def quote_to_html_node(block: str) -> ParentNode:
    lines = [line[1:].strip() for line in block.split("\n")]
    return ParentNode("blockquote", text_to_children(" ".join(lines)))


def unordered_list_to_html_node(block: str) -> ParentNode:
    items = [line[2:] for line in block.split("\n")]
    return ParentNode("ul", [ParentNode("li", text_to_children(item)) for item in items])


def ordered_list_to_html_node(block: str) -> ParentNode:
    items = [line.split(". ", 1)[1] for line in block.split("\n")]
    return ParentNode("ol", [ParentNode("li", text_to_children(item)) for item in items])
