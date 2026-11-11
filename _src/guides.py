"""Original copy for buysmarttoilet.com. Facts are cited inline with links to the source."""
import html

def esc(s):
    return html.escape(str(s), quote=True)

AUTHOR = "Zach Wennstedt"
UPDATED = "2026-11-10"
UPDATED_TXT = "November 10, 2026"

ADA = "https://www.access-board.gov/ada/chapter/ch06/"
WATERSENSE = "https://www.epa.gov/watersense/residential-toilets"
LOWES_MEASURE = "https://www.lowes.com/n/how-to/how-to-measure-toilet-seat"

GUIDE_FOR_TYPE = {
    "Bidet Seat": ("/smart-toilet-vs-bidet-seat/", "Smart toilet or bidet seat? How to choose"),
    "Smart Toilet": ("/smart-toilet-vs-bidet-seat/", "Smart toilet or bidet seat? How to choose"),
    "Toilet": ("/smart-toilet-for-seniors/", "Choosing a toilet for an older adult"),
    "Toilet Seat": ("/smart-toilet-for-seniors/", "Choosing a toilet for an older adult"),
    "Upflush Toilet": ("/upflush-toilet-basement/", "Upflush toilets for basements: will one work for you?"),
    "Macerating Toilet": ("/upflush-toilet-basement/", "Upflush toilets for basements: will one work for you?"),
}

def lowest(products, handle, fmt):
    for p in products:
        if p["handle"] == handle:
            return fmt(min(float(v["price"]) for v in p["variants"]))
    return "[CONFIRM price]"

def plink(products, handle, fmt, text=None):
    for p in products:
        if p["handle"] == handle:
            name = text or p["title"].split(" — ")[0]
            return f'<a href="/products/{handle}/">{esc(name)}</a> ({lowest(products, handle, fmt)})'
    return esc(text or handle)

# ---------------------------------------------------------------- home
def home(products, fmt, shop_html):
    P = lambda h, t=None: plink(products, h, fmt, t)
    return f"""
<section class="hero">
  <h1>Smart toilets and bidet seats, explained plainly</h1>
  <p class="lede">Most people don't need a $1,200 smart toilet. Some do. We sell both, plus comfort-height, upflush and heavy-duty options, and we'll tell you which one actually fits your bathroom, your outlet and the person using it.</p>
  <div class="cta-row"><a class="btn" href="/pages/contact/">Get a quote</a><a class="btn btn-ghost" href="/round-vs-elongated-toilet/">Check your bowl size</a></div>
  <p class="note">No online checkout yet. Send a request and we confirm price, stock and delivery in writing before you pay.</p>
</section>

<section class="pick" aria-labelledby="pick-h">
  <h2 id="pick-h">Start with the problem, not the product</h2>
  <div class="tiles">
    <div class="tile"><h3>"I want a bidet but there's no outlet"</h3><p>A manual seat runs on water pressure alone: {P("minnow-manual-bidet-seat", "ANZZI Minnow")}. No heat, no dryer, no electrician.</p></div>
    <div class="tile"><h3>"My toilet works fine, I just want warm water and a heated seat"</h3><p>An electric seat bolts onto the toilet you have. Start with the {P("anzzi-smart-bidet-seat-auto-lid", "auto-lid seat")} and read <a href="/smart-toilet-vs-bidet-seat/">smart toilet vs bidet seat</a> first.</p></div>
    <div class="tile"><h3>"Standing up from the toilet is getting hard"</h3><p>Seat height matters more than features. See <a href="/smart-toilet-for-seniors/">choosing a toilet for an older adult</a>, then the {P("anzzi-two-piece-ada-toilet", "ADA comfort-height toilet")}.</p></div>
    <div class="tile"><h3>"There's no drain where I want a bathroom"</h3><p>An upflush (macerating) toilet pumps waste up and over. Read <a href="/upflush-toilet-basement/">will an upflush toilet work for you</a> before buying the {P("nesso-upflush-macerating-toilet", "Nesso")}.</p></div>
  </div>
</section>

<section id="shop" aria-labelledby="shop-h">
  <h2 id="shop-h">Shop</h2>
  {shop_html}
</section>

<section class="how" aria-labelledby="how-h">
  <h2 id="how-h">How ordering works right now</h2>
  <ol>
    <li><strong>Request the item.</strong> Tell us the model, your bowl shape (round or elongated) and your ZIP code.</li>
    <li><strong>We confirm in writing.</strong> Current price, stock, delivery method (small parcel or freight) and a delivery estimate.</li>
    <li><strong>You decide.</strong> Nothing is charged until you approve the written quote.</li>
  </ol>
</section>
"""

