"""Static site generator for buysmarttoilet.com (replaces the Shopify store, Nov 2026).

Run:  python -I _src/build.py <path-to-products.json>
Reads the Shopify products.json export, writes every page at the SAME paths the
Shopify store used (/products/<handle>/, /pages/contact/, ...) so old URLs keep working.
Guide copy lives in _src/guides.py. No checkout: every buy button opens the quote form.
"""
import html, json, os, re, sys, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import guides  # noqa: E402

SITE = "https://buysmarttoilet.com"
NAME = "Buy Smart Toilet"
TODAY = datetime.date(2026, 11, 10)
PRICE_DATE = "November 10, 2026"
LEAD = "https://clients.eyetoad.com/lead/send.php"
DEFAULT_OG = [""]

CSP = ("default-src 'self'; img-src 'self' https://cdn.shopify.com data:; script-src 'self'; "
       "style-src 'self'; connect-src https://clients.eyetoad.com; form-action https://clients.eyetoad.com; "
       "base-uri 'self'; object-src 'none'")

GROUPS = [
    ("Smart toilets", ["Smart Toilet"]),
    ("Bidet seats", ["Bidet Seat"]),
    ("Toilets", ["Toilet"]),
    ("Upflush toilets", ["Upflush Toilet", "Macerating Toilet"]),
    ("Seats", ["Toilet Seat"]),
]

def esc(s):
    return html.escape(str(s), quote=True)

def money(v):
    v = float(v)
    return "${:,.2f}".format(v).replace(".00", "") if v != int(v) or True else ""

def fmt(v):
    v = float(v)
    s = "${:,.2f}".format(v)
    return s[:-3] if s.endswith(".00") else s

def write(path, content):
    full = os.path.join(ROOT, path.strip("/"), "index.html") if not path.endswith(".html") and not path.endswith(".xml") and not path.endswith(".txt") else os.path.join(ROOT, path.strip("/"))
    if path == "/":
        full = os.path.join(ROOT, "index.html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

NAV = [("/#shop", "Shop"), ("/guides/", "Guides"), ("/round-vs-elongated-toilet/", "Fit checker"), ("/about/", "About")]

def page(path, title, desc, body, schema=None, crumbs=None, og_img=None, noindex=False):
    canon = SITE + path
    ld = []
    if schema:
        ld.extend(schema if isinstance(schema, list) else [schema])
    if crumbs:
        ld.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (u, n) in enumerate(crumbs)]})
    ld_html = "".join('<script type="application/ld+json">%s</script>\n' % json.dumps(x, ensure_ascii=False).replace("</", "<\\/") for x in ld)
    crumb_html = ""
    if crumbs and len(crumbs) > 1:
        parts = ['<a href="%s">%s</a>' % (u, esc(n)) for u, n in crumbs[:-1]] + ['<span aria-current="page">%s</span>' % esc(crumbs[-1][1])]
        crumb_html = '<nav class="crumbs" aria-label="Breadcrumb">%s</nav>' % " / ".join(parts)
    nav = "".join('<a href="%s">%s</a>' % (u, t) for u, t in NAV)
    og = og_img or DEFAULT_OG[0]
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="{CSP}">
<meta name="referrer" content="strict-origin-when-cross-origin">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canon}">
{'<meta name="robots" content="noindex">' if noindex else ''}
<meta property="og:type" content="website">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{esc(og)}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/site.css">
{ld_html}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top">
  <div class="wrap bar">
    <a class="brand" href="/" aria-label="{NAME} home"><span class="mark" aria-hidden="true">B</span><span>Buy<b>Smart</b>Toilet</span></a>
    <nav class="mainnav" aria-label="Main">{nav}</nav>
    <a class="btn btn-sm" href="/pages/contact/">Get a quote</a>
  </div>
