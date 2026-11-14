# Daily page rewrite plan (started November 2026)

Goal: rewrite every indexed page so it reads like a person who has lived the problem wrote it.
It should be warm, specific and easy to read, while staying accurate. That is how we pass AdSense's
"low value content" review, and it is why people come back.

## Rules for every rewrite

**Voice**
- Write to one reader ("you"), the way a friend who has been through it would explain it over tea.
- Open with the reader's real situation, not a definition. For example: "Your resignation letter is
  ready, but one question is keeping you up: what happens to my iqama?"
- Short sentences. One idea per paragraph. Vary rhythm. A short punchy line after a long one is fine.
- Use real, concrete examples with names, salaries and dates, such as "Ravi, a site engineer in Dammam on
  SAR 9,000, resigns after 4 years 11 months…".
- Mix English expat vocabulary naturally (iqama, huroob, Qiwa, Absher, Muqeem) without over-explaining.

**Headlines and hooks**
- Titles and H2s should make people want to read, and must stay honest. Good: "The 5-Year Cliff That
  Halves Your End of Service", "Before You Sign Anything, Check These 4 Numbers".
- Never clickbait, never promise what the page doesn't deliver, and never use fake urgency.
  AdSense penalises misleading titles.
- Keep the main keyword in the `<title>` (for example "End of Service Calculator Saudi Arabia"). The
  hook can go after it, or in the H1.
- Drop "2026" from titles unless the page really is about a 2026 change.

**Trust**
- Keep every fact traceable to the official sources already cited on the page. Do not invent fees,
  articles or statistics. Where sources conflict, say so once, plainly.
- Use one clear "check the official service" line per page. Delete repeated hedging such as "estimate",
  "may vary" and "not independently verified" scattered through the text.
- Keep the calculator, its inputs, IDs and JavaScript untouched. Rewrite only the prose around it.
- Keep URLs, canonical tags, the shared header/footer/author markers and existing JSON-LD types.
  Update the FAQ JSON-LD to match any FAQ text you change, and set dateModified to the rewrite date.

**Structure for each page**
1. A hook paragraph (2–3 sentences) showing you understand the reader's situation.
2. A short answer box: the answer in 2–4 sentences.
3. The tool (calculator pages only).
4. How it works, with one worked example that has real numbers.
5. "Mistakes people make" or "What most people get wrong". Real-world tips are the most valuable part.
6. FAQ: 4–6 questions people actually type into Google.
7. Official sources plus a "last reviewed" date.

**Quality gate before merging**
- At least 900 words on tool pages and 1,000 on guides. Don't pad: every paragraph must help.
- Read it out loud in your head. If it sounds like a template, rewrite it.
- No broken links. JSON-LD must parse. No horizontal scroll at 390px.
- Run `python3 scripts/normalize_layout.py` after editing.

## Order (3 pages a day, highest traffic first)

| Day | Pages | Status |
|---|---|---|
| 1 | muqeem-visa-check.html, ksa-eos-calculator.html, dependent-levy-calculator.html | ☑ 2026-11-10 |
| 2 | iqama-expiry-calculator.html, salary-calculator.html, gosi-calculator.html | ☑ 2026-11-11 |
| 3 | final-settlement-calculator.html, iqama-renewal-fees.html, iqama-transfer-calculator.html | ☑ 2026-11-12 |
| 4 | leave-calculator.html, overtime-calculator.html, working-hours-calculator.html | ☑ 2026-11-13 |
| 5 | probation-calculator.html, exit-reentry-calculator.html, gross-to-net-salary-saudi-arabia.html | ☑ 2026-11-14 |
| 6 | family-visit-visa-guide.html, family-residence-visa.html, family-visa-cost-calculator.html | ☐ |
| 7 | 5-year-resident-id-guide-2026.html, umrah-visa-guide.html, musaned-calculator.html | ☐ |
| 8 | premium-residency-cost-calculator.html, eos-payouts-by-salary-2026.html, index.html | ☐ |
| 9 | what-happens-to-iqama-if-you-resign.html, notice-period-saudi-labour-law.html, final-exit-vs-exit-reentry-visa.html | ☐ |
| 10 | salary-not-paid-saudi-arabia.html, how-to-file-a-labour-complaint-saudi-arabia.html, employer-holding-passport-saudi-arabia.html | ☐ |
| 11 | company-closed-end-of-service-saudi-arabia.html, sick-leave-maternity-leave-saudi-arabia.html, renew-iqama-with-expired-passport.html | ☐ |
| 12 | about.html, guides.html, ar/index.html | ☐ |
| 13 | ar/ksa-eos-calculator.html, ar/salary-calculator.html, ar/gosi-calculator.html | ☐ |
| 14 | ar/iqama-expiry-calculator.html, final full-site check | ☐ |

**Do not re-apply to AdSense** until every row is done **and** about 2 weeks have passed so Google can
re-crawl. That puts the earliest re-application at the start of December 2026.
