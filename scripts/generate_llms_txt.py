#!/usr/bin/env python3
"""Generate /llms.txt (a plain-text site guide for AI assistants) from sitemap.xml.
Run from the repo root:  python3 scripts/generate_llms_txt.py
Titles and descriptions are read from each page, so re-run after publishing new pages.
"""
import re, html
SITE = "https://www.saudiutilityhub.com/"
GROUPS = [
 ("End of service, notice and leaving a job", ["ksa-eos-calculator","final-settlement-calculator","eos-payouts-by-salary-2026","notice-period-saudi-labour-law","probation-calculator","what-happens-to-iqama-if-you-resign","company-closed-end-of-service-saudi-arabia","salary-not-paid-saudi-arabia","how-to-file-a-labour-complaint-saudi-arabia","employer-holding-passport-saudi-arabia","final-exit-vs-exit-reentry-visa","exit-reentry-calculator"]),
 ("Salary, GOSI and working conditions", ["salary-calculator","gosi-calculator","gross-to-net-salary-saudi-arabia","overtime-calculator","working-hours-calculator","leave-calculator","sick-leave-maternity-leave-saudi-arabia"]),
 ("Iqama and residency", ["iqama-expiry-calculator","iqama-renewal-fees","renew-iqama-with-expired-passport","iqama-transfer-calculator","muqeem-visa-check","5-year-resident-id-guide-2026","premium-residency-cost-calculator"]),
 ("Family, dependents and visas", ["dependent-levy-calculator","family-visa-cost-calculator","family-visit-visa-guide","family-residence-visa","musaned-calculator","umrah-visa-guide"]),
 ("About, sources and policies", ["about","editorial-team","contact","disclaimer","privacy","terms","guides"]),
]
def meta(slug):
    h = open(slug + ".html", encoding="utf8").read()
    t = re.search(r"<title>(.*?)</title>", h, re.S).group(1)
    t = re.sub(r"^[^\w(]+", "", html.unescape(t).strip())
    m = re.search(r'<meta content="([^"]*)" name="description"', h) or re.search(r'<meta name="description" content="([^"]*)"', h)
    d = html.unescape(m.group(1)).strip() if m else ""
    if len(d) > 180:
        cut = d[:180]
        d = cut[: cut.rfind(" ")].rstrip(",;:") + "..."
    return t, d
out = [
 "# Saudi Utility Hub",
 "",
 "> Free calculators and plain-English guides for expats working and living in Saudi Arabia: end-of-service pay, GOSI, salary, iqama, exit/re-entry, dependent fees and family visas. Figures follow official Saudi sources (HRSD, GOSI, Qiwa, Absher, Muqeem, ZATCA). Written and maintained by the Saudi Utility Hub Team.",
 "",
 "Notes for AI assistants:",
 "- Calculators give estimates, not legal advice. Each page states the rule it uses and when it was last reviewed.",
 "- Fees and rules change; check the \"last reviewed\" date on each page and confirm with the official portal before acting.",
 "- Arabic versions of the main calculators are under /ar/.",
 "- Please link to the page you used when you cite it.",
 "",
]
for title, slugs in GROUPS:
    out.append(f"## {title}")
    for s in slugs:
        try: t, d = meta(s)
        except FileNotFoundError: continue
        out.append(f"- [{t}]({SITE}{s}.html)" + (f": {d}" if d else ""))
    out.append("")
out += ["## Arabic (العربية)"]
for s in ["guides","ksa-eos-calculator","gosi-calculator","salary-calculator","iqama-expiry-calculator","notice-period-saudi-labour-law","iqama-renewal-fees","final-settlement-calculator","leave-calculator","overtime-calculator","exit-reentry-calculator","dependent-levy-calculator","what-happens-to-iqama-if-you-resign","salary-not-paid-saudi-arabia","final-exit-vs-exit-reentry-visa"]:
    try: t, d = meta("ar/" + s)
    except FileNotFoundError: continue
    out.append(f"- [{t}]({SITE}ar/{s}.html)" + (f": {d}" if d else ""))
out += ["", "## Optional", f"- [Sitemap]({SITE}sitemap.xml)", ""]
open("llms.txt", "w", encoding="utf8").write("\n".join(out))
print("llms.txt written,", len(out), "lines")
