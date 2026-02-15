# Project Context & Conventions

**⚠️ IMPORTANT: Keep this file updated as the project evolves. When significant changes are made to workflows, structure, or conventions, update this file accordingly.**

## Project Overview

This is Spencer Beecher's personal website hosted at https://spencebeecher.github.io (GitHub Pages).

**Repository Structure:**
- `/bingo/` - Standalone bingo game generator (previously the entire repo, now a sub-page)
- `/content/posts/` - Markdown files for blog posts
- `/templates/` - Jinja2 templates (index.html, post.html, page.html)
- `/site/` - Generated intermediate output directory (not deployed to root)
- `/posts/` - Generated blog post HTML files (deployed to repo root)
- `/assets/` - Static assets (images, PDFs, etc.)
- `index.html` - Generated blog index (deployed to repo root)
- `about.html` - Static about page
- `misc.html` - Static misc/projects page
- `generate_blog_pages.py` - Converts markdown posts to HTML
- `publish_site_root.py` - Copies generated site/ files to repo root
- `blog-ideas.txt` - Future blog post topics

## Common Workflows

### "publish" Command
When the user says "publish", execute this sequence:
```bash
python3 generate_blog_pages.py && python3 publish_site_root.py && git add -A && git commit -m "<descriptive message>" && git push origin master
```

This:
1. Generates HTML from markdown posts into `site/`
2. Copies `site/index.html` and `site/posts/` to repo root
3. Commits all changes
4. Pushes to GitHub (triggers GitHub Pages deployment)

### Adding a Blog Post
1. Create markdown file in `content/posts/` with format: `YYYY-MM-DD-slug.md`
2. Include YAML frontmatter: `title`, `date`, `summary`
3. Run "publish" workflow

### Editing Static Pages
- `about.html`, `misc.html` are static HTML files in repo root
- Edit directly, then commit and push
- Use the same nav bar and styling conventions

## Code Conventions

### Styling
- **Font**: Helvetica (specified as `Helvetica, "Helvetica Neue", Arial, sans-serif`)
- **Nav bar**: Contains "Blog" (home), "Misc", "About"
- **Logo**: "Spencer Beecher" (links to home)
- Templates use consistent color scheme: #0066cc for links, #eee borders, #888 for meta text

### File Paths
- Blog posts link to `/posts/<slug>.html`
- Assets stored in `/assets/`
- Bingo games live at `/bingo/` with their own index

### Bingo Specifics
- Bingo games use `bingo_template.html` and `generate_pages.py` inside `/bingo/`
- "Games" button links to `index.html` within bingo folder
- Share URLs include `/bingo/` prefix

## Personal Details (for About page, etc.)

- **Name**: J. Spencer Beecher (goes by Spencer Beecher)
- **Current Role**: Data scientist at Meta, works on ads
- **Education**: MS in Computer Science (Johns Hopkins), BS in Computer Engineering (University of Maryland)
- **LinkedIn**: https://www.linkedin.com/in/spencer-beecher-9986b712/
- **GitHub**: https://github.com/spencebeecher
- **Profile Photo**: `/assets/spencer.jpeg`
- **Resume**: `/assets/resume.pdf`

## Git Branch
- Main branch: `master` (not `main`)

## Python Dependencies
- Jinja2 >= 3.0
- Markdown >= 3.4
- Install via: `pip install -r requirements.txt`

## Notes
- GitHub Pages serves directly from repo root on `master` branch
- `site/` folder is intermediate; final output goes to repo root
- Site uses static generation (not dynamic rendering)
- Keep bingo folder contents unchanged when making blog updates
