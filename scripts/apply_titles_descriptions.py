#!/usr/bin/env python3
"""Apply shortened <title>/og:title and meta description/og:description.
Titles <= 60 chars (so Google doesn't cut them), descriptions <= 155 chars.
Run from the repo root:  python3 scripts/apply_titles_descriptions.py
Edit COPY below to change the wording, then re-run (it only touches pages listed).
"""
import re, html, sys
COPY = {
"5-year-resident-id-guide-2026": ("5-Year Resident ID Saudi Arabia vs Your Iqama Expiry", "The Saudi Resident ID card lasts 5 years, but your iqama renews every 3–12 months. How to check your real expiry in Absher and what to do if the card is lost."),
"company-closed-end-of-service-saudi-arabia": ("Company Closed in Saudi Arabia? Your End of Service Rights", "If your Saudi employer closes or goes bankrupt: your Article 84 end of service, unpaid salary, leave pay, the payment deadline and how to transfer your iqama."),
"dependent-levy-calculator": ("Dependent Fee Calculator Saudi Arabia — SAR 400 Per Month", "Calculate your Saudi dependent fee: SAR 400 per family member per month, paid at iqama renewal. Cost table, a real example and how to pay through SADAD."),
"disclaimer": (None, "Our calculators give estimates for information only, not legal, financial or immigration advice. Not affiliated with HRSD, Qiwa, GOSI or Absher."),
"editorial-team": (None, "Who writes and reviews Saudi Utility Hub, the official sources behind every calculator, our review schedule, and how to report an error."),
"employer-holding-passport-saudi-arabia": ("Can Your Employer Keep Your Passport in Saudi Arabia?", "Saudi rules bar employers from holding a worker's passport without written consent. The fine, how to get it back and where to report it (Qiwa, 19911)."),
"eos-payouts-by-salary-2026": ("End of Service Payouts by Salary — Saudi Arabia 2026", "Gratuity tables for Saudi Arabia: payouts for eight salary bands (SAR 3,000–30,000) after 1–20 years, for termination and resignation (Articles 84–85)."),
"exit-reentry-calculator": ("Exit Re-Entry Visa Fee Calculator Saudi Arabia", "Calculate your exit re-entry visa fee: SAR 200 single, SAR 500 multiple, plus extra months, for you and family. How to issue it in Absher and what if you're late."),
"family-residence-visa": ("Family Residence Visa Saudi Arabia — Sponsor Your Family", "How expats sponsor a wife and children in Saudi Arabia: who qualifies, attestation, the SAR 2,000 visa fee, embassy stamping and the SAR 400 monthly fee."),
"family-visa-cost-calculator": ("Family Visa Cost Calculator Saudi Arabia — Real Total Cost", "Add up the real cost of bringing your family to Saudi Arabia: SAR 2,000 visa fee, iqama cards, insurance, the SAR 400 monthly fee, or a visit visa instead."),
"family-visit-visa-guide": ("Family Visit Visa Saudi Arabia — Apply, Fees, Stay, Extend", "Invite parents, spouse or children on a Saudi family visit visa: where to apply, documents, the SAR 300 fee, insurance, how long they can stay and extension."),
"final-exit-vs-exit-reentry-visa": ("Final Exit vs Re-Entry Visa Saudi Arabia — Which to Use", "Final exit or exit re-entry? One is a round trip, the other ends your residency. Fees, validity, what to clear first and the lifted 3-year re-entry ban."),
"final-settlement-calculator": ("Final Settlement Calculator Saudi Arabia — What You're Owed", "Add up your Saudi final settlement: unpaid salary, end of service, unused leave, notice pay and deductions. Payment deadlines and three real examples."),
"gosi-calculator": ("GOSI Calculator Saudi Arabia — Employee & Employer Rates", "See what goes to GOSI each month: 9.75% or 10.75% for Saudis, 0% for expats, employer shares, the SAR 45,000 cap and the new-entrant phase-in table."),
"gross-to-net-salary-saudi-arabia": ("Gross to Net Salary Saudi Arabia — Take-Home Pay Table", "Gross-to-net table for expats (0% GOSI) and Saudis (9.75–10.75%), three real payslips, why the basic/allowance split matters and how to compare job offers."),
"guides": ("Guides for Working and Living in Saudi Arabia", "Plain-English guides for expats in Saudi Arabia: resigning, notice periods, final exit, unpaid salary, labour complaints, passports, leave, iqama."),
"how-to-file-a-labour-complaint-saudi-arabia": ("How to File a Labour Complaint in Saudi Arabia (Qiwa, 19911)", "Step-by-step guide to filing a labour complaint in Saudi Arabia on Qiwa or 19911: evidence, amicable settlement, the labour court, deadlines and retaliation."),
"index": ("Saudi Salary, GOSI & End of Service Calculators for Expats", "Free calculators for life and work in Saudi Arabia: take-home salary, GOSI, end of service, leave, overtime, iqama, dependent fees and visas. No login."),
"iqama-expiry-calculator": ("Iqama Expiry Calculator & Renewal Planner — Saudi Arabia", "Count the days to your iqama expiry and get reminder dates. What renewal costs, who renews it, the SAR 500 late fine and a simple 90-day renewal timeline."),
"iqama-renewal-fees": ("Iqama Renewal Fees Saudi Arabia — Full Cost, Line by Line", "What an iqama renewal really costs: SAR 650 iqama fee, SAR 800 monthly worker levy, SAR 400 per dependant, insurance and the SAR 500 late fine."),
"iqama-transfer-calculator": ("Iqama Transfer Without Employer Approval — Qiwa Steps", "Transfer your iqama to a new employer through Qiwa: the steps, when you don't need your current employer's approval, who pays the SAR 2,000–6,000 fee."),
"ksa-eos-calculator": ("End of Service Calculator Saudi Arabia — Check Your Gratuity", "Calculate your Saudi end-of-service award in seconds. Articles 84–85 explained with examples: the 2-, 5- and 10-year cliffs and resignation vs termination."),
"leave-calculator": ("Annual Leave Calculator Saudi Arabia — 21 or 30 Days", "Work out your Saudi annual leave: 21 days a year, 30 after 5 years, payout of unused days when you leave, other paid leave and public holidays."),
"muqeem-visa-check": ("Muqeem Visa Check & Saudi Visa Check Online — Step by Step", "Check a Saudi visa in two minutes: your own exit re-entry in Absher, a family member's on Muqeem, and visas issued abroad on the MOFA portal."),
"musaned-calculator": ("Musaned Domestic Worker Cost Calculator — First-Year Cost", "What hiring a housemaid, nanny or driver through Musaned costs: SAR 2,000 visa fee, recruitment fee caps by nationality, contract authentication and salary."),
"notice-period-saudi-labour-law": ("Notice Period Saudi Arabia — 30 or 60 Days? 2025 Law Rules", "Saudi notice period rules after the 2025 Labour Law changes: 30 days to resign, 60 days if the employer ends the contract, pay in lieu and fixed-term contracts."),
"overtime-calculator": ("Overtime Calculator Saudi Arabia — Are You Paid Fairly?", "Work out your Saudi overtime pay under Article 107: hourly wage plus 50% of basic, rest-day and holiday hours, Ramadan limits and what to do if it isn't paid."),
"premium-residency-cost-calculator": ("Saudi Premium Residency Cost Calculator — Is It Worth It?", "Compare all seven Saudi Premium Residency products (SAR 4,000 to 800,000) and see if escaping the SAR 400 monthly dependent fee covers the cost for you."),
"probation-calculator": ("Probation Period Saudi Arabia — When Does Yours End?", "Work out when your Saudi probation ends: up to 180 days, Eid and sick days excluded, what happens if either side ends the contract, and common myths."),
"renew-iqama-with-expired-passport": ("Renew Iqama With an Expired Passport — Absher & Muqeem", "Can't renew your iqama because your passport expired? Renew the passport, update it in Absher or Muqeem, then renew the iqama. Who updates what, fines, timeline."),
"salary-calculator": ("Salary Calculator Saudi Arabia — Your Real Take-Home Pay", "Work out your real take-home pay in Saudi Arabia: no income tax, GOSI for Saudis and expats, three payslip examples and what to check in job offers."),
"salary-not-paid-saudi-arabia": ("Salary Not Paid in Saudi Arabia? Your Rights & Next Steps", "Salary late or unpaid in Saudi Arabia? Your rights under the Wage Protection System, how to complain on Qiwa, and leaving under Article 81 with full end of service."),
"sick-leave-maternity-leave-saudi-arabia": ("Sick & Maternity Leave Saudi Arabia — 30/60/30 Days", "Sick leave in Saudi Arabia: 30 days full pay, 60 at 75%, 30 unpaid. Maternity leave is 12 weeks' full pay since 2025, paternity 3 days. Seha certificates and protections."),
"umrah-visa-guide": ("Umrah Visa Guide — eVisa, Nusuk Permit & Iqama Holders", "How to perform Umrah from inside or outside Saudi Arabia: Nusuk permit for iqama holders, tourist eVisa, Rawdah booking, costs, Hajj-season pauses and mistakes."),
"what-happens-to-iqama-if-you-resign": ("What Happens to Your Iqama If You Resign? The 60-Day Rule", "Resigning doesn't cancel your iqama. How the 60-day window works, transferring through Qiwa without your old employer's approval, avoiding huroob and your end of service."),
"working-hours-calculator": ("Working Hours in Saudi Arabia — Daily Limits & Ramadan Hours", "Saudi working hours explained: 8 a day, 48 a week, 6 in Ramadan, breaks, rest days and the 12-hour limit, plus a calculator for extra hours under Article 107."),
}

