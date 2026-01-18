# Contributing to Substance Designer Tutor

Thank you for your interest in expanding this tutor's knowledge base! This guide explains how to document additional parts of the Designer First Steps course.

## Overview

The tutor's knowledge comes from studying the video tutorials and extracting:
- Node chains and workflows
- Parameter values (actual numbers, not just concepts)
- Key quotes and teaching moments
- Timestamps for reference

## How to Add a New Part

### 1. Watch the Video

- Watch the entire video at least once for context
- Follow along in Substance Designer if possible
- Note the timestamps of key moments

### 2. Create a Part File

Create a new file in `skills/tutor/references/parts/` using the naming convention:
```
part-XX-title.md
```

For example: `part-08-importing-images.md`

Use the template in `parts/TEMPLATE.md` as your starting point.

### 3. Document Key Information

**Required sections:**
- Video metadata (URL, duration, timestamps)
- Node chain / workflow summary
- Parameter values with actual numbers
- Key quotes from the instructor
- Common issues and solutions

**Quality standards:**
- Include **actual parameter values**, not just "adjust as needed"
- Note **specific timestamps** for key moments
- Use **artist-friendly language** - explain jargon
- Focus on the **"why"** not just the "what"

### 4. Update Index Files

After adding a new part:

1. Update `references/video-tutorials.md` with:
   - Video URL and duration
   - Chapter breakdown with timestamps

2. Update `references/node-parameters.md` with:
   - Any new nodes introduced
   - Parameter values used in the project

3. Update `ROADMAP.md`:
   - Mark the part as "Complete"
   - Update the coverage percentage

### 5. Test the Knowledge

Ask the tutor questions about the new content to verify it's accessible:
- "Explain [new concept]"
- "How do I use [new node]?"
- "What values should I use for [parameter]?"

## Checklist for New Parts

- [ ] Video watched and notes taken
- [ ] Part file created from template
- [ ] All timestamps documented
- [ ] Node chains clearly explained
- [ ] Actual parameter values included (not placeholders)
- [ ] Key quotes captured
- [ ] video-tutorials.md updated
- [ ] node-parameters.md updated (if new nodes)
- [ ] ROADMAP.md status updated
- [ ] Tested with sample questions

## File Structure

```
skills/tutor/
├── SKILL.md                 ← Main tutor instructions
├── sources/                 ← Raw extracted material
│   ├── course-overview.md   ← All video URLs
│   └── transcripts/         ← Raw video transcripts
└── references/              ← Processed knowledge
    ├── video-tutorials.md   ← Video index
    ├── node-parameters.md   ← Parameter reference
    ├── troubleshooting.md   ← Problem/solution guide
    ├── project-analysis.md  ← Ornate_Fabric analysis
    └── parts/               ← Per-part documentation
        ├── TEMPLATE.md
        └── part-XX-*.md
```

## Style Guide

### Language
- Write for artists, not programmers
- Explain technical terms when first used
- Use visual analogies where helpful
- Keep explanations concise but complete

### Formatting
- Use tables for parameter values
- Use code blocks for node names
- Include timestamps in `MM:SS` format
- Bold key concepts and node names

### Example

**Good:**
> The **Fibers** node generates directional strand patterns. Set `Samples` to 256 for detail, `Distribution` to 0.5 for even spacing.

**Avoid:**
> Use the Fibers node and adjust the parameters until it looks right.

## Questions?

Open an issue or reach out if you have questions about contributing.

---

*See ROADMAP.md for the list of parts that still need documentation.*
