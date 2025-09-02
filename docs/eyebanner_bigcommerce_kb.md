# eyeBanner BigCommerce Blog & SEO Knowledge Base
_A single source of truth for content, SEO, design, and publishing on_ **retractable-banner-stands.com**

---

## 0) Scope & Purpose
This document codifies **fixed rules** for eyeBanner’s BigCommerce store and blog—brand voice, layout, media, SEO, architecture, and QA. It is written so any external content or SEO agent can work without additional prompts.

**Who should use this:** writers, editors, SEOs, designers, devs, VA/publishers.

**Where it applies:**
- Primary domain only: **https://www.retractable-banner-stands.com** (never a BigCommerce subdomain)
- All public web content: product/category pages, blog posts, general web pages

---

## 1) Brand Identity & Voice

### 1.1 Voice snapshot
- **Tone:** friendly-expert, pragmatic, data-driven, encouraging, U.S. plain-English
- **POV:** “we” for eyeBanner; speak to “you”
- **Style:** mix short punch lines with longer explanatory sentences; natural contractions; define jargon

**E-E-A-T cues:** cite reputable sources; add first-hand details (e.g., “We stress-test poles to ±30 mph at our Phoenix facility.”)

**On-brand vs. off-brand**
- ✅ “A 12-ft double-sided flag increased curb visibility by **48 %** in our A/B test last fall.”
- ❌ “Please know that we are thrilled to collaborate…” (formal fluff)

### 1.2 Forbidden & discouraged phrases (apply everywhere)
- **Formal fluff:** “please know that,” “kindly note,” “on behalf of,” “request to inform,” “understanding the focus of the event”
- **Hype:** “revolutionary,” “world-class,” “game-changing,” “amazing,” “ultimate guide/solution”
- **Clichés:** “collaboration,” “strategic vision,” “demonstrating leadership,” “diplomatic interactions”
- **Email/event lingo:** “RSVP,” “kindly RSVP,” “appears,” “public service” (self-description)
- **Wrap-ups:** “in conclusion,” “to sum up,” “overall” (end with a **CTA** section instead)

> Exception: appearing inside a **direct, cited** quotation.

### 1.3 Brand value pillars (embed in copy where relevant)
- **Transparent wholesale pricing:** all displayed prices already include our wholesale discount—**no coupon needed**.
- **No minimum order:** wholesale price applies even for **1 unit**.
- **Lowest-price guarantee:** we match any published price among Google’s **Top 5 organic** results for “wholesale feather flags” (proof within 7 days).
- **Extra savings:** **Reseller** and **Non-profit** (churches, schools, colleges) discounts on top of listed wholesale.
- **Manufacturer-direct:** we own the presses—economies of scale = **lower prices + better materials** (e.g., 210 g knitted poly, UV-safe inks).

---

## 2) Design System (Typography, Palette, Logo)

### 2.1 Typography
| Area | Font stack | Notes |
|---|---|---|
| Headings (H1–H3) | `Inter, "Helvetica Neue", Arial, sans-serif` | H1 weight 700; H2–H3 600; H1 title-case, others sentence-case; line-height ~1.25 |
| Body | same as above | 16 px desktop / 15 px mobile; max ~75-char measure; line-height ~1.6 |
| Captions | same | 14 px, #666 |
| Code (rare) | `"Courier New", Courier, monospace` | Only for literal commands |

**Accessibility:** target **WCAG 2.1 AA** contrast. Avoid using green for small body text.

### 2.2 Palette (from logo)
- **Blue primary:** `#0099CC` (dark: `#007CA3`; tint: `#E6F7FB`)
- **Green accent:** `#66CC00` (dark: `#4CA300`; tint: `#F1FAE9`)
- **Neutrals:** `#111` (H1–H2), `#222` (body), `#666` (muted), `#FAFAFA` (card), `#F5F5F5` (section), `#E6E6E6` (border)

### 2.3 Logo usage
- Source: `https://cdn11.bigcommerce.com/s-awvsv/images/stencil/300x60/retractable_banner_stands_eyebanner_onelogo.original.png`
- Alt text: `eyeBanner logo`
- Min width: 120 px; maintain safe-zone (height of “e”)
- **No gradients, shadows, textures, or color edits.** Place on white, `#FAFAFA`, or blue-tint `#E6F7FB`.

---

## 3) Media & Image Rules

### 3.1 File, size, paths
- **Format:** WebP (JPG fallback only if necessary); PNG only for transparency
- **Size:** ≤ **100 KB** each (compress aggressively); hero ≤ 150 KB
- **Dimensions:** hero **1200×800 px**; inline square **800×800 px**
- **Paths:** `/content/blog_images/…` (lowercase-hyphenated filenames)
- **Performance:** `loading="lazy"`, width/height attributes set; **no base64** embeds

