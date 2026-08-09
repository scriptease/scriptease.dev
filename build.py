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
SITE_TITLE = "scriptease.dev"
SITE_TAGLINE = "Notes from building with AI, one story at a time."
SITE_URL = "https://scriptease.dev"


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


def tag_slug(tag):
    """`Open Source` / `open-source` -> url-safe `open-source`."""
    return re.sub(r'[^a-z0-9]+', '-', tag.lower()).strip('-')


PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="/theme-init.js"></script>
<title>{title}</title>
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="alternate" type="application/rss+xml" title="{site}" href="/feed.xml">
<link rel="stylesheet" href="/style.css">
</head>
<body>
<header class="site">
  <a class="brand" href="/"><img class="brand-shark" src="/shark.png" alt="" width="20" height="20"> {site}</a>
  <div class="header-actions">
    <a class="rss-link" href="/feed.xml" aria-label="RSS feed" title="RSS feed">
      <svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><circle cx="6.2" cy="17.8" r="2.2"/><path d="M4 4v3a13 13 0 0 1 13 13h3A16 16 0 0 0 4 4z"/><path d="M4 10.5v3A6.5 6.5 0 0 1 10.5 20h3A9.5 9.5 0 0 0 4 10.5z"/></svg>
    </a>
    <button class="theme-toggle" id="theme-toggle" aria-label="Toggle dark mode" title="Toggle dark mode">
      <svg class="icon-moon" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="currentColor" d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>
      <svg class="icon-sun" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M5 5l1.4 1.4M17.6 17.6L19 19M19 5l-1.4 1.4M6.4 17.6L5 19"/></svg>
    </button>
    <button class="menu-toggle" id="menu-toggle" aria-label="Menu" aria-expanded="false">☰</button>
  </div>
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
<script src="/theme-init.js"></script>
<meta http-equiv="refresh" content="0; url=/posts/{slug}/">
<link rel="canonical" href="/posts/{slug}/">
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="stylesheet" href="/style.css">
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
    tags = [t.strip().lstrip("#") for t in fm.get("tags", "").strip("[] ").split(",") if t.strip()]
    tags_html = ""
    if tags:
        links = " ".join(
            '<a href="/tags/%s/">#%s</a>' % (tag_slug(t), escape(t)) for t in tags)
        tags_html = '<p class="post-tags">%s</p>\n' % links
    article = '<article class="post">\n<h1>{t}</h1>\n{tags}{h}\n</article>'.format(
        t=escape(title), tags=tags_html, h=html)
    created = fm.get("created", "")
    # Page is written later by write_post_pages(), which appends prev/next nav
    # once the full chronological order is known.
    return {
        "slug": slug,
        "title": title,
        "hook": fm.get("hook", ""),
        "created": created,
        "month": month_of(created),
        "tags": tags,
        "article": article,
    }


def post_nav(older, newer):
    """Bottom-of-post linear nav: chronologically older post on the left,
    newer on the right. Oldest post has no left link, newest has no right."""
    left = ('<a class="prev" href="/posts/%s/">← %s</a>'
            % (older["slug"], escape(older["title"]))) if older else "<span></span>"
    right = ('<a class="next" href="/posts/%s/">%s →</a>'
             % (newer["slug"], escape(newer["title"]))) if newer else "<span></span>"
    return '<nav class="post-nav">%s%s</nav>' % (left, right)


