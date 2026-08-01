#!/usr/bin/env python3
"""Build the scriptease.dev static site from the Obsidian vault Blog/ folder.

Usage:
    python3 build.py                 # build every published post
    python3 build.py <slug> [<slug>] # build only these post slugs (by filename stem)

Reads published posts (frontmatter `status: published`) out of the vault, copies
each post's local assets into the repo, converts the markdown body to HTML, and
writes:

    index.html                 root: redirects to the latest post
    posts/<slug>/index.html    one page per post
    posts/<slug>/assets/...    the post's copied images
    archive/<YYYY-MM>/index.html   month overview (that month's posts)
    posts.js                   window.POSTS metadata (newest first), for the sidebar

The site is served at an apex domain (scriptease.dev), so pages use absolute
`/...` paths and load `/posts.js` + `/sidebar.js` for the shared sidebar.
Preview locally with a web server (see README), not file://.

Output is plain static HTML/JS committed to the repo; GitHub Pages serves it
as-is (no Jekyll). Wikilinks (`[[...]]`) point at vault notes that don't exist
publicly, so they're flattened to plain text.
"""
import re
import sys
import json
import shutil
import datetime
from pathlib import Path

VAULT_BLOG = Path(
    "/Users/florian/Library/Mobile Documents/iCloud~md~obsidian/Documents/V1/Blog"
)
REPO = Path(__file__).resolve().parent
SITE_TITLE = "scriptease"
SITE_TAGLINE = "Notes from building with AI, one story at a time."


def split_frontmatter(text):
    """Return (frontmatter_dict, body). Minimal YAML: key: value."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm_block = text[3:end].strip("\n")
    body = text[end + 4:].lstrip("\n")
    fm = {}
    for line in fm_block.splitlines():
        m = re.match(r'^([A-Za-z0-9_]+):\s*(.*)$', line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
                val = val[1:-1]
            fm[key] = val
    return fm, body


def extract_title(body):
    """Pull the first `# Title` line; return (title, body_without_it)."""
    lines = body.splitlines()
    for i, line in enumerate(lines):
        m = re.match(r'^#\s+(.+)$', line)
        if m:
            del lines[i]
            if i < len(lines) and lines[i].strip() == "":
                del lines[i]
            return m.group(1).strip(), "\n".join(lines).lstrip("\n")
    return None, body


def flatten_wikilinks(body):
    """`[[target|alias]]` -> alias, `[[path/to/note]]` -> note. Internal vault
    links have no public target, so render just their human-readable text."""
    def repl(m):
        inner = m.group(1)
        if "|" in inner:
            return inner.split("|", 1)[1].strip()
        tail = inner.split("/")[-1].strip()
        return re.sub(r'\.md$', "", tail)
    return re.sub(r'\[\[([^\]]+)\]\]', repl, body)


def collapse_paragraph_wraps(body):
    """Join hard-wrapped prose lines within a paragraph so a single newline
    doesn't survive into the HTML. Structural lines are left untouched."""
    out, para, in_fence = [], [], False

    def flush():
        if para:
            out.append(" ".join(l.strip() for l in para))
            para.clear()

    for ln in body.split("\n"):
        s = ln.strip()
        if s.startswith("```") or s.startswith("~~~"):
            flush(); in_fence = not in_fence; out.append(ln); continue
        if in_fence:
            out.append(ln); continue
        if s == "":
            flush(); out.append(""); continue
        if re.match(r'^(#{1,6}\s|>|\s*[-*+]\s|\s*\d+[.)]\s|\||-{3,}|={3,}|!\[)', ln) or ln.startswith("    "):
            flush(); out.append(ln); continue
        para.append(ln)
    flush()
    return "\n".join(out)


def md_to_html(body):
    import markdown
    return markdown.markdown(
        collapse_paragraph_wraps(flatten_wikilinks(body)),
        extensions=["extra", "sane_lists"],
    )


