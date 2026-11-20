#!/usr/bin/env python3
"""Add a topic-cluster "Related guides and tools" block to content pages.

Run from the repository root:  python3 scripts/add_related_links.py

Safe to re-run: the block lives between <!-- suh:related --> / <!-- /suh:related -->
markers and is regenerated each time. For each page the script takes the curated
candidate list in CLUSTER below and skips any destination the page already links
to in its main content (header, footer and breadcrumb links don't count), so
only genuinely new internal links are added (max 4 per page).
Edit CLUSTER to change the linking plan, then re-run.
"""
import os, re

SITE = "https://www.saudiutilityhub.com/"

# slug -> (anchor text, one-line reason shown next to the link)
DEST = {
 "ksa-eos-calculator.html": ("End of service gratuity calculator", "Work out your Article 84 gratuity from your salary and years of service."),
 "final-settlement-calculator.html": ("Final settlement calculator", "Add up gratuity, unpaid salary and leave pay in one total."),
 "eos-payouts-by-salary-2026.html": ("End of service payouts by salary (2026 table)", "See typical payouts at common salary levels and service lengths."),
 "notice-period-saudi-labour-law.html": ("Notice period under Saudi labour law", "How long a notice period must be and who it applies to."),
 "what-happens-to-iqama-if-you-resign.html": ("What happens to your iqama if you resign", "Your residency and transfer options after you leave a job."),
 "company-closed-end-of-service-saudi-arabia.html": ("End of service when your company closes", "Your rights to gratuity and unpaid wages if the employer shuts down."),
 "probation-calculator.html": ("Probation period calculator", "Check probation length and what happens to gratuity if it ends early."),
 "salary-not-paid-saudi-arabia.html": ("What to do if your salary is not paid", "Steps to take when wages are late or withheld."),
 "how-to-file-a-labour-complaint-saudi-arabia.html": ("How to file a labour complaint", "Step-by-step guide to the official complaint process."),
 "employer-holding-passport-saudi-arabia.html": ("Employer holding your passport", "What the rules say and how to get it back."),
 "final-exit-vs-exit-reentry-visa.html": ("Final exit vs exit re-entry visa", "Which visa to use when you leave Saudi Arabia."),
 "exit-reentry-calculator.html": ("Exit re-entry visa fee calculator", "Calculate the fee for your trip length and visa type."),
 "renew-iqama-with-expired-passport.html": ("Renewing an iqama with an expired passport", "What to do when your passport expires before your iqama."),
 "iqama-expiry-calculator.html": ("Iqama expiry checker and renewal reminder", "Find your expiry date and plan the renewal in time."),
 "iqama-renewal-fees.html": ("Iqama renewal fees", "A breakdown of the fees due at renewal."),
 "iqama-transfer-calculator.html": ("Iqama transfer cost calculator", "Estimate the cost of moving to a new employer."),
 "dependent-levy-calculator.html": ("Dependent levy calculator", "Work out the monthly fee for each family member."),
 "family-visa-cost-calculator.html": ("Family visa cost calculator", "Estimate the cost of bringing your family to Saudi Arabia."),
 "family-visit-visa-guide.html": ("Family visit visa guide", "Who can invite relatives and how to apply."),
 "family-residence-visa.html": ("Family residence visa guide", "Requirements for sponsoring your spouse and children."),
 "5-year-resident-id-guide-2026.html": ("5-year resident ID guide", "Who qualifies for a longer-validity residency card."),
 "premium-residency-cost-calculator.html": ("Premium Residency cost calculator", "Compare Premium Residency fees with the levy you would avoid."),
 "musaned-calculator.html": ("Musaned domestic worker cost calculator", "Estimate the cost of hiring a domestic worker through Musaned."),
 "umrah-visa-guide.html": ("Umrah visa guide", "Rules and steps for Umrah visits."),
 "muqeem-visa-check.html": ("Muqeem visa status check", "How to check an iqama or visa status on Muqeem."),
 "salary-calculator.html": ("Saudi salary calculator", "See take-home pay after deductions."),
 "gosi-calculator.html": ("GOSI calculator", "Calculate social insurance contributions."),
 "gross-to-net-salary-saudi-arabia.html": ("Gross to net salary in Saudi Arabia", "What is and isn't deducted from your pay."),
 "overtime-calculator.html": ("Overtime pay calculator", "Calculate overtime pay under the Labour Law."),
 "working-hours-calculator.html": ("Working hours calculator", "Check daily and weekly hours, including Ramadan hours."),
 "leave-calculator.html": ("Annual leave calculator", "Work out your leave entitlement and leave pay."),
 "sick-leave-maternity-leave-saudi-arabia.html": ("Sick leave and maternity leave rules", "How many days you get and how much is paid."),
}
K, FS, EP, NP, RS, CL, PR, SNP, LC, PP, FE, ER, RX, IE, IR, IT, LV, FC, FV, FR, FY, PM, MU, UM, MQ, SAL, GO, GN, OT, WH, LE, SK = list(DEST)

