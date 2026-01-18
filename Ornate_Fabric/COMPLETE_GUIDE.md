# Substance Designer: Complete Ornate Fabric Material Guide

A step-by-step written guide based on Adobe's "Designer First Steps" 22-part video series.

---

## Course Overview

**Project Goal**: Create an ornate fabric material with woven ornaments, embroidery trim, and gemstones.

**Pipeline Flow**: Thread → Weave → Embroidery → Trim → Gemstones → Colors → Export

**Core Principle**: Height-first workflow - the height map is the backbone that drives all other channels (normal, AO, roughness, color, metallic).

---

## PHASE 1: FOUNDATIONS (Parts 1-4)

### 1.1 Understanding Substance Designer

**What It Is**:
- Material authoring tool that generates textures using procedural operations
- Materials are **parametric** - "not a still bitmap, but a dynamic recipe"
- Node-based workflow where changes propagate downstream (non-destructive)

**Key Distinction**: Designer creates tileable base materials (paint bucket); Painter applies them to meshes (brush).

**Graph Concepts**:
- Graphs read **left to right** (left = beginning, right = final result)
- **Gray connections** = grayscale nodes
- **Yellow connections** = color nodes

### 1.2 Interface Overview

| Panel | Location | Purpose |
|-------|----------|---------|
| File Manager | Top left | Stores projects in packages (.sbs files) |
| Library | Below File Manager | All available nodes, filters, noises |
| Graph View | Center | Main workspace for connecting nodes |
| Properties | Right | Context-sensitive node parameters |
| 3D View | Bottom right | Real-time material preview |
| 2D View | Bottom left | Inspect node outputs, check tiling |

**Navigation**:
- Middle mouse: Pan
- Scroll wheel: Zoom
- F: Frame selected nodes
- Space/Tab: Quick search for nodes
- Ctrl+Shift+right-click drag: Rotate environment light

### 1.3 First Project Setup

**Step 1: Create New Graph**
```
File → New Substance Graph
Name: Ornate_Fabric
Template: Empty (for learning)
Resolution: 2048 (good starting point)
Save immediately (Ctrl+S)
```

**Step 2: Three Ways to Add Nodes**
1. **Toolbar** - Atomic nodes (fundamental building blocks)
2. **Library** - Browse all categories
3. **Quick Search** (Space/Tab) - Fastest method

**Step 3: Add Base Material Node**
- Press Space → type "base material"
- Place at right side of graph (the "end")
- Right-click → "View in 3D View"

**Step 4: Configure Preview Chain**
1. Scroll to User-Defined Maps section
2. Enable: **Normal**, **AO** (check boxes)
3. Keep **Height OFF** initially (performance)
4. Add **Normal** node (intensity: 3)
5. Add **RT_ao** node
6. Connect your height chain to both

---

## PHASE 2: FABRIC MATERIAL CREATION (Parts 5-10)

### 2.1 Thread Creation (Part 5)

**Goal**: Build the procedural thread - the fundamental building block.

**Node Chain**: Shape → Fibers → Transformation 2D → Blend → Levels

**Step 1: Create Thread Cross-Section**
```
Add: Shape node
Select: Bell or Paraboloid shape
Adjust: Width/height for oval cross-section
```

**Step 2: Add Fiber Strands**
```
Add: Fibers node
Parameters:
  - Samples: 128-256
  - Distribution: 0.5
  - Curve: 0.5
  - Maximum Distance: 0.7
  - Spread Angle: 25°
```

**Step 3: Position Fibers**
```
Add: Transformation 2D
Scale and position fibers over shape
Hold Ctrl to scale from center
```

**Step 4: Combine Elements**
```
Add: Blend node
Background: Shape
Foreground: Fibers
Mode: Multiply or Add
Opacity: 0.5-0.8
```

**Step 5: Adjust Contrast**
```
Add: Levels node
Compress range for softer thread
Output High: 0.7-0.9
```

**Tips**:
- Shift+D: Toggle disable/mute node
- Space in 2D view: Show tiling preview
- Height map: White = pushed up, Black = pulled down

---

### 2.2 Fabric Weaving (Part 6)

**Goal**: Create warp and weft interwoven pattern.

**Step 1: Create Warp (Horizontal) Threads**
```
Add: Tile Generator
Connect: Thread as Pattern Input
Parameters:
  - Pattern: Horizontal bar
  - X Amount: 800 (high)
  - Y Amount: 100 (low)
  - Enable: Non Square Expansion
```

