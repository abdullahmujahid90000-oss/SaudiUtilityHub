# Post-Approval Ads & Privacy Activation Checklist

**Internal file. Not linked from any public page. Do not deploy this file's existence as a claim that a CMP is active — it is not.**

Status as of this document's creation (28 July 2026): Google Analytics is not active. AdSense advertising is not active. No consent-management platform (CMP) is installed or configured. The site connects to Google AdSense only through `ads.txt` and a publisher-account meta tag on `index.html`, neither of which serves ads.

Do **not** simply restore the old `adsbygoogle.js` script tags, `<ins class="adsbygoogle">` slots, or the `adsbygoogle.push({})` calls that were removed during the pre-approval privacy hardening pass. Restoring them without the steps below would recreate the exact compliance and honesty problems this hardening pass fixed.

## Required steps, in order

1. **Re-review current Google AdSense CMP requirements.** Requirements and certified-CMP lists change; re-check `support.google.com/adsense` before assuming anything below is still accurate.
2. In the AdSense dashboard, open **Privacy & messaging**.
3. Create and publish a **European regulations message** for this site (covers EEA, UK, Switzerland requirements).
4. Confirm the CMP you use — Google's own CMP or a certified third-party CMP — is currently certified and integrates with the **current required IAB TCF version** at the time of activation.
5. Provide "Do not consent" and "Manage options" choices wherever legally required, not just a single "Accept" button.
6. Confirm there is a way for a returning visitor to revisit, change, or withdraw a previously made consent choice (a persistent "Privacy choices" or "Manage cookies" control, not a one-time banner).
7. Review which ad-technology providers (ATPs) are selected in the AdSense account; remove any not actually needed.
8. Configure US-state privacy messages (e.g. CCPA/CPRA-related opt-outs) where applicable to this site's audience.
9. Assess whether a global consent mechanism or an additional Saudi-specific consent/notice mechanism is needed, given the site's Saudi subject matter and likely visitor mix.
10. Obtain qualified Saudi PDPL advice before activating advertising and data collection aimed at or reaching individuals in the Kingdom — see the PDPL gaps noted in `privacy.html` Sections 2, 14, and 17 (operator identity, cross-border processing, and rights/response deadlines all still need qualified review).
11. Update `privacy.html` to describe the **actual** active advertising setup: which CMP, which ad-technology providers, what data each collects, what storage each uses (cookie name/purpose/duration), and what choices a visitor actually has. Do not leave the "future" language from Section 21 in place once this is live — replace it with present-tense, accurate description.
12. Only after 1–11 are done: restore the AdSense loader script (`pagead2.googlesyndication.com/pagead/js/adsbygoogle.js`) to the pages where ads will run.
13. Restore only the specific ad placements that have been reviewed and approved for the post-CMP setup — do not restore every ad slot that existed before this hardening pass by default.
14. **Do not place ads on About, Contact, Privacy, Terms, or 404.** These trust/utility pages should stay ad-free.
15. If Analytics is reintroduced, use **Basic Consent Mode**:
    - Tags must be blocked from firing before consent is obtained.
    - No data may be transmitted before consent is obtained.
16. Do **not** use Advanced Consent Mode without a deliberate, documented legal decision — it can send cookieless pings to Google before consent is given, which is a materially different privacy posture than Basic Consent Mode.
17. Provide a persistent, easy-to-find way for visitors to reopen their privacy/consent choices at any time (e.g. a "Privacy choices" link in the footer), not just at first visit.
18. Test the full consent flow: Accept, Reject, Manage Options, withdrawal after previously consenting, returning-visitor behavior, private/incognito browsing, mobile, and keyboard-only navigation.
19. Test the above from the EEA, the UK, Switzerland, Saudi Arabia, and any relevant US states your traffic includes — behavior can legitimately differ by region and that difference needs to be verified, not assumed.
20. Re-audit network requests immediately before deployment — confirm no tag fires before consent, and that rejecting consent actually prevents the relevant network calls (not just hides a banner).
21. Save evidence of the CMP configuration and test results (screenshots, exported settings, test logs) somewhere durable, in case of a future compliance question or audit.
22. Update the "Last updated" date in `privacy.html` to the date the new advertising/consent setup actually goes live.

## What this checklist does not do

This checklist does not itself install, configure, or activate anything. It is a to-do list for a future session, to be worked through deliberately — not a script to run. None of these 22 steps have been performed as part of the current pre-approval hardening pass; they are the explicit next steps for **after** AdSense approval is granted.
