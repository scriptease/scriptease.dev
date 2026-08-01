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

  var seen = {}, months = [];
  posts.forEach(function (p) {
    if (!seen[p.month]) { seen[p.month] = 1; months.push(p.month); }
  });
  var archive = months.map(function (m) {
    return '<li><a href="/archive/' + m + '/">' + esc(m) + "</a></li>";
  }).join("");

  el.innerHTML =
    '<h2>Latest</h2><ul class="side-latest">' + latest + "</ul>" +
    '<h2>Archive</h2><ul class="side-archive">' + archive + "</ul>" +
    '<h2>Elsewhere</h2><ul class="side-links">' +
    '<li><a href="https://scripteasesite.wordpress.com">WordPress mirror</a></li>' +
    "</ul>";

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
