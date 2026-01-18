# Video Tutorial Reference

Course: **Designer First Steps** by Adobe Substance 3D (22 videos total)

## Part 5: Creating a Thread (19:38)

**URL**: https://www.youtube.com/watch?v=km-aBsLvG-c

**Focus**: Building the base thread texture procedurally

### Chapter Breakdown

| Timestamp | Topic |
|-----------|-------|
| 0:00 | Introduction to thread creation |
| ~2:00 | Shape node for cross-section |
| ~5:00 | Fibers node parameters |
| ~8:00 | Transformation 2D positioning |
| ~12:00 | Blend node combining |
| ~15:00 | Levels adjustment |
| ~18:00 | Final thread result |

### Key Concepts Covered
- Shape node for creating thread cross-section (elongated oval)
- Fibers node with parameters: Samples, Distribution, Curve, Maximum Distance, Spread Angle
- Transformation 2D for positioning and orientation
- Blend node: Opacity, Blending Mode, Use Source Alpha
- Levels for contrast and brightness adjustment

### Key Quote
"Not a still bitmap, but a dynamic recipe that we can interact with"

---

## Part 6: Fabric Weaving (15:48)

**URL**: https://www.youtube.com/watch?v=N0zw_owXnfE

**Focus**: Combining threads into woven fabric pattern

### Chapter Breakdown

| Timestamp | Topic |
|-----------|-------|
| 0:00 | Introduction to weaving |
| ~2:00 | Tile Generator setup |
| ~5:00 | Warp thread creation |
| ~8:00 | Weft thread creation |
| ~11:00 | Directional Noise application |
| ~13:00 | RT AO for depth |
| ~15:00 | Combining warp and weft |

### Key Concepts Covered
- Tile Generator: Pattern, Size, Position, Non Square Expansion
- Directional Noise: Turns, Distance, Angle Random
- RT_ao (Real-time AO) for ambient occlusion
- Warp threads (horizontal) and Weft threads (vertical)
- Interweaving pattern creation

---

## Part 7: Procedural Shape Design (18:57)

**URL**: https://www.youtube.com/watch?v=_tLjvmGcEcc

**Focus**: Creating custom ornament shapes procedurally

### Chapter Breakdown

| Timestamp | Topic |
|-----------|-------|
| 0:00 | Introduction to shape design |
| ~3:00 | Spline (Poly Quadratic) node |
| ~6:00 | Control points (p0, p1, p2) |
| ~9:00 | Show Direction Helper and Tangents |
| ~12:00 | Warp node for distortion |
| ~15:00 | Perlin Noise for variation |
| ~17:00 | Edge processing considerations |

### Key Concepts Covered
- Spline (Poly Quadratic): Points Coordinates, Show Direction Helper, Show Tangents, Segment Amount
- Warp node with Non Square Expansion
- Blend for combining shape elements
- Perlin Noise for organic variation
- Edge detection importance

### Key Quote
"Just a shapeless blob" won't make a good ornament - proper edge design is essential

---

## Part 9: Fabric Embroidery (9:14)

**URL**: https://www.youtube.com/watch?v=YCKO5P-pCfE

**Focus**: Adding ornaments/embroidery using Tile Sampler and Height Blend

### Chapter Breakdown

| Timestamp | Topic |
|-----------|-------|
| 0:00-0:11 | Introduction |
| 0:11-2:24 | Scale and Resolution |
| 2:24-6:25 | Tile Sampler Node |
| 6:25-8:35 | Height Blend Node |
| 8:35-9:14 | Final adjustments |

### Detailed Timestamps

#### Scale and Resolution (0:11 - 2:24)
- Testing materials at different resolutions
- Avoid 8K (makes things "extremely heavy")
- Higher resolution for close-up renders
- Resolution switching during development

#### Tile Sampler Node (2:24 - 6:25)
- Pattern parameter for layout
- Position Random for variation
- Rotation Random for angle changes
- Scale Random for size variation
- Symmetry Random Mode
- **Dynamic Sizing Technique**: Connect Perlin Noise to Scale input

#### Height Blend Node (6:25 - 8:35)
- Levels node first to flatten ornament heights
- Height Blend for intelligent combination
- Two key sliders for ornament prominence

### Key Quote
Tile Sampler is "a very important node"

---

## Course Continuation

### Part 10: Make Customized Shapes
- Advanced shape creation
- Custom ornament design

### Future Parts Cover:
- Gemstones/sequins
- Color and roughness
- Displacement
- Dynamic parameters
- Export workflows

---

## Quick Reference Links

| Part | Topic | Duration | URL |
|------|-------|----------|-----|
| 5 | Thread | 19:38 | https://www.youtube.com/watch?v=km-aBsLvG-c |
| 6 | Weaving | 15:48 | https://www.youtube.com/watch?v=N0zw_owXnfE |
| 7 | Shapes | 18:57 | https://www.youtube.com/watch?v=_tLjvmGcEcc |
| 9 | Embroidery | 9:14 | https://www.youtube.com/watch?v=YCKO5P-pCfE |
