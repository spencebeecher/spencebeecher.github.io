# spencebeecher.github.io

The personal site: a blog, a Projects page pointing at three small web apps, and the
generator that builds the blog from markdown.

## Build it

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt   # Markdown and Jinja2, nothing else
.venv/bin/python publish.py
```

`publish.py` reads `content/posts/*.md`, renders through `templates/`, writes
`site/`, then copies the result to the repository root, which is what both hosts
serve. Check it locally by opening `index.html` — every link is relative, so it
works straight off disk.

## Writing a post

A file in `content/posts/`, named `YYYY-MM-DD-slug.md`, starting with a
front-matter block:

```
---
title: New sprites for the Living Legends map
date: 2026-09-20
summary: One sentence, shown under the title on the index.
---
```

A project is a file in `content/projects/`. One with a body becomes its own
page at `projects/<slug>.html`; one with just a `link:` is a row on the Projects
page that points at the app. `projects.html` is generated from those same files,
so the list cannot drift from the pages.

**Links must stay relative** (`index.html`, `posts/x.html`, `../assets/…`),
because the site is served from more than one place.

## Deployment — two hosts, two mechanisms

| | |
|---|---|
| **spencebeecher.github.io** | GitHub Pages, from `master` at the repository root. Nothing to configure; a push deploys it |
| **spencebeecher.me** | Cloudflare Workers. It clones the repo, runs `pip install -r requirements.txt`, then deploys with wrangler, with the **assets directory set to the repository root** |

**`.assetsignore` is load-bearing for the Cloudflare half.** Because the assets
directory is the repo root, wrangler tries to upload `.git` along with the site,
and the pack file is larger than the 25 MiB per-asset limit, so the deploy
fails. That happened on 2026-09-21 and left spencebeecher.me a commit behind,
**showing the previous version with no error anywhere the browser could see it.**
If the two domains ever disagree again, read the Cloudflare build log before
anything else.
