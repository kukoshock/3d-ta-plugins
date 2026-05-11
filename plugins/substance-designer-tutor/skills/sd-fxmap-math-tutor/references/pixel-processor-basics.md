# Pixel Processor Basics

Knowledge in this reference is paraphrased from Andrei Zelenco's free YouTube tutorials, primarily *"Substance Designer Loops with Pixel Processor, FX map and Instance graphs"* and *"Working with data in Substance Designer"*. Per-paragraph `*Source: ...*` citations point back to the specific videos.

---

## What Pixel Processor is, in one sentence

Pixel Processor is a node that runs a small math program **once per output pixel**, using values it samples from input images and the pixel's own coordinates. Where Tile Sampler and Splatter consume parameters, Pixel Processor consumes an *expression*. That makes it the right tool whenever the rule for what a pixel should be is shorter to write as math than to wire as a graph.
*Source: Andrei Zelenco — Working with data in Substance Designer — https://www.youtube.com/watch?v=0QLUkp5l_KQ*

## Three ways to loop in Substance Designer (Pixel Processor's place among them)

Andrei opens his loops tutorial by enumerating the three loop constructs available in Substance Designer:

1. **While loop node inside the Pixel Processor.** Per-pixel iteration with a halting condition — the most general construct, since the body of the loop is itself an expression.
2. **Iterate node inside the FX-Map.** Iteration over scattered instances rather than over pixels — covered in `fx-map-fundamentals.md`.
3. **Loops constructed outside both Pixel Processor and FX-Map**, by chaining a small subgraph back to itself with the right structure (Instance graphs, feedback chains).

The choice between Pixel Processor's while loop and FX-Map's Iterate is not "which is better"; it is "what is the loop iterating over?" If you are iterating over pixels (e.g. tracing a path step by step from each starting pixel), Pixel Processor wins. If you are iterating over instances of a shape being scattered, FX-Map wins.
*Source: Andrei Zelenco — Substance Designer Loops with Pixel Processor, FX map and Instance graphs — https://www.youtube.com/watch?v=mNaoWTs3VT8*

## The expression-as-output discipline

A non-obvious constraint Andrei surfaces in the data tutorial: a Pixel Processor's output expression must resolve to a `float1` (grayscale) or `float4` (color) — *not* `float2` or `float3`. If your computation naturally produces a 2-vector (e.g. a UV coordinate, a position offset), you cannot output it directly; you must compose it into a 4-vector first (e.g. `(x, y, 0, 1)`). The Function Editor enforces this with a type label at the top showing what the output channel expects.
*Source: Andrei Zelenco — Working with data in Substance Designer — https://www.youtube.com/watch?v=0QLUkp5l_KQ*

The right-click "Set as Output" menu item is greyed out for any node whose type does not match the channel's expected output. This is your first-line type checker — if the menu item is unavailable, the type is wrong, and the fix is upstream of where you tried to set the output.
*Source: Andrei Zelenco — Working with data in Substance Designer — https://www.youtube.com/watch?v=0QLUkp5l_KQ*

## Pixel Processor as a per-pixel data writer

A Pixel Processor's output image does not have to be a *picture*. Andrei demonstrates using a Pixel Processor to write **lists of data** that the FX-Map then reads back as input. The pattern:

1. Resize a small image (e.g. 256×1) so each "pixel" is one entry in a logical list.
2. Use a Pixel Processor to compute the value at each list slot from input images plus the slot index.
3. Pass the resulting image into an FX-Map, where Iterate reads each pixel one at a time and treats it as instance data (position, scale, color).

Two White Noise nodes resized to 256×1 with different seeds produce two scalar lists; combining them with a third Pixel Processor produces a list of `(x, y)` positions. That list is then a procedural point cloud the FX-Map can scatter from. This is the "lists with attributes" mental model from Houdini and Grasshopper, ported to Substance Designer.
*Source: Andrei Zelenco — Working with data in Substance Designer — https://www.youtube.com/watch?v=0QLUkp5l_KQ*

## Worked example: the marble-in-bowl simulation

The single most striking demonstration of what Pixel Processor enables, from the loops tutorial: imagine a bowl with three (or six) low-points. Drop a marble at some starting position, let physics decide which low-point it ends up in. The deterministic answer ("starting position X → final low-point Y") is itself a function — and it can be evaluated for *every* starting position in a 2K image in parallel, since each pixel's simulation is independent.

Wired up: each output pixel's expression is a while loop simulating the marble dropped at *that pixel's coordinates*, terminating when the marble has settled, returning the index of the low-point it settled into. Color each pixel by that index. The result is a fractal-looking partition of the image into "basins of attraction" — the same mathematical construct that produces classic chaos visualizations like Newton's-method fractals, generated by the same per-pixel parallelism.
*Source: Andrei Zelenco — Substance Designer Loops with Pixel Processor, FX map and Instance graphs — https://www.youtube.com/watch?v=mNaoWTs3VT8*

This is the pedagogical pattern of Andrei's whole approach in microcosm: the visual is striking, but the *idea* — "I can run an independent simulation per pixel and the GPU evaluates them all at once" — is what generalizes.
*Source: Andrei Zelenco — Substance Designer Loops with Pixel Processor, FX map and Instance graphs — https://www.youtube.com/watch?v=mNaoWTs3VT8*

## When to reach for Pixel Processor (vs. FX-Map vs. a node chain)

A pragmatic decision tree distilled from how Andrei uses each:

- **Reach for Pixel Processor** when the rule is naturally per-pixel and benefits from sampling neighbors or iterating until a condition is met (path tracing, simulation, custom blends, math-driven displacement).
- **Reach for FX-Map** when the rule is naturally per-instance (scattering, Quadrant subdivision, drawing N copies of a shape with per-instance variation).
- **Reach for a node chain** when the rule is a small composition of existing nodes (most production texture work). A custom expression is overkill for what a Levels + Blend can already do.

The three-way choice is independent of complexity — Pixel Processor is not "the advanced option," it is "the per-pixel option."
*Source: Andrei Zelenco — Substance Designer Loops with Pixel Processor, FX map and Instance graphs — https://www.youtube.com/watch?v=mNaoWTs3VT8*

## Where to go next

- `math-expressions.md` covers the expression language Pixel Processor (and FX-Map) share — types, operators, common functions, the `$number` / `$pos` style variables.
- `fx-map-fundamentals.md` covers the iteration construct in its instance-scattering home (FX-Map's Iterate node).
- The "Loops" video transcript at `../sources/transcripts/loops-pixel-processor-fx-map-instance.txt` contains additional worked examples (cone-gradient banding, Perlin contour-line stair-step, spiral construction outside both Pixel Processor and FX-Map) not covered above. Pull from it as the skill grows.
