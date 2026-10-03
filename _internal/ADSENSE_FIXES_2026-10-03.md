# AdSense pre-application fixes — 3 October 2026

## Fixed in this commit
| Issue | Why it mattered | Fix |
|---|---|---|
| Musaned page stated fees (SAR 100/200 "verification", SAR 300–500 medical) and walk-in "service centres" that don't match Musaned's own site (contract authentication is free) | Inaccurate YMYL content; false "fact-checked" claim | `noindex`, ads removed, out of sitemap/homepage. URL still works. |
| Traffic fine calculator used single per-violation fines that don't match published min–max ranges (e.g. mobile use is SAR 500–900, not 200) | Inaccurate YMYL content | Same as above; footer and in-content links removed |
| Premium Residency calculator: category fees stated as annual, wrong family comparison | Inaccurate YMYL content | Same as above |
| Dependent levy guide vs calculator contradicted each other (any-age children/parents/domestic workers vs "spouse + under-18 only"); guide said the SAR 400 rate also applied to employees | Contradictory facts | Both now: SAR 400/month per family member (spouse, children of any age, parents); domestic workers excluded; expat worker levy (SAR 800) named as separate. Calculator gained a "parents / other companions" field. |
| "Related Blog Posts" cards for articles that don't exist (IBAN, traffic, Musaned, letter generators) | Misleading navigation | Removed |
| "Reviewed by Abdullah Al-Qahtani … Next review: July 1, 2026" blocks (stale, inconsistent name) | Stale/contradictory authorship | Removed; one sitewide author box (scripts/normalize_layout.py) |
| About/Terms/Privacy/Editorial said "two topics" and "editorial team"; Terms said the site doesn't cover energy, water or loans while it has those calculators | Contradictory policy pages | Rewritten around the founder and three topic areas; Person/AboutPage schema added |
| EOS FAQ said "customary commissions" are included in the wage; another FAQ said commissions can be excluded | Contradiction | Aligned with HRSD wording |
| Cost-of-living dashboard: "First tool of its kind" badge, "SAR 400/child", "Housing Allowance Calculator" link that opened the salary calculator | Puffery / misleading link | Fixed |

## Still on you before applying
1. Re-submit `sitemap.xml` in Search Console; request indexing for About, the data page and the levy pages.
2. AdSense → Privacy & messaging → publish the Google-certified GDPR message (required for EEA/UK visitors).
3. Wait until Google has recrawled (check URL Inspection shows the new About page) before re-applying.
4. Paused pages can return once rewritten from primary sources: musaned-calculator, traffic-fine-calculator, premium-residency-cost-calculator.
