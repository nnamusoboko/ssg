# Static Site Generator

A small static site generator: write Markdown, get ready-to-serve HTML.

## Requirements

Python 3.13+

## Usage

```bash
./main.sh    # build and serve at http://localhost:8888
./build.sh   # build for deployment under /repo-name/
./test.sh    # run tests
```

- `main.sh` builds with basepath `/` 
- `build.sh` builds with `/repo-name/` for GitHub Pages.

## Structure

```
content/       Markdown sources (blog posts, homepage, etc.)
docs/          Generated site (build output)
src/           Generator logic
static/        Assets copied into the build
tests/         Test suite
template.html  Page shell with {{ Title }} and {{ Content }}
```

## Credit

Guided project from [boot.dev](https://www.boot.dev/courses/build-static-site-generator-python)
