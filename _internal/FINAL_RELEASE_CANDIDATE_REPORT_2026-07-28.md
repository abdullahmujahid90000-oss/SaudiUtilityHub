# Final Minimal AdSense Release Candidate Report — 2026-07-28

## 1. Scope of this pass

This report documents the reduction of Saudi Utility Hub from a 40-URL site to a
**20-URL minimal release candidate** covering exactly two subject areas: Saudi
employment/payroll/HR, and Saudi residency/Iqama/visa preparation. This is a local,
uncommitted-until-Phase-20 working-tree change. Nothing has been pushed, deployed, or
submitted to AdSense.

## 2. Starting and ending state

- **Starting commit:** `ef8daec` ("Rebuild transparent Terms of Use") — branch `main`
- **Recovery checkpoint tag:** `pre-final-adsense-prune-2026-07-28` (annotated, points at `ef8daec`)
- **Recovery checkpoint branch:** `backup/pre-final-adsense-prune-2026-07-28` (points at `ef8daec`)
- **Final local commit (this pass):** created in Phase 20, see below — message
  "Prepare 20-page AdSense release candidate"
- Both recovery refs verified to dereference to `ef8daec` and to contain all 20
  retained pages plus all 20 newly-paused pages in their pre-prune state.

## 3. Retained pages (20 indexable URLs + 1 non-indexable error page)

Homepage, 7 employment/payroll calculators (salary, GOSI, EOS, final settlement,
working hours, leave, probation), 8 residency/visa pages (dependent levy, Iqama
expiry, Iqama transfer, exit/re-entry, family visit visa guide, family residence
visa, Muqeem visa check, 5-year resident ID guide), and 4 trust pages (about,
contact, privacy, terms). `404.html` exists but is intentionally excluded from the
sitemap and marked `noindex, follow`.

Confirmed via crawl: **exactly 20 pages**, matching the specified set exactly, with
zero deviation.

## 4. Paused pages

20 additional pages were paused this pass (9 root files + 11 blog files, including
`blog/index.html`), on top of the 41 pages already paused in the prior restructure.
**Total paused-pages manifest count: 61** (verified — no duplicates, all fields
present). Full per-page reasoning, backlink status, and redirect decisions are in
`_internal/FINAL_PAUSE_DECISIONS_2026-07-28.md`.

All 20 newly-paused files are confirmed physically removed from the working tree via
`git rm`, and confirmed recoverable via:
```
git checkout pre-final-adsense-prune-2026-07-28 -- <path>
```
or by restoring from branch `backup/pre-final-adsense-prune-2026-07-28`.

## 5. Redirect matrix

`vercel.json` was audited and cleaned:
- **4 stale rules removed** (destinations were themselves paused pages): sources
  `/blog/saudi-work-visa-types-2026.html`, `/absher-guide-expats-2026.html`,
  `/blog/salary-certificate-guide-2026.html`, `/blog/noc-letter-saudi-arabia-2026.html`.