CLUSTER = {
 K:  [EP, FS, NP, RS, CL, PR],
 FS: [K, EP, SNP, LC, FE, NP],
 EP: [K, FS, NP, CL, GN],
 NP: [K, RS, PR, FS, LC],
 RS: [K, FE, IT, NP, PP],
 CL: [K, FS, SNP, LC, EP],
 PR: [NP, K, FS, LE, WH],
 SNP:[LC, FS, PP, K, NP],
 LC: [SNP, PP, FS, NP, CL],
 PP: [LC, SNP, FE, RS, IE],
 FE: [ER, RS, K, FS, IT],
 ER: [FE, IE, RS, IR, MQ],
 RX: [IE, IR, MQ, FY, ER],
 IE: [IR, RX, ER, LV, PM],
 IR: [IE, LV, RX, PM, IT],
 IT: [RS, FE, IR, K, PR],
 LV: [FC, MU, IR, PM, FR],
 FC: [LV, FR, FV, MU, PM, IR],
 FV: [FC, FR, UM, MQ, ER],
 FR: [FC, LV, PM, FY, FV],
 FY: [PM, IR, FR, LV, IE],
 PM: [FY, LV, IR, FR, FC, MU],
 MU: [LV, FC, PM, IR, SAL],
 UM: [FV, MQ, ER, FY],
 MQ: [ER, IE, FV, UM, FE],
 SAL:[GO, GN, OT, LE, K, WH],
 GO: [SAL, GN, K, SK],
 GN: [SAL, GO, OT, K, LE],
 OT: [WH, SAL, GN, LE],
 WH: [OT, LE, SAL, PR],
 LE: [SK, SAL, K, WH, PR],
 SK: [LE, SAL, SNP, WH],
}

START, END = "<!-- suh:related -->", "<!-- /suh:related -->"

def strip_div(h, cls):
    while True:
        m = re.search(r'<div[^>]*class="[^"]*\b' + cls + r'\b[^"]*"[^>]*>', h)
        if not m:
            return h
        i, d, j = m.end(), 1, len(h)
        for t in re.finditer(r'<(/?)div\b', h[i:]):
            d += -1 if t.group(1) else 1
            if d == 0:
                j = i + t.end(); break
        h = h[:m.start()] + h[j:]

def body_links(h):
    for c in ("suh-nav", "suh-footer"):
        h = strip_div(h, c)
    h = re.sub(r'<nav aria-label="Breadcrumb".*?</nav>', '', h, flags=re.S)
    h = re.sub(re.escape(START) + r'.*?' + re.escape(END), '', h, flags=re.S)
    return {l.replace(SITE, '').split('#')[0] for l in re.findall(r'href="([^"]+)"', h)}

def block(items):
    lis = "\n".join(f'<li><a href="{SITE}{s}">{DEST[s][0]}</a> &mdash; {DEST[s][1]}</li>' for s in items)
    return (f'{START}\n<section class="suh-related" aria-labelledby="suh-related-h">\n'
            f'<div class="suh-wrap">\n<h2 id="suh-related-h">Related guides and tools</h2>\n<ul>\n{lis}\n</ul>\n</div>\n'
            f'</section>\n{END}\n')

def main():
    changed = 0
    for src, cands in CLUSTER.items():
        h = open(src, encoding="utf8").read()
        h = re.sub(re.escape(START) + r'.*?' + re.escape(END) + r'\n?', '', h, flags=re.S)
        have = body_links(h)
        items = [c for c in cands if c not in have and c != src][:4]
        if not items:
            open(src, "w", encoding="utf8").write(h); continue
        for marker in ('<div class="suh-updated"', '<!-- suh:author -->', '<!-- suh:footer -->'):
            k = h.find(marker)
            if k != -1:
                h = h[:k] + block(items) + h[k:]; break
        else:
            print("NO MARKER", src); continue
        open(src, "w", encoding="utf8").write(h); changed += 1
        print(f"{src}: +{len(items)}")
    print("pages updated:", changed)

if __name__ == "__main__":
    main()
