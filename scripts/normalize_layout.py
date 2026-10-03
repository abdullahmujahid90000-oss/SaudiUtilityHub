#!/usr/bin/env python3
"""Apply the shared Saudi Utility Hub header, footer and head hygiene to every
English page in the site root.

Run from the repository root:  python3 scripts/normalize_layout.py

Safe to re-run: the header and footer live between <!-- suh:header --> /
<!-- suh:footer --> markers and are simply regenerated on later runs. To change
the navigation or footer links sitewide, edit NAV / FOOTER_COLUMNS below and
re-run the script.
"""
import glob
import os
import re
import sys

SITE = "https://www.saudiutilityhub.com"

# Pages that generate employer documents (letters, certificates, payslips).
# They stay reachable for existing visitors but are kept out of search and
# carry no advertising: AdSense's "dishonest behaviour" policy covers tools
# that can be used to produce documents a person would present as issued by
# someone else, and they are the riskiest pages to show a reviewer.
NOINDEX_NO_ADS = {
    "experience-letter-generator.html",
    "noc-letter-generator.html",
    "salary-certificate.html",
    "salary-slip-generator.html",
}

NAV = [
    ("Salary", "/salary-calculator.html"),
    ("GOSI", "/gosi-calculator.html"),
    ("End of Service", "/ksa-eos-calculator.html"),
    ("Leave", "/leave-calculator.html"),
    ("Iqama", "/iqama-expiry-calculator.html"),
    ("All Tools", "/#all-tools"),
    ("About", "/about.html"),
]

FOOTER_COLUMNS = [
    ("Salary &amp; Labour Law", [
        ("Salary Calculator", "/salary-calculator.html"),
        ("Gross-to-Net Salary Table", "/gross-to-net-salary-saudi-arabia.html"),
        ("GOSI Calculator", "/gosi-calculator.html"),
        ("End of Service Calculator", "/ksa-eos-calculator.html"),
        ("EOS Payouts by Salary (Data)", "/eos-payouts-by-salary-2026.html"),
        ("Final Settlement Calculator", "/final-settlement-calculator.html"),
        ("Annual Leave Calculator", "/leave-calculator.html"),
        ("Working Hours Calculator", "/working-hours-calculator.html"),
        ("Overtime Calculator", "/overtime-calculator.html"),
        ("Probation Calculator", "/probation-calculator.html"),
    ]),
    ("Iqama &amp; Visas", [
        ("Iqama Expiry Planner", "/iqama-expiry-calculator.html"),
        ("Iqama Renewal Fees", "/iqama-renewal-fees.html"),
        ("Iqama Transfer Worksheet", "/iqama-transfer-calculator.html"),
        ("Dependent Levy Calculator", "/dependent-levy-calculator.html"),
        ("Exit / Re-entry Planner", "/exit-reentry-calculator.html"),
        ("Family Visit Visa Guide", "/family-visit-visa-guide.html"),
        ("Family Residence Visa Guide", "/family-residence-visa.html"),
        ("5-Year Resident ID Guide", "/5-year-resident-id-guide-2026.html"),
        ("Umrah Visa Guide", "/umrah-visa-guide.html"),
    ]),
    ("Living in Saudi Arabia", [
        ("Electricity Bill Calculator", "/sec-electricity-bill-calculator.html"),
        ("Water Bill Calculator", "/nwc-water-bill-calculator.html"),
        ("Fuel Cost Calculator", "/fuel-cost-calculator.html"),
        ("Cost of Living Dashboard", "/expat-affordability-dashboard.html"),
        ("Gold Price Calculator", "/gold-prices.html"),
        ("Traffic Fine Calculator", "/traffic-fine-calculator.html"),
        ("Home Finance Calculator", "/mortgage-calculator.html"),
        ("Islamic Finance Calculator", "/islamic-finance-calculator.html"),
        ("Driving Licence Conversion", "/driving-license-conversion.html"),
    ]),
    ("Saudi Utility Hub", [
        ("About Us", "/about.html"),
        ("Editorial Policy", "/editorial-team.html"),
        ("Contact", "/contact.html"),
        ("Privacy Policy", "/privacy.html"),
        ("Terms of Use", "/terms.html"),
        ("العربية", "/ar"),
    ]),
]


