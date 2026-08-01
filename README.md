# scriptease.dev

The static site behind **[scriptease.dev](https://scriptease.dev)** — a GitHub Pages
mirror of the [WordPress blog](https://scripteasesite.wordpress.com), built from
posts written in an Obsidian vault.

## How it works

`build.py` reads published posts (`status: published`) out of the vault's `Blog/`
folder, copies each post's assets, flattens vault wikilinks to plain text, and
emits plain static HTML — no Jekyll, no build step on GitHub's side.

```
python3 build.py                 # build every published post
python3 build.py <slug> [<slug>] # build only these posts
```

Output:

```
index.html                 root → redirects to the latest post
posts/<slug>/index.html     one page per post (+ assets/)
archive/<YYYY-MM>/index.html   month overviews
posts.js                    window.POSTS metadata (newest first)
sidebar.js                  shared sidebar: Latest 5 + Archive + links
```

The site is served at an apex domain, so pages use absolute `/…` paths. Preview
locally with a web server (`python3 -m http.server`), not `file://`.