</header>
<main id="main" class="wrap">
{crumb_html}
{body}
</main>
<footer class="foot">
  <div class="wrap cols">
    <div><p class="fbrand">Buy<b>Smart</b>Toilet</p>
      <p>Smart toilets, bidet seats and accessible toilets, explained plainly. Independent store based in Denver, Colorado. We are not ANZZI or any other manufacturer.</p></div>
    <div><p class="fh">Shop</p><ul>
      <li><a href="/#shop">All products</a></li><li><a href="/pages/contact/">Request a quote</a></li></ul></div>
    <div><p class="fh">Guides</p><ul>
      <li><a href="/smart-toilet-vs-bidet-seat/">Smart toilet or bidet seat?</a></li>
      <li><a href="/smart-toilet-for-seniors/">For older adults and caregivers</a></li>
      <li><a href="/round-vs-elongated-toilet/">Round or elongated fit checker</a></li>
      <li><a href="/upflush-toilet-basement/">Upflush toilets for basements</a></li></ul></div>
    <div><p class="fh">Company</p><ul>
      <li><a href="/about/">About</a></li><li><a href="/privacy/">Privacy</a></li></ul></div>
  </div>
  <p class="wrap small">Prices shown were checked {PRICE_DATE} and are confirmed in writing before any payment. &copy; 2026 BuySmartToilet.com</p>
</footer>
</body>
</html>
"""

# ---------- products ----------
PRICE_FIXES = []  # filled after load: (old text, new text)

def clean_body(b, prices):
    b = b or ""
    b = re.sub(r"\s(style|class|data-[\w-]+)=\"[^\"]*\"", "", b)
    b = b.replace("<h3>", "<h2>").replace("</h3>", "</h2>")
    # The Shopify copy quoted old prices for sibling products; point those at today's prices.
    for old, new in prices:
        b = b.replace(old, new)
    return b

def kind(p):
    t = p["product_type"]
    return t

def short_title(p):
    return p["title"].split(" — ")[0].replace("ANZZI ", "ANZZI ")

def product_page(p, all_products):
    h = p["handle"]
    path = f"/products/{h}/"
    st = short_title(p)
    vs = p["variants"]
    prices = sorted(float(v["price"]) for v in vs)
    lo, hi = prices[0], prices[-1]
    price_txt = fmt(lo) if lo == hi else f"{fmt(lo)}–{fmt(hi)}"
    compare = [v for v in vs if v.get("compare_at_price") and float(v["compare_at_price"]) > float(v["price"])]
    imgs = p["images"][:5]
    main_img = imgs[0]["src"] if imgs else ""
    alt = esc(st)
    thumbs = "".join(f'<img src="{esc(i["src"])}?width=320" width="160" height="160" decoding="async" alt="{alt}, view {n+2}">' for n, i in enumerate(imgs[1:5]))
    var_rows = "".join(f'<tr><td>{esc(v["title"] if v["title"] != "Default Title" else st)}</td><td>{esc(v["sku"])}</td><td>{fmt(v["price"])}' +
                       (f' <s>{fmt(v["compare_at_price"])}</s>' if v.get("compare_at_price") and float(v["compare_at_price"]) > float(v["price"]) else "") + '</td></tr>' for v in vs)
    tags = p.get("tags", [])
    ship = "Freight (LTL) delivery" if "LTL Freight" in tags or p["product_type"] in ("Smart Toilet", "Toilet") else "Small-parcel delivery"
    if "Small Parcel" in tags:
        ship = "Small-parcel delivery"
    others = [q for q in all_products if q["handle"] != h]
    same = [q for q in others if q["product_type"] == p["product_type"]]
    diff = [q for q in others if q["product_type"] != p["product_type"]]
    idx = all_products.index(p)
    related = same[:1] + [diff[(idx + k) % len(diff)] for k in range(2)] if diff else same[:3]
    rel_html = "".join(card(q) for q in related)
    guide_link = guides.GUIDE_FOR_TYPE.get(p["product_type"], ("/smart-toilet-vs-bidet-seat/", "Smart toilet or bidet seat? How to choose"))
    body = f"""
