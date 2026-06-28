# spencebeecher.github.io — TODO

## What this is
Spencer Beecher's personal website, served by GitHub Pages from the repo root on the `master` branch (https://spencebeecher.github.io). It's a small static-site generator: `publish.py` converts markdown in `content/posts/*.md` and `content/journal.md` into HTML via Jinja2 templates in `templates/`, writes to `site/`, then copies the output (`index.html`, `posts/`, `journal.html`) to the repo root. It also hosts a standalone bingo-card generator under `/bingo/`. Visitor entry point is `index.html`; build entry point is `publish.py`.

## Current state
Active and working. Last commit is "Publish March 8 journal entry" (combining the two old build scripts into `publish.py` was done just before). There is one blog post (`content/posts/2026-02-15-books-that-helped-my-career.md`) plus an ongoing journal.
- Uncommitted change: an "April 25, 2026" entry has been appended to `content/journal.md` but the site has NOT been rebuilt/published — `journal.html` still reflects March 8.
- Stale docs: `README.md` and `CONTEXT.md` still reference the old script names `generate_blog_pages.py` and `publish_site_root.py`, which no longer exist (replaced by `publish.py`).
- `venv/` exists locally for the Jinja2 + Markdown deps.

## Pick back up here
- [ ] Run `python3 publish.py` to regenerate `journal.html` (and index/posts) with the April 25 journal entry, then `git add -A && git commit && git push origin master`.
- [ ] Update `README.md` and `CONTEXT.md` to reference `publish.py` (single command) instead of the removed `generate_blog_pages.py` / `publish_site_root.py`.
- [ ] (Optional) Draft a new blog post from `blog-ideas.txt` (e.g. "Simplify simplify simplify") in `content/posts/` and publish.

## Key files
- `publish.py` — static-site generator + publisher (build + copy to repo root).
- `content/journal.md` — source for the continuous journal page (has unpublished edits).
- `content/posts/*.md` — markdown sources for blog posts.
- `templates/` — Jinja2 templates: `index.html`, `post.html`, `page.html`, `journal.html`.
- `index.html` / `journal.html` / `posts/` — generated output deployed at repo root.
- `bingo/` — standalone bingo-card generator (`generate_pages.py`, templates, images).
- `CONTEXT.md` — project conventions and "publish" workflow notes (currently stale).
