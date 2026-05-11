# Math Expressions

Knowledge in this reference is paraphrased from Andrei Zelenco's free YouTube tutorials. The expression language used in Substance Designer's Function Editor is shared between FX-Map (per-instance) and Pixel Processor (per-pixel) — same syntax, different iteration model.

---

## The two-word summary

The Function Editor's expression language is **a tiny dataflow program**: each node is a typed value, you wire nodes together to compute new values, and one node is marked as the output. Read a graph as `output = expression(inputs)`, where the expression is the topology of nodes from inputs to output.

Andrei's discipline: name every meaningful intermediate value with a Set node, then `Get` it where needed. The graph stops being a wiring puzzle and starts being readable as code.
*Source: Andrei Zelenco — Substance Designer basic to advanced FX map tutorial Part 2 — https://www.youtube.com/watch?v=qnnt9N5NSM8*

## Types

Everything has a type, and types do not silently coerce. The five types you spend the most time with:

- `Float1` — single scalar
- `Float2` — pair (most common: a UV or `(x, y)`)
- `Float3` — triple (positions, RGB)
- `Float4` — quadruple (RGBA, homogeneous coords)
- `Integer` — used for iteration counts, indices, type-strict where the API demands it

Pixel Processor outputs are restricted to `Float1` or `Float4` — `Float2` and `Float3` cannot be set as output (compose into a `Float4`). The Function Editor surfaces the expected output type at the top of the canvas; if the right-click "Set as Output" item is greyed out, your terminal expression's type doesn't match.
*Source: Andrei Zelenco — Working with data in Substance Designer — https://www.youtube.com/watch?v=0QLUkp5l_KQ*

## Variables and scope

Variables are created with `Set` nodes and consumed with `Get` nodes. A `Set` writes a name; a downstream `Get` of the same name reads it. Scope is the enclosing function — variables do not leak between Pixel Processors or between separately-edited FX-Maps.

Andrei's naming convention, borrowed directly from Houdini's SOP context:

- `numpt0` — number of points / iterations at the outer loop level (Houdini's `npt`)
- `pity num0` — current point/iteration index (0 to numpt0−1) (Houdini's `ptnum`)
- `t0` — normalized parameter, computed as `pity num0 / numpt0`, sweeping 0 → 1 across the loop
- The trailing `0` is the loop level. Use `1` for the inner loop in nested constructs (`numpt1`, `pity num1`, `t1`).

The naming is not magic — Andrei explicitly says "feel free to use whatever names you want." The *discipline* is: every conceptual quantity gets a named variable, and every nested level gets a level-tagged variant. Without it, two-deep loops become unreadable.
*Source: Andrei Zelenco — Substance Designer basic to advanced FX map tutorial Part 2 — https://www.youtube.com/watch?v=qnnt9N5NSM8*

## The built-in iteration variable

Inside an FX-Map's Iterate context, `$number` is automatically populated with the current iteration index (an Integer, 0 to N−1). It is the analogue of `i` in `for (int i = 0; i < N; i++)`. The first thing most Iterate-driven graphs do is divide `$number` by the iteration count to get a `Float1` parameter that sweeps 0 → 1 — Andrei stores this as the variable `t0` and reaches for it constantly.
*Source: Andrei Zelenco — Working with data in Substance Designer — https://www.youtube.com/watch?v=0QLUkp5l_KQ*

A typical opening sequence inside a Quadrant's parameter expression:

1. `Get` the integer `numpt0` (set elsewhere as the Iterate count).
2. Get `$number` (current index).
3. Divide → `t0` as `Float1` in [0, 1).
4. Set `t0` so other expressions can read it.
5. Use `t0` to index into an input image, drive a position, parametrize a shape, etc.

This pattern shows up in essentially every Iterate-driven FX-Map Andrei builds.
*Source: Andrei Zelenco — Substance Designer basic to advanced FX map tutorial Part 2 — https://www.youtube.com/watch?v=qnnt9N5NSM8*

## Reading values from images

`Sample Color` and `Sample Gray` nodes read from an input image at a `Float2` UV coordinate. They are how a math expression accesses external data — the input is "an image's worth of values addressable as a function `f(uv)`."

A common pattern: build a UV from `(t0, 0)` and sample a 256×1 image to read entry `t0` of a precomputed list. The image is a list, the UV is the index, the sampler is the lookup. This is the bridge between FX-Map's Iterate and Pixel Processor's data-writing role described in `pixel-processor-basics.md`.
*Source: Andrei Zelenco — Working with data in Substance Designer — https://www.youtube.com/watch?v=0QLUkp5l_KQ*

## The "Substance Designer is a parametric tool" framing

The mental model Andrei keeps returning to: Substance Designer is closer to Houdini and Grasshopper than to Photoshop. Lists of data with attributes (position, velocity, scale, color) are first-class; what looks like an image is sometimes literally a list of values laid out spatially; what looks like a graph of nodes is a small program. Once you accept that framing, the Function Editor stops feeling like a constraint and starts feeling like the language the rest of the tool is *also* speaking, just less explicitly.
*Source: Andrei Zelenco — Working with data in Substance Designer — https://www.youtube.com/watch?v=0QLUkp5l_KQ*

## Common pitfalls

| Symptom | Cause | Fix |
|---------|-------|-----|
| "Set as Output" is greyed out | Terminal expression's type doesn't match the channel's expected output type | Compose into the expected type (most often: `Float2` → wrap in `Float4` with zeros for unused components) |
| Output is constant when it should vary per pixel/instance | A scalar is being used where a per-pixel value is expected (broadcast collapses variation) | Trace back to where the per-pixel input enters the expression — likely an unused `$pos` or `$number` |
| Tile-by-tile seam in FX-Map output | FX-Map considers `(0, 0)` to be the *center* of its space, not a corner. Branch offset of `-0.5, -0.5, -0.5` recenters | Set the Branch offset on the relevant Quadrant |
| `$number` is zero on every iteration | Iterate node's Set Root flag is on the wrong node, so the iteration context isn't the one being read | Verify which node is the FX-Map root; `$number` lives in the Iterate context |

*Source: Andrei Zelenco — Working with data in Substance Designer — https://www.youtube.com/watch?v=0QLUkp5l_KQ; Substance Designer basic to advanced FX map tutorial Part 2 — https://www.youtube.com/watch?v=qnnt9N5NSM8*

## Where to go next

- `pixel-processor-basics.md` for how the per-pixel loop construct (`while` inside Pixel Processor) compares to Iterate.
- `fx-map-fundamentals.md` for how Iterate fits into FX-Map's Quadrant model.
- The "Working with data" transcript at `../sources/transcripts/working-with-data.txt` contains four worked data-list examples not summarized above — read it for additional worked patterns.