OV = {
"5-year-resident-id-guide-2026": "The Saudi Resident ID lasts 5 years, but your iqama renews every 3–12 months. Check your real expiry in Absher and what to do if the card is lost.",
"company-closed-end-of-service-saudi-arabia": "If your Saudi employer closes or goes bankrupt: your Article 84 end of service, unpaid salary, leave pay, payment deadline and how to transfer your iqama.",
"exit-reentry-calculator": "Calculate your exit re-entry visa fee: SAR 200 single, SAR 500 multiple, plus extra months, for you and family. How to issue it in Absher and late rules.",
"family-visit-visa-guide": "Invite parents, spouse or children on a Saudi family visit visa: where to apply, documents, the SAR 300 fee, insurance, length of stay and extensions.",
"guides": "Plain-English guides for expats in Saudi Arabia: resigning, notice periods, final exit, unpaid salary, labour complaints, passports, leave, iqama.",
"how-to-file-a-labour-complaint-saudi-arabia": "Step-by-step guide to filing a labour complaint in Saudi Arabia on Qiwa or 19911: evidence, amicable settlement, the labour court, deadlines, retaliation.",
"iqama-renewal-fees": "What an iqama renewal really costs: SAR 650 iqama fee, SAR 800 monthly worker levy, SAR 400 per dependant, insurance and the SAR 500 late fine.",
"musaned-calculator": "What hiring a housemaid, nanny or driver through Musaned costs: SAR 2,000 visa fee, recruitment fee caps by nationality, contract authentication, salary.",
"notice-period-saudi-labour-law": "Saudi notice period rules after the 2025 Labour Law changes: 30 days to resign, 60 if the employer ends the contract, pay in lieu, fixed-term contracts.",
"overtime-calculator": "Work out your Saudi overtime pay under Article 107: hourly wage plus 50% of basic, rest-day and holiday hours, Ramadan limits and what to do if unpaid.",
"renew-iqama-with-expired-passport": "Can't renew your iqama because your passport expired? Renew the passport, update it in Absher or Muqeem, then renew the iqama. Who updates what, fines.",
"salary-not-paid-saudi-arabia": "Salary late or unpaid in Saudi Arabia? Your rights under the Wage Protection System, how to complain on Qiwa, and leaving under Article 81 with full EOS.",
"sick-leave-maternity-leave-saudi-arabia": "Saudi sick leave: 30 days full pay, 60 at 75%, 30 unpaid. Maternity leave is 12 weeks' full pay since 2025, paternity 3 days. Seha certificates.",
"umrah-visa-guide": "How to perform Umrah from inside or outside Saudi Arabia: Nusuk permit for iqama holders, tourist eVisa, Rawdah booking, costs and Hajj-season pauses.",
"what-happens-to-iqama-if-you-resign": "Resigning doesn't cancel your iqama. How the 60-day window works, transferring via Qiwa without your old employer's approval, and your end of service.",
"working-hours-calculator": "Saudi working hours explained: 8 a day, 48 a week, 6 in Ramadan, breaks, rest days and the 12-hour limit, plus a calculator for Article 107 extra hours.",
}
for k,v in OV.items(): COPY[k]=(COPY[k][0],v)
def esc(s): return html.escape(s, quote=True).replace("&#x27;", "'")
bad = [(k, len(t or ''), len(d)) for k,(t,d) in COPY.items() if (t and len(t) > 60) or len(d) > 155]
if bad: print("TOO LONG:", bad); sys.exit(1)
for slug,(t,d) in COPY.items():
    f = slug + ".html"; h = open(f, encoding="utf8").read(); o = h
    if t:
        m = re.search(r"<title>(.*?)</title>", h, re.S); old_t = m.group(1)
        h = h.replace(f"<title>{old_t}</title>", f"<title>{esc(t)}</title>")
        h = h.replace(f'<meta content="{old_t}" property="og:title"/>', f'<meta content="{esc(t)}" property="og:title"/>')
    m = re.search(r'<meta content="([^"]*)" name="description"/>', h); old_d = m.group(1)
    h = h.replace(f'<meta content="{old_d}" name="description"/>', f'<meta content="{esc(d)}" name="description"/>')
    h = h.replace(f'<meta content="{old_d}" property="og:description"/>', f'<meta content="{esc(d)}" property="og:description"/>')
    if t: h = re.sub(r'<meta content="[^"]*" name="twitter:title"/>', f'<meta content="{esc(t)}" name="twitter:title"/>', h)
    h = re.sub(r'<meta content="[^"]*" name="twitter:description"/>', f'<meta content="{esc(d)}" name="twitter:description"/>', h)
    pass
    open(f, "w", encoding="utf8").write(h)
print("updated", len(COPY), "pages")
