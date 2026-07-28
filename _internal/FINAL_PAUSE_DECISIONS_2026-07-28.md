# Final Pause Decisions — 2026-07-28

This document records the pausing of 20 additional pages to bring the public, deployable, indexable site down to exactly 20 URLs plus 404.html, for a minimal AdSense release candidate. It supplements `_internal/PAUSED_PAGES.md` and `_internal/paused-pages-manifest.json`, which together now describe 61 paused pages (41 from the 2026-07-26 restructure plus these 20).

**Recovery checkpoint for all 20 pages below:**
- Annotated tag: `pre-final-adsense-prune-2026-07-28`
- Backup branch: `backup/pre-final-adsense-prune-2026-07-28`
- Both point to commit `ef8daec` (the state of the repository immediately before this pause).
- Restore a single file: `git checkout pre-final-adsense-prune-2026-07-28 -- <path>`
- Restore everything: check out or merge from `backup/pre-final-adsense-prune-2026-07-28`.

**Backlink evidence status (applies to all 20 pages):** Unknown — no verified Search Console, Ahrefs, Semrush, or other backlink export was supplied for this task. No page below is treated as having confirmed backlinks, and no page is treated as having confirmed zero backlinks either. This status is recorded, not assumed.

**Restoration requirement for all 20 pages:** Before any of these pages is restored to the live site, it must go through the same factual-accuracy and AdSense-quality review already applied to the 20 retained pages (primary-source verification, removal of unsupported claims, removal of any remaining Analytics/AdSense/cookie-banner/Google Fonts code, and consistency with the current Privacy Policy and Terms of Use).

---

## 1. experience-letter-generator.html
- **Public URL:** https://www.saudiutilityhub.com/experience-letter-generator.html
- **Reason for pausing:** Workplace-document generator tool. Outside the site's two approved AdSense-release subject areas (employment/payroll/HR calculators and residency/Iqama/visa preparation guides); document-generation tools raise a separate authenticity/misuse risk class not yet reviewed for this release.
- **Redirect decision:** None — returns 404.
- **Destination:** N/A.
- **Why 404 was selected:** No retained page covers generating an experience letter; this is a distinct document-generation intent with no equivalent among the 20 retained calculators/guides.
- **Recovery source:** Tag `pre-final-adsense-prune-2026-07-28` / branch `backup/pre-final-adsense-prune-2026-07-28`.
- **Restoration command:** `git checkout pre-final-adsense-prune-2026-07-28 -- experience-letter-generator.html`

## 2. family-visa-cost-calculator.html
- **Public URL:** https://www.saudiutilityhub.com/family-visa-cost-calculator.html
- **Reason for pausing:** Broadens scope beyond the 20-page minimal release; a cost-total calculator whose fee/levy/insurance figures need a fresh accuracy pass before re-publication.
- **Backlink evidence status:** Unknown — no verified export supplied.
- **Redirect decision:** None — returns 404 (considered and declined).
- **Candidate destination reviewed:** family-residence-visa.html.
- **Why 404 was selected instead of a 301:** family-residence-visa.html was read directly. Its "Ongoing Dependant Levy" section explicitly states it does *not* restate a levy figure ("Use [the dependent-levy] page for the current estimate"), and its preparation checklist deliberately lists "COST WORKSHEET CATEGORIES ... no fixed fees listed here" rather than a calculated total. The removed page's central intent — produce a total cost figure — is therefore not delivered by the candidate destination. Redirecting would send a cost-calculation search to a page that explicitly declines to calculate a cost, which risks misleading the user. 404 is the honest outcome.
- **Recovery source:** Tag `pre-final-adsense-prune-2026-07-28` / branch `backup/pre-final-adsense-prune-2026-07-28`.
- **Restoration command:** `git checkout pre-final-adsense-prune-2026-07-28 -- family-visa-cost-calculator.html`

## 3. musaned-calculator.html
- **Public URL:** https://www.saudiutilityhub.com/musaned-calculator.html
- **Reason for pausing:** Domestic-worker/Musaned-platform subject matter not part of the two approved release subject areas.
- **Redirect decision:** None — returns 404.
- **Destination:** N/A.
- **Why 404 was selected:** No retained page addresses Musaned or domestic-worker employment specifically.
- **Recovery source/command:** as above; `git checkout pre-final-adsense-prune-2026-07-28 -- musaned-calculator.html`

## 4. nitaqat-saudization-guide.html
- **Public URL:** https://www.saudiutilityhub.com/nitaqat-saudization-guide.html
- **Reason for pausing:** Employer-facing Nitaqat/Saudization compliance topic — different audience (employers/HR compliance officers) than the individual-employee-facing calculators being retained; not part of the approved release scope.
- **Redirect decision:** None — returns 404.
- **Destination:** N/A.
- **Why 404 was selected:** No retained page covers Nitaqat/Saudization quota rules.
- **Recovery source/command:** `git checkout pre-final-adsense-prune-2026-07-28 -- nitaqat-saudization-guide.html`

