# Procedural Cloth via Vector Fields

This reference is the **math route to fabric**. Where the sibling `Substance Designer Tutor` skill teaches fabric via project-anchored Tile-Sampler workflows (the Ornamental_Fabric pipeline), this reference covers Andrei Zelenco's approach: build the fabric directly from a vector field that math defines per pixel. Both routes solve fabric. Their trade-offs are different, and one user can want one or the other depending on the project.

---

## What a vector field is, in fabric terms

A vector field is "an arrow at every pixel" — a `Float2` value (direction + magnitude, or `(dx, dy)`) defined as a function of position. For fabric, the arrows encode the local **warp + weft directions** of the weave. A constant vector field is a perfectly straight grid; a vector field with curl is a fabric draped over an invisible curvature; a vector field with discontinuities is a tear or a seam.

The single most important consequence: once you have the vector field, the actual *appearance* of the fabric (thread thickness, twist, color, sheen) is downstream — the field is the geometry, the appearance is shading. This separates the structural problem from the look-development problem, which is the math approach's main pedagogical advantage over the recipe approach.
*Source: Andrei Zelenco — Substance Designer Basic to Advanced FX map tutorial Part 3 — https://www.youtube.com/watch?v=nXFZ8nx9y8M*

## How Andrei builds the field

Part 3 of the FX-Map series is the canonical demonstration: start from any input height map, take its **normal map** as the vector field, and at each starting position iterate L steps where each step nudges the current position by the local field vector. Draw a small disc at every step and you have a stream traced along the field. Rotate the step vector by 90° and you have a stream tracing **contour lines** of the field instead of falling lines — same algorithm, perpendicular result.

For fabric, the contour-line variant is the warp; rotated 90° again you get the weft; cross them and you have the weave. The field can come from any source — a hand-painted height map for a specific weave, a Perlin noise for organic distortion, a parametric equation for a regular grid.
*Source: Andrei Zelenco — Substance Designer Basic to Advanced FX map tutorial Part 3 — https://www.youtube.com/watch?v=nXFZ8nx9y8M*

## When the math route beats the recipe route

The math approach earns its keep when:

- **The weave is non-rectangular** (radial, concentric, organic) — recipes assume a rectangular Tile Sampler grid; math doesn't.
- **You want continuous control over warp/weft direction** — varying the vector field smoothly across the texture is trivial in math; reproducing it as Tile Sampler parameters is fiddly.
- **You want emergent distortion** — a noise-modulated field produces fabric that looks draped or stretched without manually placing every tile.
- **The fabric needs to respond to geometry** (e.g. wraps a shape) — feed the shape's normal map in as the field input.

In production texturing for a single defined material with predictable parameters, the recipe route from the sibling tutor is faster. Don't reach for math when a Tile Sampler chain already does the job.
*Source: Andrei Zelenco — Substance Designer Basic to Advanced FX map tutorial Part 3 — https://www.youtube.com/watch?v=nXFZ8nx9y8M*

## Cross-reference: the sibling tutor's fabric pipeline

For the project-anchored, recipe-driven fabric pipeline (Tile Sampler + Height Blend + the 14-stage Ornamental_Fabric workflow), see the **`Substance Designer Tutor`** skill. Its `references/workflows.md` covers thread → weave → ornament → embroidery as a single composed material. It is the right starting point if you have a specific fabric to make and want to ship it; this skill's vector-field route is the right starting point if you are designing a *new kind* of fabric or want continuous parametric control over the weave.

A user asking "I want to make fabric in Substance Designer" should be offered both routes and helped to pick. A user asking "explain the math behind procedural cloth" goes here.

## Field discontinuities and how to avoid seams

A common failure mode: visible seams in the procedural fabric. Almost always traceable to a **discontinuity in the field equation**. The classic culprit is `atan2(y, x)`, which has a branch cut from −π to +π — the field jumps suddenly across that line, and the streams traced through it inherit the jump. Fixes:

- Use `mod` or `frac` to wrap field values into a continuous range when the underlying quantity is naturally periodic.
- For atan2-style angular fields, work in `(cos θ, sin θ)` representation instead of `θ` directly — sin and cos are continuous everywhere.
- For sampled fields, ensure the input image's tiling is compatible with the field's expected periodicity.

When a seam is unavoidable (e.g. a deliberate seam in the fabric design), put it where the visual story justifies it.
*Source: Andrei Zelenco — Substance Designer Basic to Advanced FX map tutorial Part 3 — https://www.youtube.com/watch?v=nXFZ8nx9y8M*

## Where Andrei goes deeper

- **`Cloth wrinkles in Substance Designer`** (https://www.youtube.com/watch?v=JGBh3CCRZ4g) — a 1-minute portfolio demo of the technique. Visual reference; no captions available, watch the video itself.
- **Andrei's ArtStation reference piece** (https://www.artstation.com/artwork/1Nrr6K) — the canonical fabric-from-math portfolio piece, with parameter breakdowns in the description.
- **Andrei's ArtStation portfolio** (https://www.artstation.com/andreizelenco) — additional fabric and textile pieces; each has a description that often includes the technique snapshot.

When pulling deeper content from these later, prefer specific ArtStation breakdowns over the channel's short demos, since the breakdowns include parameter values and Andrei's commentary.

## See also in this skill

- `fx-map-fundamentals.md` — Part 3 vector-field flow lines is the underlying mechanic
- `pixel-processor-basics.md` — alternative implementation route (per-pixel sampling of the field directly, without FX-Map's per-instance Iterate)
- `math-expressions.md` — the sine, cosine, dot, length operations the field equation uses
- `sine-patterns.md` — periodic patterns from sums of sines, often used as the field source for regular-weave fabrics
