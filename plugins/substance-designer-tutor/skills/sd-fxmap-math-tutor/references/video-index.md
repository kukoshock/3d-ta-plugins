# Video Index — Andrei Zelenco

Map of Andrei's videos that have been pulled into `../sources/transcripts/` and the references they feed.

| Video Title | YouTube URL | Transcript file | Topic | Used by reference |
|-------------|-------------|-----------------|-------|-------------------|
| Substance Designer basic to advanced FX map tutorial Part 1 | https://www.youtube.com/watch?v=_FGp6G9LEDM | `fx-map-01-basics.txt` | What FX-Map is, Quadrant model, scattering, pattern parameter routing, multi-input pattern selection | `fx-map-fundamentals.md` |
| Substance Designer basic to advanced FX map tutorial Part 2 | https://www.youtube.com/watch?v=qnnt9N5NSM8 | `fx-map-02-pattern-input.txt` | Iterate node, variables (Houdini-style `numpt` / `pity num` / `t0` naming), procedural workflow, nested loops | `fx-map-fundamentals.md`; planned: `math-expressions.md` |
| Substance Designer Basic to Advanced FX map tutorial Part 3 | https://www.youtube.com/watch?v=nXFZ8nx9y8M | `fx-map-03-iterate-loops.txt` | Vector-field flow lines from height maps, contour-following streams, halting thresholds, portrait-as-streams effect | `fx-map-fundamentals.md`; planned: `procedural-cloth-vector-fields.md` |

## Open transcript work

A fourth FX-Map video is referenced in 80.lv's announcement of the series ("the four videos") but its URL has not been confirmed. When it is located it will be pulled, cleaned, and added here as `fx-map-04-*.txt`.

Andrei's broader channel (`@andreizelenco4164`) contains many shorter uploads on Pixel Processor, math expressions, vector field cloth, sine patterns, and reaction-diffusion. These are pulled in their respective subsequent issues (`pixel-processor-basics.md`, `math-expressions.md`, `procedural-cloth-vector-fields.md`, `sine-patterns.md`).

## Why this index exists

Three audiences:

1. **The skill at runtime** — when answering a question, the skill checks this index to decide which transcript to read for source-grounded detail.
2. **Skill authors** — when adding a new reference file, this index is the canonical map of which transcripts cover which topics, avoiding redundant re-watches.
3. **Users who want to learn from the original** — citation lines in references include the URL from this index, so a user's next click takes them to Andrei's video, not a paraphrase.

## Transcript provenance

Transcripts are YouTube auto-generated English captions, downloaded with `yt-dlp` and cleaned with `scripts/vtt_to_text.py` (deduplication, timestamp / inline-tag stripping). Auto-captions occasionally mistranscribe technical terms and proper names (e.g. "Andre" for "Andrei", garbled names of credited artists in Part 1's acknowledgments). Where this matters for content, the references flag the issue rather than propagating the garbled text.

## Channel root

https://www.youtube.com/@andreizelenco4164
