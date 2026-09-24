#!/usr/bin/env python3
"""
Static blog generator and publisher for personal site.

Usage:
  pip install -r requirements.txt
  python3 publish.py

Reads markdown files from `content/posts/` and `content/journal.md`,
builds HTML files into `site/`, then publishes to repository root.
"""
import shutil
from datetime import datetime
from pathlib import Path

import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).parent
CONTENT_DIR = ROOT / 'content' / 'posts'
PROJECTS_DIR = ROOT / 'content' / 'projects'
TEMPLATES_DIR = ROOT / 'templates'
OUTPUT_DIR = ROOT / 'site'

# The whole tag vocabulary. One tag per post, and it has to be on this list.
# Keeping it short is the point: a tag that only ever lands on one post is a
# title, not a theme. Adding one is a deliberate edit here, not a typo in a post.
TAGS = ['Data Science', 'Games', 'Living Legends', 'Technology']


def fail(msg: str):
    print('ERROR:', msg)
    exit(1)


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
    """Generate HTML files from markdown sources."""
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(['html', 'xml']),
    )

    post_template = env.get_template('post.html')
    index_template = env.get_template('index.html')
    journal_template = env.get_template('journal.html')

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

        tag = meta.get('tag', '').strip()
        if not tag:
            fail(f'{md_file.name} has no "tag:" — one is required, from {TAGS}')
        if tag not in TAGS:
            fail(f'{md_file.name} has tag {tag!r}, which is not in {TAGS}')

        slug = meta.get('slug') or slugify(md_file.stem)
        output_path = OUTPUT_DIR / 'posts' / f"{slug}.html"

        rendered = post_template.render(title=title, date=date, content=html_body, tag=tag, base='../')
        output_path.write_text(rendered, encoding='utf-8')

        posts.append({
            'title': title,
            'date': date,
            'url': f'posts/{slug}.html',
            'summary': meta.get('summary', ''),
            'tag': tag,
        })

    # sort posts by date desc when available
    posts.sort(key=lambda p: p['date'] or datetime.min, reverse=True)

    # ---- projects: a write-up gets its own page, a bare entry just links out
    projects = []
    if PROJECTS_DIR.exists():
        (OUTPUT_DIR / 'projects').mkdir(parents=True, exist_ok=True)
        page_template = env.get_template('page.html')
        projects_template = env.get_template('projects.html')
        for md_file in sorted(PROJECTS_DIR.glob('*.md')):
            html_body, meta = read_markdown_file(md_file)
            title = meta.get('title') or md_file.stem
            slug = meta.get('slug') or slugify(md_file.stem)
            link = meta.get('link', '').strip()
            if html_body.strip():
                out = OUTPUT_DIR / 'projects' / f'{slug}.html'
                out.write_text(page_template.render(title=title, content=html_body, base='../'),
                               encoding='utf-8')
                url = f'projects/{slug}.html'
            elif link:
                url = link
            else:
                fail(f'{md_file.name} has neither a body nor a "link:"')
            try:
                order = int(meta.get('order', '99'))
            except ValueError:
                order = 99
            projects.append({'title': title, 'summary': meta.get('summary', ''),
                             'url': url, 'order': order})
        projects.sort(key=lambda p: (p['order'], p['title']))
        (OUTPUT_DIR / 'projects.html').write_text(
            projects_template.render(projects=projects), encoding='utf-8')
        print(f'Built {len(projects)} projects into {OUTPUT_DIR!s}')

    # tag counts for the index filter, in TAGS order, skipping the unused ones
    tag_counts = [(t, sum(1 for p in posts if p['tag'] == t)) for t in TAGS]
    tag_counts = [(t, n) for t, n in tag_counts if n]

    # render index
    index_html = index_template.render(posts=posts, tag_counts=tag_counts, base='')
    (OUTPUT_DIR / 'index.html').write_text(index_html, encoding='utf-8')

    # render journal if it exists
    journal_path = ROOT / 'content' / 'journal.md'
    if journal_path.exists():
        journal_html, _ = read_markdown_file(journal_path)
        rendered_journal = journal_template.render(content=journal_html, base='')
        (OUTPUT_DIR / 'journal.html').write_text(rendered_journal, encoding='utf-8')
        print(f'Built journal into {OUTPUT_DIR!s}/journal.html')

    print(f'Built {len(posts)} posts into {OUTPUT_DIR!s}')


def publish():
    """Copy generated site/ output to repository root."""
    if not OUTPUT_DIR.exists():
        fail('site/ directory not found — run build() first')

    src_index = OUTPUT_DIR / 'index.html'
    if not src_index.exists():
        fail('site/index.html not found')

    dest_index = ROOT / 'index.html'
    shutil.copy2(src_index, dest_index)
    print(f'Wrote {dest_index}')

    src_posts = OUTPUT_DIR / 'posts'
    dest_posts = ROOT / 'posts'
    if src_posts.exists():
        if dest_posts.exists():
            shutil.rmtree(dest_posts)
        shutil.copytree(src_posts, dest_posts)
        print(f'Copied posts to {dest_posts}')
    else:
        print('No posts/ found in site/, skipping posts copy')

    # projects index and the write-up pages
    src_projects_index = OUTPUT_DIR / 'projects.html'
    if src_projects_index.exists():
        shutil.copy2(src_projects_index, ROOT / 'projects.html')
        print(f"Wrote {ROOT / 'projects.html'}")
    src_projects = OUTPUT_DIR / 'projects'
    if src_projects.exists() and any(src_projects.iterdir()):
        dest_projects = ROOT / 'projects'
        if dest_projects.exists():
            shutil.rmtree(dest_projects)
        shutil.copytree(src_projects, dest_projects)
        print(f'Copied project pages to {dest_projects}')

    # copy journal if it exists
    src_journal = OUTPUT_DIR / 'journal.html'
    if src_journal.exists():
        dest_journal = ROOT / 'journal.html'
        shutil.copy2(src_journal, dest_journal)
        print(f'Wrote {dest_journal}')


if __name__ == '__main__':
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    TEMPLATES_DIR.mkdir(parents=True, exist_ok=True)
    build()
    publish()
