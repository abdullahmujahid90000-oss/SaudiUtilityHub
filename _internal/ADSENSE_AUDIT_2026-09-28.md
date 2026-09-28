# AdSense & SEO Audit — 28 September 2026

Why AdSense kept rejecting the site, what was fixed in this commit, what you still
need to do yourself, and a growth plan.

---

## 1. What was blocking approval (found in the code)

| # | Problem | Why it matters to an AdSense reviewer | Status |
|---|---|---|---|
| 1 | **Privacy Policy said "no analytics, no ads, no AdSense script on any page"** while every page loaded AdSense and 12 pages ran Google Analytics. Terms of Use and the homepage FAQ said the same. | AdSense requires an accurate privacy policy that discloses third-party ad cookies. An inaccurate one is a policy violation by itself. | Fixed — privacy §9–11, 13, 15, 21 rewritten; Terms §17–18 rewritten; homepage FAQ rewritten. |
| 2 | **Empty ad boxes** — 15 pages had hard-coded `<ins class="adsbygoogle">` units that render as blank grey rectangles until approval. | Reviewer sees half-built pages ("site under construction" / poor user experience). | Fixed — removed. Use **Auto ads** after approval. |
| 3 | **Fake cookie banners** on 6 pages whose "Decline" button only hid the bar, on top of the real sitewide banner (two banners at once). | Deceptive consent + cluttered UX. | Fixed — removed; one consent banner sitewide. |
| 4 | **Misleading navigation & links** — nav/related links labelled "VAT", "Zakat", "Nitaqat", "Remittance", "Car Finance", "Currency Converter", "Blog" pointed to unrelated pages; the gold page advertised 4 tools and 2 "blog posts" that don't exist. | "Misleading site navigation" is a common rejection reason. | Fixed — every mislabelled link relabelled to its real destination or removed. |
| 5 | **~15 different headers and ~17 different footers** across 46 pages (leftovers from repeated restructures); 10 pages linked to a deleted `/blog/`. | Site looks stitched-together / low quality; broken navigation. | Fixed — one shared header + footer on every English page (`assets/site.css`, `scripts/normalize_layout.py`). |
| 6 | **Document generators** (salary certificate "for bank loans", experience letter, NOC letter, payslip) indexed and carrying ads. | Tools that let someone produce employer documents fall under AdSense's *enabling dishonest behaviour* policy — the riskiest pages on the site. | Now `noindex`, no ad code, removed from sitemap/homepage/footer. Still reachable by direct URL. |
| 7 | **Canonical conflict** — `working-hours-calculator.html` (3,400 words) was in the sitemap but declared `overtime-calculator.html` as canonical with the same title. | Google treats it as a duplicate; sitemap and canonical disagree. | Fixed — self-canonical, retargeted at "working hours" (daily/weekly limits, Ramadan). |
| 8 | Homepage said the site covers "two topics only" and then listed a third large section; repeated disclaimers like "this is not a promise of … professional fact-checking" (4×); duplicate FAQs. | Contradictory, low-trust copy on the page reviewers read first. | Fixed — homepage directory, intro, FAQ + FAQ schema rebuilt. |
| 9 | Google Analytics only on 12 of 46 pages. | Your traffic data was useless for SEO decisions. | Fixed — GA4 now loads once, sitewide, via `assets/cookie-consent.js`, with Google Consent Mode v2 (off by default for EEA/UK/CH until "Accept"). |
| 10 | 8 pages scrolled sideways on phones (wide tables, long email). | Mobile usability. | Fixed. |

Also removed: leftover `meta keywords` tags (7 pages), placeholder GA comments.

## 2. Problems that are NOT in the code (you must handle these)

1. **Site churn.** In ~2 months the site went from 300+ pages → 20 → 49 pages, with dozens of
   URLs deleted, redirected or restored. Google's systems (and AdSense reviewers) need to see a
   *stable* site. **Stop restructuring.** From now on: add pages, improve pages, don't delete or
   move them.
2. **Wait before re-applying.** Re-apply 2–3 weeks after this deploy so Google recrawls the
   fixed pages. Resubmit `sitemap.xml` in Search Console first and use *URL Inspection → Request
   indexing* on the homepage, privacy, about and the 10 most important tools.
3. **AdSense → Privacy & messaging → create a GDPR message** (Google's own certified CMP, free).
   Google requires a certified CMP for EEA/UK/Swiss visitors. The site's own banner is fine for
   everyone else.
4. **Google Analytics → Admin → Data retention**: pick 2 or 14 months (the privacy policy says
   one of these without committing to which).
5. **Traffic.** AdSense rarely approves sites with almost no organic traffic. Check Search
   Console: if impressions are near zero, focus on the SEO plan below for a few weeks before
   re-applying.
6. **Arabic pages (`/ar/`) are thin** (400–670 words vs 2,000+ in English). Expand them to at
   least 1,200 words each — Arabic Saudi search is less competitive than English and is a real
   ranking opportunity.

## 3. After approval — how to earn more

- **Auto ads** first (no code needed — the AdSense script is already on every page).
  Turn on anchor + vignette formats; test in-page ads density "balanced".
- **Calculator result pages are the best ad slots**: users wait on them. Once approved, add
  *one* manual unit directly below each calculator's result box.
- **Affiliate income** (only where genuinely useful, disclosed on-page):
  - Remittance: Wise / STC Pay / Western Union referral links on the cost-of-living dashboard.
  - Health insurance for dependants (family visa guides).
  - Bank accounts/home finance (mortgage & Islamic finance calculators).
- **New high-intent calculators** (search demand in KSA, fits the site): Zakat calculator (was
  paused — bring back with verified ZATCA rules), VAT calculator, Saudization/Nitaqat estimator,
  housing-allowance calculator, Hijri–Gregorian date converter, prayer-time-aware Ramadan working
  hours planner, SANED unemployment benefit estimator.
- **Email list**: "Get notified when GOSI / levy rules change" — cheap to run, brings people back.

## 4. SEO plan (ongoing)

Weekly, not daily — publishing thin pages every day is exactly what gets sites labelled
"scaled/low-value content".

1. **Every week:** check Search Console → Performance → pages with high impressions and low CTR;
   rewrite title/meta for 3 of them.
2. **Every 2 weeks:** publish **one** genuinely deep new page (tool or guide, 1,500+ words,
   primary sources cited, worked examples) from the list in §3.
3. **Monthly:** refresh fees/rates pages (GOSI phase-in, levy, Iqama fees) and update their
   "last reviewed" dates only when content actually changed.
4. **Backlinks:** answer questions on Reddit r/saudiarabia, Quora, expat Facebook groups and
   Expatriates.com with links to the specific calculator that solves the question.
5. Internal linking: every guide should link to its matching calculator and vice versa.

No one can honestly guarantee position #1 — rankings depend on competitors and Google. What
reliably works is the loop above: stable URLs, deep pages, fast mobile pages, and steady links.

## 5. Maintaining the shared layout

Header/footer links live in `scripts/normalize_layout.py` (`NAV`, `FOOTER_COLUMNS`). Edit them
and run `python3 scripts/normalize_layout.py` from the repo root — it updates every English page
and is safe to run repeatedly. New pages: include `<link rel="stylesheet" href="/assets/site.css" />`
and run the script once.
