from src.textnode import TextNode, TextType
from src.htmlnode import HtmlNode, LeafNode

def main() -> None:
   text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
   html_node = HtmlNode()
   leaf_node = LeafNode("p", "Hello, world!")

   print(text_node)
   print(html_node)
   print(leaf_node)


if __name__ == "__main__":
    main()
