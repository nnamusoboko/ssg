
from src.extract_words import markdown_to_blocks

class TestMarkdown:
    def test_markdown_to_blocks(self):
        markdown = """
This is **bolded** paragraph

This is another paragraph with *italic* and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(markdown)
        assert blocks == [
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* and `code` here",
            "This is the same paragraph on a new line",
            "* This is a list",
            "* with items",
        ]
