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
    '<h2>Archive</h2><ul class="side-archive">' + archive + "</ul>";
})();