<article class="product">
  <div class="pgrid">
    <div class="gallery">
      <img class="hero-img" src="{esc(main_img)}?width=900" width="600" height="600" alt="{alt}" fetchpriority="high">
      <div class="thumbs">{thumbs}</div>
    </div>
    <div class="buy">
      <p class="eyebrow">{esc(p["vendor"])} · {esc(p["product_type"])}</p>
      <h1>{esc(p["title"])}</h1>
      <p class="price">{price_txt}{' <span class="was">was ' + fmt(compare[0]["compare_at_price"]) + '</span>' if compare and len(vs) == 1 else (' <span class="note">sale on some options</span>' if compare else '')}</p>
      <p class="note">Checked {PRICE_DATE}. Confirmed in writing before you pay.</p>
      <a class="btn" href="/pages/contact/?item={esc(h)}">Request this item</a>
      <ul class="facts">
        <li>{ship}</li>
        <li>{('Choose ' + ' or '.join(esc(v['title']) for v in vs) + ' when you request it') if 1 < len(vs) <= 2 else (str(len(vs)) + ' options, listed with SKUs below' if len(vs) > 2 else 'One size')}</li>
        <li>Need help with fit? Try the <a href="/round-vs-elongated-toilet/">round vs elongated fit checker</a></li>
      </ul>
    </div>
  </div>
  <div class="prose">
    {clean_body(p["body_html"], PRICE_FIXES)}
    <h2>Models and SKUs</h2>
    <table><thead><tr><th>Option</th><th>Manufacturer SKU</th><th>Price</th></tr></thead><tbody>{var_rows}</tbody></table>
    <p>Still deciding? Read <a href="{guide_link[0]}">{esc(guide_link[1])}</a>.</p>
  </div>
