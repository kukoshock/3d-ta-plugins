# Node Parameters Reference

Comprehensive parameter reference for 45+ Substance Designer nodes, extracted from the Ornate_Fabric.sbs project and course materials.

---

## Distribution & Tiling Nodes

### Tile Sampler

The main distribution node for pattern creation. "A very important node" that takes an input shape and tiles it across the material.

| Parameter | Value | Purpose | WHY This Value |
|-----------|-------|---------|----------------|
| pattern | 1 | Pattern mode (square grid) | Square grid provides even distribution for fabric embroidery |
| x_amount | **600** | Horizontal tile count | High density creates dense "weave" structure rather than scattered shapes |
| y_amount | **700** | Vertical tile count | Slightly more vertical than horizontal creates embroidery grain direction |
| scale | **3.8** | Base scale of each tile | Large enough for threads to overlap and form solid surface coverage |
| rotation | 0.25 | Base rotation (radians, ~90°) | Embroidery runs vertically, contrasting with horizontal weave direction |
| offset | 0.5 | Offset between rows | Breaks rigid grid pattern for natural woven look instead of mechanical alignment |
| color_random | 0.29 | Color variation per instance | Moderate variation creates realistic thread color inconsistency |
| rotation_random | **0.02** | Subtle rotation variation | Small value prevents chaotic look while adding organic imperfection |
| scale_random | **0.19** | Moderate size variation | Enough variation to look hand-made without losing uniformity |
| position_random | **0.01** | Very subtle position jitter | Minimal offset maintains pattern while breaking perfect grid |

**Input Slots:**
- **Pattern Input**: The shape to tile (reuses thread shape for fabric consistency)
- **Scale Map**: Connect Perlin Noise for dynamic sizing (creates organic size variation across surface)
- **Position Map**: Drive position with grayscale map (controls where tiles appear)
- **Rotation Map**: Drive rotation with grayscale map (directional control of tile orientation)

> **CRITICAL TECHNIQUE - Scale Map vs Mask Input:**
> Connecting the ornament mask to **Scale Map** (not Mask Input) creates tapered transitions. Scale Map shrinks threads to zero where the mask is black, making threads "dive into" the fabric with realistic tapers. Mask Input would create harsh "cookie-cutter" cutout edges.

**Pattern Modes Reference:**
| Value | Pattern Type |
|-------|--------------|
| 0 | No pattern |
| 1 | Square |
| 2 | Brick |
| 3 | Hexagonal |
| 4-14 | Various specialized patterns |

---

### Tile Generator

Creates grid patterns for warp/weft threads and basic tiling.

| Parameter | Warp Value | Weft Value | Purpose |
|-----------|------------|------------|---------|
| Pattern | Horizontal | Vertical | Thread direction |
| Size X | 1.0 | 0.1 | Thread width |
| Size Y | 0.1 | 1.0 | Thread height |
| Position | Varies | Varies | Interlocking offset |
| Non Square Expansion | On | On | Proper aspect handling |
| Pattern Input Number | 1-4 | 1-4 | Number of input patterns |
| Pattern Distribution | Random / By Pattern Number | - | How patterns alternate |

---

### Tile Generator Color

Grayscale Tile Generator with color randomization capabilities.

| Parameter | Typical Value | Purpose |
|-----------|---------------|---------|
| Amount | 200 | Number of elements |
| Scale | Varies | Size of elements |
| Hue Random | 1.0 | Randomize hue |
| Saturation Random | 0-1 | Randomize saturation |
| Main Color | Pick | Base color |

---

### Splatter Circular

Distributes inputs in circular/radial patterns.

| Parameter | Typical Value | Purpose |
|-----------|---------------|---------|
| Amount | 5-10 | Number of elements |
| Radius | 0.1-0.5 | Distance from center |
| Ring Amount | 1-5 | Number of concentric rings |
| Spread | 0.5 | Portion of circle (1 = full, 0.5 = half) |
| Size | 1-5 | Scale of each element |
| Size Non-Uniform | 0.15 | Stretch in one direction |
| Pattern Rotation | Varies | Rotate individual elements |
| Ring Rotation | 0-360 | Rotate entire arrangement |
| Global Offset | X, Y | Position offset |

---

## Shape Creation Nodes

### Shape

Creates basic primitive shapes.

| Shape Type | Use Case |
|------------|----------|
| Disc | Sequins, round elements |
| Square | Diamonds (rotated), tiles |
| Bell | Soft gradients, sphere look |
| Paraboloid | Dome shapes |
| Gaussian | Soft falloff |

