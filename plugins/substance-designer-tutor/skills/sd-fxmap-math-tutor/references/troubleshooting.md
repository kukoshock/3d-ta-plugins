# Troubleshooting — Math / FX-Map / Pixel Processor

> **Status:** stub. Populated by a follow-up increment as the technique references mature and known-failure modes accumulate.

## Planned categories

Anticipated trouble areas for math-driven SD work:

| Category | Symptom (artist perspective) | Likely cause | Why |
|----------|------------------------------|--------------|-----|
| Math expression syntax | "My expression won't compile" | Missing `;` between statements, undefined input pin, type mismatch | The Function Editor parses strictly; one missing semicolon stops the whole expression |
| FX-Map performance death spiral | "Substance Designer froze" | Iterate count too high, or recursion without a halting condition | Each iterate level multiplies cost geometrically |
| NaN / Inf propagation | "My output is solid black or solid white" | `sqrt(negative)`, `log(0)`, `1/0` somewhere upstream | Float math produces sentinel values that cascade through any subsequent math |
| Sampling artifacts at boundaries | "Hard line on the edge of my pattern" | Sampling outside [0,1] without `mod` or `frac` | Sampling functions clamp by default |
| Vector field discontinuities | "Visible seam in my procedural fabric" | Discontinuity in the field equation (e.g. `atan2` branch cut) | The field jumps in value where the math jumps; the texture follows |
| Wrong type in expression | "Result is constant when it shouldn't be" | Float used where Float2 expected (or vice versa) | Type coercion silently broadcasts a scalar; the per-pixel variation collapses |

## Format (when populated)

Each entry will follow the project's tutor convention: **Symptom → Cause → Fix → WHY this works.** The "WHY" is mandatory — it is what makes troubleshooting teaching, not just lookup.

## Citation format reminder

Each entry populated from an Andrei video must end with `*Source: Andrei Zelenco — <video title or article> — <URL>*`. Generic SD failure modes (e.g. type coercion) need no citation.
