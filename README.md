# Static site generator

Generate a static website from markdown content

## Project Structure

```bash
├── content/      # Source Markdown files (.md) organized by page/category
│   ├── blog/     # blog posts 
│   └── index.md  # Homepage source markdown
├── docs/         # Final built static assets (.html, .css, images) served by GitHub Pages
├── src/          # Core SSG application logic
├── static/       # Raw static assets (images, stylesheets) compiled into build output
├── tests/        # Test suite verifying HTML parsing, text transformations, and nodes
├── template.html # Outer shell HTML layout injected with custom {{ Title }} and {{ Content }}
├── build.sh      # For deployment
└── main.sh       # for local development 
```

## How to use

Make the scripts executable

## Apperenciation

This is a guided project on [boot.dev](https://www.boot.dev/courses/build-static-site-generator-python)
