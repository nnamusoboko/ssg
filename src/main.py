from src.textnode import TextNode, TextType
from src.htmlnode import HtmlNode, LeafNode
from utils.src_dest import src_dest
from pathlib import Path

def resolve_path() -> tuple[Path, Path]:
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent
    abs_src = project_root / "static"
    abs_dest = project_root / "public"

    return abs_src, abs_dest


def main() -> None:
   text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
   html_node = HtmlNode()
   leaf_node = LeafNode("p", "Hello, world!")

   src_dest(*resolve_path())

   print(text_node)
   print(html_node)
   print(leaf_node)


if __name__ == "__main__":
    main()