def home_schema(site, products):
    return [{"@context": "https://schema.org", "@type": "OnlineStore", "name": "Buy Smart Toilet", "url": site + "/",
             "description": "Independent online store for smart toilets, bidet seats, comfort-height and upflush toilets.",
             "areaServed": "US"},
            {"@context": "https://schema.org", "@type": "WebSite", "name": "Buy Smart Toilet", "url": site + "/"}]

# ---------------------------------------------------------------- guides
GUIDES = [
{
"path": "/smart-toilet-vs-bidet-seat/",
"crumb": "Smart toilet vs bidet seat",
"title": "Smart Toilet vs Bidet Seat: Which Should You Buy?",
"desc": "A bidet seat gives you most of a smart toilet for a third of the price. When the full smart toilet is worth it, with a side-by-side table.",
"h1": "Smart toilet or bidet seat? How to choose",
"answer": "If your current toilet flushes well, buy a bidet seat. You get warm water, a heated seat and a dryer for roughly a quarter to a third of the price of a smart toilet, and it installs in under an hour with no plumber. Buy a full smart toilet when the toilet itself needs replacing, when you're remodeling, or when you want a tankless, low-profile look and features a seat can't add, like auto flush.",
"sections": lambda P: f"""
<h2>The difference in one sentence</h2>
<p>A bidet seat replaces only your toilet seat. A smart toilet replaces the whole fixture: bowl, tank (or no tank), flush mechanism and seat, built as one unit with its own electronics.</p>

<h2>Side by side</h2>
<table>
<thead><tr><th></th><th>Electric bidet seat</th><th>Smart toilet</th></tr></thead>
<tbody>
<tr><th scope="row">Typical price here</th><td>{P("anzzi-smart-bidet-seat-auto-lid","Auto-lid seat")} to {P("dive-smart-electric-bidet-seat","ENVO Dive")}</td><td>{P("envo-echo-smart-bidet-toilet","ENVO Echo")} to {P("envo-dia-smart-bidet-toilet","ENVO Dia")}</td></tr>
<tr><th scope="row">Install</th><td>Most people do it themselves: unbolt the old seat, add a T-valve to the water line, bolt on the new one.</td><td>Remove the old toilet, set a new wax ring and flange bolts, connect water and power. Many people hire a plumber.</td></tr>
<tr><th scope="row">Power</th><td>Needs an outlet near the toilet (manual seats need none)</td><td>Needs an outlet near the toilet</td></tr>
<tr><th scope="row">Delivery</th><td>Small parcel, a box you can carry</td><td>Freight; someone has to be home and it's heavy</td></tr>
<tr><th scope="row">Renters</th><td>Easy to take with you when you move</td><td>Not realistic</td></tr>
<tr><th scope="row">What it can't do</th><td>Can't change how your toilet flushes, its height or its water use</td><td>If the electronics fail, the whole fixture is affected</td></tr>
</tbody></table>

<h2>When the bidet seat is the right call</h2>
<ul>
<li>Your toilet is under about 15 years old, flushes cleanly and isn't cracked or rocking.</li>
<li>You rent, or you might move in the next few years.</li>
<li>You want to try a bidet before committing. Plenty of people start with a {P("minnow-manual-bidet-seat","manual seat")} and only then decide whether warm water matters to them.</li>
<li>The budget is firm. The money saved can pay for a comfort-height toilet underneath the seat later.</li>
</ul>

<h2>When the full smart toilet is worth it</h2>
<ul>
<li>The toilet needs replacing anyway (old 3.5-gallon flush, cracked tank, constant running). Replacing it with a smart toilet means one install instead of two.</li>
<li>You're remodeling and want the clean, tankless look. A seat on a standard toilet will always look like an add-on.</li>
<li>You want features that live in the toilet, not the seat, such as automatic flushing or a foot sensor flush. Check each model's page; not every smart toilet has every feature.</li>
</ul>

<h2>Two checks before you buy either one</h2>
<p><strong>1. Bowl shape.</strong> Seats come in round and elongated, and the wrong one won't seal. Use our <a href="/round-vs-elongated-toilet/">round vs elongated fit checker</a>.</p>
<p><strong>2. The outlet.</strong> Electric seats and smart toilets plug in, and a bathroom outlet should be GFCI-protected. If there's no outlet within reach of the cord, either budget for an electrician or go manual. Follow the manufacturer's manual on extension cords; brands differ, and several say not to use one at all.</p>

<h2>A middle path a lot of people miss</h2>
<p>A new comfort-height toilet plus an electric bidet seat. For example, the {P("anzzi-two-piece-ada-toilet","ADA comfort-height toilet")} with the {P("anzzi-smart-bidet-seat-107","Smart Bidet Seat 107")}. You get the right seat height for aging knees, a water-efficient flush and the warm-water features, and if the seat ever fails you replace a seat, not a toilet.</p>
""",
"faq": [
("Is a smart toilet better than a bidet seat?", "Not automatically. The wash, heat and dryer features are similar. A smart toilet adds the fixture itself (flush, height, looks) and sometimes auto-flush. If your toilet is fine, a bidet seat gets you most of the benefit for much less."),
("Can I install a bidet seat myself?", "Usually, yes. If you can unbolt a toilet seat and tighten a water fitting by hand, you can install most bidet seats. The electric ones also need an outlet nearby. If you're unsure about the water connection, a handyman can do it in under an hour."),
("Do smart toilets need a special drain?", "No. They set on a standard floor flange like a regular toilet. Check the rough-in (the distance from the wall to the center of the drain, commonly 12 inches) before ordering."),
("Will a bidet seat fit my toilet?", "It needs to match your bowl shape (round or elongated) and the bolt spacing. Most seats fit standard bolt spacing. Measure from the center of the seat bolts to the front edge of the bowl."),
],
},
{
"path": "/smart-toilet-for-seniors/",
"crumb": "For older adults",
"title": "Smart Toilets & Bidet Seats for Seniors: A Caregiver's Checklist",
"desc": "What actually matters when choosing a toilet or bidet seat for an older adult: seat height, simple controls, power-outage behavior and weight rating.",
"h1": "Choosing a toilet or bidet seat for an older adult",
"answer": "For most older adults, the two changes that make the biggest difference are seat height and hygiene without twisting. A comfort-height toilet (17 to 19 inches to the top of the seat, the ADA range) makes standing up easier, and a bidet seat with a simple remote handles cleaning without reaching back. Fancy features matter less than big, clear buttons and a seat that won't shift.",
"sections": lambda P: f"""
<h2>Start with height, not features</h2>
<p>The ADA standard puts the top of a toilet seat at 17 to 19 inches above the floor (<a href="{ADA}" rel="noopener">2010 ADA Standards, section 604.4</a>). Many older standard toilets sit lower, around 15 inches. Those two to four inches are the difference between standing up on your own and needing a hand.</p>
<p>A quick way to check: sit on the current toilet. If the knees end up higher than the hips, the seat is too low for comfortable standing. Note that a bidet seat adds a little height of its own, so measure the toilet and seat together.</p>

<h2>A checklist for caregivers</h2>
<table>
<thead><tr><th>Check</th><th>Why it matters</th><th>What to look for</th></tr></thead>
<tbody>
<tr><td>Seat height</td><td>Standing and sitting safely</td><td>17–19 in to the top of the seat, or a comfort-height toilet</td></tr>
<tr><td>Controls</td><td>Small, crowded buttons get ignored or pressed by accident</td><td>A remote with large labeled buttons, or a side panel that's reachable without twisting</td></tr>
<tr><td>Seat sensor</td><td>Stops the spray when nobody is seated</td><td>Listed as "seat sensor" or "occupancy sensor"</td></tr>
<tr><td>Water temperature</td><td>Thin or sensitive skin</td><td>Adjustable warm water with a low setting</td></tr>
<tr><td>Weight rating</td><td>Seats flex and shift under heavier users</td><td>Stated capacity; heavy-duty seats such as an 800 lb rated seat</td></tr>
<tr><td>Night use</td><td>Most falls happen on night trips</td><td>Built-in night light</td></tr>
<tr><td>Power outage</td><td>Electric features stop working</td><td>Know how the toilet flushes without power (see each product manual)</td></tr>
<tr><td>Cleaning</td><td>The caregiver usually does it</td><td>Self-rinsing nozzle, quick-release seat</td></tr>
</tbody></table>

<h2>Good combinations by situation</h2>
<h3>Living alone, still fairly mobile</h3>
<p>A comfort-height toilet with a soft-close seat, plus a {P("minnow-manual-bidet-seat","manual bidet seat")} if there's no outlet. Simple, nothing to charge or reset.</p>
<h3>Limited reach or shoulder pain</h3>
<p>An electric seat with a wireless remote and warm-air dryer, like the {P("anzzi-smart-bidet-seat-auto-lid","Smart Bidet Seat with auto lid")}. The dryer and the wash do the reaching. Mount the remote where it's visible from the seat.</p>
<h3>Heavier user, or a seat that keeps shifting</h3>
<p>The {P("xl-comfort-round-toilet-seat","XL Comfort seat")} is rated to 800 lb and has wide bumpers that stop the side-to-side shift that makes a seat feel unsafe. Check that the toilet itself is firmly set; a rated seat can't fix a rocking bowl.</p>
<h3>Replacing the whole toilet anyway</h3>
<p>The {P("anzzi-two-piece-ada-toilet","two-piece ADA comfort-height toilet")} with a bidet seat on top, or a one-piece smart toilet if the person is comfortable with a remote. Ask us for the seat height of a specific model before ordering.</p>

<h2>Things that sound good but often go unused</h2>
<ul>
<li>Many wash modes. Most people settle on one. Simpler is safer for someone with memory changes.</li>
<li>App control. Fine for the caregiver, rarely used by the person on the seat.</li>
<li>Auto-opening lids. Handy, but they can startle someone who isn't expecting them. Most can be switched off.</li>
</ul>

<h2>Grab bars still matter</h2>
<p>No toilet replaces a properly anchored grab bar. The ADA places side grab bars near the toilet; in a home, have a bar installed into studs or with rated anchors next to the toilet. A towel bar is not a grab bar.</p>
""",
"faq": [
("What height toilet is best for seniors?", "A comfort-height toilet that puts the top of the seat between 17 and 19 inches above the floor, the range in the 2010 ADA Standards. Shorter adults sometimes prefer the lower end; taller adults the higher end. A bidet seat adds a small amount of height."),
("Are bidet seats good for elderly people?", "Often, yes. They reduce twisting and reaching for hygiene, and warm water is gentler on skin. Choose one with simple, clearly labeled controls and a seat sensor so it won't spray when nobody is seated."),
("Is a raised toilet seat or a comfort-height toilet better?", "A comfort-height toilet is more stable because there's nothing extra to shift or loosen. A raised seat is cheaper and faster for a short-term need, like recovery after surgery."),
("What weight can a toilet seat hold?", "It varies widely, and many standard seats don't list a rating. Heavy-duty seats list one; the XL Comfort seat we carry is rated to 800 lb. The bowl and how it's anchored to the floor matter too."),
],
},
{
"path": "/round-vs-elongated-toilet/",
"crumb": "Round vs elongated",
"title": "Round vs Elongated Toilet: Measure in 1 Minute (Fit Checker)",
"desc": "Measure from the seat bolts to the front of the bowl and our fit checker tells you round or elongated, and which seats and toilets fit.",
"h1": "Round or elongated? Measure your toilet in one minute",
"answer": "Measure from the center of the two seat bolts to the front edge of the bowl. About 16 to 17 inches is round. About 18 to 19 inches is elongated. Enter your number below and we'll tell you which seats fit.",
"sections": lambda P: f"""
<div class="fitbox" id="fit">
  <h2>Fit checker</h2>
  <label for="fit-in">Bolt center to front of bowl (inches)</label>
  <input id="fit-in" type="number" inputmode="decimal" min="10" max="25" step="0.25" placeholder="e.g. 18.5">
  <button type="button" class="btn" id="fit-go">Check my fit</button>
  <div id="fit-out" role="status" aria-live="polite"></div>
  <noscript><p>The checker needs JavaScript. Use the rule above: about 16–17 in is round, about 18–19 in is elongated.</p></noscript>
</div>

<h2>How to measure, step by step</h2>
<ol>
<li>Lift the seat and lid.</li>
<li>Find the two bolts that hold the seat on, at the back of the bowl.</li>
<li>Put the end of a tape measure at the midpoint between the bolts.</li>
<li>Measure straight forward to the outside front edge of the bowl rim.</li>
<li>While you're there, measure the distance between the two bolts. Most toilets are about 5.5 inches apart.</li>
</ol>
<p>Those ranges match what major retailers publish (for example <a href="{LOWES_MEASURE}" rel="noopener">Lowe's guide to measuring a toilet seat</a>). If you land in between, say 17.5 inches, send us a photo with the tape in it and we'll check before you order.</p>

<h2>Which shape is better?</h2>
<table>
<thead><tr><th></th><th>Round</th><th>Elongated</th></tr></thead>
<tbody>
<tr><td>Front-to-back space</td><td>About 2 inches shorter</td><td>Needs more room</td></tr>
<tr><td>Comfort for adults</td><td>Fine for short visits</td><td>Most adults find it more comfortable</td></tr>
<tr><td>Best for</td><td>Small powder rooms, tight doors</td><td>Main bathrooms, accessibility, bidet seats</td></tr>
</tbody></table>
<p>Elongated is generally recommended for accessibility because it gives more seating surface. In a tight room, check the clearance in front of the bowl too: you need room to stand, turn and, if a walker is used, to bring it close.</p>

<h2>What fits what</h2>
<ul>
<li><strong>Elongated or round:</strong> {P("anzzi-smart-bidet-seat-auto-lid","Smart Bidet Seat (auto lid)")}, {P("anzzi-smart-bidet-seat-107","Smart Bidet Seat 107")}, {P("anzzi-two-piece-ada-toilet","Two-piece ADA toilet")}.</li>
<li><strong>Elongated only:</strong> {P("minnow-manual-bidet-seat","Minnow manual seat")}, {P("dive-smart-electric-bidet-seat","ENVO Dive")}.</li>
<li><strong>Covers either shape:</strong> {P("xl-comfort-round-toilet-seat","XL Comfort heavy-duty seat")}.</li>
</ul>

<h2>Don't forget the rough-in</h2>
<p>If you're replacing the whole toilet, also measure the rough-in: the distance from the finished wall behind the toilet to the center of the floor bolts. Most homes are 12 inches; some older homes are 10 or 14. A toilet built for the wrong rough-in either won't fit or leaves a gap behind the tank.</p>
""",
"faq": [
("How do I know if my toilet is round or elongated?", "Measure from the center between the seat bolts to the front edge of the bowl. Roughly 16 to 17 inches is round, roughly 18 to 19 inches is elongated."),
("Will an elongated seat fit a round toilet?", "No. It will overhang the front of the bowl and won't sit or seal properly. A few oversized heavy-duty seats are designed to cover both shapes, which the product page will say."),
("Is elongated or round better for seniors?", "Elongated, in most cases. The longer bowl gives more seating surface and is easier to use. Choose round only when the room is too tight for the extra length."),
("What is a toilet rough-in?", "The distance from the finished wall to the center of the drain (the floor bolts). Most U.S. homes use 12 inches. It matters when you replace the whole toilet, not when you replace only the seat."),
],
"script": "/assets/fit.js",
},
{
"path": "/upflush-toilet-basement/",
"crumb": "Upflush toilets",
"title": "Upflush Toilet for a Basement: Will It Work for You?",
"desc": "How upflush (macerating) toilets work, the three measurements that decide if one works in your basement, and the honest downsides.",
"h1": "Upflush toilets for basements: will one work for you?",
"answer": "An upflush toilet works when you can't put a drain under the floor. It sends waste into a sealed pump unit behind the toilet, which grinds it and pumps it through a small pipe up to your existing drain stack. It works if your run to the stack is within the pump's limits, you have a dedicated outlet, and you can vent it. It's the wrong choice if a gravity drain is easy to reach.",
"sections": lambda P: f"""
<h2>How it works</h2>
<p>A regular toilet drops waste straight down into a 3-inch drain and lets gravity do the rest. An upflush toilet discharges out the back into a sealed macerator box. Blades break down the waste, and a pump pushes it through a much smaller pipe (about 3/4 to 1 inch on most units) that can run up a wall and across a ceiling to the nearest drain stack. Because the pipe is small and pressurized, you don't need to break concrete.</p>

<h2>The three measurements that decide it</h2>
<ol>
<li><strong>Vertical lift.</strong> How far up the pipe has to go to reach the stack. The {P("nesso-upflush-macerating-toilet","ANZZI Nesso")} is rated for up to 26 feet vertical.</li>
<li><strong>Horizontal run.</strong> How far across. The Nesso is rated for up to 197 feet horizontal. Lift and run trade off against each other, so check the pump chart in the manual for your exact combination.</li>
<li><strong>Power.</strong> The pump plugs in. Plan a dedicated GFCI outlet close to the unit.</li>
</ol>
<p>Measure the route the pipe will actually take, not the straight-line distance, and count every elbow.</p>

<h2>It can drain more than the toilet</h2>
<p>Most units have extra inlets, so a sink and sometimes a shower in the same room can drain into the same pump. That's how a basement corner becomes a full bathroom. A shower usually needs the toilet raised a few inches or a small step-up so the shower drain can fall into the unit. Check the inlet heights before you frame anything.</p>

<h2>The honest downsides</h2>
<ul>
<li><strong>Noise.</strong> You'll hear the pump for a few seconds after each flush. Quieter than it used to be, still not silent.</li>
<li><strong>What goes in.</strong> Only toilet paper and waste. Wipes, even "flushable" ones, and hygiene products jam macerators. Put a sign up for guests.</li>
<li><strong>Venting.</strong> The unit needs a vent like any other fixture. Local plumbing code decides how; ask your local building department.</li>
<li><strong>Power outages.</strong> No power, no pump. Plan on not using it during an outage.</li>
<li><strong>Permits.</strong> Adding a bathroom usually needs a plumbing permit. Many inspectors accept macerating systems; some jurisdictions have specific rules. Ask before you buy.</li>
</ul>

<h2>When a gravity drain is the better answer</h2>
<p>If your basement already has a rough-in (capped pipes in the floor), or the main drain is close and below the slab, a regular toilet is simpler and has no pump to maintain. An upflush system makes the most sense when the alternative is cutting a trench through concrete.</p>

<h2>What to ask a plumber for</h2>
<p>Get at least two written quotes that list the unit, the pipe route, venting, the electrical work and the permit separately. That way you can see where the money goes and compare like for like.</p>
""",
"faq": [
("Do upflush toilets smell?", "A properly sealed and vented unit shouldn't. Smells usually point to a venting problem, a bad seal on the macerator lid, or something that shouldn't have been flushed."),
("Do upflush toilets need a vent?", "Yes, in most installations. The unit has a vent connection, and local plumbing code decides how it's run. Check with your building department."),
("How far can an upflush toilet pump?", "It depends on the unit. The ANZZI Nesso is rated for up to 26 feet up or 197 feet across. Higher lift reduces the horizontal distance; use the pump chart in the manual."),
("Can a shower drain into an upflush toilet?", "On units with extra inlets, often yes. The shower drain has to sit higher than the inlet so water can fall into it, which may mean a raised shower base."),
],
},
]

