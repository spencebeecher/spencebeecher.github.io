#!/usr/bin/env python3
"""
Static blog generator for personal site.

Usage:
  pip install -r requirements.txt
  python3 generate_blog_pages.py

Reads markdown files from `content/posts/` and writes HTML files to `site/`.
Designed for GitHub Pages self-hosting: push `site/` contents to `gh-pages` or configure GitHub Pages to serve from `site/` if desired.
"""
import os
import shutil
from datetime import datetime
from pathlib import Path

import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).parent
CONTENT_DIR = ROOT / 'content' / 'posts'
TEMPLATES_DIR = ROOT / 'templates'
OUTPUT_DIR = ROOT / 'site'


def slugify(name: str) -> str:
    name = name.strip().lower()
    for ch in ' _':
        name = name.replace(ch, '-')
    # keep alphanum and -
    return ''.join(c for c in name if c.isalnum() or c == '-')


def read_markdown_file(path: Path):
    text = path.read_text(encoding='utf-8')
    md = markdown.Markdown(extensions=['meta', 'fenced_code', 'codehilite', 'tables'])
    html = md.convert(text)
    meta = {}
    if hasattr(md, 'Meta'):
        # md.Meta values are lists
        meta = {k: ' '.join(v) for k, v in md.Meta.items()}
    return html, meta


def build():
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(['html', 'xml']),
    )

    post_template = env.get_template('post.html')
    index_template = env.get_template('index.html')

    # prepare output
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    (OUTPUT_DIR / 'posts').mkdir(parents=True, exist_ok=True)

    posts = []
    for md_file in sorted(CONTENT_DIR.glob('*.md')):
        html_body, meta = read_markdown_file(md_file)
        title = meta.get('title') or md_file.stem
        date_str = meta.get('date')
        try:
            date = datetime.fromisoformat(date_str) if date_str else None
        except Exception:
            date = None

        slug = meta.get('slug') or slugify(md_file.stem)
        output_path = OUTPUT_DIR / 'posts' / f"{slug}.html"

        rendered = post_template.render(title=title, date=date, content=html_body)
        output_path.write_text(rendered, encoding='utf-8')

        posts.append({
            'title': title,
            'date': date,
            'url': f'posts/{slug}.html',
            'summary': meta.get('summary', '')
        })

    # sort posts by date desc when available
    posts.sort(key=lambda p: p['date'] or datetime.min, reverse=True)

    # render index
    index_html = index_template.render(posts=posts)
    (OUTPUT_DIR / 'index.html').write_text(index_html, encoding='utf-8')

    print(f'Built {len(posts)} posts into {OUTPUT_DIR!s}')


if __name__ == '__main__':
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    TEMPLATES_DIR.mkdir(parents=True, exist_ok=True)
    build()
