(function () {
  var f = document.getElementById("quote");
  if (!f) { return; }
  try {
    var it = new URLSearchParams(location.search).get("item");
    if (it) {
      var s = document.getElementById("q-item");
      for (var k = 0; k < s.options.length; k++) { if (s.options[k].value === it) { s.selectedIndex = k; } }
    }
  } catch (e) { /* ignore */ }
  // Bots submit instantly; people take longer than 3 seconds.
  var t0 = Date.now();
  f.addEventListener("submit", function (e) {
    if (Date.now() - t0 < 3000) {
      e.preventDefault();
      e.stopImmediatePropagation();
      alert("Please take a moment to check your details, then send again.");
    }
  }, true);
})();