def render(g, products, fmt, price_date):
    P = lambda h, t=None: plink(products, h, fmt, t)
    faq = "".join(f"<h3>{esc(q)}</h3><p>{esc(a)}</p>" for q, a in g["faq"])
    script = f'<script src="{g["script"]}" defer></script>' if g.get("script") else ""
    return f"""
<article class="prose guide">
<h1>{esc(g["h1"])}</h1>
<p class="byline">By {AUTHOR} · Updated <time datetime="{UPDATED}">{UPDATED_TXT}</time> · Prices checked {price_date}</p>
<p class="answer">{esc(g["answer"])}</p>
{g["sections"](P)}
<h2>Questions people ask</h2>
{faq}
<div class="ctabox"><p><strong>Not sure which one fits?</strong> Send us your bowl measurement and a photo of the outlet area. We'll reply with a recommendation and a written quote.</p><a class="btn" href="/pages/contact/">Ask us</a></div>
</article>
{script}
"""

def article_schema(site, g):
    return [{"@context": "https://schema.org", "@type": "Article", "headline": g["h1"], "description": g["desc"],
             "author": {"@type": "Person", "name": AUTHOR}, "datePublished": UPDATED, "dateModified": UPDATED,
             "mainEntityOfPage": site + g["path"], "publisher": {"@type": "Organization", "name": "Buy Smart Toilet", "url": site + "/"}},
            {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in g["faq"]]}]

