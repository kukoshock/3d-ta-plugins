# Workflows Reference

Step-by-step procedures for common Substance Designer tasks (15 workflows).

---

## 1. Project Setup Workflow

**Goal**: Create a new material project with proper preview setup

### Steps

1. **Create New Graph**
   - File → New Substance Graph
   - Name: `your_material_name`
   - Template: Empty (for learning)
   - Resolution: 2048 (default, good for development)
   - Save package immediately (Ctrl+S)

2. **Add Base Material Node**
   - Press Space/Tab → type "base material"
   - Place at right side of graph (this is the "end")
   - Right-click → "View in 3D View"

3. **Configure Base Material**
   - Scroll to User-Defined Maps section
   - Enable: Normal, AO (check boxes)
   - Keep Height OFF initially (performance)
   - Disable Metallic/Roughness if not needed yet

4. **Create Preview Chain**
   - Add **Normal** node (intensity: 3)
   - Add **RT_ao** node
   - Connect your height chain to both
   - Connect Normal and AO outputs to Base Material

5. **Set Preview Mesh**
   - In 3D view, select appropriate mesh
   - For fabric: use cloth or plane mesh
   - Adjust UV Tiling if needed (Materials panel)

---

## 2. Thread Creation Workflow

**Goal**: Build a procedural thread from scratch

### Steps

1. **Create Thread Cross-Section**
   - Add **Shape** node
   - Select Paraboloid or Bell shape
   - Adjust width/height for oval cross-section

2. **Add Fiber Strands**
   - Add **Fibers** node
   - Parameters:
     - Samples: 128-256
     - Distribution: 0.5
     - Curve: 0.5
     - Maximum Distance: 0.7
     - Spread Angle: 25

3. **Position Fibers on Shape**
   - Add **Transformation 2D**
   - Scale and position fibers over shape
   - Hold Ctrl to scale from center

4. **Combine Elements**
   - Add **Blend** node
   - Background: Shape
   - Foreground: Fibers
   - Mode: Multiply or Add
   - Opacity: 0.5-0.8

5. **Adjust Contrast**
   - Add **Levels** node
   - Compress range for softer thread
   - Output High: 0.7-0.9

---

## 3. Fabric Weaving Workflow

**Goal**: Create warp and weft interwoven pattern

### Steps

1. **Create Warp (Horizontal) Threads**
   - Add **Tile Generator**
   - Connect thread as Pattern Input
   - Parameters:
     - Pattern: Horizontal bar
     - X Amount: High (800)
     - Y Amount: Lower (100)
   - Enable Non Square Expansion

2. **Create Weft (Vertical) Threads**
   - Duplicate Tile Generator
   - Change pattern to Vertical bar
   - Swap X/Y amounts
   - Offset: 0.5 (for interweaving)

3. **Add Variation**
   - Add **Directional Noise** to each
   - Parameters:
     - Turns: 3
     - Distance: 0.15
     - Angle Random: 0.1

4. **Combine Warp and Weft**
   - Add **Blend** node
   - Mode: Max
   - Full opacity

5. **Add Ambient Occlusion**
   - Add **RT_ao** node
   - Connect combined weave
   - Multiply result with weave for depth

---

## 4. Shape Design Workflow (Spline Method)

**Goal**: Create custom ornament shape with curves

### Steps

1. **Create Base Curve**
   - Add **Spline (Poly Quadratic)**
   - Set control points:
     - p0: Start position
     - p1: Control point (pulls curve)
     - p2: End position
   - Segment Amount: 24-32 for smoothness

2. **Visualize While Working**
   - Enable "Show Direction Helper"
   - Enable "Show Tangents"
   - Disable before final use

3. **Add Organic Variation**
   - Add **Warp** node
   - Connect **Perlin Noise** to intensity
   - Low intensity (0.05-0.1)

4. **Refine Edges**
   - Add **Levels** to control contrast
   - Add **Blur** if edges too harsh

5. **Create Multiple Parts**
   - Duplicate and modify for each element
   - Combine with **Blend** (Max mode)

---

## 5. Shape Design Workflow (Warp Method)

**Goal**: Create ornament by distorting basic shapes

### Steps

1. **Start with Basic Shape**
   - Add **Shape** (circle, square, etc.)
   - Or use imported image

2. **Create Distortion Pattern**
   - Add **Perlin Noise** or **Clouds**
   - Adjust scale for desired warping

3. **Apply Warp**
   - Add **Warp** node
   - Input: Your shape
   - Intensity: Perlin Noise
   - Adjust intensity slider (0.2-0.5)

4. **Clean Up**
   - Add **Levels** to restore contrast
   - Add **Threshold** if binary mask needed

---

## 6. Embroidery Workflow

**Goal**: Add ornaments to fabric using Tile Sampler

### Steps

1. **Prepare Ornament Mask**
   - Create or import ornament shape
   - Ensure high contrast (near black/white)
   - Clean edges with Blur/Levels if needed

