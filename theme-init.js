// Set the theme before first paint (avoids a flash): use the saved choice,
// otherwise follow the OS preference. Loaded synchronously in <head>.
(function () {
  try {
    var t = localStorage.getItem("theme");
    if (!t) t = matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
    document.documentElement.setAttribute("data-theme", t);
  } catch (e) {}
})();
