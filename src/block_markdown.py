from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    if block.startswith("# "):
        return BlockType.HEADING
    if block.startswith("```"):
        return BlockType.CODE
    if block.startswith(">") or block.startswith("> "):
        return BlockType.QUOTE
    if block.startswith("- "):
        return BlockType.UNORDERED_LIST
    if is_ordered_list(block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def is_ordered_list(block: str) -> bool:
    lines: list[str] = block.split("\n")
    for expected_num, line in enumerate(lines, start=1):
        if not line.startswith(f"{expected_num}. "):
            return False
    return True
