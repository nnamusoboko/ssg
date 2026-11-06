import os
from src.markdown_to_html import markdown_to_html_node


def extract_title(markdown: str) -> str:
    lines = markdown.split("\n")
    for line in lines:
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()

    raise ValueError("No h1 header found in markdown document")


def generate_pages_recursive(from_path, template_path, dest_path, base_path):
    check_paths(from_path, template_path)

    if os.path.isfile(from_path):
        generate_page(from_path, template_path, dest_path, base_path)
        return

    for file in os.listdir(from_path):
        source_path = os.path.join(from_path, file)
        destination_path = os.path.join(dest_path, file)
        generate_pages_recursive(source_path, template_path, destination_path, base_path)


def generate_page(from_path, template_path, dest_path, base_path) -> None:
    target_ext = ".html"
    base, ext = os.path.splitext(dest_path)
    dest_path = base + target_ext

    print(f"Generating page from [{from_path}]\n to [{dest_path}]\n using [{template_path}]")

    with open(from_path, "r", encoding="utf-8") as f:
        src_md_content = f.read()
    with open(template_path, "r", encoding="utf-8") as f:
        template_html_content = f.read()

    page: str = markdown_to_html_node(src_md_content).to_html()
    page_title = extract_title(src_md_content)

    final_html: str = template_html_content.replace("{{ Title }}", page_title).replace("{{ Content }}", page)
    final_html = final_html.replace('href="/', f'href="{base_path}').replace('src="/', f'src="{base_path}')
    write_to_dest(final_html, dest_path)


def write_to_dest(content: str, dest_path: str) -> None:
    dest_folder_path = os.path.dirname(dest_path)
    os.makedirs(dest_folder_path, exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(content)


def check_paths(*args) -> None:
    from_path, template_path = args

    if not os.path.exists(from_path):
        raise FileNotFoundError(f"{from_path} doesnt exist")

    if not os.path.exists(template_path):
        raise FileNotFoundError(f"{template_path} doesnt exist")