def escape(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def month_of(created):
    """`2026-07-31` -> `2026-07`. Empty/odd dates fall back to `undated`."""
    m = re.match(r'^(\d{4})-(\d{2})', created or "")
    return "%s-%s" % (m.group(1), m.group(2)) if m else "undated"


def month_label(ym):
    try:
        y, mo = ym.split("-")
        return datetime.date(int(y), int(mo), 1).strftime("%B %Y")
    except Exception:
        return ym


PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="/style.css">
</head>
<body>
<header class="site">
  <a class="brand" href="/">{site}</a>
</header>
<div class="layout">
  <main>
{content}
  </main>
  <aside class="sidebar" id="sidebar"></aside>
</div>
<footer class="site">
  <span>{site} — {tagline}</span>
</footer>
<script src="/posts.js"></script>
<script src="/sidebar.js"></script>
</body>
</html>
"""

REDIRECT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="refresh" content="0; url=/posts/{slug}/">
<link rel="canonical" href="/posts/{slug}/">
<title>{site}</title>
</head>
<body>
<p>Redirecting to the <a href="/posts/{slug}/">latest post</a>…</p>
</body>
</html>
"""


def copy_assets(post_dir, slug):
    """Copy the post's assets/ folder into posts/<slug>/assets/ 1:1, so img
    src paths from the markdown resolve unchanged."""
    src = post_dir / "assets"
    dst = REPO / "posts" / slug / "assets"
    if dst.exists():
        shutil.rmtree(dst)
    if src.is_dir():
        shutil.copytree(src, dst)


def entry_list(posts):
    """Shared markup for the root/month post listings."""
    rows = []
    for p in posts:
        rows.append(
            '<li class="entry">\n'
            '<a class="entry-title" href="/posts/{slug}/">{title}</a>\n'
            '<time>{date}</time>\n'
            '<p class="hook">{hook}</p>\n'
            '<a class="read-more" href="/posts/{slug}/">Read more →</a>\n'
            '</li>'.format(
                slug=p["slug"], title=escape(p["title"]),
                date=escape(p["created"]), hook=escape(p["hook"])))
    return '<ul class="entries">\n%s\n</ul>' % "\n".join(rows)


def build_post(md_path):
    raw = md_path.read_text()
    fm, body = split_frontmatter(raw)
    if fm.get("status") != "published":
        return None
    title, body = extract_title(body)
    if not title:
        print("  SKIP (no # title): %s" % md_path.name, file=sys.stderr)
        return None
    slug = md_path.stem
    copy_assets(md_path.parent, slug)
    # img src is left exactly as the markdown writes it (assets/<slug>/x.png,
    # relative to the post page) and the assets tree is copied 1:1, so paths
    # match with no rewriting.
    html = md_to_html(body)
    article = '<article class="post">\n<h1>{t}</h1>\n{h}\n</article>'.format(
        t=escape(title), h=html)
    out = REPO / "posts" / slug / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(PAGE.format(
        title=escape(title) + " — " + SITE_TITLE, site=SITE_TITLE,
        tagline=SITE_TAGLINE, content=article))
    created = fm.get("created", "")
    return {
        "slug": slug,
        "title": title,
        "hook": fm.get("hook", ""),
        "created": created,
        "month": month_of(created),
    }


def build_month_pages(posts):
    months = {}
    for p in posts:
        months.setdefault(p["month"], []).append(p)
    for ym, items in months.items():
        items = sorted(items, key=lambda p: p["created"], reverse=True)
        content = (
            '<section class="intro"><h1>{label}</h1></section>\n{list}'.format(
                label=escape(month_label(ym)), list=entry_list(items)))
        out = REPO / "archive" / ym / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(PAGE.format(
            title="%s — %s" % (escape(month_label(ym)), SITE_TITLE),
            site=SITE_TITLE, tagline=SITE_TAGLINE, content=content))


def write_posts_js(posts):
    """window.POSTS = [...] newest first — the data the sidebar reads on every
    page. Titles stored raw (JSON-escaped); sidebar.js HTML-escapes on render."""
    data = [
        {"slug": p["slug"], "title": p["title"], "hook": p["hook"],
         "date": p["created"], "month": p["month"]}
        for p in posts
    ]
    (REPO / "posts.js").write_text(
        "window.POSTS = %s;\n" % json.dumps(data, ensure_ascii=False, indent=2))


def main():
    only = set(sys.argv[1:])
    md_files = [
        p for p in VAULT_BLOG.rglob("*.md")
        if not p.name.startswith(("📌", "📜", "🧩"))
        and "rejects" not in p.parts and "drafts" not in p.parts
    ]
    if only:
        md_files = [p for p in md_files if p.stem in only]
    posts = []
    for md in md_files:
        res = build_post(md)
        if res:
            posts.append(res)
            print("  built: %s" % res["slug"])
    posts.sort(key=lambda p: p["created"], reverse=True)

    build_month_pages(posts)
    write_posts_js(posts)
    if posts:
        (REPO / "index.html").write_text(
            REDIRECT.format(slug=posts[0]["slug"], site=SITE_TITLE))
    print("Done. %d post(s). Root redirects to: %s" % (
        len(posts), posts[0]["slug"] if posts else "(none)"))


if __name__ == "__main__":
    main()