**Step 2: Create Weft (Vertical) Threads**
```
Duplicate: Tile Generator
Change: Pattern to Vertical bar
Swap: X/Y amounts
Offset: 0.5 (for interweaving)
```

**Step 3: Add Variation**
```
Add: Directional Noise to each
Parameters:
  - Turns: 3
  - Distance: 0.15
  - Angle Random: 0.1
```

**Step 4: Combine Warp and Weft**
```
Add: Blend node
Mode: Max
Opacity: Full
```

**Step 5: Add Ambient Occlusion**
```
Add: RT_ao node
Connect: Combined weave
Blend: Multiply result with weave for depth
```

---

### 2.3 Procedural Shape Design (Part 7)

**Goal**: Create custom ornament shapes using Spline nodes.

**Spline Method**:
```
Add: Spline (Poly Quadratic)
Control Points:
  - p0: Start position
  - p1: Control point (pulls curve)
  - p2: End position
Segment Amount: 24-32 (smoothness)
Enable: Show Direction Helper, Show Tangents (for editing)
```

**Warp Method** (alternative):
```
1. Add: Shape (circle, square, etc.)
2. Add: Perlin Noise (distortion pattern)
3. Add: Warp node
   - Input: Your shape
   - Intensity: Perlin Noise
   - Intensity slider: 0.2-0.5
4. Add: Levels (restore contrast)
```

---

### 2.4 Importing Images (Part 8)

**Import vs Link**:
- **Import**: Creates duplicate in package (no connection to original)
- **Link**: Live connection - changes in source update in Designer

**Requirements**:
- Images must be **square** (1024x1024, 2048x2048, etc.)
- Convert to **grayscale** in Properties if needed

**Hybrid Workflow**: Import base image, then apply procedural operations (blur, warp, tile).

---

### 2.5 Fabric Embroidery (Part 9) - KEY TECHNIQUE

**Goal**: Add ornaments to fabric using Tile Sampler and Height Blend.

**Step 1: Set Up Tile Sampler**
```
Add: Tile Sampler
Connect: Thread to Pattern Input
Parameters:
  - X Amount: 600
  - Y Amount: 700 (asymmetric for natural look)
  - Scale: 3.8
  - Rotation: 90° (vertical threads)
  - Rotation Random: 0.02
  - Scale Random: 0.2
  - Position Random: 0.01
```

**Step 2: Connect Ornament Mask to Scale Map**
```
Connect: Ornament mask → Scale Map input (NOT Mask Input!)

WHY Scale Map instead of Mask?
- Scale Map shrinks threads to zero where mask is black
- Creates threads that "dive into" fabric with tapered transitions
- Mask Input creates harsh "cookie-cutter" cutout
```

**Step 3: Flatten Height**
```
Add: Levels after Tile Sampler
Crush whites: Output High = 0.3-0.5
Creates "something a bit more flat"
```

**Step 4: Blend with Fabric using Height Blend**
```
Add: Height Blend
Background: Base weave
Foreground: Flattened ornaments
Offset: Slightly above 0.5
Contrast: 0.96 (crisp edges)

WHY 0.96 Contrast?
- Real embroidery has distinct thread boundaries
- Low contrast (<0.7) creates mushy transitions
- 0.96 is near-maximum without harsh artifacts
```

**Key Insight**: Height Blend analyzes which layer is physically "higher" and blends based on elevation - creates realistic occlusion.

---

### 2.6 Customized Trim Elements (Part 10)

**Seam Element**:
```
1. Take thread
2. Add: Transform 2D → Rotate 90°
3. Set tiling: Vertical only
```

**Sequin Element**:
```
1. Add: Shape (Disc)
2. Subtract smaller disc (hole)
3. Add: Gradient Axial (tilt effect)
4. Multiply together
```

**Loop Element**:
```
1. Take thread
2. Add: Shape Mapper (amount: 1)
3. Creates circular bend
```

**Assembly**:
```
1. Position each with Transform 2D
2. Combine with Blend (Max mode)
3. Add: Sharpen if details lost
```

**Dot Node Organization**:
- Pin connections with Dot nodes (Alt + click on connection)
- Name Dots to create **portals** for referencing elsewhere

---

## PHASE 3: ADVANCED TECHNIQUES (Parts 11-15)

### 3.1 Understanding Inheritance (Part 11)

**Three Modes**:
| Mode | Behavior |
|------|----------|
| Relative to Input | Takes parameters from primary input (dark dot) |
| Relative to Parent | Takes from graph settings |
| Absolute | Override manually |