## 5. noc-letter-generator.html
- **Public URL:** https://www.saudiutilityhub.com/noc-letter-generator.html
- **Reason for pausing:** Workplace-document generator tool, same risk class as item 1.
- **Redirect decision:** None — returns 404. The existing `vercel.json` rule `/blog/noc-letter-saudi-arabia-2026.html → /noc-letter-generator.html` is removed in Phase 8 since its destination no longer exists.
- **Destination:** N/A.
- **Why 404 was selected:** No retained page covers NOC letter generation.
- **Recovery source/command:** `git checkout pre-final-adsense-prune-2026-07-28 -- noc-letter-generator.html`

## 6. salary-certificate.html
- **Public URL:** https://www.saudiutilityhub.com/salary-certificate.html
- **Reason for pausing:** Workplace-document generator tool, same risk class as item 1.
- **Redirect decision:** None — returns 404. The existing `vercel.json` rule `/blog/salary-certificate-guide-2026.html → /salary-certificate.html` is removed in Phase 8.
- **Destination:** N/A.
- **Why 404 was selected:** No retained page generates a salary certificate; salary-calculator.html estimates net pay but does not produce a certificate document.
- **Recovery source/command:** `git checkout pre-final-adsense-prune-2026-07-28 -- salary-certificate.html`

## 7. salary-slip-generator.html
- **Public URL:** https://www.saudiutilityhub.com/salary-slip-generator.html
- **Reason for pausing:** Workplace-document generator tool, same risk class as item 1.
- **Redirect decision:** None — returns 404.
- **Destination:** N/A.
- **Why 404 was selected:** No retained page generates a payslip document.
- **Recovery source/command:** `git checkout pre-final-adsense-prune-2026-07-28 -- salary-slip-generator.html`

## 8. saudi-work-visa-types-2026.html
- **Public URL:** https://www.saudiutilityhub.com/saudi-work-visa-types-2026.html
- **Reason for pausing:** General work-visa-types explainer, broader than the site's residency/Iqama/visa *preparation* focus; overlaps only partially with retained guides and needs its own accuracy pass. The existing `vercel.json` rule `/blog/saudi-work-visa-types-2026.html → /saudi-work-visa-types-2026.html` is removed in Phase 8 since its destination no longer exists.
- **Redirect decision:** None — returns 404.
- **Destination:** N/A.
- **Why 404 was selected:** None of the 20 retained pages substantially covers the full work-visa-category taxonomy this page addressed.
- **Recovery source/command:** `git checkout pre-final-adsense-prune-2026-07-28 -- saudi-work-visa-types-2026.html`

## 9. visit-visa-to-iqama.html
- **Public URL:** https://www.saudiutilityhub.com/visit-visa-to-iqama.html
- **Reason for pausing:** Broadens release scope; a conversion/eligibility page whose central claim (a direct answer on who can convert) needs a fresh accuracy pass.
- **Backlink evidence status:** Unknown — no verified export supplied.
- **Redirect decision:** None — returns 404 (considered and declined).
- **Candidate destination reviewed:** family-residence-visa.html.
- **Why 404 was selected instead of a 301:** family-residence-visa.html was read directly. Its own "In-Country Status Conversion" section explicitly states: "We could not confirm, from reliable primary evidence, whether a family member already inside Saudi Arabia on a different status (such as a visit visa) can be converted to dependent residence... This guide does not present in-country conversion as routine, automatic, or guaranteed." This directly contradicts the removed page's central promise of "The Direct Answer — Can You Convert?" plus a full comparison table, child-conversion cost calculator, and a Jawazat office list — none of which the candidate destination reproduces. Redirecting a "can I convert" search to a page that explicitly declines to answer that question, and drops the fee/office/step content entirely, is a different and narrower intent. 404 is the honest, non-misleading outcome.
- **Recovery source/command:** `git checkout pre-final-adsense-prune-2026-07-28 -- visit-visa-to-iqama.html`

## 10. blog/index.html
- **Public URL:** https://www.saudiutilityhub.com/blog/
- **Reason for pausing:** The Blog section (index + 10 posts) is removed entirely from this release; the site is being narrowed to calculators and preparation guides only, with no blog/article archive.
- **Redirect decision:** None — returns 404.
- **Destination:** N/A.
- **Why 404 was selected:** A blog index has no single-page equivalent; redirecting an index page to any one retained page would misrepresent it as a substitute for the whole archive.
- **Recovery source/command:** `git checkout pre-final-adsense-prune-2026-07-28 -- blog/index.html`

