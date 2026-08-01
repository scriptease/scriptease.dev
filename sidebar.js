// Renders the shared sidebar (Latest 5 + Archive by month) from window.POSTS,
// which is defined in /posts.js and identical on every page.
(function () {
  var posts = window.POSTS || [];
  var el = document.getElementById("sidebar");
  if (!el) return;

  function esc(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
  }

  var latest = posts.slice(0, 5).map(function (p) {
    return '<li><a href="/posts/' + p.slug + '/">' + esc(p.title) + "</a>" +
      "<time>" + esc(p.date) + "</time></li>";
  }).join("");

  var counts = {}, months = [];
  posts.forEach(function (p) {
    if (!counts[p.month]) months.push(p.month);
    counts[p.month] = (counts[p.month] || 0) + 1;
  });
  var archive = months.map(function (m) {
    return '<li><a href="/archive/' + m + '/">' + esc(m) + "</a> " +
      '<span class="count">(' + counts[m] + ")</span></li>";
  }).join("");

  // Compact tag cloud, sized by how often each tag is used.
  function tslug(t) {
    return t.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "");
  }
  var tagCounts = {};
  posts.forEach(function (p) {
    (p.tags || []).forEach(function (t) { tagCounts[t] = (tagCounts[t] || 0) + 1; });
  });
  var tagNames = Object.keys(tagCounts);
  var tc = tagNames.map(function (t) { return tagCounts[t]; });
  var mx = Math.max.apply(null, tc), mn = Math.min.apply(null, tc);
  function tsize(n) {
    return mx === mn ? "0.9" : (0.75 + (n - mn) / (mx - mn) * (1.15 - 0.75)).toFixed(2);
  }
  tagNames.sort(function (a, b) { return tagCounts[b] - tagCounts[a] || (a < b ? -1 : 1); });
  // On a post page, highlight that post's own tags (blue) and dim the rest (gray).
  var pm = location.pathname.match(/\/posts\/([^\/]+)\/?$/);
  var current = pm && posts.filter(function (p) { return p.slug === pm[1]; })[0];
  var onTags = {};
  if (current) (current.tags || []).forEach(function (t) { onTags[t] = 1; });
  var cloud = tagNames.map(function (t) {
    var cls = current ? (onTags[t] ? ' class="on"' : ' class="off"') : "";
    return "<a" + cls + ' href="/tags/' + tslug(t) + '/" style="font-size:' +
      tsize(tagCounts[t]) + 'rem">#' + esc(t) + "</a>";
  }).join(" ");

  el.innerHTML =
    '<h2>Latest</h2><ul class="side-latest">' + latest + "</ul>" +
    '<h2>Archive</h2><ul class="side-archive">' + archive + "</ul>" +
    '<h2><a href="/tags/">Tags</a></h2><div class="side-cloud">' + cloud + "</div>" +
    '<h2>Elsewhere</h2><ul class="side-links">' +
    '<li><a href="https://scripteasesite.wordpress.com">WordPress mirror</a></li>' +
    "</ul>";

  // Dark/light toggle: flip the theme and remember it. theme-init.js set the
  // initial value before paint.
  var tt = document.getElementById("theme-toggle");
  if (tt) {
    tt.addEventListener("click", function () {
      var root = document.documentElement;
      var next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      function apply() {
        root.setAttribute("data-theme", next);
        try { localStorage.setItem("theme", next); } catch (e) {}
      }
      var reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
      // Circular reveal from the button's centre (View Transitions API).
      if (!document.startViewTransition || reduce) { apply(); return; }
      var r = tt.getBoundingClientRect();
      var x = r.left + r.width / 2, y = r.top + r.height / 2;
      var end = Math.hypot(Math.max(x, innerWidth - x), Math.max(y, innerHeight - y));
      root.style.setProperty("--vt-x", x + "px");
      root.style.setProperty("--vt-y", y + "px");
      root.style.setProperty("--vt-r", end + "px");
      document.startViewTransition(apply);
    });
  }

  // Hamburger toggle (only visible when the sidebar doesn't fit; see CSS).
  var btn = document.getElementById("menu-toggle");
  if (btn) {
    function setOpen(open) {
      el.classList.toggle("open", open);
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    }
    btn.addEventListener("click", function (e) {
      e.stopPropagation();
      setOpen(!el.classList.contains("open"));
    });
    // Tapping a link or anywhere outside closes it.
    el.addEventListener("click", function (e) {
      if (e.target.closest("a")) setOpen(false);
    });
    document.addEventListener("click", function (e) {
      if (!el.contains(e.target) && e.target !== btn) setOpen(false);
    });
  }
})();