- **1 new rule added** (the only approved 301 from this pass's candidate list):
  `/blog/iqama-renewal-2026.html` → `/iqama-expiry-calculator.html` (permanent).
- **16 total redirect rules remain**, all verified: every destination exists in the
  20-page retained set, no chains, no loops, no blanket redirects to `/`, all
  `permanent: true`, all destination canonical tags self-reference correctly.
- 4 other candidate redirects (sick-leave, salary-deduction, family-visa-cost,
  visit-visa-to-iqama) were reviewed by reading destination content directly and
  **declined** — the destination pages honestly answer a *related but distinct*
  question rather than the removed page's specific claim, so a 301 there would
  mislead. Those paths now 404, which is the honest and correct outcome, not a bug.
- **Backlink data:** No verified backlink export was supplied for this project.
  Every pause-decision record states backlink status as **"Unknown — no verified
  export supplied"** — this is not the same as "no backlinks exist," and should be
  treated as an open item for the site owner if external backlink data becomes
  available later.

## 6. Removed link-graph references

22 dead-link-removal operations were applied across 14 files (Blog nav links,
Nitaqat nav links, one stale "related tools" card, and footer expansions to restore
missing About/Contact/Terms links on 8 pages using an older footer template). Two
further footer gaps (missing About link only) were found and fixed on
`muqeem-visa-check.html` and `5-year-resident-id-guide-2026.html`.

## 7. Crawler results (Phase 15)

Full local crawl from Home, starting at `index.html`, following only internal
`saudiutilityhub.com` links:
- **20 pages reached**, exact match to the expected retained set — zero orphans,
  zero unexpected pages.
- **0 broken internal links.**
- **0 missing local assets** (images, scripts, stylesheets all resolve).
- **All 20 pages reachable within one click of Home** (via nav or homepage category
  cards).
- Sitemap URL set (20 entries) == crawled/retained set == canonical-tag set.
  All three sets are identical.

## 8. Functional regression test matrix (Phase 14)

16 interactive pages tested (Home + 15 calculators/guides) via a jsdom harness with
network calls blocked/spied and real page JavaScript executed:

| Result | Count |
|---|---|
| Pages with 0 uncaught JS errors | 16 / 16 |
| Pages with 0 external network requests during load + interaction | 16 / 16 |
| Pages with exactly 1 `<h1>` | 16 / 16 |
| Edge cases tested per numeric-input page (normal / zero / blank / negative / decimal / huge) | all clean, no visible NaN/Infinity |
| Edge cases tested per date-input page (normal / invalid string / boundary-past date) | all clean, no visible NaN/Infinity |
| Reset buttons tested | all worked |

**PDF generation (3 pages: final-settlement, leave, family-residence-visa):** local
`jsPDF` (v4.2.1) loads successfully in all 3, PDF generation completes with 0
errors, 0 external requests, and every "Download PDF" button is labeled
"Unofficial" in its visible text.

One test-harness false positive was investigated and ruled out: `exit-reentry-calculator.html`
appeared to show "NaN" during an early test run — this was traced to the test
script matching the literal substring `NaN` inside `<script>` source code
(`isNaN(...)`), not rendered output. After excluding `<script>` tag text from the
check, the page shows zero NaN/Infinity in actual visible content in any tested
state.

## 9. Browser / mobile / accessibility (Phases 16–17) — LIMITATION NOTICE

**No real browser (Claude-in-Chrome or equivalent) was available in this
environment for this task**, since this is a local file-editing session with no
live site or connected browser. Responsive layout and accessibility were checked
via static HTML/CSS analysis only:
- All 21 files have a viewport meta tag that does not disable zoom.
- All 21 files contain `@media` responsive breakpoints.
- No `outline:none`/`outline:0` is used anywhere on the 7 pages that lack custom
  `:focus` CSS — meaning native browser focus indicators remain visible and
  functional (not a real gap, just absence of custom styling).
- All interactive elements are native `<button>`/`<a>` elements (keyboard-operable
  by default); no fake clickable `<div>`/`<span>` controls found.
- All non-hidden form inputs have an associated label.
- **Known, pre-existing, non-blocking finding:** several pages skip from `<h2>` to
  `<h4>` for section-card sub-labels (e.g. "💰 Outstanding payroll" cards) without
  an intervening `<h3>`. This predates this pass, is a minor semantic-structure
  polish item, not a WCAG blocker, and was left as-is rather than risk introducing
  new regressions with a same-day, unreviewed heading-hierarchy rewrite across 12
  files right before a release commit.

**This supports a LOCAL pass, not a production-ready declaration.** Real-browser
and real-device verification (actual viewport rendering at ~1440×900 and ~390×844,
screen-reader pass, touch-target measurement) is still required before this
candidate is considered production-ready. This report does not claim WCAG
certification of any level.

## 10. Content/trust/privacy audits (Phases 11–13)

- **Technical SEO (25-item):** clean. One meta-keywords tag was found and removed
  from 6 pages (salary, GOSI, EOS, working-hours, dependent-levy, about) — a real
  gap caught and fixed during this audit. FAQ JSON-LD verified to match visible FAQ
  text exactly (word-for-word) on every page that has FAQ schema, across three
  different FAQ markup templates used across the site.
- **Content/trust consistency:** clean. Three initial regex flags (a
  "government-affiliation" hit, and two "physical office" hits) were manually
  reviewed and confirmed to be false positives — the actual text in each case is an
  explicit *negation* ("not affiliated with the Saudi government"; "we have not yet
  published... a physical office address"), i.e. exactly the honest disclosure the
  spec requires, not a violation of it.
- **Privacy / AdSense-connection audit:** clean across all 21 files. No GA/GTM, no
  AdSense JS, no ad slots, no Google Fonts requests, no external jsPDF, no
  cookie-banner/consent-banner markup, no localStorage/sessionStorage used for
  consent. The AdSense publisher meta tag (`ca-pub-5391037132181133`) appears **only**
  on `index.html`, exactly as required. `ads.txt` content:
  `google.com, pub-5391037132181133, DIRECT, f08c47fec0942fa0`. One flagged
  "cookie-banner" text hit in `privacy.html` was confirmed to be prose describing
  the *absence* of a banner, not banner markup.

## 11. AdSense quality-readiness review (Phase 18)

- Clear, narrow two-topic purpose. Easy navigation (verified: every page one click
  from Home). All 4 trust pages present, internally consistent, and non-contradictory.
- No thin content: all 20 pages range from 958 to 3,387 words of substantive text.
- No blog archive (fully removed). No ads anywhere, including nav/error/trust pages.
- No active advertising or Analytics of any kind currently running.
- No broken or crawler-inaccessible pages (0 found).
- No under-construction/placeholder/test-value language found anywhere.

**This review is an internal readiness check, not a guarantee of AdSense approval.**
Approval is Google's decision alone and depends on factors outside this repository
(account history, policy interpretation, manual review, etc.).

## 12. Remaining owner actions (not done in this pass, by design)

1. Independent fact-checking / legal review of calculator content by qualified
   professionals — this project's own "Legal-Review Notice" (terms.html §24) and
   About-page maintenance language already state this has not happened.
2. Obtain and implement a certified Consent Management Platform (CMP) **before**
   any future AdSense/Analytics activation — none is active or claimed active now.
3. Real-browser and real-device responsive/accessibility verification (see §9).
4. If/when a verified backlink export becomes available, re-review the 4 declined
   redirect candidates and the "Unknown" backlink-status entries in the pause
   decisions doc.
5. Submit to AdSense for review — **not done, and not requested, in this pass.**

## 13. Rollback procedure (non-destructive)

If any part of this release candidate needs to be reverted, no destructive git
commands (`reset --hard`, force-push, branch deletion) are required or recommended:

- **Restore the entire pre-prune state:** `git checkout backup/pre-final-adsense-prune-2026-07-28`
  or `git checkout pre-final-adsense-prune-2026-07-28` to inspect/branch from the
  exact prior state, then cherry-pick or merge forward as needed.
- **Restore one paused page:** `git checkout pre-final-adsense-prune-2026-07-28 -- <path>`,
  then re-add its sitemap entry, canonical tag (already present in the recovered
  file), and any nav/footer links that were removed elsewhere.
- **Re-add a sitemap entry:** add a `<url>` block to `sitemap.xml` pointing at the
  restored page's canonical URL.
- **Re-add nav/footer links:** the removed link-graph edits are recorded in this
  report (§6) and in `_internal/FINAL_PAUSE_DECISIONS_2026-07-28.md`; reverse them
  manually per-page.
- **Re-add a redirect:** re-insert the corresponding rule into `vercel.json`
  `redirects`, pointing at the restored page.
- **Before republishing any previously-paused page or reactivating
  advertising/Analytics:** re-run the Phase 11–13 privacy/SEO/trust audits, since
  restoring content can reintroduce the exact issues this pass removed.

## 14. Known limitations (full list)

- No real-browser/device testing was performed (see §9) — static/jsdom checks only.
- No independent legal or regulatory review of calculator content.
- No verified backlink export was available; all backlink-status fields are marked
  "Unknown — no verified export supplied."
- Minor pre-existing heading-hierarchy skips (h2→h4) on several pages, left
  unaddressed to avoid unreviewed same-day structural changes.
- This report and its underlying checks are not a certification of WCAG
  compliance, AdSense approval likelihood, or legal compliance in any jurisdiction.

## 15. Go / no-go decision

All 20 phases of this pass completed with either a clean result or an explicitly
documented, non-blocking finding. No FAIL-condition trigger from the original task
spec was encountered. This candidate is recommended as **GO for local finalization**
(Phase 20 commit), subject to the owner actions in §12 before any public
republishing, AdSense submission, or advertising/Analytics activation.

---

**MINIMAL ADSENSE RELEASE CANDIDATE: PASS**