**Common Issue: 8-bit Banding**
```
Problem: 8-bit image in primary input → banding artifacts
Fix: Swap inputs OR set Absolute 16-bit
```

**Common Issue: Vertical Gradient in Curvature**
```
Problem: Tiling disabled upstream breaks Curvature Smooth
Fix: Swap blend inputs OR set node to Absolute full tiling
```

---

### 3.2 Radial Gemstones (Part 13)

**Diamond Shape - Method A (Square + Bevel)**:
```
1. Add: Shape → Square
2. Add: Transform 2D → Rotate 45°
3. Add: Transform 2D → Scale non-uniformly (squeeze)
4. Add: Bevel → Distance: -2 (inward)
5. Add: Levels → Flatten top if needed
```

**Splatter Circular Distribution**:
```
Add: Splatter Circular
Parameters:
  - Amount: 5-8
  - Radius: 0.3
  - Spread: 0.5 (half circle)
  - Size: Appropriate scale
  - Global Offset: Position adjustment
```

**Mountings (Metal Base)**:
```
1. Threshold → Edge Detect → Invert
2. Blur → Levels
3. Removes internal gradients, leaves silhouette
```

---

### 3.3 Mask Extraction (Part 14)

**Anticipate Needs While Building Height**:
- Ornament area (from Height Blend mask output)
- Trim area (from Threshold)
- Gemstones (from Threshold)

**Extraction Methods**:

| Method | Use Case |
|--------|----------|
| Height Blend Mask Output | Perfect for ornament/weave area |
| Threshold | Quick mask from height differences |
| Blur + Threshold | Clean up noisy masks |

**Dot Node Portals**:
```
1. Create Dot at mask source
2. Name it (e.g., "ornament_weave_mask")
3. Elsewhere, add Dot → select from dropdown
4. Avoids messy crossing connections
```

---

### 3.4 Imperfections & Details (Part 15)

**Lip/Border Effect**:
```
1. Take trim mask (Dot reference)
2. Add: Blur (0.8)
3. Add: Blend → Subtract original mask
4. Result: Outline only
5. Subtract from height = recessed border
   OR Add to height = raised border
```

**Micro-Distortions**:
```
1. Add: Directional Scratches
   - Pattern Amount: 0.2 (very subtle)
   - Align angle with weave direction
2. Add: Directional Warp
   - Connect scratches to intensity
   - Angle: Match weave (90° for vertical)
```

**Folds/Wrinkles**:
```
1. Add: Crease noise
2. Add: Warp with Perlin Noise
3. Add: Blur (soften)
4. Add: Normal node (intensity: 6-7)
5. Add: Normal Combine with main normal
6. Add: Non-Uniform Blur
   - Intensity map: Trim mask (inverted)
   - Samples: Max
   - Intensity: 25+
   - Protects trim from blur
```

---

## PHASE 4: FINISHING & EXPORT (Parts 16-21)

### 4.1 Color Pipeline (Part 16)

**PBR Rules for Base Color**:
- No pure black or white (no material is perfectly either)
- No shadows or lighting baked in
- Use **PBR Validate** node (green = good, red = too dark/bright)

**Method A: Gradient Map (Recommended)**

```
Step 1: Extract Curvature
Add: Normal node from height
Add: Curvature Smooth (from normal)
Fix: If vertical artifact, check tiling inheritance

Step 2: Apply Gradient Map
Add: Gradient Map node
Connect: Curvature
Open: Gradient editor
Sample: Colors from reference (drag line across image)

Step 3: Add Subtle Variation
Add: Tile Generator Color
  - Randomize Hue/Saturation
  - Warp with blurred curvature
Add: Blend with base (Soft Light, opacity: 0.1)
```

**Eye Dropper Tip**: Click eyedropper in Uniform Color, sample any pixel on screen.

**Metal Colors**: Use accurate values from charts (gold, silver, copper have specific RGB values).

---

### 4.2 Roughness & Metallic (Part 17)

**Roughness Map** (Dark = smooth, Light = rough):

```
Step 1: Start with Curvature
Take: Curvature Smooth output
Add: Levels → Invert
Reason: Cavities collect dust = rougher

Step 2: Control Contrast
Add: Histogram Range
  - Range slider: Shrinks value distribution
  - Position slider: Shifts overall darkness/brightness

Step 3: Add Material Details
Blend → Subtract ornament weave (shinier)
Blend → Subtract trim (shinier)
Blend → Subtract gemstones (shinier)
```