def build_header(page):
    links = []
    for label, path in NAV:
        cur = ' aria-current="page"' if path.lstrip("/") == page or (path == "/#all-tools" and page == "index.html") else ""
        links.append(f'<a href="{SITE}{path}"{cur}>{label}</a>')
    links.append(f'<a class="suh-lang" href="{SITE}/ar" hreflang="ar" lang="ar">العربية</a>')
    return (
        "<!-- suh:header -->\n"
        '<div class="suh-header" role="banner">\n'
        '<div class="suh-wrap">\n'
        f'<a class="suh-brand" href="{SITE}/">Saudi<span>Utility</span>Hub</a>\n'
        '<div class="suh-nav" role="navigation" aria-label="Main">\n'
        + "\n".join(links)
        + "\n</div>\n</div>\n</div>\n<!-- /suh:header -->"
    )


def build_footer():
    cols = []
    for heading, items in FOOTER_COLUMNS:
        lis = "\n".join(f'<li><a href="{SITE}{p}">{t}</a></li>' for t, p in items)
        cols.append(f'<div>\n<p class="suh-fh">{heading}</p>\n<ul>\n{lis}\n</ul>\n</div>')
    return (
        "<!-- suh:footer -->\n"
        '<div class="suh-footer" role="contentinfo">\n'
        '<div class="suh-wrap suh-fgrid">\n'
        + "\n".join(cols)
        + "\n</div>\n"
        '<div class="suh-wrap suh-fnote">\n'
        "<p>Saudi Utility Hub is an independent website. It is not affiliated with GOSI, the Ministry of Human Resources "
        "and Social Development, Qiwa, Absher, Muqeem, Jawazat or any other Saudi government body. Calculator results "
        "are estimates — confirm anything binding with your employer or the official service.</p>\n"
        f'<p>© 2026 Saudi Utility Hub · <a href="mailto:info@saudiutilityhub.com">info@saudiutilityhub.com</a></p>\n'
        "</div>\n</div>\n<!-- /suh:footer -->"
    )


def balanced_end(html, start, tag):
    """Return the index just past the element opened at `start`."""
    depth = 0
    pat = re.compile(rf"<(/?){tag}\b[^>]*>", re.I)
    for m in pat.finditer(html, start):
        depth += -1 if m.group(1) else 1
        if depth == 0:
            return m.end()
    raise ValueError(f"unbalanced <{tag}>")


def replace_header(html, page):
    new = build_header(page)
    if "<!-- suh:header -->" in html:
        return re.sub(r"<!-- suh:header -->[\s\S]*?<!-- /suh:header -->", lambda _: new, html, count=1)
    body = re.search(r"<body[^>]*>", html, re.I).end()
    h1 = html.find("<h1", body)
    for m in re.finditer(r"<(header|nav)\b([^>]*)>", html[body:], re.I):
        if "breadcrumb" in m.group(2).lower():
            continue
        s = body + m.start()
        if h1 != -1 and s > h1:
            break
        e = balanced_end(html, s, m.group(1))
        return html[:s] + new + html[e:]
    # No legacy site header: put the shared one straight after <body>.
    return html[:body] + "\n" + new + html[body:]


def replace_footer(html):
    new = build_footer()
    if "<!-- suh:footer -->" in html:
        return re.sub(r"<!-- suh:footer -->[\s\S]*?<!-- /suh:footer -->", lambda _: new, html, count=1)
    spans = []
    for m in re.finditer(r"<footer\b[^>]*>", html, re.I):
        if spans and m.start() < spans[-1][1]:
            continue
        spans.append((m.start(), balanced_end(html, m.start(), "footer")))
    if not spans:
        return html.replace("</body>", new + "\n</body>", 1)
    for s, e in reversed(spans[1:]):
        html = html[:s] + html[e:]
    s, e = spans[0]
    return html[:s] + new + html[e:]