## 11. blog/absher-guide-expats-2026.html
- **Public URL:** https://www.saudiutilityhub.com/blog/absher-guide-expats-2026.html
- **Reason for pausing:** Blog-archive removal (see item 10). The existing `vercel.json` rule `/absher-guide-expats-2026.html → /blog/absher-guide-expats-2026.html` is removed in Phase 8 since its destination no longer exists.
- **Redirect decision:** None — returns 404.
- **Destination:** N/A.
- **Why 404 was selected:** No retained page is a general Absher-platform guide; retained pages only link to Absher as an external official destination, they do not explain how to use it.
- **Recovery source/command:** `git checkout pre-final-adsense-prune-2026-07-28 -- blog/absher-guide-expats-2026.html`

## 12. blog/driving-license-guide-2026.html
- **Public URL:** https://www.saudiutilityhub.com/blog/driving-license-guide-2026.html
- **Reason for pausing:** Blog-archive removal; driving-license topic is also outside both approved subject areas.
- **Redirect decision:** None — returns 404.
- **Why 404 was selected:** No retained page covers driving licenses at all.
- **Recovery source/command:** `git checkout pre-final-adsense-prune-2026-07-28 -- blog/driving-license-guide-2026.html`

## 13. blog/how-to-file-labour-complaint-qiwa-2026.html
- **Public URL:** https://www.saudiutilityhub.com/blog/how-to-file-labour-complaint-qiwa-2026.html
- **Reason for pausing:** Blog-archive removal; a labour-dispute/complaint-filing procedure guide, adjacent to but distinct from the retained calculators (none of which cover the complaint process).
- **Redirect decision:** None — returns 404.
- **Why 404 was selected:** No retained page explains how to file a Qiwa labour complaint.
- **Recovery source/command:** `git checkout pre-final-adsense-prune-2026-07-28 -- blog/how-to-file-labour-complaint-qiwa-2026.html`

## 14. blog/iqama-renewal-2026.html
- **Public URL:** https://www.saudiutilityhub.com/blog/iqama-renewal-2026.html
- **Reason for pausing:** Blog-archive removal. Also carried specific renewal-fee and late-penalty figures (SAR 650 / SAR 500) that were not independently reconfirmed for this release.
- **Backlink evidence status:** Unknown — no verified export supplied.
- **Redirect decision:** 301 (permanent) → https://www.saudiutilityhub.com/iqama-expiry-calculator.html
- **Why the destination is substantially equivalent:** Both pages address the same central intent — "help me deal with my Iqama renewal." iqama-expiry-calculator.html's own FAQ directly answers the removed page's central question ("How much does Iqama renewal cost, and is there a grace period or late penalty?") — honestly, by explaining that fee/grace-period figures were found inconsistent across sources and are not stated as fact — and provides the same renewal-responsibility guidance (employer/sponsor via Muqeem, individual via Absher) plus direct links to Absher, Muqeem, and my.gov.sa for authoritative current figures. It additionally gives the user a working date-tracking/reminder planner the blog post did not have. This redirect corrects rather than repeats the blog post's unverified fee figures, so it does not mislead the user.
- **Recovery source/command:** `git checkout pre-final-adsense-prune-2026-07-28 -- blog/iqama-renewal-2026.html`

## 15. blog/mudad-wps-wage-protection-guide-2026.html
- **Public URL:** https://www.saudiutilityhub.com/blog/mudad-wps-wage-protection-guide-2026.html
- **Reason for pausing:** Blog-archive removal; Wage Protection System/Mudad platform explainer, not duplicated by any retained calculator.
- **Redirect decision:** None — returns 404.
- **Why 404 was selected:** No retained page covers WPS/Mudad.
- **Recovery source/command:** `git checkout pre-final-adsense-prune-2026-07-28 -- blog/mudad-wps-wage-protection-guide-2026.html`

## 16. blog/qiwa-portal-guide.html
- **Public URL:** https://www.saudiutilityhub.com/blog/qiwa-portal-guide.html
- **Reason for pausing:** Blog-archive removal; general Qiwa-platform explainer.
- **Redirect decision:** None — returns 404.
- **Why 404 was selected:** Retained pages link to Qiwa as an external official destination but do not contain a general "how Qiwa works" explainer to substitute for this page.
- **Recovery source/command:** `git checkout pre-final-adsense-prune-2026-07-28 -- blog/qiwa-portal-guide.html`

## 17. blog/saned-unemployment-insurance-guide-2026.html
- **Public URL:** https://www.saudiutilityhub.com/blog/saned-unemployment-insurance-guide-2026.html
- **Reason for pausing:** Blog-archive removal; SANED unemployment-insurance topic not covered by any retained calculator.
- **Redirect decision:** None — returns 404.
- **Why 404 was selected:** No retained page covers SANED.
- **Recovery source/command:** `git checkout pre-final-adsense-prune-2026-07-28 -- blog/saned-unemployment-insurance-guide-2026.html`