**Metallic Map**:
```
Base: Uniform Color (grayscale)
  - Fabric: 0.3-0.5 (slight shimmer trick)
  - Trim/mountings: White (fully metallic)
  - Gemstones: Black (non-metallic)
```

**Verification**:
- Switch 3D view to **Iray** renderer
- Reduce Normal intensity if needed (3 → 2)

---

### 4.3 Displacement & Translucency (Part 18)

**Displacement Setup**:
```
Step 1: Identify Elements to Displace
Only: Trim and gemstones (significant height)
NOT: Weave threads (too detailed)

Step 2: Build Displacement Map
Take: Trim+ornaments mask
Add: Blur (0.2) to prevent spikes
Add: Levels to control height

Step 3: Enable Tessellation
In material settings: Tessellation = 50+
"That's one very common mistake" - too low = no displacement
```

**Custom Translucency Output**:
```
1. Add: Output node
2. Set: Identifier, label, group (Material), usage (translucency)
3. Connect: Gemstone mask
```

---

### 4.4 Parameter Exposure (Parts 19-20)

**Exposing Slider Parameters**:
```
1. Click icon next to parameter
2. Select "Expose as new graph input"
3. Set: Label, Min/Max/Default values
4. Enable: Clamp if needed
```

**Switch Nodes (Toggles)**:
```
Add: Switch node
Connect: Both options
Expose: Switch selector
Rename: True/False to Yes/No
```

**Multi-Switch (Dropdowns)**:
```
Add: Multi-Switch node
Connect: Multiple options
Expose: Selector
Change: Type Editor to Dropdown
Name: Each input
```

**visible_if Conditions**:
```
Syntax: input("identifier") == value
Example: Show custom input only when "Custom" selected
```

**Creating Presets**:
```
1. Go to Preview tab
2. Configure desired settings
3. Name preset
4. Click "New"
```

---

### 4.5 Export & Integration (Part 21)

**Method A: Direct Export (Quick)**
```
1. Tools → Export Outputs
2. Choose: Location, format (PNG, TGA)
3. Enable: "Automatic Export" for live linking
4. Changes in Designer auto-update files
```

**Method B: SBSAR Publishing (Full)**
```
1. Click graph background
2. Attributes → Type: Standard Material
3. Select subgraph → Exposed in SBSAR: No
4. Select Package (not graph)
5. Publish: Ctrl+P (or click publish icon)
6. Update: Ctrl+Shift+P
```

**Integration**:
| Application | Method |
|-------------|--------|
| Blender | Install Substance add-on, load in Shader Editor |
| Unreal | Install Substance plugin, import SBSAR |
| Painter/Stager | Send To menu, or load directly |

---

## Quick Reference: Key Nodes

| Node | Purpose | Key Parameters |
|------|---------|----------------|
| **Tile Sampler** | Advanced tiling with map inputs | X/Y Amount, Scale, Scale Map |
| **Height Blend** | Realistic layer combination | Offset, Contrast (0.96) |
| **Fibers** | Yarn-like strand pattern | Samples, Curve, Spread Angle |
| **Splatter Circular** | Radial distribution | Amount, Radius, Spread |
| **Gradient Map** | Grayscale → Color conversion | Gradient editor, sampling |
| **Curvature Smooth** | Extract edge/cavity info | From Normal input |
| **Histogram Range** | Easy contrast control | Range, Position sliders |
| **Non-Uniform Blur** | Selective blur with mask | Samples, Intensity map |

---

## Troubleshooting Quick Guide

| Problem | Solution |
|---------|----------|
| 8-bit banding | Swap inputs or set Absolute 16-bit |
| Vertical gradient in Curvature | Fix tiling inheritance upstream |
| No displacement visible | Increase tessellation (50+) |
| Ornaments too prominent | Flatten with Levels before Height Blend |
| Pattern too uniform | Add randomness, connect Perlin to scale |
| Colors too dark/bright | Use PBR Validate, adjust values |

---

## Project Files

### Download Official Sample Files

The official sample project files for this tutorial are available from Adobe:

