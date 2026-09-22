# spencebeecher.github.io

The personal site: a blog, a Misc page pointing at three small web apps, and the
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
tag: Living Legends
date: 2026-09-20
summary: One sentence, shown under the title on the index.
---
```

**Every post needs exactly one `tag`, and it has to be one of the three in
`TAGS` in `publish.py`:** Data Science, Living Legends, Technology. The build
fails on a missing tag or an unknown one, which is deliberate — a tag that lands
on one post is a title, not a theme. Adding a fourth is an edit to that list.

The index carries the filter: a pill per tag with counts, a search box over
title, summary and tag, and `?tag=` in the URL so a tag chip is a shareable
link. It is plain JavaScript inside the template, with no dependencies.

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
