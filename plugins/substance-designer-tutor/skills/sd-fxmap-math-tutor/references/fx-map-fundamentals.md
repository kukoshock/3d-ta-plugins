# FX-Map Fundamentals

Knowledge in this reference is paraphrased from Andrei Zelenco's free three-part FX-Map series on YouTube (`@andreizelenco4164`). Per-paragraph `*Source: ...*` citations point back to the specific video each idea comes from. Direct quotes are kept under fair-use length. To learn the full pedagogy, watch the original videos.

---

## What FX-Map actually is

The plain-English definition Andrei opens with: FX-Map is a node that takes one or more input patterns and *scatters* them into the 2D output space, while exposing controls over each pattern's **position, scale, rotation, and color/luminosity**. Multiple input patterns can be supplied and routed through grayscale masks or gradients so different regions of the output use different patterns. If you are familiar with Tile Sampler, the difference is that FX-Map lets you build the scattering rules yourself instead of picking from a fixed parameter set.
*Source: Andrei Zelenco — Substance Designer basic to advanced FX map tutorial Part 1 — https://www.youtube.com/watch?v=_FGp6G9LEDM*

Andrei recommends, before writing your own FX-Map graph, opening some of the existing Substance Designer nodes that are themselves built on FX-Map and reading their internals. That habit teaches you the idiom by example faster than any tutorial can.
*Source: Andrei Zelenco — Substance Designer basic to advanced FX map tutorial Part 1 — https://www.youtube.com/watch?v=_FGp6G9LEDM*

## The Quadrant model

You enter an FX-Map's interior with `Ctrl+E` while the FX-Map node is selected. Inside, the central building block is the **Quadrant** node: each Quadrant subdivides the current 2D space into four equal regions and instances whatever pattern is plugged into it once per region. Chain Quadrants together and the subdivision compounds — one Quadrant produces a 2×2 grid, two produces 4×4, three produces 8×8, and so on. The "root" flag on a Quadrant determines which subdivision level is the one actually rendered to the output.
*Source: Andrei Zelenco — Substance Designer basic to advanced FX map tutorial Part 1 — https://www.youtube.com/watch?v=_FGp6G9LEDM*

A practical wiring shortcut Andrei demonstrates: hold `Ctrl+Shift` and drag from one node to another to let Substance Designer auto-create all the connections between them. With several Quadrants in a chain this saves a noticeable amount of clicking once you have done it a few times.
*Source: Andrei Zelenco — Substance Designer basic to advanced FX map tutorial Part 1 — https://www.youtube.com/watch?v=_FGp6G9LEDM*

## Driving pattern parameters from input maps

Each Quadrant exposes parameters such as `pattern size`, pattern offset, rotation, and color. The interesting move is to *not* hard-code these values but to wire them to expressions that read from input images. Andrei walks through five specific examples in Part 1, each demonstrating one driver-to-parameter mapping:

- A Perlin-noise input wired to `pattern size` produces a grid where the pattern is small in the dark regions of the noise and large in the bright regions.
- A Normal map wired to position offset pushes each pattern around in the direction the normal map encodes — a vector field interpreted as displacement.
- A grayscale checker map wired to color makes each tile inherit its luminosity from the checker.
- A gradient wired to rotation makes each tile rotate by an amount proportional to the gradient's brightness.
- All four combined produce a single pattern that simultaneously moves, scales, recolors, and rotates according to the four input maps.

The mental model is consistent across all five: an input image becomes per-pattern data, and FX-Map applies that data point-by-point as it scatters.
*Source: Andrei Zelenco — Substance Designer basic to advanced FX map tutorial Part 1 — https://www.youtube.com/watch?v=_FGp6G9LEDM*

## Routing multiple patterns

FX-Map accepts multiple image inputs (image input 0, 1, 2, …) and lets you select between them per scattered instance using a mask or gradient. In Andrei's example, two shapes (a circle and a square) are routed through a brightness mask: bright pixels emit circles, dark pixels emit squares. A more advanced variant adds a per-shape predicate so that, say, only the squares respond to a movement parameter while the circles stay fixed. This is where FX-Map starts to feel less like a scatterer and more like a tiny program.
*Source: Andrei Zelenco — Substance Designer basic to advanced FX map tutorial Part 1 — https://www.youtube.com/watch?v=_FGp6G9LEDM*

