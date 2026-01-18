# Extraction Workflow

Step-by-step browser automation workflow for extracting FAQs from community forums.

---

## Overview

This workflow uses Claude's browser automation tools to systematically scan forums, identify high-quality posts, and extract FAQ entries.

**Estimated Time per Forum**:
- Reddit: 10-15 minutes for 10 FAQs
- Adobe Community: 15-20 minutes for 10 FAQs
- Polycount: 20-25 minutes for 5 FAQs (lower volume)

---

## Prerequisites

Before starting extraction:

1. **Verify browser tools available**:
   - tabs_context_mcp
   - tabs_create_mcp (if needed)
   - navigate
   - read_page
   - find (for locating elements)
   - computer (for clicking, scrolling)

2. **Load reference files**:
   - forum-sources.md (URLs and patterns)
   - faq-template.md (output format)
   - category-taxonomy.md (categorization)

3. **Check existing troubleshooting.md**:
   - Avoid extracting duplicates
   - Understand current coverage gaps

---

## Workflow: Reddit Extraction

### Phase 1: Setup and Navigation

**Step 1: Initialize Browser Session**

```
Tool: tabs_context_mcp
Parameters: { createIfEmpty: true }
Expected: Returns current tabs or creates new tab group
Action: Note the tabId for subsequent calls
```

**Step 2: Navigate to Sorted View**

```
Tool: navigate
Parameters: {
  tabId: [from step 1],
  url: "https://reddit.com/r/SubstanceDesigner/top/?t=year"
}
Expected: Loads Reddit sorted by Top This Year
Action: Wait 2-3 seconds for page load
```

**Step 3: Verify Page Loaded**

```
Tool: computer
Parameters: {
  action: "screenshot",
  tabId: [tabId]
}
Expected: Screenshot shows Reddit post list
Action: Visually confirm loaded correctly
```

### Phase 2: Extract Post List

**Step 4: Read Page Structure**

```
Tool: read_page
Parameters: {
  tabId: [tabId],
  filter: "all"
}
Expected: Accessibility tree with post elements
Action: Identify post cards, titles, vote counts
```

**Step 5: Identify High-Quality Posts**

From read_page output, find posts with:
- 10+ upvotes (visible in vote count element)
- 5+ comments (visible in comment count)
- Flair: "Question" or "Help"

Create list of candidate posts (titles + reference IDs or coordinates).

### Phase 3: Process Each Post

**For each candidate post:**

**Step 6: Navigate to Post**

```
Tool: computer
Parameters: {
  action: "left_click",
  ref: [post title reference from read_page],
  tabId: [tabId]
}
Expected: Opens full post view
Action: Wait 2-3 seconds for comments to load
```

**Step 7: Extract Post Content**

```
Tool: read_page
Parameters: {
  tabId: [tabId],
  filter: "all"
}
Expected: Post title, body text, comments
Action: Record question and context
```

**Step 8: Find Solution**

From read_page output:
1. Look for top-voted comment (highest score)
2. Check OP's post body for "Edit: Solved by..."
3. Look for "Accepted Answer" or "Solution" markers

Record solution text and any explanations.

**Step 9: Extract Metadata**

Record:
- Upvote count (from vote element)
- Comment count
- Post date (from timestamp)
- Post URL (from address bar)

**Step 10: Navigate Back**

```
Tool: navigate
Parameters: {
  tabId: [tabId],
  url: "back"
}
Expected: Returns to post list
Action: Ready for next post
```

Repeat steps 6-10 for each candidate post.

### Phase 4: Format and Present

**Step 11: Categorize Extracted FAQs**

For each extracted post:
- Determine category from category-taxonomy.md
- Visual Quality / Nodes / Tiling / Export / etc.

**Step 12: Format Using Template**

Apply faq-template.md structure:
```markdown
### [Number]. [Question from title]

**Symptom**: [Extract from post body - what user sees]

**Cause**: [Infer from solution or explanation in comments]

**Solution**:
| Step | Action | WHY This Works |
|------|--------|----------------|
| 1 | [Extract from top comment] | [Infer or extract explanation] |

**Source**: Reddit r/SubstanceDesigner - [URL] (Posted: [date], [X] upvotes, [Y] comments)

**Related**: [Check troubleshooting.md for related sections]
```

**Step 13: Present to User**