GA_RE = re.compile(
    r"[ \t]*<script async(?:=\"\")? src=\"https://www\.googletagmanager\.com/gtag/js\?id=G-[A-Z0-9]+\"></script>\s*"
    r"<script>[\s\S]*?gtag\(\s*'config'\s*,\s*'G-[A-Z0-9]+'\s*\);?\s*</script>\n?"
)
AD_SLOT_RE = re.compile(
    r"[ \t]*<div class=\"ad-[a-z-]*\"[^>]*>\s*<ins class=\"adsbygoogle\"[\s\S]*?</ins>\s*"
    r"<script>\s*\(adsbygoogle\s*=\s*window\.adsbygoogle\s*\|\|\s*\[\]\)\.push\(\{\}\);?\s*</script>\s*</div>\n?"
)
LONE_AD_RE = re.compile(
    r"[ \t]*<ins class=\"adsbygoogle\"[\s\S]*?</ins>\s*"
    r"(?:<script>\s*\(adsbygoogle\s*=\s*window\.adsbygoogle\s*\|\|\s*\[\]\)\.push\(\{\}\);?\s*</script>)?\n?"
)
ADS_LOADER_RE = re.compile(
    r"[ \t]*<script async[^>]*src=\"https://pagead2\.googlesyndication\.com/pagead/js/adsbygoogle\.js\?client=ca-pub-\d+\"[^>]*></script>\n?"
)
KEYWORDS_RE = re.compile(r"[ \t]*<meta\s+(?:name=\"keywords\"\s+content=\"[^\"]*\"|content=\"[^\"]*\"\s+name=\"keywords\")\s*/?>\n?", re.I)
GTM_HINT_RE = re.compile(r"[ \t]*<link[^>]+href=\"https://www\.googletagmanager\.com\"[^>]*>\n?")
ROBOTS_RE = re.compile(r"<meta\s+(?:name=\"robots\"\s+content=\"[^\"]*\"|content=\"[^\"]*\"\s+name=\"robots\")\s*/?>", re.I)
# Old per-page cookie bars whose "Decline" button only hid the bar. The real
# notice (assets/cookie-consent.js) is loaded on every page.
LEGACY_BANNER_JS_RE = re.compile(r"[ \t]*function (?:accept|decline)Cookies\(\) \{ document\.getElementById\('cookieBanner'\)\.style\.display = 'none'; \}\n?")
AD_PUSH_ON_LOAD_RE = re.compile(
    r"[ \t]*window\.addEventListener\('load', \(\) => \{\s*if \(typeof adsbygoogle !== 'undefined'\) \{\s*try \{\s*"
    r"(?:\(adsbygoogle = window\.adsbygoogle \|\| \[\]\)\.push\(\{\}\);\s*)+\} catch \(e\) \{\}\s*\}\s*\}\);\n?"
)
GA_COMMENT_RE = re.compile(r"[ \t]*<!-- Google Analytics GA4[^>]*-->\n?")
CSS_LINK = '<link rel="stylesheet" href="/assets/site.css" />'


def process(path):
    page = os.path.basename(path)
    html = open(path, encoding="utf-8").read()
    orig = html

    html = GA_RE.sub("", html)          # GA is now loaded once, sitewide, by assets/cookie-consent.js
    html = GTM_HINT_RE.sub("", html)
    html = AD_SLOT_RE.sub("", html)     # empty manual ad boxes; Auto ads places units after approval
    html = LONE_AD_RE.sub("", html)
    html = KEYWORDS_RE.sub("", html)
    html = GA_COMMENT_RE.sub("", html)
    i = html.find('<div class="cookie-banner" id="cookieBanner">')
    if i != -1:
        html = html[:i] + html[balanced_end(html, i, "div"):]
    html = LEGACY_BANNER_JS_RE.sub("", html)
    html = AD_PUSH_ON_LOAD_RE.sub("", html)

    if page in NOINDEX_NO_ADS:
        html = ADS_LOADER_RE.sub("", html)
        html = ROBOTS_RE.sub('<meta name="robots" content="noindex, follow" />', html, count=1)

    if CSS_LINK not in html:
        html = html.replace("</head>", CSS_LINK + "\n</head>", 1)

    html = replace_header(html, page)
    html = replace_footer(html)

    # The /blog/ section no longer exists; its URL only redirects to the homepage.
    html = html.replace(f'href="{SITE}/blog/"', f'href="{SITE}/"')

    if html != orig:
        open(path, "w", encoding="utf-8").write(html)
        return True
    return False


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(root)
    changed = [p for p in sorted(glob.glob("*.html")) if process(p)]
    print(f"updated {len(changed)} pages")
    for p in changed:
        print("  " + p)
    leftovers = [p for p in glob.glob("*.html") if "<ins class=\"adsbygoogle" in open(p, encoding="utf-8").read()]
    if leftovers:
        print("WARNING: manual ad units still present in:", leftovers, file=sys.stderr)


if __name__ == "__main__":
    main()