**Source**: [Substance Designer for Beginners - Official Tutorial](https://www.adobe.com/learn/substance-3d-designer/web/substance-designer-for-beginners)

This includes:
- Complete `Ornate_Fabric.sbs` project file
- All dependencies and referenced materials
- Example exports and presets

### Local Project Structure

If you have the sample files, the main project is:
- **Main Project**: `Ornate_Fabric.sbs`
- **Dependencies**: Located in `dependencies/` subdirectory (48 SBS files)
- **Video Sources**: All 22 parts documented in the substance-designer-tutor plugin

---

## SBS File Analysis: Ornate_Fabric.sbs

### Graph Structure (Frames/Sections)

The graph is organized into 14 logical sections:

| Section | Purpose |
|---------|---------|
| **Base thread** | Foundational thread element creation |
| **thread** | Thread refinement and variations |
| **Base weave** | Warp/weft fabric pattern |
| **Stylized flower** | Floral ornament shape design |
| **Random shape** | Procedural shape generation |
| **ornaments** | Ornament mask subgraph reference |
| **Ornament weave** | Thread embroidery on fabric |
| **loop** | Loop trim element |
| **sequin** | Sequin trim element |
| **Radial ornaments** | Gemstone circular arrangements |
| **Folds** | Fabric wrinkle effects |
| **Fabric color** | Base color pipeline |
| **Roughness** | Surface roughness map |
| **Metallic** | Metal vs non-metal definition |

### Exposed Parameters (User Interface)

| Parameter | Purpose |
|-----------|---------|
| **Ornament type** | Multi-switch for pattern selection |
| **Floral ornament** | Enable/disable floral pattern |
| **Geometrical pattern** | Enable/disable geometric pattern |
| **Custom ornament** | User-provided mask input |
| **Ornament emboss intensity** | Height blend offset control |
| **Fabric color** | Base fabric color selection |
| **Fabric roughness** | Surface roughness adjustment |
| **Folds intensity** | Wrinkle strength control |
| **Gemstones position** | Radial arrangement positioning |
| **Gemstones color** | Gem color selection |
| **Metal color** | Trim/mounting metal color |
| **Trim** | Enable/disable trim elements |

### Output Channels

| Output | Type | Description |
|--------|------|-------------|
| Base Color | RGBA | Diffuse color map |
| Normal | RGBA | Surface normal details |
| Roughness | Grayscale | Surface reflection control |
| Metallic | Grayscale | Metal/non-metal mask |
| Height | Grayscale | Displacement source |
| Ambient Occlusion | Grayscale | Shadow information |
| Translucency | Grayscale | Light transmission (gems) |

### Node Usage Statistics

**Most Used Nodes:**
| Count | Node | Purpose |
|-------|------|---------|
| 8 | Blur HQ | Smoothing/softening |
| 7 | Threshold | Binary mask creation |
| 7 | Shape | Basic primitives |
| 5 | Switch | Toggle options |
| 4 | Tile Generator | Pattern tiling |
| 4 | Spline Poly Quadratic | Custom curves |
| 3 | Perlin Noise | Organic variation |
| 3 | Edge Detect | Outline extraction |
| 2 | Splatter Circular | Radial distribution |
| 2 | RT_ao | Ambient occlusion |
| 2 | Histogram Range | Contrast control |
| 2 | Directional Scratches | Micro detail |
| 2 | Bevel | Edge softening |

**Key Single-Instance Nodes:**
- Tile Sampler (embroidery)
- Height Blend (layer combination)
- Fibers 1 (thread creation)
- Shape Mapper (loop creation)
- Normal Combine (fold integration)
- Non-Uniform Blur (selective blur)
- PBR Base Material (final output)

### Dependencies (48 SBS Files)

**Pattern Nodes:**
- pattern_fibers_1.sbs
- pattern_shape.sbs
- pattern_tile_generator.sbs
- pattern_tile_sampler.sbs
- pattern_splatter_circular.sbs
- pattern_polygon_2.sbs

**Noise Nodes:**
- noise_perlin_noise.sbs
- noise_directional_noise_3.sbs
- noise_directional_scratches.sbs
- noise_anisotropic_noise.sbs
- noise_creased.sbs

**Effect Nodes:**
- height_blend.sbs
- bevel.sbs
- blur_hq.sbs
- curvature_smooth.sbs
- non_uniform_blur.sbs
- edge_detect.sbs
- threshold.sbs

**Normal Map Tools:**
- normal_color.sbs
- normal_combine.sbs
- normal_normalise.sbs

---

## Verification

To test this guide:
1. Open `Ornate_Fabric.sbs` in Substance Designer
2. Follow node chains matching each stage
3. Compare parameter values with documented settings
4. Reference video transcripts for visual confirmation
5. Verify frame organization matches documented sections

---

## Additional Resources

For interactive help with Substance Designer concepts, techniques, and troubleshooting, you can use the substance-designer-tutor plugin available in this project.