### 3.2 Alt-text style (≤ 125 chars)
- Lead with the **object**; include **one** keyword only if natural; describe action/setting; omit “image of / picture of”
- Example: `double-sided feather flag kit outside Phoenix car-wash`

### 3.3 Visual creation – decision tree
- **Data charts / infographics:** **Matplotlib (Python)** only—ensures numerical accuracy; export WebP 1600 px; include alt + one-line caption
- **Lifestyle/case-study photos (wide scenes):** **FLUX-Kontext** (add `text_in_english=true`; keep file small)
- **Exact text graphics (SALE, OPEN HOUSE, step-by-step diagrams):** **ChatGPT Image** (high text accuracy)
- **Product mockups with text:** FLUX render background → ChatGPT overlay for text if needed

**Quota per major piece:** ≥ **5 images**, **1–2 short videos** (5–15 s), **≥1 PDF** (templates, spec sheet, setup guide)

---

## 4) Advanced CSS Layout (Inline-First)

**Policy:** inline styles preferred; tiny optional `<style>` (≤1 KB) only for responsive tables.
**Visual stance:** **no gradients**. Use flat fills, 1 px borders, 12–14 px radii, generous white space.

- **Global content wrapper:** `max-width:840px;margin:0 auto;padding:16px 20px;line-height:1.6;`
- **Responsive columns (no media queries):** `display:flex;flex-wrap:wrap;gap:16px;min-width:320px` cards auto-stack
- **Image+caption figure:** `max-width:100%;height:auto;border-radius:12px;border:1px solid #E6E6E6`
- **CTA band (flat):** blue background `#0099CC`, white button; **no gradient**
- **Info/Warning boxes:** left accent bar (green), neutral card bg
- **Comparison cards:** economy / standard / premium tiles (links to mapped URLs)
- **Responsive tables:** see `.rb-table` pattern with mobile stacking (Section K.10)
- **FAQ toggles:** HTML `<details><summary>` (no JS)

> Lint before publish: **0 occurrences** of `gradient`, `box-shadow`; blue for primary CTA; green only for accents.

### 4.1 Responsive Table Snippet
```html
<style>
@media (max-width:720px){
  .rb-table{display:block;width:100%}
  .rb-table thead{display:none}
  .rb-table tr{display:block;border:1px solid #E6E6E6;border-radius:12px;margin:10px 0;background:#FAFAFA}
  .rb-table td{display:flex;justify-content:space-between;gap:12px;padding:10px 12px;border-bottom:1px solid #E6E6E6}
  .rb-table td:last-child{border-bottom:0}
  .rb-table td::before{content:attr(data-label);font-weight:600;color:#111}
}
</style>
<table class="rb-table" style="width:100%;border-collapse:collapse;margin:12px 0;">
  <thead>
    <tr>
      <th style="text-align:left;border-bottom:2px solid #E6E6E6;padding:8px 10px;">Size</th>
      <th style="text-align:left;border-bottom:2px solid #E6E6E6;padding:8px 10px;">Single-Sided</th>
      <th style="text-align:left;border-bottom:2px solid #E6E6E6;padding:8px 10px;">Double-Sided</th>
      <th style="text-align:left;border-bottom:2px solid #E6E6E6;padding:8px 10px;">With Pole Kit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td data-label="Size" style="padding:10px;border-bottom:1px solid #E6E6E6;">8 ft</td>
      <td data-label="Single-Sided" style="padding:10px;border-bottom:1px solid #E6E6E6;">From $XX</td>
      <td data-label="Double-Sided" style="padding:10px;border-bottom:1px solid #E6E6E6;">From $XX</td>
      <td data-label="With Pole Kit" style="padding:10px;border-bottom:1px solid #E6E6E6;">From $XX</td>
    </tr>
    <tr>
      <td data-label="Size" style="padding:10px;border-bottom:1px solid #E6E6E6;">13.5 ft</td>
      <td data-label="Single-Sided" style="padding:10px;border-bottom:1px solid #E6E6E6;">From $XX</td>
      <td data-label="Double-Sided" style="padding:10px;border-bottom:1px solid #E6E6E6;">From $XX</td>
      <td data-label="With Pole Kit" style="padding:10px;border-bottom:1px solid #E6E6E6;">From $XX</td>
    </tr>
  </tbody>
</table>
```

---

## 5) SEO Framework

### 5.1 Micro-SEO guardrails
- **Keyword density:** ≤ **3 %** (primary + synonyms)
- **Meta title:** ≤ **60 chars**; include primary keyword once; brand optional
- **Meta description:** ≤ **155 chars**; 1× keyword + 1 benefit + 1 CTA
- **Schema required:**
  - Posts: `Article`/`BlogPosting`; add `FAQPage` if ≥3 FAQs
  - Product: `Product` (extend with `additionalProperty` as needed)
  - Category: `ItemList` (`CollectionPage`) + `BreadcrumbList`
  - All pages: `BreadcrumbList`