---

### Polygon

Creates customizable polygon shapes.

| Parameter | Typical Value | Purpose |
|-----------|---------------|---------|
| Sides | 3-8 | Number of polygon sides |
| Rotation | 0-360 | Rotate polygon |
| Gradient | 0-1 | Slope/bevel on edges |
| Width | 0.5 | Polygon size |

**Common Presets:**
- 3 sides = Triangle
- 4 sides = Diamond (rotated 45°)
- 6 sides = Hexagon

---

### Pyramid

Pre-beveled square shape, useful for gemstones.

| Parameter | Purpose |
|-----------|---------|
| Base Shape | Built-in square base |
| Flatten with Levels | Crush whites to create flat-top gem |

---

### Spline (Poly Quadratic)

Creates curves with control points.

| Parameter | Purpose |
|-----------|---------|
| Points Coordinates | Array of (x, y) control points |
| Segment Amount | Curve smoothness (8-32 typical) |
| Show Direction Helper | Visual aid (design time only) |
| Show Tangents | Visual aid (design time only) |
| Thickness | Line width |

**Example Control Points for Simple Curve:**
```
p0: (0.0, 0.5)   - Start point
p1: (0.5, 0.0)   - Control point (pulls curve)
p2: (1.0, 0.5)   - End point
```

---

### Shape Mapper

Bends/distorts input into circular arrangement.

| Parameter | Typical Value | Purpose |
|-----------|---------------|---------|
| Amount | 1 | Single circular bend (for loops) |
| Amount | 5+ | Multiple circular repetitions |
| Radius | 0.3-0.5 | Circle size |

---

## Transformation Nodes

### Transform 2D

Standard transformation with tiling-safe options.

| Parameter | Purpose |
|-----------|---------|
| X/Y Offset | Position adjustment |
| X/Y Scale | Size adjustment |
| Rotation | Angle adjustment |
| 90° Button | Quick 90-degree rotation |
| Horizontal Mirror | Flip horizontally |
| Power-of-2 Buttons | Divide by 2 repeatedly for quick tiling |

**Pro Tip:** Hold **Ctrl** to resize from center. Hold **Shift** for finer control.

**Tiling Trick:**
1. Offset by 0.5 on one axis
2. Blend with non-offset version using Max mode
3. Creates continuous line from repeated element

---

### Safe Transform 2D

Same as Transform 2D but prevents tiling seams.

| Parameter | Purpose |
|-----------|---------|
| Rotation | Safe rotation preserving tiles |
| Use only for | Elements that must tile perfectly |

---

## Blending & Combination Nodes

### Blend

Combines two inputs with various modes.

| Parameter | Common Values | Purpose |
|-----------|---------------|---------|
| Opacity | 0.0-1.0 | Layer visibility |
| Blending Mode | See below | Combination method |
| Use Source Alpha | On/Off | Alpha channel handling |
| Mask Input | Grayscale | Control blend distribution |

**Blending Modes Quick Reference:**
| Mode | Effect | Use Case |
|------|--------|----------|
| Normal | Standard overlay | General compositing |
| Multiply | Darkens | Shadows, cavities |
| Add | Brightens | Highlights, glow |
| Max | Takes lighter value | Combining heights |
| Min | Takes darker value | Masking |
| Subtract | Removes foreground | Creating borders |
| Overlay | Contrast enhancement | Detail enhancement |
| Soft Light | Subtle overlay | Color variations |

**Important:** Primary input is **background** - determines inheritance.

---

### Height Blend

Intelligent height-based blending that combines layers realistically based on their height values.

| Parameter | Value | Purpose | WHY This Value |
|-----------|-------|---------|----------------|
| Contrast | **0.96** | Edge sharpness (0.9-1.0 = crisp) | Near-maximum value creates crisp ornament edges that "sit on top" of fabric instead of blending into mush |
| Offset | 0.5 | Foreground height offset | Controls how much ornament "sinks into" vs "rises above" the fabric base |

**Contrast Values Effect:**
| Range | Effect | Use Case | WHY Choose This |
|-------|--------|----------|-----------------|
| 0.0-0.3 | Very soft, gradual blending | Subtle overlays, organic merges | Simulates gradual material transitions like melting wax |
| 0.3-0.6 | Moderate blending | Weathered surfaces, worn edges | Mimics erosion and natural wear patterns |
| 0.6-0.9 | Sharp but smooth edges | Most fabric details, general use | Balanced realism without harsh artifacts |
| **0.9-1.0** | Very crisp ornament edges | Embroidery, applied trim, sequins | Ornaments are physically ON TOP of fabric, not blended into it - creates clear separation like real sewn-on elements |