</article>
<section class="related"><h2>Compare with</h2><div class="cards">{rel_html}</div></section>
"""
    offers = [{"@type": "Offer", "price": "%.2f" % float(v["price"]), "priceCurrency": "USD", "sku": v["sku"],
               "availability": "https://schema.org/InStock", "url": SITE + path,
               "priceValidUntil": "2026-12-31"} for v in vs]
    schema = {"@context": "https://schema.org", "@type": "Product", "name": p["title"], "brand": {"@type": "Brand", "name": p["vendor"]},
              "image": [i["src"] for i in imgs], "description": re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", clean_body(p["body_html"], PRICE_FIXES)))[:300].strip(),
              "sku": vs[0]["sku"], "offers": offers}
    desc = f"{st}: {price_txt}. " + re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", clean_body(p["body_html"], PRICE_FIXES)))[:110].strip()
    desc = desc[:152].rsplit(" ", 1)[0] + "…"
    title = f"{st[:45]} | {price_txt}"
    return path, page(path, title, desc, body, schema, [("/", "Home"), ("/#shop", p["product_type"] + "s"), (path, st)], og_img=main_img)

def card(q):
    st = short_title(q)
    pr = sorted(float(v["price"]) for v in q["variants"])
    src = q["images"][0]["src"] if q["images"] else ""
    return (f'<a class="card" href="/products/{q["handle"]}/"><img src="{esc(src)}?width=480" width="240" height="240" loading="lazy" alt="{esc(st)}">'
            f'<span class="ct">{esc(st)}</span><span class="cp">{fmt(pr[0])}{"+" if pr[0] != pr[-1] else ""}</span></a>')

def main():
    src = sys.argv[1]
    products = json.load(open(src, encoding="utf-8"))["products"]
    DEFAULT_OG[0] = next((p["images"][0]["src"] for p in products if p["product_type"] == "Smart Toilet" and p["images"]), products[0]["images"][0]["src"])
    by = {p["handle"]: p for p in products}
    def price_of(handle):
        return fmt(min(float(v["price"]) for v in by[handle]["variants"]))
    # Fix stale cross-references in the Shopify copy.
    # Measurement and pricing lines in the Shopify copy that were wrong.
    PRICE_FIXES.append(("Measure from your seat bolts to the front rim first — about 18.5 inches means round, about 20.5 means elongated. Note the round version is currently the better-priced of the two.",
                        "Measure from the midpoint between your seat bolts to the front of the rim first: about 16 to 17 inches is round, about 18 to 19 is elongated. Our <a href=\"/round-vs-elongated-toilet/\">fit checker</a> will tell you."))
    PRICE_FIXES.append(("measure from the seat bolts to the front rim. Roughly 18.5 inches is round; roughly 20.5 inches is elongated.",
                        "measure from the midpoint between the seat bolts to the front of the rim. Roughly 16 to 17 inches is round; roughly 18 to 19 inches is elongated (<a href=\"/round-vs-elongated-toilet/\">fit checker</a>)."))
    if "minnow-manual-bidet-seat" in by:
        PRICE_FIXES.append(("$99.99", price_of("minnow-manual-bidet-seat")))
    if "anzzi-smart-bidet-seat-auto-lid" in by:
        PRICE_FIXES.append(("$239.20", price_of("anzzi-smart-bidet-seat-auto-lid")))
    if "anzzi-smart-bidet-seat-107" in by:
        PRICE_FIXES.append(("$279.20", price_of("anzzi-smart-bidet-seat-107")))
        a = min(float(v["price"]) for v in by["anzzi-smart-bidet-seat-auto-lid"]["variants"])
        b = min(float(v["price"]) for v in by["anzzi-smart-bidet-seat-107"]["variants"])
        diff = int(round(b - a))
        words = {40: "forty", 50: "fifty", 60: "sixty"}
        PRICE_FIXES.append(("forty dollars apart", f"{words.get(diff, str(diff))} dollars apart"))
        PRICE_FIXES.append(("extra $40", f"extra ${diff}"))
        PRICE_FIXES.append(("worth the $40", f"worth the ${diff}"))

    urls = []
    for p in products:
        path, content = product_page(p, products)
        write(path, content); urls.append(path)

    # Home
    sections = []
    for label, types in GROUPS:
        items = [p for p in products if p["product_type"] in types]
        if items:
            sections.append(f'<h3 class="grp">{label}</h3><div class="cards">' + "".join(card(q) for q in items) + "</div>")
    seen = {t for _, ts in GROUPS for t in ts}
    other = [p for p in products if p["product_type"] not in seen]
    if other:
        sections.append('<h3 class="grp">More</h3><div class="cards">' + "".join(card(q) for q in other) + "</div>")
    home_body = guides.home(products, fmt, "".join(sections))
    write("/", page("/", "Smart Toilets & Bidet Seats, Explained Plainly | Buy Smart Toilet",
                    "Smart toilets, bidet seats, comfort-height and upflush toilets with straight answers on fit, power and price. Request a quote; we confirm before you pay.",
                    home_body, guides.home_schema(SITE, products), None))
    urls.insert(0, "/")

    # Guides + static pages
    for g in guides.GUIDES:
        write(g["path"], page(g["path"], g["title"], g["desc"], guides.render(g, products, fmt, PRICE_DATE), guides.article_schema(SITE, g),
                              [("/", "Home"), ("/guides/", "Guides"), (g["path"], g["crumb"])]))
        urls.append(g["path"])
    write("/guides/", page("/guides/", "Smart Toilet & Bidet Seat Buying Guides | Buy Smart Toilet",
                           "Plain-English guides: smart toilet vs bidet seat, picks for older adults, round vs elongated fit checker and upflush toilets for basements.",
                           guides.hub(), None, [("/", "Home"), ("/guides/", "Guides")]))
    urls.append("/guides/")
    for sp in guides.static_pages(products, fmt, LEAD):
        write(sp["path"], page(sp["path"], sp["title"], sp["desc"], sp["body"], None, sp.get("crumbs"), noindex=sp.get("noindex", False)))
        if not sp.get("noindex"):
            urls.append(sp["path"])

    # Old Shopify URLs that have no direct equivalent: forward them.
    for old, new in [("/collections/frontpage/", "/#shop"), ("/collections/all/", "/#shop"), ("/collections/", "/#shop"),
                     ("/products/", "/#shop"), ("/blogs/news/", "/guides/"), ("/pages/data-sharing-opt-out/", "/privacy/"),
                     ("/cart/", "/pages/contact/"), ("/account/", "/")]:
        write(old, redirect_stub(new))

    write("/sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
          "".join(f"  <url><loc>{SITE}{u}</loc><lastmod>{TODAY.isoformat()}</lastmod></url>\n" for u in urls) + "</urlset>\n")
    write("/robots.txt", f"User-agent: *\nAllow: /\nDisallow: /_src/\nSitemap: {SITE}/sitemap.xml\n")
    print("built", len(urls), "indexable pages")

def redirect_stub(target):
    t = SITE + target
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Moved</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="canonical" href="{t}"><meta http-equiv="refresh" content="0; url={target}">
</head><body><p>This page moved: <a href="{target}">{t}</a></p></body></html>
"""

if __name__ == "__main__":
    main()
