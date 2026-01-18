# Ornate_Fabric Project Analysis

Complete analysis of the Ornate_Fabric.sbs project file.

## Project Location

```
D:\Downloads\substance-designer-for-beginners\Ornate_Fabric\
```

## Node Dependencies

The project relies on these Substance Designer library nodes:

| Node | Library File | Purpose |
|------|--------------|---------|
| Tile Sampler | `pattern_tile_sampler.sbs` | Distribute ornaments |
| Tile Generator | `pattern_tile_generator.sbs` | Generate tile patterns |
| Height Blend | `height_blend.sbs` | Combine height layers |
| Perlin Noise | `noise_perlin_noise.sbs` | Randomization/variation |
| Fibers | `pattern_fibers_1.sbs` | Weave texture |
| PBR Base Material | `pbr_base_material.sbs` | Final material output |
| Histogram Scan | `histogram_scan.sbs` | Levels adjustment |
| Normal Combine | `normal_combine.sbs` | Normal map processing |
| Curvature Smooth | `curvature_smooth.sbs` | Surface detail |
| RT AO | `rt_ao_v2.sbs` | Ambient occlusion |

---

## User-Exposed Parameters

These parameters are exposed to end users of the material:

### Ornament Controls

| Parameter ID | Label | Type | Description |
|--------------|-------|------|-------------|
| input_selection | **Ornament type** | Integer (0-3) | Selects ornament preset |
| Custom_ornament | **Custom ornament** | Image Input | Custom mask (visible when type=3) |
| height_position | **Ornament emboss intensity** | Float | Controls ornament height prominence |

### Fabric Controls

| Parameter ID | Label | Type | Description |
|--------------|-------|------|-------------|
| target_color | **Fabric color** | Color | Main fabric base color |
| position | **Fabric roughness** | Float | Surface roughness value |
| intensity | **Folds intensity** | Float | Height of fabric folds |

### Detail Controls

| Parameter ID | Label | Type | Description |
|--------------|-------|------|-------------|
| switch | **Trim** | Boolean | Toggle trim details on/off |
| offset | **Gemstones position** | Float2 | 2D position offset of gemstones |
| outputcolor | **Gemstones color** | Color | Color of gemstone elements |
| outputcolor_1 | **Metal color** | Color | Color of metallic elements |

---

## Material Outputs

The final material generates these PBR maps:

| Output | Purpose |
|--------|---------|
| Base Color | Albedo/diffuse color map |
| Normal | Surface normal details |
| Roughness | Specular roughness |
| Metallic | Metal vs non-metal areas |
| Height | Displacement/parallax mapping |
| Ambient Occlusion | Soft shadows in crevices |
| Translucency | Light transmission through fabric |

---

## Graph Structure Overview

### Main Processing Stages

```
1. Thread Generation
   └── Shape → Fibers → Transform → Blend → Levels

2. Weave Pattern
   └── Tile Generator (Warp) ─┐
   └── Tile Generator (Weft) ─┴── Directional Noise → RT AO → Combine

3. Ornament Processing
   └── Ornament Input → Tile Sampler → Levels → Height Blend (with Weave)

4. Material Finalization
   └── Combined Height → Normal → Curvature → PBR Base Material
```

### Data Flow

```
[Ornament Mask] ──┬──────────────────────────────────────┐
                  │                                       │
                  ▼                                       │
           [Tile Sampler] ◄── [Perlin Noise (Scale)]    │
                  │                                       │
                  ▼                                       │
             [Levels]                                     │
                  │                                       │
                  ▼                                       │
           [Height Blend] ◄── [Base Weave Height]        │
                  │                                       │
                  ▼                                       │
            [Normal Map] ◄───────────────────────────────┘
                  │                        (for color)
                  ▼
         [PBR Base Material]
                  │
                  ▼
         [Material Outputs]
```

---

## Key Configuration Values

### Tile Sampler (Main Instance)

```
pattern = 1           (Square grid)
x_amount = 600        (Dense horizontal)
y_amount = 700        (Dense vertical)
scale = 3.8           (Large ornaments)
rotation = 0.25       (Slight angle)
offset = 0.5          (Row offset)
color_random = 0.29   (Color variation)
rotation_random = 0.02 (Subtle rotation)
scale_random = 0.19   (Moderate size var)
position_random = 0.01 (Minimal position)
```

### Height Blend

```
contrast = 0.96       (Very crisp edges)
```

### Perlin Noise Instances

```
Instance 1: scale=5, disorder=0.31  (Fine detail)
Instance 2: scale=6, disorder=0.45  (Medium detail)
Instance 3: scale=19, disorder=0.35 (Large features)
```

---

## Design Insights

### Why These Values Work

1. **High Tile Count (600x700)**
   - Creates dense, fine embroidery typical of ornate fabrics
   - Enough instances to fill the material without gaps

2. **Subtle Randomization**
   - rotation_random=0.02 keeps ornaments mostly aligned
   - position_random=0.01 prevents perfect grid while maintaining order
   - This mimics real embroidery which has slight imperfections

3. **Moderate Scale Variation (0.19)**
   - Creates natural variation without chaos
   - Ornaments noticeably different but still cohesive

4. **High Height Blend Contrast (0.96)**
   - Creates crisp, defined ornament edges
   - Embroidery appears to sit distinctly on fabric
   - Lower values would create mushy, undefined borders

5. **Multiple Perlin Noise Scales**
   - Different scales create variation at multiple frequencies
   - Fine (5), medium (6), and large (19) features combined
   - Results in natural, non-repetitive appearance

---

## Ornament Presets

The material includes built-in ornament options:

| Preset | input_selection Value | Description |
|--------|----------------------|-------------|
| Preset 0 | 0 | Default ornament shape |
| Preset 1 | 1 | Alternative pattern |
| Preset 2 | 2 | Different ornament style |
| Custom | 3 | User-provided mask via Custom_ornament |

When input_selection = 3, the Custom_ornament input becomes visible and active.

---

## Extending the Material

### Adding New Ornament Presets

1. Create new ornament shape using Spline nodes
2. Add to the preset selector logic
3. Update input_selection range

### Adjusting Density

For different fabric types:
- **Dense brocade**: x_amount=800, y_amount=900
- **Sparse decoration**: x_amount=200, y_amount=200
- **Scattered accents**: x_amount=50, y_amount=50

### Color Variations

Modify these for different looks:
- target_color: Base fabric hue
- outputcolor: Gemstone/accent color
- outputcolor_1: Metallic thread color

---

## Common Modifications

### Make Ornaments More Prominent
```
height_position: Increase value
Height Blend contrast: Increase toward 1.0
Levels Output High: Increase toward 0.7-0.8
```

### Make Ornaments More Subtle
```
height_position: Decrease value
Height Blend contrast: Decrease toward 0.6-0.7
Levels Output High: Decrease toward 0.2-0.3
```

### Add More Randomness
```
rotation_random: Increase to 0.05-0.1
scale_random: Increase to 0.3-0.4
position_random: Increase to 0.05-0.1
```

### Make Pattern More Regular
```
rotation_random: Decrease to 0.01
scale_random: Decrease to 0.05-0.1
position_random: Decrease to 0.005
```
