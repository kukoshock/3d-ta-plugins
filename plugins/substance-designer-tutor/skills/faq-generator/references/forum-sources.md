# Forum Sources

Comprehensive guide to forum URLs, navigation patterns, search strategies, and quality indicators for extracting Substance Designer FAQs.

---

## Forum Index

| Forum | Artist Level | Content Type | Update Frequency | Quality Variance |
|-------|--------------|--------------|------------------|------------------|
| **Reddit r/SubstanceDesigner** | Beginner-Advanced | Mixed Q&A, showcases, tips | Daily | High (filter carefully) |
| **Adobe Community** | Beginner-Intermediate | Technical support, bugs | Weekly | Medium (official support) |
| **Polycount** | Intermediate-Advanced | Deep technical, workflows | Monthly | Low (consistently high quality) |

---

## Reddit r/SubstanceDesigner

### URLs

**Main Subreddit**: https://reddit.com/r/SubstanceDesigner

**Sorted Views**:
- Top This Year: https://reddit.com/r/SubstanceDesigner/top/?t=year
- Top This Month: https://reddit.com/r/SubstanceDesigner/top/?t=month
- Hot (Recent + Popular): https://reddit.com/r/SubstanceDesigner/hot/

**Search URL Pattern**:
```
https://reddit.com/r/SubstanceDesigner/search/?q={query}&restrict_sr=1&sort=top&t=year
```

### Quality Metrics

| Metric | Threshold | Meaning |
|--------|-----------|---------|
| **Upvotes** | 10+ | Strong community validation |
| **Comments** | 5+ | Active discussion, likely has solutions |
| **Upvote Ratio** | > 85% | Not controversial, helpful content |
| **Flair** | "Question", "Help" | Directly relevant |

**Excellent Candidates**: 50+ upvotes, 10+ comments, [Solved] or [Answered] flair

### Navigation Pattern

1. **Load sorted view** (Top This Year recommended)
2. **Identify post list** - Look for article cards with vote counts
3. **Filter by flair** - "Question", "Help", "Tutorial"
4. **Check engagement** - Upvotes + comment count
5. **Open high-quality posts** - Click title to view full post + comments
6. **Find solution** - Top comment or OP's edit with "Edit: Solved by..."

### Artist-Focused Search Terms

**Visual Quality Issues**:
```
"blurry normal map"
"stepping in gradient"
"banding artifacts"
"material looks flat"
"seam visible"
"tiling problem"
```

**Node Confusion**:
```
"Tile Sampler not working"
"Height Blend edges"
"Curvature artifacts"
"inheritance issue"
```

**Integration Problems**:
```
"looks different in Unreal"
"export to Unity"
"normal map flipped"
"roughness too dark"
```

**Workflow Questions**:
```
"where to start"
"beginner mistakes"
"best practices"
"material workflow"
```

### Exclude Terms

**Technical Artist Content** (Add to search with `-term`):
```
-python
-script
-automation
-API
-batch
-pipeline
-SDK
-procedural generation (code context)
```

### Example High-Quality Post Patterns

**Title Patterns That Indicate Good FAQs**:
- "Why does [X] happen when I [Y]?"
- "How do I fix [visual problem]?"
- "[Node name] not working as expected"
- "Material looks wrong in [engine]"

**Title Patterns to Skip**:
- "Check out my material!" (showcase, not Q&A)
- "Substance vs [other tool]" (comparison, not tutorial)
- "Is this good?" (subjective feedback request)

---

## Adobe Community

### URLs

**Main Forum**: https://community.adobe.com/t5/substance-3d-designer/bd-p/substance-3d-designer

**Sorted Views**:
- Most Views: Add `?sort=views` parameter
- Recent Activity: Add `?sort=latest` parameter
- Unanswered: Add `?filter=unanswered` parameter (then invert - find ANSWERED)

**Search URL Pattern**:
```
https://community.adobe.com/t5/forums/searchpage/tab/message?filter=location&location=forum-board:substance-3d-designer&q={query}&sort_by=relevance
```

### Quality Metrics

| Metric | Threshold | Meaning |
|--------|-----------|---------|
| **Views** | 500+ | Widely encountered problem |
| **Likes** | 5+ | Community finds it useful |
| **Accepted Solution** | ✓ (green checkmark) | Officially resolved |
| **Replies** | 3+ | Active troubleshooting |

**Excellent Candidates**: 1000+ views, Accepted Solution, Adobe staff response

### Navigation Pattern

1. **Load forum** - Main board URL
2. **Apply sort** - Views or Latest
3. **Identify post list** - Table with view count, reply count
4. **Filter for "Solved"** - Look for green checkmark icon
5. **Open post** - Click title
6. **Find Accepted Solution** - Look for green "Accepted Solution" banner
7. **Check date** - Posted within 3 years

### Adobe-Specific Considerations

**Official Responses**: Posts with Adobe employee responses are high-quality (staff badge visible)

**Bug Reports vs Questions**:
- Bug reports may not have solutions (just "acknowledged")
- Focus on "How do I..." and "Why does..." questions

**Version-Specific Issues**:
- Check which SD version the post references
- Solutions for very old versions (< 2020) may be outdated

### Artist-Focused Search Terms

Same as Reddit, plus:

**Installation/Setup** (artist-relevant only):
- "material not loading"
- "preview not working"
- "export failed"