**Key Feature:** Has **Mask Output** - perfect for extracting ornament area later for color/roughness masks.

> **WHY Use Height Blend (Not Regular Blend):**
> Height Blend analyzes which layer is "higher" at each pixel and blends accordingly. This creates realistic overlaps where tall ornament threads naturally cover the lower fabric weave, just like physical embroidery. Regular Blend would create unrealistic transparency or flat overlays.

---

### Normal Combine

Merges multiple normal maps.

| Parameter | Purpose |
|-----------|---------|
| Input 1 | Base normal map |
| Input 2 | Detail normal map (folds, scratches) |
| Intensity | Relative strength |

---

## Noise & Texture Nodes

### Perlin Noise

Organic, cloud-like noise pattern.

| Parameter | Typical Range | Effect |
|-----------|---------------|--------|
| Scale | 1-20 | Feature size (lower = larger features) |
| Disorder | 0.0-1.0 | Randomness/chaos level |
| Non Square Expansion | On/Off | Proper aspect ratio handling |

**Ornate_Fabric Instances:**
| Instance | Scale | Disorder | Purpose |
|----------|-------|----------|---------|
| 1 | 5 | 0.31 | Fine detail variation |
| 2 | 6 | 0.45 | Medium detail |
| 3 | 19 | 0.35 | Large-scale variation |

---

### Directional Noise

Adds directional variation while maintaining structure - crucial for organic fabric appearance.

| Parameter | Value | Purpose | WHY This Value |
|-----------|-------|---------|----------------|
| Turns | **2-4** | Number of direction changes | 3 turns creates gentle wave pattern that mimics fabric tension variations without creating chaotic distortion. Too few (1) = boring straight lines, too many (> 5) = messy tangles. |
| Distance | **0.1-0.3** | Displacement amount | 0.15 provides subtle weave irregularity visible at close inspection but not overwhelming from normal viewing distance. Real fabric has micro-variations in thread paths from weaving tension. |
| Angle Random | 0.1-0.2 | Angular variation | Small angular changes prevent perfectly parallel threads (machine-like) while keeping overall weave direction coherent. |

> **WHY Directional Noise for Fabric:**
> Real woven fabric never has perfectly straight, uniform threads. Weaving tension, fiber elasticity, and settling create subtle directional variations. Directional Noise maintains the overall weave pattern (unlike random warp which destroys structure) while adding these micro-scale organic deviations that separate hand-crafted from CG-generated appearance.

---

### Directional Scratches

Creates directional scratch patterns.

| Parameter | Typical Value | Purpose |
|-----------|---------------|---------|
| Pattern Amount | 0.2 | Number of scratches (subtle = low) |
| Scale | 9 | Overall size |
| X Thickness | Varies | Horizontal stretch |
| Y Thickness | Varies | Vertical stretch |
| Angle | 0-360 | Scratch direction |

---

### Crease

Creates fold/wrinkle patterns.

| Parameter | Purpose |
|-----------|---------|
| Scale | Overall size of creases |
| Intensity | Depth of creases |
| Disorder | Randomness |

**Workflow:** Crease → Warp (with Perlin) → Blur → Normal

---

### Fibers

Generates directional strand patterns for thread, hair, scratches, and other linear details.

| Parameter | Typical Value | Purpose | WHY This Value |
|-----------|---------------|---------|----------------|
| Samples | 64-256 | Number of fiber strands | 128-256 provides enough strands for realistic density without excessive performance cost. Too few (< 64) looks sparse and artificial. |
| Distribution | 0.5 | Spread of fibers | 0.5 creates balanced coverage across the shape. Lower values cluster at center, higher spreads to edges. |
| Curve | 0.3-0.7 | Fiber curvature | Moderate curvature mimics natural fiber relaxation. 0 = straight (artificial), 1.0 = excessive loops. |
| Maximum Distance | 0.5-1.0 | Fiber length | Full length (1.0) ensures fibers span the entire thread cross-section for continuous coverage. |
| Spread Angle | **15-45°** | Angular spread (degrees) | 25° creates natural fiber divergence - not perfectly parallel (robotic) nor wildly scattered (chaotic). Real threads have slight directional variation. |

> **WHY 25° Spread Angle Specifically:**
> Real fabric threads aren't laser-straight. Individual fibers naturally diverge slightly due to spinning tension and material properties. 25° provides just enough variation to break perfect alignment while maintaining the thread's overall direction. Lower values (< 15°) look too uniform; higher values (> 45°) look messy and unspun.

