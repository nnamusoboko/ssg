
import unittest

from src.block_markdown import BlockType, block_to_block_type
from src.extract_words import markdown_to_blocks


class TestMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_markdown_heading(self):
        self.assertEqual(block_to_block_type("# Hello"), BlockType.HEADING)

    def test_block_markdown_code(self):
        self.assertEqual(block_to_block_type("```hello```"), BlockType.CODE)

    def test_block_markdown_quote(self):
        self.assertEqual(block_to_block_type("> Hello"), BlockType.QUOTE)

    def test_block_markdown_quote_without_space(self):
        self.assertEqual(block_to_block_type(">Hello"), BlockType.QUOTE)

    def test_block_markdown_unordered_list(self):
        result = block_to_block_type(
            """- Hello
            - hello2
            """
        )
        self.assertEqual(result, BlockType.UNORDERED_LIST)

    def test_block_markdown_ordered_list(self):
        result = block_to_block_type("1. hello\n2. hello2")
        self.assertEqual(result, BlockType.ORDERED_LIST)
