# Video Index — Andrei Zelenco

Map of Andrei's videos that have been pulled into `../sources/transcripts/` and the references they feed.

| Video Title | YouTube URL | Transcript file | Topic | Used by reference |
|-------------|-------------|-----------------|-------|-------------------|
| Substance Designer basic to advanced FX map tutorial Part 1 | https://www.youtube.com/watch?v=_FGp6G9LEDM | `fx-map-01-basics.txt` | What FX-Map is, Quadrant model, scattering, pattern parameter routing, multi-input pattern selection | `fx-map-fundamentals.md` |
| Substance Designer basic to advanced FX map tutorial Part 2 | https://www.youtube.com/watch?v=qnnt9N5NSM8 | `fx-map-02-pattern-input.txt` | Iterate node, variables (Houdini-style `numpt` / `pity num` / `t0` naming), procedural workflow, nested loops | `fx-map-fundamentals.md`, `math-expressions.md` |
| Substance Designer Basic to Advanced FX map tutorial Part 3 | https://www.youtube.com/watch?v=nXFZ8nx9y8M | `fx-map-03-iterate-loops.txt` | Vector-field flow lines from height maps, contour-following streams, halting thresholds, portrait-as-streams effect | `fx-map-fundamentals.md`; planned: `procedural-cloth-vector-fields.md` |
| Substance Designer basic to advanced FX MAP part 4 | https://www.youtube.com/watch?v=FCrwogNp5rY | `fx-map-04-advanced.txt` | Point cloud generation, point-cloud-to-list conversion via Pixel Processor + Matrix, drawing connection graphs from list data, portrait-as-graph effect | `fx-map-fundamentals.md` |
| Substance Designer Loops with Pixel Processor, FX map and Instance graphs | https://www.youtube.com/watch?v=mNaoWTs3VT8 | `loops-pixel-processor-fx-map-instance.txt` | Three-way comparison of loop constructs (Pixel Processor while, FX-Map Iterate, instance graph chains); marble-in-bowl basin-of-attraction simulation | `pixel-processor-basics.md`; planned: deeper coverage in advanced refs |
| Working with data in Substance Designer | https://www.youtube.com/watch?v=0QLUkp5l_KQ | `working-with-data.txt` | Lists-of-data discipline (Houdini/Grasshopper analogue), Pixel Processor as data writer, scalar-list-to-vector-list composition, FX-Map reading lists via Iterate, branch-offset coordinate fix | `pixel-processor-basics.md`, `math-expressions.md` |

## Open transcript work

Andrei's broader channel (`@andreizelenco4164`) contains many shorter uploads on procedural cloth (`Cloth wrinkles in Substance Designer`), reaction-diffusion (`Custom reaction diffusion tutorial`), partial differential equations (`Advanced simulation tutorial`), and many one-minute demos illustrating individual concepts. These are pulled in their respective subsequent issues (`procedural-cloth-vector-fields.md`, `sine-patterns.md`, plus optional follow-ups for advanced simulation topics).

A short `Houdini concepts in Substance Designer` demo (`09Vn8xB3IoQ`, 1 min) was attempted for the math-expressions reference but had no auto-captions available. Pull manually if and when transcribable.

## Why this index exists

Three audiences:

1. **The skill at runtime** — when answering a question, the skill checks this index to decide which transcript to read for source-grounded detail.
2. **Skill authors** — when adding a new reference file, this index is the canonical map of which transcripts cover which topics, avoiding redundant re-watches.
3. **Users who want to learn from the original** — citation lines in references include the URL from this index, so a user's next click takes them to Andrei's video, not a paraphrase.

## Transcript provenance

Transcripts are YouTube auto-generated English captions, downloaded with `yt-dlp` and cleaned with `scripts/vtt_to_text.py` (deduplication, timestamp / inline-tag stripping). Auto-captions occasionally mistranscribe technical terms and proper names (e.g. "Andre" for "Andrei", garbled names of credited artists in Part 1's acknowledgments). Where this matters for content, the references flag the issue rather than propagating the garbled text.

## Channel root

https://www.youtube.com/@andreizelenco4164