---

## Distortion Nodes

### Warp

General-purpose distortion node.

| Parameter | Purpose |
|-----------|---------|
| Intensity Input | Grayscale map driving distortion |
| Intensity | Strength of effect |
| Non Square Expansion | Enable for non-square ratios |

---

### Directional Warp

Distorts in a specific direction.

| Parameter | Typical Value | Purpose |
|-----------|---------------|---------|
| Angle | 0 (horizontal) or 90 (vertical) | Warp direction |
| Intensity | 1-5 | Warp strength |
| Intensity Input | Directional Scratches | Drive warp pattern |

**Use Case:** Micro-distortions aligned with weave direction.

---

### Swirl

Creates swirling distortion.

| Parameter | Purpose |
|-----------|---------|
| Scale | Size of swirl |
| Amount | Strength of rotation |

---

### Mirror

Creates mirrored copies.

| Mode | Effect |
|------|--------|
| Horizontal | Left-right mirror |
| Vertical | Top-bottom mirror |
| Both | Quadrant mirror |

---

## Filter & Adjustment Nodes

### Levels

Adjusts contrast and brightness.

| Parameter | Recommended Range | Purpose |
|-----------|-------------------|---------|
| Input Low | 0.0 | Black point |
| Input High | 0.5-0.8 | Compress height range |
| Output Low | 0.0 | Output black |
| Output High | 0.3-0.5 | Flatten peak heights |
| Gamma | Middle slider | Mid-tone adjustment |

**Quick Actions (Tab Icons):**
- **Invert**: Swap black/white
- **Auto Level**: Automatic contrast

---

### Histogram Range

Easy contrast control with two sliders.

| Parameter | Purpose |
|-----------|---------|
| Range | Shrinks value distribution (contrast) |
| Position | Shifts overall darkness/brightness |

**Use Case:** Quick roughness adjustments, taming noisy inputs.

---

### Threshold

Creates binary black/white mask.

| Parameter | Purpose |
|-----------|---------|
| Threshold | Cutoff point (values above = white) |

**Use Case:** Extract silhouette from height, create mask from brightness differences.

---

### Invert

Inverts grayscale values (can also use Levels).

---

### Sharpen

Enhances edge contrast.

| Parameter | Typical Value | Purpose |
|-----------|---------------|---------|
| Intensity | 0.5-2.0 | Sharpening strength |

---

### High Pass Grayscale

Extracts fine details.

| Parameter | Purpose |
|-----------|---------|
| Radius | Size of detail to extract |

---

## Blur Nodes

### Blur HQ (High Quality)

Uniform blur across entire image.

| Parameter | Typical Value | Purpose |
|-----------|---------------|---------|
| Intensity | 0.1-1.0 | Blur strength |

**Use Cases:**
- Soften edges before blending
- Create soft masks
- Smooth displacement inputs (0.2)

---

### Non-Uniform Blur

Selective blur driven by intensity map.

| Parameter | Typical Value | Purpose |
|-----------|---------------|---------|
| Intensity | 25+ | Maximum blur amount |
| Samples | Max | Smoothness of transitions |
| Intensity Map | Grayscale mask | Where to blur |

**Use Case:** Blur folds away from trim area using trim mask.

---

### Radial Blur

Blur radiating from center.

---

## Edge & Detection Nodes

### Edge Detect

Finds edges in grayscale images.

| Parameter | Purpose |
|-----------|---------|
| Edge Width | Thickness of detected edge |
| Edge Roundness | Softness |
| Tolerance | Sensitivity |

**Important:** Use **Threshold** before Edge Detect to get clean silhouette outline only (removes internal gradients).

---

### Bevel

Adds beveled edges to shapes.

| Parameter | Typical Value | Purpose |
|-----------|---------------|---------|
| Distance | -2 to +2 | Bevel amount |
| Direction | Inward (-) / Outward (+) | Bevel direction |

**Inward (-2):** Creates pointy gemstone look.
**Outward (+):** Expands edges outward.

---

## Color Nodes

### Uniform Color

Single solid color.

| Parameter | Purpose |
|-----------|---------|
| Color Picker | Select RGB color |
| HSV Sliders | Hue, Saturation, Value |
| Hex Code | Precise color input |
| Eye Dropper | Sample from screen |

**Grayscale Mode:** Click grayscale button in Properties.

---

### Gradient Map

Converts grayscale to color.