def hub():
    items = "".join(f'<li><a href="{g["path"]}">{esc(g["h1"])}</a><br><span>{esc(g["desc"])}</span></li>' for g in GUIDES)
    return f"""<article class="prose"><h1>Buying guides</h1>
<p class="answer">Straight answers on fit, power, height and price, written to help you pick the right fixture, including when the right answer is the cheaper one.</p>
<ul class="guidelist">{items}</ul></article>"""

# ---------------------------------------------------------------- static pages
def static_pages(products, fmt, lead):
    opts = "".join(f'<option value="{esc(p["handle"])}">{esc(p["title"].split(" — ")[0])}</option>' for p in products)
    form = f"""
<form class="quote" action="{lead}" method="post" id="quote">
  <input type="hidden" name="_subject" value="Quote request - buysmarttoilet.com">
  <input type="hidden" name="_next" value="https://buysmarttoilet.com/pages/contact/thanks/">
  <div class="hp" aria-hidden="true"><label for="q-h">Leave this empty</label><input id="q-h" type="text" name="_honey" tabindex="-1" autocomplete="off"></div>
  <label for="q-item">Product</label>
  <select id="q-item" name="product"><option value="">Not sure yet / need advice</option>{opts}</select>
  <label for="q-shape">Bowl shape</label>
  <select id="q-shape" name="bowl_shape"><option value="">Not sure</option><option>Round</option><option>Elongated</option></select>
  <label for="q-name">Your name</label>
  <input id="q-name" name="name" autocomplete="name" required maxlength="80">
  <label for="q-email">Email</label>
  <input id="q-email" name="email" type="email" autocomplete="email" required maxlength="120">
  <label for="q-phone">Phone (optional)</label>
  <input id="q-phone" name="phone" type="tel" autocomplete="tel" maxlength="30">
  <label for="q-zip">Delivery ZIP code</label>
  <input id="q-zip" name="zip" inputmode="numeric" pattern="[0-9]{{5}}" maxlength="5" required>
  <label for="q-msg">Anything we should know? (outlet nearby, who will use it, measurements)</label>
  <textarea id="q-msg" name="message" rows="4" maxlength="2000"></textarea>
  <label class="check"><input type="checkbox" name="consent" value="yes" required> You may contact me by email or phone about this request. No marketing lists.</label>
  <button class="btn" type="submit">Send request</button>
  <p class="small">We use your details only to answer this request. See our <a href="/privacy/">privacy notice</a>.</p>
</form>
<script src="/assets/lead-send.js" defer></script>
<script src="/assets/quote.js" defer></script>
"""
    return [
        {"path": "/pages/contact/", "title": "Request a Quote | Buy Smart Toilet",
         "desc": "Request a smart toilet, bidet seat or accessible toilet. We confirm price, stock and delivery in writing before you pay anything.",
         "crumbs": [("/", "Home"), ("/pages/contact/", "Request a quote")],
         "body": f"""<article class="prose"><h1>Request a quote</h1>
<p class="answer">Tell us what you're looking at and where it's going. We reply with the current price, stock, delivery method and an estimate in writing. Nothing is charged until you approve it.</p>
{form}</article>"""},
        {"path": "/pages/contact/thanks/", "title": "Request received | Buy Smart Toilet", "desc": "Thanks, your request was received.",
         "noindex": True, "crumbs": [("/", "Home"), ("/pages/contact/thanks/", "Thanks")],
         "body": """<article class="prose"><h1>Thanks, we have your request</h1><p>We'll reply by email with a written quote. While you wait, double-check your bowl shape with the <a href="/round-vs-elongated-toilet/">fit checker</a>.</p><p><a class="btn" href="/">Back to the shop</a></p></article>"""},
        {"path": "/about/", "title": "About Buy Smart Toilet", "desc": "Who runs Buy Smart Toilet, what we sell, and how ordering works while online checkout is being set up.",
         "crumbs": [("/", "Home"), ("/about/", "About")],
         "body": f"""<article class="prose"><h1>About Buy Smart Toilet</h1>
<p class="answer">Buy Smart Toilet is a small independent store run by {AUTHOR} in Denver, Colorado. We sell smart toilets, bidet seats and accessible toilets, and we write plain guides on choosing them.</p>
<h2>Why this store exists</h2>
<p>Most toilet and bidet pages are written to sell the most expensive option. Ours start from the problem: no outlet, a low seat, no drain, a seat that shifts. Sometimes the right answer is a $150 seat instead of a $1,200 toilet, and we'll say so.</p>
<h2>What we sell</h2>
<p>Right now our catalog is ANZZI products. We are an independent seller, not ANZZI, and manufacturer warranties are provided by the manufacturer as described on each product page and in the product manual.</p>
<h2>How ordering works</h2>
<p>Online checkout is being set up. Until then, <a href="/pages/contact/">request a quote</a> and we confirm price, stock and delivery in writing before any payment.</p>
</article>"""},
        {"path": "/privacy/", "title": "Privacy Notice | Buy Smart Toilet", "desc": "What Buy Smart Toilet collects when you request a quote, why, and how to ask us to delete it.",
         "crumbs": [("/", "Home"), ("/privacy/", "Privacy")],
         "body": """<article class="prose"><h1>Privacy notice</h1>
<p>Updated November 10, 2026.</p>
<h2>What we collect</h2><p>Only what you type into the quote form: name, email, optional phone, delivery ZIP code, the product you're asking about and your message. We also record the page you sent it from.</p>
<h2>Why</h2><p>To answer your request and prepare a quote. We don't sell your details or add you to marketing lists.</p>
<h2>Cookies and tracking</h2><p>This site sets no advertising cookies.</p>
<h2>Deleting your details</h2><p>Reply to any email from us and ask, and we'll delete your request.</p>
</article>"""},
    ]
