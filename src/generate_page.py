# from src.markdown_to_html import

def extract_title(markdown: str) -> str:
    lines = markdown.split("\n")
    for line in lines:
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()

    raise ValueError("No h1 header found in markdown document")

def generate_page(from_path, template_path, dest_path):
    pass
