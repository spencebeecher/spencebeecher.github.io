#!/usr/bin/env python3
"""
Copy generated `site/` output into repository root so `index.html` sits at repo root.

Usage:
  python3 publish_site_root.py

This will copy `site/index.html` -> `./index.html` and `site/posts/` -> `./posts/` (replacing existing `posts/`).
"""
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).parent
SITE = ROOT / 'site'


def fail(msg: str):
    print('ERROR:', msg)
    sys.exit(1)


def publish():
    if not SITE.exists():
        fail('site/ directory not found — run generate_blog_pages.py first')

    src_index = SITE / 'index.html'
    if not src_index.exists():
        fail('site/index.html not found')

    dest_index = ROOT / 'index.html'
    shutil.copy2(src_index, dest_index)
    print(f'Wrote {dest_index}')

    src_posts = SITE / 'posts'
    dest_posts = ROOT / 'posts'
    if src_posts.exists():
        if dest_posts.exists():
            shutil.rmtree(dest_posts)
        shutil.copytree(src_posts, dest_posts)
        print(f'Copied posts to {dest_posts}')
    else:
        print('No posts/ found in site/, skipping posts copy')


if __name__ == '__main__':
    publish()
