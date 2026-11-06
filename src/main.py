import sys
from pathlib import Path

from src.copy_files import src_to_dest
from src.generate_page import generate_pages_recursive


def get_root() -> str:
    script_dir = Path(__file__).resolve().parent
    return str(script_dir.parent)


def main() -> None:
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    src_path = Path(get_root() + "/static")
    dest_path = Path(get_root() + "/docs")
    from_path = Path(get_root() + "/content")
    template_path = Path(get_root() + "/template.html")

    src_to_dest(src_path, dest_path)
    generate_pages_recursive(from_path, template_path, dest_path, basepath)


if __name__ == "__main__":
    main()
