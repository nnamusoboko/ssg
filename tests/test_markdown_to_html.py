import unittest

from src.markdown_to_html import markdown_to_html_node


class TestMarkdownToHtml(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading_levels(self):
        for level in range(1, 7):
            md = f"{'#' * level} Title"
            html = markdown_to_html_node(md).to_html()
            self.assertEqual(html, f"<div><h{level}>Title</h{level}></div>")

    def test_heading_with_inline_markdown(self):
        html = markdown_to_html_node("## A **bold** title").to_html()
        self.assertEqual(html, "<div><h2>A <b>bold</b> title</h2></div>")

    def test_quote(self):
        md = """
> first line
>second _line_
"""
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><blockquote>first line second <i>line</i></blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
- one
- **two**
- `three`
"""
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><ul><li>one</li><li><b>two</b></li><li><code>three</code></li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. one
2. _two_
3. three
"""
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><ol><li>one</li><li><i>two</i></li><li>three</li></ol></div>",
        )

    def test_mixed_document(self):
        md = """
# Title

Some [link](https://www.boot.dev) text

- item

1. first

> quoted

```
code
```
"""
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            '<div><h1>Title</h1><p>Some <a href="https://www.boot.dev">link</a> text</p>'
            "<ul><li>item</li></ul><ol><li>first</li></ol>"
            "<blockquote>quoted</blockquote><pre><code>code\n</code></pre></div>",
        )


if __name__ == "__main__":
    unittest.main()
