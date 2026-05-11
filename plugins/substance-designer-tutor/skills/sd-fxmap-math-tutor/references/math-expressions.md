# Math Expressions

> **Status:** stub. Populated by a follow-up increment.

## Planned coverage

- The expression language used in Substance Designer's Function Editor (FX-Map and Pixel Processor share it)
- Types: Float, Float2/3/4, Integer, Boolean
- Common operators and built-ins: `sin`, `cos`, `dot`, `length`, `normalize`, `lerp`, `step`, `smoothstep`, `mod`, `floor`, `frac`
- Conditionals (`if`) and how they compile to per-pixel branching
- Iteration constructs (`while`) and their cost
- Common pitfalls: missing `;`, undefined inputs, integer-vs-float coercions, NaN/Inf propagation
- Reading a math expression: how to "narrate" what each line computes

## Primary sources (to be ingested)

- Andrei's math-expression tutorials and FX-Map series segments where math is shown explicitly
- Adobe's official Function Editor documentation (linked, not redistributed) for syntax canon

## Citation format reminder

Every paragraph populated here must end with `*Source: Andrei Zelenco — <video title or article> — <URL>*`. Citations to Adobe documentation use `*Source: Adobe Substance 3D — <doc title> — <URL>*`.