- **Internal links:** **≥4 per 1 000 words** (≈1 every 150–200 wds). First link within first two subsections.
- **External links:** add 3–5 to reputable sources (.gov/.org, trade journals, Wikipedia). **Never** to competitor shops. Use `rel="noopener"`
- **URLs:** lowercase, hyphenated, ≤ 5 words, match intent (product vs category vs blog)

### 5.2 SERP-fit by BigCommerce page type
- **Product page:** `Product` schema; best for **transactional single-SKU** queries (e.g., *double-sided*, *with pole*, *custom*).
- **Category page:** `ItemList` schema; best for **browse & compare** (e.g., *wholesale*, *cheap*, *church*, *open house*).
- **Web page:** general `WebPage` (use for static hub/landing when needed).
- **Blog page:** `BlogPosting`; for informational queries, case studies, news.

---

## 6) Site Architecture & URL Mapping (Phase-1)

**Home page:** aim to rank **“Retractable Banner Stand”**; include a **Feather Flags** content block near the bottom.

**FAQ page:** `/faq/` doubles as blog-sitemap. **Update** whenever a new post goes live.

### 6.1 Final mapping (non-overlapping; match intent)

| Keyword focus | URL | BC page type | Notes |
|---|---|---|---|
| **Wholesale Feather Flags** | `/wholesale-feather-flags/` | **Category** | Convert existing web page → category; exact-match slug; bulk pricing tables; canonical to base |
| **Cheap Feather Flags** | `/cheap-feather-flags/` | **Category** | Genuine budget SKUs; “From $XX” price labels |
| **Double-Sided Feather Flags** | `/double-sided-feather-flags/` | **Product** | One master SKU w/ size variants; include comparison table (single vs double) |
| **Feather Flags with Pole** | `/feather-flags-with-pole/` | **Product** | Kit option defaulted; “Includes Pole: Yes” in schema |
| **Custom Feather Flags** | `/custom-feather-banners/` | **Product** (legacy) | Keep slug; optimize for “custom feather flags (banners)”; add `alternateName` |
| **Church Feather Flags** | `/church-feather-flags/` | **Category** | 8–12 faith designs + “Design Your Own” tile |
| **Open-House Feather Flags** | `/open-house-feather-flags/` | **Category** | 8–12 real-estate/open-house designs |

**Rule:** Blogs and general web pages **must not** duplicate the exact SEO target of these primary URLs. They **support** with internal links.

### 6.2 Menu & silo guidelines
- Products/Categories vs Blog Categories must **complement, not duplicate**.
- Surface long-tails in menus where they drive conversions (e.g., **Church Feather Flags**, **Open House**).
- Tertiary helpful menu ideas: *Feather flag banners*, *Templates*, *Pole & base*, *Design tips*, *Sizes*, *Outdoor advertising*.

---

## 7) Content Production Standards

### 7.1 Length & structure
- **≥ 1 500 words** per blog post (pillar posts 3 000+)
- Use H2/H3 hierarchy; no “Conclusion” section—end with **CTA** block
- Add tables for specs/comparisons; use our responsive table pattern

### 7.2 Links & rewrites
- Keep **all original links** when rewriting legacy posts
- Add internal links per cadence rule and to **Phase-1 pillar URLs**
- Add 3–5 **authoritative** external links (no competitor shops)

### 7.3 Topic strategy
- **Case studies** (church welcome flags, open-house boosts, car-wash promos)
- **Cost & ROI** vs. other media (include real numbers)
- **Industry-adjacent news** for our buyers (sign/print trade shows, AI design tools, small-business marketing). If off-topic, add at least one paragraph + internal link to feather-flag products.

### 7.4 Multimedia placements (italicize placeholders in drafts)
- *[Hero image here]* *[Setup video placeholder]* *[Download: template PDF]*

---

## 8) Humanization & Originality

### 8.1 Humanization checklist (operational)
- Sentence-length variance; natural contractions; rhetorical questions; occasional fragments
- First-hand anecdotes; specific numbers and quotes; mild idioms
- Vary paragraph lengths; one short punch fragment per article is fine

### 8.2 Plagiarism threshold
- External checker pass: **≤ 5 % matched words** (proper citations excluded)