| Feature | Purpose |
|---------|---------|
| Gradient Editor | Add/remove color keys |
| Screen Sampling | Drag across reference image to sample gradient |
| Precision | Control number of sampled colors |
| Interpolation | Linear, Constant, etc. |

**Workflow:**
1. Connect grayscale (curvature works great)
2. Open gradient editor
3. Sample from reference or manually set colors

---

### Gradient Axial

Creates linear gradient with position handles.

| Parameter | Purpose |
|-----------|---------|
| Handles | Drag to position gradient |
| Direction | Gradient angle |

**Use Case:** Sequin tilt effect, directional masks.

---

### HSL (Hue Saturation Lightness)

Adjusts color properties.

| Parameter | Purpose |
|-----------|---------|
| Hue | Shift color wheel position |
| Saturation | Color intensity |
| Lightness | Brightness |

---

### Color Match

Substitutes uniform colors throughout.

| Parameter | Purpose |
|-----------|---------|
| Source Color | Original color to match |
| Target Color | Replacement color |

**Use Case:** Expose fabric color when Gradient Map can't be exposed directly.

---

## Material Output Nodes

### Normal

Generates normal map from height.

| Parameter | Typical Value | Purpose |
|-----------|---------------|---------|
| Intensity | 2-6 | Normal map strength |

**Ray Tracing Note:** Reduce intensity (6 → 2) for ray-traced rendering.

---

### RT AO (Real-time Ambient Occlusion)

Generates AO from height.

| Parameter | Typical Value | Purpose |
|-----------|---------------|---------|
| Radius | 0.1-0.5 | AO spread distance |
| Intensity | 0.5-1.0 | Shadow darkness |
| Quality | Medium-High | Detail level |

---

### Curvature Smooth

Extracts curvature from normal map.

| Input | Purpose |
|-------|---------|
| Normal Map | Source normal information |

**Output:** Grayscale highlighting edges and cavities.

**Common Issue:** Vertical gradient artifact if upstream tiling is disabled. Fix: set Absolute full tiling.

---

### PBR Validate

Checks base color PBR compliance.

| Output Color | Meaning |
|--------------|---------|
| Green | Values within PBR range |
| Red | Values too dark or too bright |

---

### Base Material

All-in-one material preview node.

| Channel | Enable/Disable |
|---------|----------------|
| Base Color | True/False |
| Metallic | True/False (built-in slider when False) |
| Roughness | True/False (built-in slider when False) |
| Normal | True/False |
| Height | True/False (enables displacement) |
| AO | True/False |

**User-Defined Maps:** Enable custom inputs for each channel.

---

### Output

Creates custom output channel.

| Parameter | Purpose |
|-----------|---------|
| Identifier | Internal name |
| Label | User-facing name |
| Group | Category (Material) |
| Usage | Channel type (e.g., translucency) |

---

## Control & Logic Nodes

### Switch

Toggles between two inputs.

| Parameter | Purpose |
|-----------|---------|
| Input Selection | True/False (Boolean) |
| Input 1 | First option |
| Input 2 | Second option |

---

### Multi-Switch

Cycles through multiple inputs.

| Parameter | Purpose |
|-----------|---------|
| Input Selection | Integer selector |
| Input Count | Number of inputs |
| Type Editor | Slider or Dropdown |

**When Exposing:** Rename inputs for user-friendly dropdown.

---

### Input (Grayscale/Color)

Creates user-input slot for external content.

| Parameter | Purpose |
|-----------|---------|
| Identifier | Internal reference |
| Label | User-facing name |
| Description | Help text for users |

**Use Case:** Allow users to load custom ornament masks.

---

### Dot

Connection organization and portals.

| Feature | How to Use |
|---------|------------|
| Add Dot | Alt + click on connection |
| Move | Drag to reorganize |
| Group | Alt + click to group same-origin connections |
| Name | Set in Properties for portal reference |
| Portal | Reference named Dot from anywhere in graph |
| Remove | Backspace |

---

## Base Parameters (All Nodes)

These parameters exist on every node:

| Parameter | Inheritance Options | Purpose |
|-----------|---------------------|---------|
| Output Size | Relative to Input, Parent, Absolute | Resolution |
| Pixel Size | Relative to Input, Parent, Absolute | Pixel format |
| Tiling | Relative to Input, Parent, Absolute | Edge behavior |
| Bit Depth | Relative to Input, Parent, Absolute | Color precision |

**Inheritance Methods:**
- **Relative to Input:** Takes from primary input (dark dot)
- **Relative to Parent:** Takes from graph settings
- **Absolute:** Manual override

**Primary Input:** In Blend nodes, always the **background** connection.