2. **Set Up Tile Sampler**
   - Add **Tile Sampler**
   - Connect ornament to Pattern Input
   - Initial parameters:
     - X/Y Amount: 600/700
     - Scale: 3-4
     - Rotation Random: 0.02
     - Scale Random: 0.2
     - Position Random: 0.01

3. **Add Dynamic Sizing**
   - Create **Perlin Noise** (scale: 5-10)
   - Connect to Tile Sampler's Scale Map input
   - This creates "dynamic sizing" effect

4. **Flatten Height**
   - Add **Levels** after Tile Sampler
   - Crush whites: Output High = 0.3-0.5
   - Creates "something a bit more flat"

5. **Blend with Fabric**
   - Add **Height Blend**
   - Background: Base weave
   - Foreground: Flattened ornaments
   - Contrast: 0.96 (crisp edges)

---

## 7. Gemstone Creation Workflow

**Goal**: Create faceted gemstone shape

### Method A: Square + Bevel

1. Add **Shape** → Square
2. Add **Transform 2D** → Rotate 45°
3. Add **Transform 2D** → Scale non-uniformly (squeeze)
4. Add **Bevel** → Distance: -2 (inward)
5. Add **Levels** → Flatten top if needed

### Method B: Pyramid

1. Add **Pyramid** shape
2. Add **Levels** → Compress range
3. Flatten top by crushing whites

### Method C: Polygon

1. Add **Polygon** → Sides: 4
2. Rotate 45°
3. Use Gradient slider for slope

### Final Assembly

1. Add **Splatter Circular**
   - Amount: 5-8
   - Radius: 0.3
   - Spread: 0.5 (half circle)
   - Size: appropriate scale
2. Add Global Offset to position

---

## 8. Trim Assembly Workflow

**Goal**: Create decorative trim with multiple elements

### Steps

1. **Create Seam Element**
   - Take thread
   - Add **Transform 2D** → Rotate 90°
   - Set tiling: Vertical only
   - Divide by 2 repeatedly for tiling

2. **Create Sequin Element**
   - **Shape** (Disc)
   - Subtract smaller disc (hole)
   - Add **Gradient Axial** for tilt effect
   - Multiply together

3. **Create Loop Element**
   - Take thread
   - Add **Shape Mapper** (amount: 1)
   - Creates circular bend

4. **Assemble Trim**
   - Position each element with **Transform 2D**
   - Combine with **Blend** (Max mode)
   - Add **Sharpen** if details lost

5. **Create Trim Mask**
   - Add **Threshold** to get silhouette
   - Save to named **Dot** for later use

---

## 9. Mask Extraction Workflow

**Goal**: Extract masks from height map for other channels

### Anticipate Needs

While building height, identify what masks you'll need:
- Ornament area (from Height Blend output)
- Trim area (from Threshold)
- Gemstones (from Threshold)
- Combined elements (from blends)

### Extraction Methods

**From Height Blend:**
- Height Blend has Mask output
- Connect Dot node to this output
- Name it (e.g., "ornament_weave_mask")

**From Height Differences:**
- Add **Threshold** node
- Adjust threshold value
- Clean with Blur + Threshold if needed

**Outline Extraction:**
- Take mask
- Add **Blur** (0.8)
- **Subtract** original
- Result: outline only

### Organize with Portals

1. Create **Dot** at mask source
2. Name it descriptively
3. Elsewhere, add Dot and select from dropdown
4. Avoids messy crossing connections

---

## 10. Imperfections Workflow

**Goal**: Add realistic details and wear

### Lip/Border Effect

1. Take trim mask (Dot reference)
2. Add **Blur** (0.8)
3. Add **Blend** → Subtract original mask
4. Result: outline/border only
5. **Subtract** from main height (or add for raised border)

### Micro-Distortions

1. Add **Directional Scratches**
   - Pattern Amount: 0.2 (subtle)
   - Align angle with weave direction
2. Add **Directional Warp**
   - Connect scratches to intensity
   - Angle: Match weave direction (90° for vertical)
3. Apply to weave before final blend

### Folds/Wrinkles

1. Add **Crease** noise
2. Add **Warp** with **Perlin Noise**
3. Add **Blur** (soften)
4. Add **Normal** node (intensity: 6-7)
5. Add **Normal Combine** with main normal
6. Add **Non-Uniform Blur**
   - Intensity map: Trim mask (inverted)
   - Samples: Max
   - Intensity: 25+
   - Protects trim from blur

---

## 11. Color Pipeline Workflow

**Goal**: Build PBR-compliant base color map

### Method A: Gradient Map (Recommended)

1. **Extract Curvature**
   - Add **Normal** node from height
   - Add **Curvature Smooth** (from normal)
   - If vertical artifact: fix tiling inheritance

2. **Apply Gradient Map**
   - Add **Gradient Map** node
   - Connect curvature
   - Open gradient editor
   - Sample colors from reference (drag line)
   - Or manually set color keys

3. **Add Subtle Variation**
   - Add **Tile Generator Color**
   - Randomize Hue/Saturation
   - Warp with curvature (blurred)
   - **Blend** with base (Soft Light, opacity: 0.1)

### Method B: Mask-Based Blending