### 8.3 Appendix A — Zero-AI-Detection Writing Playbook
*(Merged faithfully from Notes #1 and #2; use this for every long-form piece.)*

**Core framework**
- **Natural flow:** mix 5-word jolts with 25-word explainers; 1-sentence zingers next to 6-sentence blocks; transitions like “But here’s the thing…”, “Now here’s where it gets interesting…”
- **Conversational tone:** direct address (“You’ve probably noticed…”), casual connectors (“Plus,” “And honestly,”), rhetorical questions
- **Imperfection strategy:** start some sentences with **And/But**; fragments (“Sometimes. Just because.”); ~**80 % active / 20 % passive**
- **Authenticity markers:** specific numbers (tested **5** times), **time stamps** (six weeks ago; back in 2019), **real scenarios** and quirks (“I’m paranoid about breaking new stuff”)
- **Language variety:** contractions everywhere; idioms/colloquialisms (used judiciously); industry jargon when relevant
- **Structure rules:** conversational sub-heads; natural lists; parenthetical asides; write like explaining to a colleague over coffee
- **Honest voice:** real pros & cons; minor complaints okay; light humor if earned

**Never-use list (AI flags):** “delve into,” “dive deep,” “comprehensive guide,” “ultimate solution,” “it’s important to note,” “in conclusion,” “furthermore.” Don’t end every paragraph with a tidy summary; avoid perfect grammar—allow **1–2 micro slips per 1 000 words.**

**Pre-publish checks**
- Contractions: **≥ 5–8 per 500 words**
- Varied sentence lengths: visible pattern
- Conversational transitions: every ~150 words
- Rhetorical questions: ≥ 2 per 1 000 words
- Personal pronouns: frequent “I / we / you”
- Specific examples: ≥ 3 with numbers
- Minor imperfections: 1–2 deliberate per 1 000 words

**Advanced:** personality injection (insight only a practitioner knows), side-thought tangent (brief), coffee-shop read-aloud test.

---

## 9) Publishing Workflow (BigCommerce)

1. Draft in Markdown with YAML front-matter (Section 10), then convert to HTML.
2. Upload images to `/content/blog_images/…` first (WebDAV).
3. Paste HTML into **Blog** or **Product/Category Description** block.
4. Insert **inline CSS** components from Section 4 as needed (no gradients).
5. Add schema blocks if the theme lacks them (FAQ, HowTo, etc.).
6. Update `/faq/` page index when a post goes live.
7. Smoke test: meta length, canonical, breadcrumbs, internal links to Phase-1 pillars.

> **Legacy special-handling:** `/custom-feather-banners/` is a product page with a fixed top listing block—**do not alter**. Re-work only the Description HTML (keep all existing downloads/media/links).

---

## 10) Front-Matter / Metadata (for drafts)
```yaml
---
title: "How Double-Sided Feather Flags Double Your Foot Traffic"
slug: double-sided-feather-flags
metaTitle: "Double-Sided Feather Flags | eyeBanner"
metaDescription: "Two-way visibility with double-sided feather flags—UV-safe, from $49. Ships in 48 hrs."
datePublished: 2025-09-02
author: eyeBanner Editorial
tags: [feather flags, double-sided, outdoor advertising]
featuredImage: /content/blog_images/double-sided-flag-hero.webp
schemaType: Article
---
```

---

## 11) Internal Linking Policy (Topical Authority)

- Link density: ≥ 4 internal links per 1 000 words; place the **first** within the first two subsections.
- **Must-link hubs:**
  - `/wholesale-feather-flags/`
  - `/cheap-feather-flags/`
  - `/double-sided-feather-flags/`
  - `/feather-flags-with-pole/`
  - `/custom-feather-banners/`
- Sibling support: link horizontally between church/open-house and core categories.
- Anchors ≤ 6 words; vary phrasing (“bulk feather flags,” “wholesale options,” “double-sided kits”).

---

## 12) Legal & Footer
```
© 2025 eyeBanner®. All rights reserved.
All prices include wholesale discount; additional reseller & nonprofit pricing available.
Lowest-Price Guarantee: We match any published price among the current Google Top-5 organic results for “wholesale feather flags.” Proof required within 7 days of purchase.
```
Place copyright after the CTA on blog posts (12 px, #666).

---

## 13) Changelog (maintain in this file)
- **2025-09-02** – Initial consolidated KB; URL map finalized; no-gradient CSS; Appendix A (Zero-AI-Detection) added.

---

### Quick Start (TL;DR for new contributors)
1) **Write human:** follow Appendix A; end with a **CTA**, not a conclusion.
2) **Match intent:** product vs category vs blog per Section 5.2.
3) **Images:** WebP ≤ 100 KB; Matplotlib for any charts.
4) **Links:** 4+ internal per 1 000 words; 3–5 authoritative outbound; never competitors.
5) **Publish:** inline CSS components; update `/faq/`; check schema & meta lengths.

— End of Knowledge Base —
