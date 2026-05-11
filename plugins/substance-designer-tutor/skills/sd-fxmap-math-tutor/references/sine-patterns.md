# Sine / Fourier Patterns

Periodic visual patterns from sums of sines. This reference draws on Andrei Zelenco's portfolio piece *"Making patterns with the sine function"* and on the math-expression language covered in `math-expressions.md`. Andrei does not have a dedicated multi-part video series on sine patterns specifically; the technique surfaces across many of his FX-Map and Pixel Processor demos, and most cleanly in his ArtStation breakdowns.

---

## The minimum mental model

Substance Designer evaluates math expressions per pixel (Pixel Processor) or per instance (FX-Map). `sin` and `cos` are first-class operators in that expression language. Once you accept that, every periodic pattern in image space is reachable as `sin(f * x + φ) * A`, where `f` is frequency (controls how many stripes), `φ` is phase (slides the pattern), and `A` is amplitude (controls contrast).

That single equation already covers stripes. Sums of those equations cover the rest.
*Source: Andrei Zelenco — Working with data in Substance Designer — https://www.youtube.com/watch?v=0QLUkp5l_KQ; channel demos at https://www.youtube.com/@andreizelenco4164*

## The three creative dials

For a single sine `sin(f * x + φ) * A`:

| Dial | What changes | Range to try |
|------|-------------|--------------|
| **Frequency `f`** | How many cycles fit across the image | 1 → 64+ |
| **Phase `φ`** | Where the pattern starts (slides it left/right) | 0 → 2π (or just expose as 0–1 and multiply by 2π inside) |
| **Amplitude `A`** | Peak-to-trough height of the wave | 0 → 1 (clamp at the end) |

A common ergonomic move: expose `frequency` and `phase` as named variables (per the `math-expressions.md` discipline) so you can tweak them at the FX-Map / Pixel Processor input level rather than inside expressions. This matches Andrei's broader pattern of separating data generation from drawing.

## 2D sine fields: separable vs coupled

The interesting structure in 2D comes from how you combine sines on each axis:

- **Separable** — `sin(fx * x) * sin(fy * y)` produces a checker-like grid of bumps. Each axis is independent. Good for plaid, lattice, regular dot patterns.
- **Coupled** — `sin(fx * x + sin(fy * y) * coupling)` produces wavy stripes that *bend* in response to the other axis. Good for organic patterns, herringbone, water surfaces. The `coupling` constant controls how much one axis distorts the other.
- **Modulated** — `sin(fx * x) * (some_other_pattern)` uses one sine as a carrier and another pattern (sine or otherwise) as an envelope. Good for moiré and interference effects.

Each of the three has a different aesthetic and a different control surface. Knowing which to reach for is the only "art" in the otherwise mechanical formula. Andrei's ArtStation portfolio includes several pieces where coupled sine fields produce organic-looking textiles and surfaces — the breakdowns there are the cleanest existing demonstration of the technique applied.
*Source: Andrei Zelenco — ArtStation portfolio — https://www.artstation.com/andreizelenco*

## Sums of sines and the Fourier bridge

A core mathematical fact: any periodic 1D pattern can be approximated to arbitrary accuracy as a sum of sines with appropriately chosen frequencies, phases, and amplitudes. This is Fourier's theorem. In practice, three or four well-chosen sine terms already produce extremely rich patterns — square waves from the first three odd harmonics, sawtooth from successive integer harmonics, etc.

For procedural texturing, you don't usually need theoretical Fourier rigor; you need *useful intuition*. Two terms with close frequencies produces beating; two terms with very different frequencies produces a low-frequency carrier with high-frequency detail; many random-frequency terms produces noise. Each effect is one-line of math expression.
*Source: Andrei Zelenco — Substance Designer basic to advanced FX map tutorial Part 2 — https://www.youtube.com/watch?v=qnnt9N5NSM8*

## A note on this reference's sourcing

Andrei does not have a multi-part dedicated video series on sine patterns, the way he does for FX-Map. The technique appears across his work as a building block rather than as a standalone topic — sine fields inside FX-Map graphs, sine-driven Pixel Processor expressions, sine-modulated vector fields for cloth. This reference therefore synthesizes the math (which is general — sine has been math since Pythagoras) with pointers to where Andrei *uses* sine patterns in his work, rather than paraphrasing a single canonical source. If you want a dedicated sine-pattern walkthrough, his channel's shorter demos are the closest thing — search for pieces named after specific patterns (plaid, herringbone, moiré).
*Source: Andrei Zelenco — channel — https://www.youtube.com/@andreizelenco4164*

## Practical pattern recipes

A handful of common patterns and the sine-based recipe that makes each:

| Pattern | Recipe sketch |
|---------|---------------|
| Stripes | `sin(f * x)` — one axis only |
| Plaid | `sin(fx * x) + sin(fy * y)` — sum, not product |
| Dots / lattice | `sin(fx * x) * sin(fy * y)`, then thresholded |
| Herringbone | `sin(f * (x + sin(g * y)))` — one axis modulated by the other |
| Wavy stripes | `sin(f * x + amplitude * sin(g * y))` |
| Moiré | `sin(f1 * x) + sin(f2 * x)` with `f1` and `f2` close together |

These are starting points, not finished textures. The interesting variation comes from: thresholding the sine output to get hard edges; remapping the sine output through a Levels-like curve for smooth-to-hard transitions; using one sine pattern as a mask for a second, totally different pattern.

## Where to go next

- `math-expressions.md` for the language used to write the recipes above (operators, types, naming).
- `procedural-cloth-vector-fields.md` for one major application — sine-modulated vector fields produce regular-weave fabrics.
- **Andrei's ArtStation portfolio** (https://www.artstation.com/andreizelenco) — search for "sine" or "pattern" in his pieces; the descriptions often include the specific math used.
- **Andrei's channel** (https://www.youtube.com/@andreizelenco4164) — many short demos illustrate sine-driven effects in passing.

## See also in this skill

- `fx-map-fundamentals.md` — sine patterns as inputs to FX-Map (drive scale, rotation, color of scattered shapes via a sine-based parameter)
- `pixel-processor-basics.md` — sine as a per-pixel computation (the most direct way to render a sine-pattern image without involving instances at all)