1. Add **Uniform Color** for base
2. Add **Uniform Color** for variation
3. **Blend** using grayscale mask
4. Repeat for additional colors

### Final Steps

1. Add colors for trim/ornaments
   - Use mask to control distribution
2. **Blend** all color groups
3. Test with **PBR Validate** node
   - Green = compliant
   - Red = too dark/bright

---

## 12. Roughness & Metallic Workflow

**Goal**: Create material property maps

### Roughness Map

1. **Start with Curvature**
   - Take Curvature Smooth output
   - Add **Levels** → Invert (or click Invert icon)
   - Reason: Cavities should be rough, edges smooth

2. **Control Contrast**
   - Add **Histogram Range**
   - Range slider: Reduce contrast
   - Position slider: Shift darker/lighter

3. **Add Material Details**
   - **Blend** → Subtract ornament weave (make shinier)
   - **Blend** → Subtract trim (make shinier)
   - **Blend** → Subtract gemstones (make shinier)

### Metallic Map

1. **Create Base**
   - Add **Uniform Color** (grayscale)
   - Value: 0.3-0.5 for fabric (shimmer trick)

2. **Add Metallic Elements**
   - **Blend** → Add ornament weave mask (mode: Max, low opacity)
   - **Blend** → Add trim+ornaments mask (full metallic)
   - **Blend** → Subtract gemstones mask (non-metallic)

### Verify

1. Switch 3D view to **Iray** renderer
2. Check under different HDRIs
3. Reduce Normal intensity if needed (3 → 2)

---

## 13. Displacement Workflow

**Goal**: Add physical depth to material

### Create Displacement Map

1. **Identify Elements to Displace**
   - Only trim and gemstones (significant height)
   - NOT weave threads (too much detail)

2. **Build Displacement Map**
   - Take trim+ornaments mask
   - Add **Blur** (0.2) to prevent spikes
   - Add **Levels** to control height

3. **Add Gemstone Detail**
   - Take gemstone mask
   - **Blend** → Add on top of blurred base
   - Keeps gem edges sharper

### Configure Displacement

1. **Enable in Base Material**
   - Height input: Connect displacement map

2. **Set Tessellation**
   - In material settings, tessellation: 50+
   - "That's one very common mistake" - too low = no displacement

3. **Adjust Scale**
   - Displacement scale slider
   - Test at different angles

---

## 14. Parameter Exposure Workflow

**Goal**: Make material parameters accessible to end users

### Identify Key Parameters

Good candidates:
- Ornament type (Multi-Switch)
- Emboss intensity (Height Blend offset)
- Fabric color (Color Match/Uniform Color)
- Roughness (Histogram Range position)
- Enable/disable features (Switch nodes)

### Expose Parameters

1. **For Sliders**
   - Click icon next to parameter
   - "Expose as new graph input"
   - Set Label, Min/Max/Default
   - Enable Clamp if needed

2. **For Toggles**
   - Add **Switch** node
   - Connect both options
   - Expose switch selector
   - Rename True/False to Yes/No

3. **For Dropdowns**
   - Add **Multi-Switch** node
   - Connect multiple options
   - Expose selector
   - Change Type Editor to Dropdown
   - Name each input

4. **For Custom User Content**
   - Add **Input** node (Grayscale)
   - Set Label and Description
   - Add visible_if condition if needed

### Link Related Parameters

1. Expose main parameter
2. On related nodes: "Use existing" → select exposed param
3. Keeps transforms synchronized

### Organize

1. Double-click graph background
2. Go to Parameters tab
3. Drag to reorder
4. Add visible_if to hide related params when disabled

### Create Presets

1. Go to Preview tab
2. Configure desired settings
3. Give name
4. Click "New"

---

## 15. Export & Integration Workflow

**Goal**: Use material in external applications

### Method A: Direct Export (Quick)

1. **Configure Export**
   - Tools → Export Outputs
   - Choose location (create folder)
   - Format: PNG or TGA
   - Select outputs to export

2. **Enable Live Link**
   - Check "Automatic Export"
   - Changes auto-update files

3. **Use in External App**
   - Blender: Ctrl+Shift+T with Node Wrangler
   - Unreal: Import to Content Browser
   - Refresh textures when Designer changes

### Method B: SBSAR Publishing (Full)

1. **Configure Graph**
   - Click graph background
   - Attributes → Type: Standard Material
   - Set Physical Size if needed

2. **Configure Subgraph**
   - Select subgraph
   - Attributes → Exposed in SBSAR: No

3. **Publish**
   - Select Package (not graph)
   - Click publish icon (or Ctrl+P)
   - Choose location
   - To update: Ctrl+Shift+P

4. **Use SBSAR**
   - Blender: Install Substance add-on, load in Shader Editor
   - Unreal: Install Substance plugin, import SBSAR
   - Painter/Stager: Send To menu, or load directly

### Painter Integration

1. In Designer: Send To → Painter
2. Material appears in shelf
3. Apply to layer
4. Use Anchor Points:
   - Add anchor below fabric layer
   - Reference from exposed Custom Input
   - Combines procedural + manual painting
