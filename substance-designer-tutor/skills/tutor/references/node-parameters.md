# Node Parameters Reference

Actual parameter values extracted from the Ornate_Fabric.sbs project.

## Tile Sampler Configuration

The main Tile Sampler distributing ornaments uses these values:

| Parameter | Value | Purpose |
|-----------|-------|---------|
| pattern | 1 | Pattern mode (square grid) |
| x_amount | **600** | Horizontal tile count |
| y_amount | **700** | Vertical tile count |
| scale | **3.8** | Base scale of each tile |
| rotation | 0.25 | Base rotation (radians) |
| offset | 0.5 | Offset between rows |
| color_random | 0.29 | Color variation per instance |
| rotation_random | **0.02** | Subtle rotation variation |
| scale_random | **0.19** | Moderate size variation |
| position_random | **0.01** | Very subtle position jitter |

### Key Observations

1. **High Tile Count (600x700)**: Creates dense, fine embroidery pattern
2. **Subtle Randomization**: rotation_random=0.02 and position_random=0.01 keep pattern orderly
3. **Moderate Scale Variation**: scale_random=0.19 creates natural size variation without chaos
4. **Large Base Scale**: scale=3.8 makes each ornament clearly visible

### Pattern Modes Reference

| Value | Pattern Type |
|-------|--------------|
| 0 | No pattern |
| 1 | Square |
| 2 | Brick |
| 3 | Hexagonal |
| 4-14 | Various specialized patterns |

---

## Height Blend Configuration

| Parameter | Value | Purpose |
|-----------|-------|---------|
| contrast | **0.96** | High contrast for sharp blending |

### Effect of Contrast Values

| Range | Effect |
|-------|--------|
| 0.0-0.3 | Very soft, gradual blending |
| 0.3-0.6 | Moderate blending |
| 0.6-0.9 | Sharp but smooth edges |
| **0.9-1.0** | Very crisp ornament edges (used in project) |

---

## Perlin Noise Instances

Multiple Perlin Noise nodes with different scales:

| Instance | Scale | Disorder | Purpose |
|----------|-------|----------|---------|
| 1 | 5 | 0.31 | Fine detail variation |
| 2 | 6 | 0.45 | Medium detail |
| 3 | 19 | 0.35 | Large-scale variation |

### Perlin Noise Parameter Guidelines

| Parameter | Typical Range | Effect |
|-----------|---------------|--------|
| Scale | 1-20 | Feature size (lower = larger features) |
| Disorder | 0.0-1.0 | Randomness/chaos level |
| Non Square Expansion | On/Off | Proper aspect ratio handling |

---

## Levels Node (Pre-Height Blend)

Used to flatten ornament heights before blending:

| Parameter | Recommended Range | Purpose |
|-----------|-------------------|---------|
| Input Low | 0.0 | Black point |
| Input High | 0.5-0.8 | Compress height range |
| Output Low | 0.0 | Output black |
| Output High | 0.3-0.5 | Flatten peak heights |

**Purpose**: Creates "something a bit more flat" so ornaments don't protrude excessively.

---

## Fibers Node (Thread Creation)

| Parameter | Typical Value | Purpose |
|-----------|---------------|---------|
| Samples | 64-256 | Number of fiber strands |
| Distribution | 0.5 | Spread of fibers |
| Curve | 0.3-0.7 | Fiber curvature |
| Maximum Distance | 0.5-1.0 | Fiber length |
| Spread Angle | 15-45 | Angular spread (degrees) |

---

## Tile Generator (Weaving)

| Parameter | Warp Value | Weft Value | Purpose |
|-----------|------------|------------|---------|
| Pattern | Horizontal | Vertical | Thread direction |
| Size X | 1.0 | 0.1 | Thread width |
| Size Y | 0.1 | 1.0 | Thread height |
| Position | Varies | Varies | Interlocking offset |
| Non Square Expansion | On | On | Proper aspect handling |

---

## Directional Noise

| Parameter | Value | Purpose |
|-----------|-------|---------|
| Turns | 2-4 | Number of direction changes |
| Distance | 0.1-0.3 | Displacement amount |
| Angle Random | 0.1-0.2 | Angular variation |

---

## Spline (Poly Quadratic)

| Parameter | Purpose |
|-----------|---------|
| Points Coordinates | Array of (x, y) control points |
| Segment Amount | Curve smoothness (8-32 typical) |
| Show Direction Helper | Visual aid (design time only) |
| Show Tangents | Visual aid (design time only) |

### Example Control Points for Simple Curve
```
p0: (0.0, 0.5)   - Start point
p1: (0.5, 0.0)   - Control point (pulls curve)
p2: (1.0, 0.5)   - End point
```

---

## RT AO (Real-time Ambient Occlusion)

| Parameter | Typical Value | Purpose |
|-----------|---------------|---------|
| Radius | 0.1-0.5 | AO spread distance |
| Intensity | 0.5-1.0 | Shadow darkness |
| Quality | Medium-High | Detail level |

---

## Blend Node

| Parameter | Common Values | Purpose |
|-----------|---------------|---------|
| Opacity | 0.0-1.0 | Layer visibility |
| Blending Mode | Normal, Multiply, Add | Combination method |
| Use Source Alpha | On/Off | Alpha channel handling |

### Blending Modes Quick Reference

| Mode | Effect |
|------|--------|
| Normal | Standard overlay |
| Multiply | Darkens (good for shadows) |
| Add | Brightens (good for highlights) |
| Overlay | Contrast enhancement |
| Screen | Lighter multiply inverse |
