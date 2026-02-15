# Personal static blog (generator)

This repository now contains a small static blog generator that converts markdown posts into a static `site/` directory suitable for GitHub Pages or other static hosts.

Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 generate_blog_pages.py
```

Output will be in `site/`. Serve locally to check:

```bash
python3 -m http.server --directory site 8000
# then open http://localhost:8000
```

Write posts as markdown files in `content/posts/`. Include optional metadata using the Markdown `meta` extension, for example:

```
Title: Hello
Date: 2026-02-15

Your markdown content here
```

Deployment

- Configure GitHub Pages to serve the repository's `site/` folder, or copy `site/` contents to the branch GitHub Pages serves (e.g., `gh-pages`).