Show formatted FAQs with summary:
```
Found 10 FAQ candidates from r/SubstanceDesigner (Top This Year):

1. "Why does my normal map have stepping?" (847 upvotes)
   Category: Visual Quality
   Preview: 8-bit inheritance issue...

2. "Tile Sampler scale map not working" (134 upvotes)
   Category: Nodes & Parameters
   Preview: Connection to wrong input...

[... remaining 8 ...]

Options:
- Save to file for review
- Scan another forum (Adobe Community / Polycount)
- Filter by specific category
- Add to troubleshooting.md
```

---

## Workflow: Adobe Community Extraction

### Phase 1: Setup and Navigation

**Step 1: Initialize Browser** (same as Reddit)

**Step 2: Navigate to Forum**

```
Tool: navigate
Parameters: {
  tabId: [tabId],
  url: "https://community.adobe.com/t5/substance-3d-designer/bd-p/substance-3d-designer"
}
Expected: Loads Adobe Community forum board
```

**Step 3: Apply Sort Filter**

```
Tool: find
Parameters: {
  tabId: [tabId],
  query: "sort by views"
}
Expected: Finds sort dropdown or filter
Action: Note reference for clicking
```

```
Tool: computer
Parameters: {
  action: "left_click",
  ref: [sort dropdown ref],
  tabId: [tabId]
}
Expected: Opens sort options
```

```
Tool: find
Parameters: {
  tabId: [tabId],
  query: "most views"
}
Action: Select "Most Views" option
```

### Phase 2: Extract Post List

**Step 4: Read Forum Table**

```
Tool: read_page
Parameters: {
  tabId: [tabId],
  filter: "all"
}
Expected: Table structure with post titles, view counts, reply counts
Action: Parse table rows
```

**Step 5: Identify High-Quality Posts**

Filter for:
- 500+ views
- Accepted Solution icon (green checkmark)
- 3+ replies
- Posted within 3 years

### Phase 3: Process Each Post

**Step 6-10: Same pattern as Reddit**

Key differences:
- Look for "Accepted Solution" green banner (not just top comment)
- Check for Adobe staff responses (staff badge)
- Record view count instead of upvotes

### Phase 4: Format and Present

Same as Reddit workflow.

---

## Workflow: Polycount Extraction

### Phase 1: Google Site Search

**Step 1: Initialize Browser**

**Step 2: Navigate to Google Search**

```
Tool: navigate
Parameters: {
  tabId: [tabId],
  url: "https://google.com/search?q=site:polycount.com+substance+designer+problem"
}
```

**Step 3: Filter by Date**

```
Tool: find
Parameters: {
  query: "tools" or "search tools"
}
Action: Click to expand filters
```

```
Tool: find
Parameters: {
  query: "any time" or "past year"
}
Action: Select time filter (e.g., "Past 3 years")
```

### Phase 2: Extract Search Results

**Step 4: Read Search Results**

```
Tool: read_page
Parameters: {
  tabId: [tabId],
  filter: "all"
}
Expected: Google search result cards
Action: Identify Polycount thread links
```

**Step 5: Filter Results**

Look for:
- Thread titles with "[SOLVED]" or resolution keywords
- Recent dates (within 3 years)
- Substance Designer keywords in snippet

### Phase 3: Process Each Thread

**Step 6: Navigate to Thread**

```
Tool: computer
Parameters: {
  action: "left_click",
  ref: [search result link],
  tabId: [tabId]
}
Expected: Opens Polycount thread
```

**Step 7: Scan Thread**

```
Tool: read_page
Parameters: {
  tabId: [tabId],
  filter: "all"
}
Expected: Thread posts
Action: Find original question (first post) and solution (later posts)
```

**Step 8: Navigate to Last Page** (if multi-page thread)

```
Tool: find
Parameters: {
  query: "last page" or page number links
}
Action: Jump to last page to find "Thanks, this worked!" confirmation
```

**Step 9: Extract and Navigate Back**

Same as Reddit workflow.

### Phase 4: Format and Present

Same as Reddit workflow.

---

## Quality Assurance Checklist

Before presenting extracted FAQs to user, verify each entry:

### Content Quality
- [ ] Problem clearly stated in title and symptom
- [ ] Solution is specific and actionable (not vague "try different settings")
- [ ] WHY explanation included (or can be inferred from context)
- [ ] No scripting/automation content (artist-focused only)

### Source Validation
- [ ] URL recorded correctly
- [ ] Date within 3 years
- [ ] Engagement metrics recorded (upvotes/views/replies)
- [ ] Forum name correct

