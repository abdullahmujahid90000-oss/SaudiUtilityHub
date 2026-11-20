#!/usr/bin/env python3
"""Idempotent wiring for the Arabic pages: hreflang + switch on English twins, sitemap entries,
'read also' blocks and nav/footer links on the older Arabic pages."""
import re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from build_arabic_pages import PAGES, ARM, SITE, u
NEW = [p["slug"] for p in PAGES]
# 1. English twins
for s in NEW + ["guides"]:
    f = f"{s}.html"; h = open(f, encoding="utf8").read()
    ar = f"{SITE}/ar/{s}.html"
    if f'hreflang="ar" rel="alternate"' not in h:
        canon = f'<link href="{SITE}/{s}.html" rel="canonical"/>'
        assert canon in h, s
        h = h.replace(canon, canon + f'\n<link href="{SITE}/{s}.html" hreflang="en" rel="alternate"/>\n<link href="{ar}" hreflang="ar" rel="alternate"/>\n<link href="{SITE}/{s}.html" hreflang="x-default" rel="alternate"/>', 1)
    if 'class="lang-switch"' not in h:
        sw = f'<a class="lang-switch" href="{ar}" hreflang="ar" lang="ar" style="display:inline-block;margin-bottom:1rem;font-weight:600;color:#0a7c3e;text-decoration:none">🇸🇦 اقرأ هذه الصفحة بالعربية</a>\n'
        m = re.search(r'<div class="hero"|<h1', h)
        h = h[:m.start()] + sw + h[m.start():]
    open(f, "w", encoding="utf8").write(h)
# 2. sitemap
sm = open("sitemap.xml", encoding="utf8").read()
add = ""
for s in NEW + ["guides"]:
    if f"/ar/{s}.html</loc>" in sm: continue
    add += f'''  <url>
    <loc>{SITE}/ar/{s}.html</loc>
    <lastmod>2026-11-20</lastmod>
    <xhtml:link rel="alternate" hreflang="ar" href="{SITE}/ar/{s}.html"/>
    <xhtml:link rel="alternate" hreflang="en" href="{SITE}/{s}.html"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE}/{s}.html"/>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
'''
if add: sm = sm.replace("</urlset>", add + "</urlset>")
open("sitemap.xml", "w", encoding="utf8").write(sm)
# 3. older Arabic pages
OLD = ["index","salary-calculator","gosi-calculator","ksa-eos-calculator","iqama-expiry-calculator"]
PICK = {"index": ["notice-period-saudi-labour-law","iqama-renewal-fees","final-settlement-calculator","leave-calculator"],
 "salary-calculator": ["overtime-calculator","leave-calculator","dependent-levy-calculator","final-settlement-calculator"],
 "gosi-calculator": ["overtime-calculator","final-settlement-calculator","notice-period-saudi-labour-law","iqama-renewal-fees"],
 "ksa-eos-calculator": ["notice-period-saudi-labour-law","final-settlement-calculator","what-happens-to-iqama-if-you-resign","salary-not-paid-saudi-arabia"],
 "iqama-expiry-calculator": ["iqama-renewal-fees","dependent-levy-calculator","exit-reentry-calculator","what-happens-to-iqama-if-you-resign"]}
for s in OLD:
    f = f"ar/{s}.html"; h = open(f, encoding="utf8").read()
    if "<!-- suh:ar-more -->" not in h:
        cards = "\n".join(f'<div class="related-card"><h3>{ARM[x][1]}</h3><p>{ARM[x][2]}</p><a href="{u(x)}">افتح الصفحة ←</a></div>' for x in PICK[s])
        blk = f'<!-- suh:ar-more -->\n<div class="container"><h2>اقرأ أيضًا</h2>\n<div class="related-grid">\n{cards}\n</div>\n<p><a href="{SITE}/ar/guides.html">← تصفّح كل الأدلة والحاسبات</a></p></div>\n<!-- /suh:ar-more -->\n'
        anchor = "<!-- suh:author -->" if "<!-- suh:author -->" in h else "<footer>"
        h = h.replace(anchor, blk + anchor, 1)
    if "/ar/guides.html\">الأدلة" not in h:
        h = h.replace(f'<li><a href="{SITE}/ar/iqama-expiry-calculator.html">الإقامة</a></li>\n</ul>\n</nav>', f'<li><a href="{SITE}/ar/iqama-expiry-calculator.html">الإقامة</a></li>\n<li><a href="{SITE}/ar/guides.html">الأدلة</a></li>\n</ul>\n</nav>', 1)
    open(f, "w", encoding="utf8").write(h)
print("wired")
