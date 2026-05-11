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

## Auditing this boundary

A periodic check:

```
grep -ri "gumroad" plugins/substance-designer-tutor/skills/sd-fxmap-math-tutor/
```

should match **only** this file (`sources/gumroad-referral.md`) and possibly `sources/creator-overview.md` (which references this file). No matches in `references/` or `SKILL.md` other than the attribution flow.