## 18. blog/saudi-salary-deduction-rules-2026.html
- **Public URL:** https://www.saudiutilityhub.com/blog/saudi-salary-deduction-rules-2026.html
- **Reason for pausing:** Blog-archive removal.
- **Backlink evidence status:** Unknown — no verified export supplied.
- **Redirect decision:** None — returns 404 (considered and declined).
- **Candidate destination reviewed:** salary-calculator.html.
- **Why 404 was selected instead of a 301:** salary-calculator.html was read directly and contains no content about deduction *legality* (Labour Law Article 91, what an employer can/cannot deduct, how to claim back an unlawful deduction). It only estimates gross-to-net pay via GOSI contribution mechanics. The removed page's central intent — "is this deduction legal, and how do I get it back" — is a legal-compliance question the retained calculator does not address in any form. This is a genuinely different intent, not a detail-level gap, so 404 is used.
- **Recovery source/command:** `git checkout pre-final-adsense-prune-2026-07-28 -- blog/saudi-salary-deduction-rules-2026.html`

## 19. blog/sick-leave-saudi-arabia-2026.html
- **Public URL:** https://www.saudiutilityhub.com/blog/sick-leave-saudi-arabia-2026.html
- **Reason for pausing:** Blog-archive removal.
- **Backlink evidence status:** Unknown — no verified export supplied.
- **Redirect decision:** None — returns 404 (considered and declined).
- **Candidate destination reviewed:** leave-calculator.html.
- **Why 404 was selected instead of a 301:** leave-calculator.html was read directly. It does cite the core Article 117 sick-leave pay schedule (30 days full pay / 60 days at 75% / 30 days unpaid) in a reference table — but that table is explicitly labeled "Other Leave Types (Reference Only — Not Part of This Calculator)" by the page's own authors, signalling it is secondary content. The removed page's central intent was a full procedural guide — how to apply, what documents are required, whether an employer can refuse, sick leave during probation/termination/EOS interaction, and domestic-worker rules — none of which the retained page covers. Because the primary procedural intent is not served, and only a supporting reference figure overlaps, this is treated as a different intent rather than the same one at lower detail. 404 is used.
- **Recovery source/command:** `git checkout pre-final-adsense-prune-2026-07-28 -- blog/sick-leave-saudi-arabia-2026.html`

## 20. blog/worker-rights.html
- **Public URL:** https://www.saudiutilityhub.com/blog/worker-rights.html
- **Reason for pausing:** Blog-archive removal; general worker-rights overview article, broader than any single retained calculator's scope.
- **Redirect decision:** None — returns 404.
- **Destination:** N/A.
- **Why 404 was selected:** No single retained page substitutes for a general worker-rights overview.
- **Recovery source/command:** `git checkout pre-final-adsense-prune-2026-07-28 -- blog/worker-rights.html`

---

## Summary

| # | File | Redirect | Destination |
|---|---|---|---|
| 1 | experience-letter-generator.html | 404 | — |
| 2 | family-visa-cost-calculator.html | 404 | — |
| 3 | musaned-calculator.html | 404 | — |
| 4 | nitaqat-saudization-guide.html | 404 | — |
| 5 | noc-letter-generator.html | 404 | — |
| 6 | salary-certificate.html | 404 | — |
| 7 | salary-slip-generator.html | 404 | — |
| 8 | saudi-work-visa-types-2026.html | 404 | — |
| 9 | visit-visa-to-iqama.html | 404 | — |
| 10 | blog/index.html | 404 | — |
| 11 | blog/absher-guide-expats-2026.html | 404 | — |
| 12 | blog/driving-license-guide-2026.html | 404 | — |
| 13 | blog/how-to-file-labour-complaint-qiwa-2026.html | 404 | — |
| 14 | blog/iqama-renewal-2026.html | **301** | /iqama-expiry-calculator.html |
| 15 | blog/mudad-wps-wage-protection-guide-2026.html | 404 | — |
| 16 | blog/qiwa-portal-guide.html | 404 | — |
| 17 | blog/saned-unemployment-insurance-guide-2026.html | 404 | — |
| 18 | blog/saudi-salary-deduction-rules-2026.html | 404 | — |
| 19 | blog/sick-leave-saudi-arabia-2026.html | 404 | — |
| 20 | blog/worker-rights.html | 404 | — |

One redirect (item 14) is added to `vercel.json`. Four existing `vercel.json` redirect rules whose destinations are among these 20 paused pages are removed in Phase 8: the rules pointing to `saudi-work-visa-types-2026.html`, `blog/absher-guide-expats-2026.html`, `salary-certificate.html`, and `noc-letter-generator.html`.
