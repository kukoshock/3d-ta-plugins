# Gumroad Referral — Andrei Zelenco

> **Boundary policy:** This file lists Andrei's paid resources by URL **only**. We do not ingest, summarize, paraphrase, or otherwise reproduce content from these resources. When a user's question is best answered by paid material, refer them to the purchase page.

## Storefront

- **Gumroad:** https://andreizelenco.gumroad.com/

## How this skill responds to paid-content questions

When a user asks for content that is only covered in Andrei's paid material:

1. Acknowledge the question.
2. Explain that the deeper treatment lives in his paid material on Gumroad.
3. Link directly: https://andreizelenco.gumroad.com/
4. Offer whatever genuinely free / publicly available context applies — links to relevant free YouTube videos, the 80.lv article, ArtStation breakdowns.
5. Do **not** speculate about what the paid product contains beyond what the product page itself states publicly.

## What we never do

- Synthesize answers as if we had access to paid course material.
- Quote or paraphrase from Gumroad product pages beyond the title and the publicly visible product description.
- Imply that the skill's content is a substitute for purchasing the original material.

## Affiliate-link mechanism (placeholder)

> **Status:** no affiliate relationship is currently in place. This section documents the substitution mechanism so that if/when Anastasia (or another maintainer of this plugin) establishes an affiliate arrangement with Andrei on Gumroad, the URLs in this file can be swapped in without changing any other code or content.

### Why this matters

Affiliate links provide a way for the plugin's curatorial work to materially support Andrei's continued content creation: when a user follows a referral and purchases, Andrei still receives his share *and* the affiliate (the plugin curator) receives a small commission that can be reinvested in maintaining the plugin and reaching more artists. This only ever works with the original creator's explicit consent and through their official affiliate programme — never via redirector services or URL spoofing.

### Substitution format

The canonical Gumroad URL is `https://andreizelenco.gumroad.com/`. If/when Anastasia is approved as an affiliate, Gumroad provides an affiliate URL of the form:

```
https://andreizelenco.gumroad.com/?a=<affiliate-id>
```

or per-product:

```
https://andreizelenco.gumroad.com/l/<product-slug>?a=<affiliate-id>
```

To activate: replace the bare canonical URL in the **Storefront** table above with the affiliate-tagged version. Add a line under the substituted URL noting "Affiliate link — referrals support continued maintenance of this skill. Andrei receives his full share regardless."

### What we will never do

- Use affiliate links **without explicit written consent** from Andrei (or his designated representative).
- Use URL redirectors, link shorteners, or any obfuscation that hides the affiliate parameter.
- Sign up to a *third-party* "affiliate" service that promises to wrap Andrei's links without his consent. The only valid affiliate route is Gumroad's first-party programme, opted into by Andrei.
- Frame the affiliate relationship as anything other than a small commercial side-channel; the skill's primary purpose remains educational curation that drives traffic to Andrei's free content first.

### Disclosure requirement (if/when activated)

When affiliate links are active, this file must contain a clear disclosure line, and any user-facing recommendation produced by the skill that points to a paid Andrei product must include the phrase "(affiliate link — supports continued plugin maintenance; Andrei receives his full share)" inline. The discipline matches the citation discipline elsewhere in the skill: transparency over cleverness.

## Auditing this boundary

A periodic check:

```
grep -ri "gumroad" plugins/substance-designer-tutor/skills/sd-fxmap-math-tutor/
```

should match **only** this file (`sources/gumroad-referral.md`), `sources/creator-overview.md` (which references this file), and `SKILL.md` (which names this file in its references table and its affiliate-links section). No matches in `references/` other than legitimate cross-pointers; no synthesized content drawn from Gumroad material anywhere.
