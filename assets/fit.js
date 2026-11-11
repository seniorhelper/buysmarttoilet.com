(function () {
  var i = document.getElementById("fit-in"), b = document.getElementById("fit-go"), o = document.getElementById("fit-out");
  if (!i || !b || !o) { return; }
  function run() {
    var v = parseFloat(i.value), r;
    if (isNaN(v)) { o.textContent = "Enter the measurement in inches, for example 18.5."; return; }
    if (v < 15 || v > 20.5) {
      r = "That number is outside the usual 16 to 19 inch range. Measure again from the midpoint between the seat bolts to the outside front edge of the rim. Still unusual? Send us a photo with the tape in view.";
    } else if (v <= 17.25) {
      r = "Round. Choose the Round option on seats that come in both shapes. Elongated-only seats will not fit.";
    } else if (v < 17.75) {
      r = "In between. Send us a photo with the tape in view before ordering a seat, and we will confirm the shape.";
    } else {
      r = "Elongated. Choose the Elongated option. Most bidet seats we carry fit elongated bowls.";
    }
    o.textContent = r;
  }
  b.addEventListener("click", run);
  i.addEventListener("keydown", function (e) { if (e.key === "Enter") { e.preventDefault(); run(); } });
})();
