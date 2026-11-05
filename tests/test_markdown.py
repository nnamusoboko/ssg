
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

    def test_markdown_to_blocks_excess_newlines(self):
        md = "\n\n\nfirst\n\n\n\n\nsecond\n\n\n"
        self.assertEqual(markdown_to_blocks(md), ["first", "second"])

    def test_markdown_to_blocks_whitespace_only_block(self):
        md = "first\n\n   \n\nsecond"
        self.assertEqual(markdown_to_blocks(md), ["first", "second"])

    def test_markdown_to_blocks_empty_document(self):
        self.assertEqual(markdown_to_blocks(""), [])

    def test_block_markdown_heading(self):
        self.assertEqual(block_to_block_type("# Hello"), BlockType.HEADING)

    def test_block_markdown_heading_levels(self):
        for level in range(1, 7):
            block = f"{'#' * level} Hello"
            self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_block_markdown_seven_hashes_is_paragraph(self):
        self.assertEqual(block_to_block_type("####### Hello"), BlockType.PARAGRAPH)

    def test_block_markdown_heading_without_space_is_paragraph(self):
        self.assertEqual(block_to_block_type("#Hello"), BlockType.PARAGRAPH)

    def test_block_markdown_code(self):
        self.assertEqual(block_to_block_type("```\nhello\n```"), BlockType.CODE)

    def test_block_markdown_code_without_newline_is_paragraph(self):
        self.assertEqual(block_to_block_type("```hello```"), BlockType.PARAGRAPH)

    def test_block_markdown_code_unclosed_is_paragraph(self):
        self.assertEqual(block_to_block_type("```\nhello"), BlockType.PARAGRAPH)

    def test_block_markdown_quote(self):
        self.assertEqual(block_to_block_type("> Hello"), BlockType.QUOTE)

    def test_block_markdown_quote_without_space(self):
        self.assertEqual(block_to_block_type(">Hello"), BlockType.QUOTE)

    def test_block_markdown_quote_multiline(self):
        self.assertEqual(block_to_block_type("> one\n>two"), BlockType.QUOTE)

    def test_block_markdown_quote_with_bad_line_is_paragraph(self):
        self.assertEqual(block_to_block_type("> one\ntwo"), BlockType.PARAGRAPH)

    def test_block_markdown_unordered_list(self):
        result = block_to_block_type("- Hello\n- hello2")
        self.assertEqual(result, BlockType.UNORDERED_LIST)

    def test_block_markdown_unordered_list_with_bad_line_is_paragraph(self):
        self.assertEqual(block_to_block_type("- one\ntwo"), BlockType.PARAGRAPH)

    def test_block_markdown_unordered_list_without_space_is_paragraph(self):
        self.assertEqual(block_to_block_type("-one"), BlockType.PARAGRAPH)

    def test_block_markdown_ordered_list(self):
        result = block_to_block_type("1. hello\n2. hello2")
        self.assertEqual(result, BlockType.ORDERED_LIST)

    def test_block_markdown_ordered_list_not_starting_at_one_is_paragraph(self):
        self.assertEqual(block_to_block_type("2. one\n3. two"), BlockType.PARAGRAPH)

    def test_block_markdown_ordered_list_skipping_number_is_paragraph(self):
        self.assertEqual(block_to_block_type("1. one\n3. two"), BlockType.PARAGRAPH)

    def test_block_markdown_paragraph(self):
        self.assertEqual(block_to_block_type("Just some text"), BlockType.PARAGRAPH)
