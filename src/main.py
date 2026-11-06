from pathlib import Path

from src.htmlnode import HtmlNode, LeafNode
from src.textnode import TextNode, TextType
from utils.src_dest import src_dest
from src.generate_page import generate_page


def get_root() -> str:
    script_dir = Path(__file__).resolve().parent
    return str(script_dir.parent)

def main() -> None:
   src_path = Path(get_root() + "/static")
   dest_path = Path(get_root() + "/public")
   from_path = Path(get_root() + "/content/index.md")
   template_path = Path(get_root() + "/template.html")
   target_page_path = Path(str(dest_path) + "/index.html")

   src_dest(src_path, dest_path)
   generate_page(from_path, template_path, target_page_path)


if __name__ == "__main__":
    main()