## The Iterate node, variables, and procedural thinking

Part 2 is the leap from "use FX-Map" to "program FX-Map." The central new construct is the **Iterate** node, which runs its child subgraph N times and exposes the current iteration index as an integer to every expression downstream. Andrei pairs Iterate with variables so the same graph can be tuned by changing a single value rather than editing wires.

Andrei's naming convention is borrowed from Houdini: a `numpt` variable holds the iteration count (he uses `numpt0` for the outer loop's count, e.g. 1024), a `pity num` (Houdini's `ptnum` analogue) holds the current iteration index (0 to N−1), and a `t0` variable holds the normalized parameter `pity num / numpt0` (so it sweeps 0 → 1 across the loop). Once these are in place, expressions inside the loop read the current iteration's normalized position by name, not by hard-coded value.
*Source: Andrei Zelenco — Substance Designer basic to advanced FX map tutorial Part 2 — https://www.youtube.com/watch?v=qnnt9N5NSM8*

Andrei is explicit about the ramp on this part of the material: *"This really took me kind of like one year to figure out. So I've made around 50 or 60 examples and literally I just had to go through it and try to guess it and try to come up with a workflow that makes sense."* Translation for the user: if Iterate and variables feel disorienting, that is the normal first reaction. Re-watching the segment two or three times is part of the curriculum, not a sign you missed something.
*Source: Andrei Zelenco — Substance Designer basic to advanced FX map tutorial Part 2 — https://www.youtube.com/watch?v=qnnt9N5NSM8*

The naming convention itself is portable advice: the specific words `numpt` and `pity num` are not magic — Andrei suggests using whatever names you prefer — but the *discipline* of giving each conceptual quantity a named variable, and labelling the level you are at in nested loops (e.g. `t0` for the outer loop, `t1` for the inner), is what makes nested-loop graphs survive their own complexity.
*Source: Andrei Zelenco — Substance Designer basic to advanced FX map tutorial Part 2 — https://www.youtube.com/watch?v=qnnt9N5NSM8*

## Worked example: vector-field flow lines

Part 3 puts the Iterate node to work building something visually striking: starting from a grid of seed points, draw streams that flow along the contour lines of a height map. The wiring sketch:

1. Generate a grid of starting positions (X/Y density parametric).
2. At each starting position, run an Iterate of length L — each iteration steps the current position by a small vector read out of the input height map's normal-map representation.
3. Draw a small disc at each step position to make the trail visible.
4. Optionally rotate the step vector by 90° so streams follow contour lines instead of falling down them — same algorithm, different visual.
5. Use a brightness threshold to halt streams that wander into very dark regions of the height map.

The same algorithm with a black-and-white portrait as the input height map produces a portrait-as-streams effect — the same code, the same wiring, just a different input image. This is the practical payoff of the math/systems approach: one graph generalizes across many visual outcomes that would each be a separate recipe in a parameter-driven workflow.
*Source: Andrei Zelenco — Substance Designer Basic to Advanced FX map tutorial Part 3 — https://www.youtube.com/watch?v=nXFZ8nx9y8M*

## Where to go next

- Watch the three videos in order — there is no substitute for seeing Andrei build the graphs node by node.
- The Pixel Processor reference in this skill (`pixel-processor-basics.md`) covers the close cousin of FX-Map: same math-expression language, same per-pixel mindset, but no recursion / no Quadrant model.
- The Math Expressions reference (`math-expressions.md`) covers the expression syntax that makes everything in Part 2 and Part 3 possible.
- Andrei has at least one further FX-Map tutorial referenced in his channel uploads beyond Part 3; when that transcript is pulled, this reference will be extended with its content.

## Acknowledgments

Andrei opens Part 1 by thanking other Substance Designer artists who showed him FX-Map techniques. The acknowledgments themselves are slightly garbled in the auto-generated captions, but the named individuals include Marco Vital and another creator whose name the captions render as "Nicolola Wman" (likely a transcription error of a real artist's name — surface this when readable in higher-quality captions).
*Source: Andrei Zelenco — Substance Designer basic to advanced FX map tutorial Part 1 — https://www.youtube.com/watch?v=_FGp6G9LEDM*