**NOT artist-focused** (exclude):
- "automation scripting"
- "batch export command line"

---

## Polycount

### URLs

**Search URL** (Polycount doesn't have dedicated SD board):
```
https://polycount.com/search?query=substance%20designer&type=post&sort=relevance
```

**Alternative - Google Site Search**:
```
site:polycount.com "substance designer" [your query]
```

### Quality Metrics

| Metric | Threshold | Meaning |
|--------|-----------|---------|
| **Replies** | 5+ | Active discussion |
| **Thread Views** | 1000+ | Popular topic |
| **Poster Reputation** | Check profile | Industry professionals common on Polycount |

**Excellent Candidates**: 10+ replies, 2000+ views, marked [SOLVED] in title

### Navigation Pattern

1. **Use Google Site Search** (more reliable than Polycount search)
2. **Identify thread titles** with SD keywords
3. **Check date** - Last 3 years
4. **Open thread** - Scan for resolution in later posts
5. **Check last page** - Often has "Thanks, this worked!" confirmation

### Polycount-Specific Considerations

**High Signal-to-Noise**: Polycount attracts industry professionals, so threads are often higher quality but less frequent

**Workflow Focus**: Polycount users often discuss production workflows and game engine integration

**Advanced Topics**: May be more advanced than typical beginner FAQs - use for intermediate/advanced categories

---

## Search Strategy Matrix

### By Problem Category

| Category | Best Forum | Search Terms | Sort Method |
|----------|-----------|--------------|-------------|
| **Visual Quality** | Reddit | "banding", "artifacts", "blurry", "stepping" | Top This Year |
| **Node Issues** | Adobe Community | [Node name] + "not working", "problem" | Most Views |
| **Export/Integration** | Polycount | "Unreal", "Unity", "export", "different look" | Google Site |
| **Workflow** | Reddit | "beginner", "workflow", "best practices" | Top All Time |
| **Performance** | Adobe Community | "slow", "lag", "performance" | Recent Activity |

### By Difficulty Level

| Level | Focus Forums | Search Approach |
|-------|--------------|-----------------|
| **Beginner** | Reddit, Adobe Community | "beginner mistakes", "getting started", basic node names |
| **Intermediate** | All three | Specific technical issues, integration questions |
| **Advanced** | Polycount, r/SubstanceDesigner | Optimization, complex graph problems, edge cases |

---

## Quality Indicators Checklist

Before extracting a post as FAQ:

- [ ] **Engagement**: Meets forum-specific threshold (upvotes/views/replies)
- [ ] **Resolution**: Has accepted/confirmed solution
- [ ] **Clarity**: Problem clearly stated in title and body
- [ ] **Artist-Focused**: Visual/workflow issue, NOT scripting/automation
- [ ] **Recency**: Posted within 3 years
- [ ] **Actionable**: Solution provides specific steps, not just "try different settings"
- [ ] **Explanation**: Solution includes WHY it works (or you can infer it)
- [ ] **Non-Duplicate**: Not already covered in troubleshooting.md

---

## Common Pitfalls to Avoid

### False Positives

**Showcase Posts Disguised as Questions**:
- Title: "How do I make this better?"
- Reality: Just showing off work, no real question

**Solution: Check post body - if it's mostly images with vague "thoughts?" ask, skip it**

### Incomplete Solutions

**Abandoned Threads**:
- OP asks question
- Some discussion
- Never confirmed what worked

**Solution: Only extract if later post confirms resolution**

### Off-Topic Content

**Substance Painter Confusion**:
- Many posts confuse Designer and Painter
- Painter questions are NOT relevant

**Solution: Verify question is about Designer specifically (node graphs, procedural generation)**

### Version-Specific Issues

**Old Software Bugs**:
- Issue from SD 2018 that was fixed in 2020

**Solution: Check if solution is still relevant or if it was a temporary bug**

---

## Browser Automation Hints

### For Reddit

**Element Patterns**:
- Post list: `<div class="Post">` or `<article>` tags
- Vote count: `<div class="vote">` or `data-score` attribute
- Title: `<h3>` with link to post
- Comments count: Look for "comments" text

**Interaction Points**:
- Click title to open post
- Back button to return to list
- Scroll for infinite load (if using continuous scroll view)

### For Adobe Community

**Element Patterns**:
- Post list: Table structure with `<tr>` rows
- Views: `<span class="lia-view-count">`
- Accepted Solution: `<span class="lia-accepted-solution">` icon
- Title: `<a class="lia-link-navigation">`

**Interaction Points**:
- Click title in table
- Look for green checkmark in solution
- Back to board

### For Polycount (via Google)

**Search Results**:
- Standard Google result cards
- Use `site:polycount.com` filter
- Click through to thread
- Check last page for resolution confirmation

---

## Example Extraction Session

**Goal**: Find 10 Visual Quality FAQs from Reddit

1. Navigate to: `https://reddit.com/r/SubstanceDesigner/search/?q=banding+OR+artifacts+OR+stepping&restrict_sr=1&sort=top&t=year`

2. Filter results:
   - Min 10 upvotes
   - Min 5 comments
   - Flair: Question/Help

3. For each result:
   - Open post
   - Read problem description
   - Find top-voted solution or OP's "Edit: Solved"
   - Record: Title, upvotes, solution summary, URL, date
   - Back to results

4. Format extracted data using faq-template.md

5. Present to user
