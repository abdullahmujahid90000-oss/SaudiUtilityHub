# Saudi Utility Hub: Off-site SEO and Community Playbook

Everything in this folder is ready to copy and paste. Read this page first, then go to the file for the platform you're working on.

| File | What's in it |
|---|---|
| `answer-bank.md` | The 25 questions expats ask again and again, each with a short answer and the page to link. **Start here.** Every other draft is built from it. |
| `reddit-quora-drafts.md` | 6 Reddit posts and 8 Quora answers, written to each platform's self-promotion rules |
| `facebook-forums-drafts.md` | Facebook group replies (Pakistani, Indian, Filipino and city groups) plus Expat.com and InterNations posts |
| `x-linkedin-drafts.md` | 4 X threads, 10 single tweets, 1 full LinkedIn article and 3 LinkedIn posts |
| `arabic-drafts.md` | Arabic X posts and Arabic Hsoub I/O answers |
| `outreach-kit.md` | The press pitch for the new EOS data study, a Qwoted/Featured expert profile, guest-post pitches, and Product Hunt, AlternativeTo and directory listings |

---

## Why this is copy-and-paste instead of automatic posting

- **No connector can post there.** Claude has no tools for Reddit, Facebook groups, Quora, X, LinkedIn, Expat.com or InterNations. The Windsor.ai connector can only publish to Instagram and Google Business Profile.
- **Automated posting would get the site banned.** Reddit and almost every expat Facebook group ban automated or scheduled link posts. A domain that gets banned on Reddit stays blocked across the whole site, and that damage is hard to undo. Answers need to come from your own account, posted by you, replying to a real question that someone asked today.
- **What can be automated safely.** Your own X and LinkedIn posts can be scheduled with **Buffer** or **Typefully**, which are free for one account. The X and LinkedIn drafts are written so you can load a month into a scheduler in about 20 minutes.

## The routine (about 45 minutes a day, 5 days a week)

| Day | Task | Time |
|---|---|---|
| Mon | Search 2–3 Facebook groups for questions about this week's topic (see the search terms in `facebook-forums-drafts.md`), then reply with the matching answer from `answer-bank.md` | 30 min |
| Mon | Load the week's 5 tweets and 1 LinkedIn post into Buffer or Typefully | 15 min |
| Tue | Post 1 Reddit answer and 1 Quora answer | 30 min |
| Wed | Post 3 more Facebook group answers, plus 1 Expat.com reply | 30 min |
| Thu | Post 2 Reddit answers and 2 Quora answers | 40 min |
| Fri | Send 1 outreach pitch from `outreach-kit.md` (journalist, guest post or directory) | 30 min |
| Fri | Record a 30–60 second phone video answering one question from the answer bank and post it to TikTok, Reels and Shorts | 20 min |

**Weekly total:** 5 Facebook answers, 3 Reddit answers, 3 Quora answers, 1 short video and 1 pitch, which matches the plan.

### Rules that keep accounts alive

1. **Answer first, link second.** The reply has to fully answer the question even if nobody clicks. The link is there for "if you want to run your own numbers".
2. **Link to only one page**, and make it the page that answers that exact question, never the homepage.
3. **Disclose that the site is yours** wherever a link appears ("I run a free calculator site, here's the EOS one"). Reddit and Quora both require it, and people trust you more for it.
4. **Keep links to no more than 1 in 10 Reddit comments.** Answer 9 questions with no link at all. Your account history is what makes the 10th comment believable.
5. **Read each group's rules before you post.** Many Facebook groups only allow links in the comments, or only on certain days.
6. **Never paste the same text twice.** Reword the opening line every time. Reddit and Facebook both flag duplicate text.

## Tracking

Every link in these drafts carries a UTM tag such as `?utm_source=reddit&utm_medium=community`. In GA4, open **Reports → Acquisition → Traffic acquisition** and filter by session source to see which platform sends visitors. Check it once a month and move your time toward whatever works.

## On-site changes made in this commit

- **New linkable asset:** `/eos-payouts-by-salary-2026.html` with its CSV at `/data/eos-payouts-by-salary-2026.csv`. It's original, calculated data with schema.org `Dataset` markup, the page you pitch to journalists. It links from the EOS calculator and the sitewide footer, and it's in the sitemap.
- **Arabic pages expanded:** the 4 existing `/ar/` calculators now have worked examples, official sources and more FAQs.

## What still needs you

1. **Posting.** Reddit, Facebook groups and Quora have no connector, and their rules ban automated or ghost-run accounts. Banned domains stay banned. If you don't have time, hire a part-time virtual assistant (about 1 hour a day). Give them this folder and the account rules above, and have them post from accounts in your name, or from their own account with disclosure.
2. **Scheduling (zero effort after setup).** Connect Typefully (or Metricool) to claude.ai, then ask Claude to load the X and LinkedIn drafts into the queue.