def write_post_pages(chrono):
    """Write each post page. `chrono` is oldest→newest, so a post's prev/next
    are simply its neighbours in the list."""
    n = len(chrono)
    for i, p in enumerate(chrono):
        older = chrono[i - 1] if i > 0 else None
        newer = chrono[i + 1] if i < n - 1 else None
        content = p["article"] + "\n" + post_nav(older, newer)
        out = REPO / "posts" / p["slug"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(PAGE.format(
            title=escape(p["title"]) + " — " + SITE_TITLE, site=SITE_TITLE,
            tagline=SITE_TAGLINE, content=content))


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


def build_tag_pages(posts):
    """One /tags/<slug>/ page per tag (its posts, newest first), plus the
    /tags/ cloud. Only complete on a full build — a filtered run reflects just
    the built subset, same as the month pages and posts.js."""
    tags = {}
    for p in posts:
        for t in p["tags"]:
            tags.setdefault(t, []).append(p)
    for tag, items in tags.items():
        items = sorted(items, key=lambda p: p["created"], reverse=True)
        content = (
            '<section class="intro"><h1>#{tag}</h1>'
            '<p>{n} post{s} tagged #{tag}.</p></section>\n{list}'.format(
                tag=escape(tag), n=len(items), s="" if len(items) == 1 else "s",
                list=entry_list(items)))
        out = REPO / "tags" / tag_slug(tag) / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(PAGE.format(
            title="#%s — %s" % (escape(tag), SITE_TITLE),
            site=SITE_TITLE, tagline=SITE_TAGLINE, content=content))
    build_tag_cloud(tags)


def build_tag_cloud(tags):
    """/tags/ — every tag as a link, font-size scaled by how often it's used."""
    if not tags:
        return
    counts = {t: len(items) for t, items in tags.items()}
    lo, hi = min(counts.values()), max(counts.values())

    def size(n):
        if hi == lo:
            return 1.2
        return round(0.85 + (n - lo) / (hi - lo) * (2.1 - 0.85), 2)

    ordered = sorted(counts, key=lambda t: (-counts[t], t))
    links = "\n".join(
        '<a href="/tags/{slug}/" style="font-size:{sz}rem" '
        'title="{n} post{s}">#{tag}</a>'.format(
            slug=tag_slug(t), sz=size(counts[t]), n=counts[t],
            s="" if counts[t] == 1 else "s", tag=escape(t))
        for t in ordered)
    content = (
        '<section class="intro"><h1>Tags</h1></section>\n'
        '<div class="tag-cloud">\n%s\n</div>' % links)
    out = REPO / "tags" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(PAGE.format(
        title="Tags — %s" % SITE_TITLE, site=SITE_TITLE,
        tagline=SITE_TAGLINE, content=content))


def write_posts_js(posts):
    """window.POSTS = [...] newest first — the data the sidebar reads on every
    page. Titles stored raw (JSON-escaped); sidebar.js HTML-escapes on render."""
    data = [
        {"slug": p["slug"], "title": p["title"], "hook": p["hook"],
         "date": p["created"], "month": p["month"], "tags": p["tags"]}
        for p in posts
    ]
    (REPO / "posts.js").write_text(
        "window.POSTS = %s;\n" % json.dumps(data, ensure_ascii=False, indent=2))


def rfc822(created):
    """`2026-07-31` -> RFC-822 date at 00:00 UTC, for RSS pubDate."""
    import email.utils
    m = re.match(r'^(\d{4})-(\d{2})-(\d{2})', created or "")
    if not m:
        return email.utils.formatdate(0, usegmt=True)
    dt = datetime.datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)),
                           tzinfo=datetime.timezone.utc)
    return email.utils.format_datetime(dt)


def write_feed(posts):
    """RSS 2.0 feed at /feed.xml, newest first. `hook` is the plain-text
    description; the rendered article HTML rides along in content:encoded."""
    items = []
    for p in posts:
        url = "%s/posts/%s/" % (SITE_URL, p["slug"])
        cats = "".join(
            "<category>%s</category>" % escape(t) for t in p["tags"])
        items.append(
            "<item>\n"
            "<title>%s</title>\n"
            "<link>%s</link>\n"
            "<guid isPermaLink=\"true\">%s</guid>\n"
            "<pubDate>%s</pubDate>\n"
            "%s"
            "<description>%s</description>\n"
            "<content:encoded><![CDATA[%s]]></content:encoded>\n"
            "</item>" % (
                escape(p["title"]), url, url, rfc822(p["created"]),
                cats, escape(p["hook"]),
                p["article"].replace("]]>", "]]]]><![CDATA[>")))
    built = rfc822(posts[0]["created"]) if posts else rfc822("")
    feed = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<?xml-stylesheet type="text/xsl" href="/feed.xsl"?>\n'
        '<rss version="2.0" xmlns:content="http://purl.org/rss/1.0/modules/content/" '
        'xmlns:atom="http://www.w3.org/2005/Atom">\n'
        "<channel>\n"
        "<title>%s</title>\n"
        "<link>%s/</link>\n"
        '<atom:link href="%s/feed.xml" rel="self" type="application/rss+xml"/>\n'
        "<description>%s</description>\n"
        "<language>en</language>\n"
        "<lastBuildDate>%s</lastBuildDate>\n"
        "%s\n"
        "</channel>\n</rss>\n" % (
            escape(SITE_TITLE), SITE_URL, SITE_URL, escape(SITE_TAGLINE),
            built, "\n".join(items)))
    (REPO / "feed.xml").write_text(feed)


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
    posts.sort(key=lambda p: (p["created"], p["slug"]), reverse=True)

    write_post_pages(sorted(posts, key=lambda p: (p["created"], p["slug"])))
    build_month_pages(posts)
    build_tag_pages(posts)
    write_posts_js(posts)
    write_feed(posts)
    if posts:
        (REPO / "index.html").write_text(
            REDIRECT.format(slug=posts[0]["slug"], site=SITE_TITLE))
    print("Done. %d post(s). Root redirects to: %s" % (
        len(posts), posts[0]["slug"] if posts else "(none)"))


if __name__ == "__main__":
    main()