### Categorization
- [ ] Fits established category from taxonomy
- [ ] Not a duplicate of existing troubleshooting.md entry
- [ ] Category clearly indicated in output

### Formatting
- [ ] Follows faq-template.md structure
- [ ] Markdown table formatted correctly
- [ ] Related links added (if applicable)

---

## Error Handling

### Common Issues and Solutions

**Issue: Page not loading**
```
Solution:
1. Wait 5 seconds
2. Take screenshot to verify
3. If still blank, try navigate again
4. If persistent, skip forum temporarily
```

**Issue: Can't find post elements**
```
Solution:
1. Use read_page with filter: "all"
2. Search output for keywords (title, vote, comment)
3. Use find tool with natural language query
4. If layout changed, adapt to new structure
```

**Issue: Lost tab context**
```
Solution:
1. Call tabs_context_mcp again
2. Get fresh tabId
3. Resume from last successful navigation
```

**Issue: Rate limiting / Blocked**
```
Solution:
1. Wait 30-60 seconds between requests
2. If Reddit shows rate limit, switch to Adobe Community
3. Respect robots.txt and forum ToS
4. Don't scrape aggressively
```

---

## Optimization Tips

### For Faster Extraction

1. **Batch similar actions**: Navigate → Extract → Navigate back → Repeat
2. **Use keyboard shortcuts**: Ctrl+W to close tabs instead of clicking
3. **Parallel forum scanning**: Open multiple tabs for different forums
4. **Pre-filter in URL**: Use search URLs with filters baked in

### For Better Quality

1. **Cross-reference solutions**: If same problem appears on multiple forums, combine insights
2. **Check comment dates**: Sometimes old solutions get outdated by new software features
3. **Verify terminology**: Ensure node names match current SD version
4. **Read full threads**: Don't just grab first answer - sometimes better solution is further down

---

## Example Complete Session

**Goal**: Extract 5 Visual Quality FAQs from Reddit

```
1. tabs_context_mcp → tabId: 123

2. navigate to reddit.com/r/SubstanceDesigner/search/?q=banding&sort=top&t=year

3. computer: screenshot → verify loaded

4. read_page → Extract post list

5. Identify candidates:
   - "Why stepping in normals?" (847 upvotes, 23 comments)
   - "Banding in gradient map" (312 upvotes, 14 comments)
   - "Blurry height artifacts" (156 upvotes, 9 comments)
   - "Material looks posterized" (89 upvotes, 7 comments)
   - "Seams in tiled normal" (67 upvotes, 11 comments)

6. For each candidate:
   - Click title
   - read_page → extract question + top solution
   - Record metadata
   - navigate: back

7. Format 5 FAQs using template

8. Present to user:

   "Extracted 5 Visual Quality FAQs from Reddit:

   1. Why does my normal map have stepping? (847 upvotes)
   2. Banding in Gradient Map output (312 upvotes)
   3. Height map appears blurry/soft (156 upvotes)
   4. Material looks posterized in 3D view (89 upvotes)
   5. Visible seams in tiled normal map (67 upvotes)

   Save to file? Scan another category? Add to troubleshooting.md?"
```

---

## Browser Automation Code Patterns

### Pattern: Safe Navigation with Verification

```
1. navigate to URL
2. wait 3 seconds (implicit)
3. computer: screenshot
4. Visually verify page loaded correctly
5. If failed, retry once
6. If still failed, report to user and skip
```

### Pattern: Extract List → Process Items → Return

```
For each item in list:
  1. Click item (computer: left_click with ref)
  2. Wait for load
  3. read_page to extract content
  4. Record data
  5. navigate: back
  6. Wait for list to reload
  7. Next item
```

### Pattern: Find Element → Interact

```
1. find: "button text" or element description
2. Get ref_id from result
3. computer: left_click with ref
4. Verify action completed (screenshot or read_page)
```

---

## Post-Extraction Workflow

After extracting FAQs:

1. **Save to temporary file** (if user requests):
   ```
   plugins/substance-designer-tutor/skills/faq-generator/extracted-faqs-[date].md
   ```

2. **Cross-check with troubleshooting.md**:
   - Read existing troubleshooting.md
   - Identify truly new issues
   - Note duplicates or related entries

3. **Present integration options**:
   - Add to troubleshooting.md
   - Save as separate FAQ reference
   - Export for manual review

4. **Update extraction log** (optional):
   - Track which forums scanned
   - Last extraction date
   - Categories covered
