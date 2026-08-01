#!/usr/bin/env python3
"""Build the scriptease.dev static site from the Obsidian vault Blog/ folder.

Usage:
    python3 build.py                 # build every published post
    python3 build.py <slug> [<slug>] # build only these post slugs (by filename stem)

Reads published posts (frontmatter `status: published`) out of the vault, copies
each post's local assets into the repo, converts the markdown body to HTML, and
writes:

    index.html                 site landing page (post list, newest first)
    posts/<slug>/index.html    one page per post
    posts/<slug>/assets/...    the post's copied images

Output is plain static HTML committed to the repo; GitHub Pages serves it as-is
(no Jekyll, no build step on GitHub's side). Wikilinks (`[[...]]`) point at other
vault notes that don't exist publicly, so they're flattened to plain text.
"""
import re
import sys
import shutil
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


PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="{root}style.css">
</head>
<body>
<header class="site">
  <a class="brand" href="{root}index.html">{site}</a>
</header>
<main>
{content}
</main>
<footer class="site">
  <span>{site} — {tagline}</span>
</footer>
</body>
</html>
"""


def copy_assets(post_dir, slug):
    """Copy the post's assets/ folder into posts/<slug>/assets/. Returns True
    if there was anything to copy."""
    src = post_dir / "assets"
    if not src.is_dir():
        return False
    dst = REPO / "posts" / slug / "assets"
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    return True


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
        tagline=SITE_TAGLINE, root="../../", content=article))
    return {
        "slug": slug,
        "title": title,
        "hook": fm.get("hook", ""),
        "created": fm.get("created", ""),
    }


def escape(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def build_index(posts):
    posts.sort(key=lambda p: p["created"], reverse=True)
    rows = []
    for p in posts:
        rows.append(
            '<li class="entry">\n'
            '<a class="entry-title" href="posts/{slug}/">{title}</a>\n'
            '<time>{date}</time>\n'
            '<p class="hook">{hook}</p>\n'
            '</li>'.format(
                slug=p["slug"], title=escape(p["title"]),
                date=escape(p["created"]), hook=escape(p["hook"])))
    content = (
        '<section class="intro"><p>{tag}</p></section>\n'
        '<ul class="entries">\n{rows}\n</ul>'.format(
            tag=SITE_TAGLINE, rows="\n".join(rows)))
    (REPO / "index.html").write_text(PAGE.format(
        title=SITE_TITLE, site=SITE_TITLE, tagline=SITE_TAGLINE,
        root="", content=content))


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
    build_index(posts)
    print("Done. %d post(s). Open index.html." % len(posts))


if __name__ == "__main__":
    main()
