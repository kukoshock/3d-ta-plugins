# Video Tutorial Reference

Course: **Designer First Steps** by Adobe Substance 3D (22 videos total)

Playlist URL: https://www.youtube.com/playlist?list=PLB0wXHrWAmCxBw92VSRjqsbqYXgkF8puC

---

## Course Overview (2:44)

**URL**: https://www.youtube.com/watch?v=At3FoFcuN6k

**Focus**: Introduction to the course structure and what you'll learn

### Key Points
- Course covers creating a fabric material from scratch
- Thread → Weave → Embroidery → Trim → Gemstones → Export
- Introduces both soft and hard-surface techniques
- Final material will be fully parametric

---

## Part 1: What is Substance Designer? (2:33)

**URL**: https://www.youtube.com/watch?v=UyF5Ie-HJ0Q

**Focus**: Understanding Substance Designer's purpose and workflow

### Key Concepts
- **Procedural material authoring** - generates textures, not paints them
- **Parametric materials** - "not a still bitmap, but a dynamic recipe"
- **Node-based workflow** - connect nodes to create effects
- **Non-destructive** - changes propagate downstream

### Designer vs Painter
- **Designer**: Creates the "paint" (tileable base materials)
- **Painter**: Applies the "brush" (specific mesh texturing)

### Key Quote
"Materials created inside it are parametric - you're not only saving static bitmaps but also the dynamic recipe to create them"

---

## Part 2: How to Make Materials (4:28)

**URL**: https://www.youtube.com/watch?v=Wg1gzR3rQeY

**Focus**: Understanding nodes and material structure

### Key Concepts
- **Nodes** = operators that transform information
- **Input** (left) = what you feed the node
- **Output** (right) = result of operation
- **Graph flow**: Left to right (start → finish)

### Height-First Workflow
- Almost always start with the **height map**
- Height drives: Normal, AO, Masks, Roughness, Color
- Build methodically: Macro → Medium → Micro details

### Connection Colors
- **Gray** = Grayscale nodes
- **Yellow** = Color nodes

### Key Quote
"The height information really flows into all the different sections of the graph"

---

## Part 3: Interface Overview (4:33)

**URL**: https://www.youtube.com/watch?v=_KlXkHLH5pc

**Focus**: Navigating the Designer interface

### Main Panels
| Panel | Purpose |
|-------|---------|
| File Manager (Top Left) | Project packages, graphs, resources |
| Library (Below File Manager) | All available nodes, textures, filters |
| Graph View (Center) | Main workspace for node connections |
| Properties Panel (Right) | Context-sensitive parameter editing |
| 3D View (Bottom) | Real-time material preview |
| 2D View (Bottom) | Detailed texture inspection |

### Navigation
| Action | Control |
|--------|---------|
| Pan graph | Middle mouse button |
| Zoom | Scroll wheel |
| Return to nodes | Press F |
| Rotate 3D model | Left mouse |
| Pan 3D view | Middle mouse |
| Zoom 3D | Right mouse / Scroll |
| Rotate environment | Ctrl + Shift + Right click drag |

### Properties Panel Structure
1. **Base Parameters** - Common to all nodes
2. **Attributes** - Node metadata (can collapse)
3. **Instance Parameters** - Node-specific settings

---

## Part 4: First Project Setup (11:29)

**URL**: https://www.youtube.com/watch?v=-DlD476pnxQ

**Focus**: Creating and setting up a new project

### Project Setup Steps
1. File → New Substance Graph
2. Name graph (e.g., "Ornate_Fabric")
3. Use Empty template (to learn from scratch)
4. Default 2048 resolution is good starting point
5. Save package immediately

### Adding Nodes (3 Methods)
1. **Toolbar** - Grab atomic nodes from top bar
2. **Library** - Browse and drag from left panel
3. **Quick Search** - Press Space/Tab, type name

### Preview Setup
1. Add **Base Material** node (sits at end of graph)
2. Right-click → drag to 3D View, or "View in 3D View"
3. Enable **Normal** and **AO** user-defined maps
4. Add **Normal** node (intensity: 3)
5. Add **RT_ao** node
6. Keep **Height** disabled initially (heavy process)

### Key Quote
"This base material node is going to sit at the very right of our node arrangement"

---

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

### Key Nodes
- **Shape** - Elongated oval for thread cross-section
- **Fibers** - Directional strand patterns
- **Transformation 2D** - Positioning and orientation
- **Blend** - Combining elements
- **Levels** - Contrast/brightness adjustment

### Fibers Parameters
| Parameter | Purpose |
|-----------|---------|
| Samples | Number of fiber strands |
| Distribution | Spread of fibers |
| Curve | Fiber curvature |
| Maximum Distance | Fiber length |
| Spread Angle | Angular spread |

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

### Key Concepts
- **Warp threads** - Horizontal
- **Weft threads** - Vertical
- **Interweaving** - Threads cross over/under each other
- **Tile Generator** - Creates grid pattern
- **Directional Noise** - Adds organic variation

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

### Key Concepts
- **Spline nodes** create curves with control points
- **Segment Amount** controls smoothness
- Design shapes with clear edges for later detection
- Blend and warp for complex shapes

### Key Quote
"Just a shapeless blob" won't make a good ornament - proper edge design is essential

---

## Part 8: Importing Images (8:22)

**URL**: https://www.youtube.com/watch?v=eGKl3dcSXxE

**Focus**: Bringing external images into Designer

### Import vs Link
| Method | Behavior |
|--------|----------|
| **Import** | Creates copy in package, no link to original |
| **Link** | Live connection, updates when source changes |

### Requirements
- Images must be **square** (2048x2048, etc.)
- Convert to **grayscale** if needed (click gray button in Properties)
- Color images show yellow connection dot

### Hybrid Workflow
1. Import/link base image
2. Apply procedural operations (blur, warp, tile)
3. Get "best of both worlds"

### Output Nodes
- Create **Output** node for subgraph exports
- Set **Identifier** and **Label**
- Can have multiple outputs per subgraph

---

## Part 9: Fabric Embroidery (9:15)

**URL**: https://www.youtube.com/watch?v=YCKO5P-pCfE

**Focus**: Adding ornaments using Tile Sampler and Height Blend

### Chapter Breakdown

| Timestamp | Topic |
|-----------|-------|
| 0:00-0:11 | Introduction |
| 0:11-2:24 | Scale and Resolution |
| 2:24-6:25 | Tile Sampler Node |
| 6:25-8:35 | Height Blend Node |
| 8:35-9:14 | Final adjustments |

### Tile Sampler Key Points
- "A very important node"
- Connect **Perlin Noise** to Scale input for dynamic sizing
- Adjust randomization for natural look

### Height Blend Workflow
1. Use **Levels** to flatten ornament height first
2. Height Blend combines realistically
3. High contrast (0.96) for crisp edges

### Key Quote
Tile Sampler is "a very important node"

---

## Part 10: Customized Shapes (8:17)

**URL**: https://www.youtube.com/watch?v=caVvzNg-iRI

**Focus**: Creating trim elements - seams, sequins, loops

### Elements Created
| Element | Technique |
|---------|-----------|
| **Seam** | Thread + Transform 2D (90° + tile) |
| **Sequin** | Disc - smaller disc + Gradient Axial |
| **Loop** | Shape Mapper (amount: 1) to bend thread |

### Dot Node
- Pin connections: Alt + click on connection
- Organize graph, keeps it clean
- Backspace to remove

### Key Technique
Offset 0.5 + Blend (Max) with original = continuous line

---

## Part 11: Understanding Inheritance (5:38)

**URL**: https://www.youtube.com/watch?v=CYWOKPRnP5o

**Focus**: How parameters flow through the graph

### Inheritance Methods
| Method | Source | Icon |
|--------|--------|------|
| Relative to Input | Primary input (dark dot) | Chain link |
| Relative to Parent | Graph settings | Up arrow |
| Absolute | Manual override | Locked |

### Primary Input
- In Blend nodes = **background** connection
- Determines inherited resolution, bit depth, tiling

### Common Issues
- **Banding artifacts** - 8-bit image in primary input
- **Solution**: Swap inputs OR set bit depth to Absolute 16-bit

---

## Part 12: Element Placement (4:35)

**URL**: https://www.youtube.com/watch?v=bJUoc8GR18E

**Focus**: Placing and tiling trim elements

### Tiling Control
1. Set tiling inheritance to **Absolute**
2. Choose: Full, Horizontal only, Vertical only, None

### Assembly Workflow
1. Create element
2. Transform 2D (rotate, offset)
3. Set tiling to Vertical only
4. Divide by 2 repeatedly for tiling
5. Blend with main height (Max mode)
6. Add **Sharpen** if details are lost

### 3D Preview Adjustment
- Materials → UV Tiling slider to shift preview
- Doesn't change actual material

---

## Part 13: Radial Gemstones (11:34)

**URL**: https://www.youtube.com/watch?v=QPD_oASJuUM

**Focus**: Creating gemstones with multiple techniques

### Diamond Shape (3 Methods)
1. **Square + Rotate + Transform + Bevel** (inward: -2)
2. **Pyramid shape + Levels** (flatten top)
3. **Polygon (4 sides) + Rotate + Gradient slider**

### Splatter Circular
| Parameter | Purpose |
|-----------|---------|
| Amount | Number of gems |
| Radius | Distance from center |
| Spread | Portion of circle (0.5 = half) |
| Size | Gem scale |
| Ring Rotation | Rotate arrangement |
| Global Offset | Position adjustment |

### Mounting Creation
1. **Threshold** → removes internal gradients
2. **Edge Detect** → gets silhouette
3. **Invert** → for proper height
4. **Blur + Levels** → refine shape

### Pro Tip
Hold **Shift** while scrubbing for finer control

---

## Part 14: Mask Extraction (7:13)

**URL**: https://www.youtube.com/watch?v=yYHTw4IKyAM

**Focus**: Extracting masks from height for other maps

### Key Principle
"Anticipate mask needs while building height"

### Extraction Methods
| Source | Use Case |
|--------|----------|
| Height Blend mask output | Ornament weave area |
| Threshold | Quick mask from brightness |
| Blur + Threshold | Clean up noisy masks |

### Dot Node Portals
1. Name Dot at source (e.g., "ornament_weave_mask")
2. Add Dot elsewhere
3. Select from dropdown to reference
4. Creates "portal" - avoids crossing connections

### Key Quote
"Think nonlinear" - reuse information, anticipate needs

---

## Part 15: Adding Imperfections (10:25)

**URL**: https://www.youtube.com/watch?v=EgvCOGkaN9E

**Focus**: Making materials more realistic

### Lip/Border Effect
1. Take trim mask
2. **Blur** (0.8) to expand
3. **Subtract** original mask (outline only)
4. **Subtract** from height = raised border

### Micro Distortions
- **Directional Warp** with **Directional Scratches**
- Pattern Amount: 0.2 (very subtle)
- Align warp angle with weave direction (90°)

### Folds/Wrinkles
1. **Crease** noise → **Warp** → **Blur**
2. **Normal** node (intensity: 6-7)
3. **Normal Combine** with main normal
4. **Non-Uniform Blur** with trim mask (protects edges)
   - Samples: Max
   - Intensity: 25+

### Key Quote
"Little somethings that just breathe life and personality into it"

---

## Part 16: Adding Colors (17:13)

**URL**: https://www.youtube.com/watch?v=8S2TTbTuqYk

**Focus**: Building the base color map

### PBR Rules
- No pure black or white
- No shadows/lighting baked in
- Use **PBR Validate** node (green = good)

### Color Techniques

**1. Uniform Colors + Blending**
- Blend colors using grayscale masks
- Layer for complexity

**2. Gradient Map (Powerful)**
- Takes grayscale → outputs color
- Sample from reference images
- Works great with **Curvature Smooth**

**3. Tile Generator Color**
- Randomize Hue/Saturation
- Blend with **Soft Light** at 0.1 opacity

### Curvature Artifact Fix
If vertical gradient appears:
- Check upstream tiling inheritance
- Set to Absolute full tiling
- Or swap Blend inputs (X key)

### Metal Colors
Use accurate RGB values from color charts (gold, silver, etc.)

---

## Part 17: Roughness & Metallic (12:46)

**URL**: https://www.youtube.com/watch?v=TWSXb94wH-Q

**Focus**: Creating roughness and metallic maps

### Roughness Map
- Dark = smooth/reflective
- Light = rough/diffuse
- Start with **inverted curvature**
- Use **Histogram Range** for easy control

### Metallic Map
- Works like binary mask
- Trim/mountings = white (metallic)
- Fabric = slight gray (anisotropy trick)
- Gemstones = black (non-metallic)

### Ray Tracing Check
- Switch to **Iray** renderer
- Reduce **Normal intensity** (3 → 2)
- Blur noisy elements if shading breaks

### HDRI Testing
- Library → HDRIs
- Drag/drop into viewport
- Ctrl + Shift + Right click to rotate

---

## Part 18: Displacement & Translucency (7:14)

**URL**: https://www.youtube.com/watch?v=med5kNfGPWk

**Focus**: Adding physical depth and light transmission

### Displacement
- Requires **tessellation** (set in material, e.g., 50)
- Only displace what sticks out (trim, gemstones)
- **Blur** input (0.2) to avoid spiky artifacts
- Create separate map from masks, not raw height

### Custom Output Creation
1. Add **Output** node
2. Set: Identifier, Label, Group (Material), Usage
3. Connect appropriate mask

### Translucency
- Use **gemstone mask** directly
- Configure absorption in final render app

---

## Part 19: Exposing Parameters (9:35)

**URL**: https://www.youtube.com/watch?v=6AVxsMTwKrk

**Focus**: Making parameters accessible to end users

### Exposing Process
1. Click icon next to parameter
2. Select "Expose as new graph input"
3. Set: Label, Type Editor, Min/Max/Default

### Switch Nodes
| Node | Purpose |
|------|---------|
| **Switch** | Toggle 2 inputs |
| **Multi-Switch** | Cycle through multiple inputs |

### Input Node
- Creates slot for user content
- Add description to guide users
- Grayscale or Color versions

### Visible_if Conditions
- Hide parameters based on other settings
- Syntax: `input("identifier") == value`

---

## Part 20: Parameter Presets (14:27)

**URL**: https://www.youtube.com/watch?v=sDy1xYqTMP8

**Focus**: Organizing parameters and creating presets

### Linking Parameters
1. Expose main node parameter
2. On other nodes: "Use existing" → select exposed param
3. All nodes now synchronized

### Parameter Organization
- Drag to reorder in Parameters tab
- Group related parameters
- Apply visible_if to related params

### Presets
1. Configure in Preview tab
2. Give name (e.g., "Golden Plain")
3. Click "New" to save
4. Users can switch between presets

### Key Parameters to Expose
- Ornament type (Multi-Switch)
- Emboss intensity (Height Blend offset)
- Fabric color (Color Match)
- Fabric roughness (Histogram Range position)
- Trim enable/disable (Switch)
- Gemstone position/color

---

## Part 21: Export & Reuse (10:56)

**URL**: https://www.youtube.com/watch?v=QEoUSOTcM1Q

**Focus**: Exporting and using materials in other apps

### Method 1: Direct Export
1. Tools → Export Outputs
2. Choose format (PNG, TGA, etc.)
3. Enable **Automatic Export** for live link
4. Changes auto-update exported files

### Method 2: SBSAR Publishing
1. Set graph: Type = Standard Material
2. Subgraph: Exposed in SBSAR = No
3. Package → Publish as SBSAR (Ctrl+P)
4. Update: Ctrl+Shift+P

### Integration Plugins
| Software | Plugin |
|----------|--------|
| Blender | Substance add-on (download) |
| Unreal | Substance 3D for Unreal (Marketplace) |
| Painter/Stager | Built-in Send To menu |

### Painter Anchor Points
- Add anchor in layer below
- Reference from exposed parameters above
- Combines procedural + manual painting

### Key Quote
"Give it a try, play, experiment and stay creative"

---

## Quick Reference Links

| Part | Topic | Duration | URL |
|------|-------|----------|-----|
| Overview | Course Intro | 2:44 | https://www.youtube.com/watch?v=At3FoFcuN6k |
| 1 | What is SD | 2:33 | https://www.youtube.com/watch?v=UyF5Ie-HJ0Q |
| 2 | Making Materials | 4:28 | https://www.youtube.com/watch?v=Wg1gzR3rQeY |
| 3 | Interface | 4:33 | https://www.youtube.com/watch?v=_KlXkHLH5pc |
| 4 | First Project | 11:29 | https://www.youtube.com/watch?v=-DlD476pnxQ |
| 5 | Thread | 19:38 | https://www.youtube.com/watch?v=km-aBsLvG-c |
| 6 | Weaving | 15:48 | https://www.youtube.com/watch?v=N0zw_owXnfE |
| 7 | Shapes | 18:57 | https://www.youtube.com/watch?v=_tLjvmGcEcc |
| 8 | Importing | 8:22 | https://www.youtube.com/watch?v=eGKl3dcSXxE |
| 9 | Embroidery | 9:15 | https://www.youtube.com/watch?v=YCKO5P-pCfE |
| 10 | Custom Shapes | 8:17 | https://www.youtube.com/watch?v=caVvzNg-iRI |
| 11 | Inheritance | 5:38 | https://www.youtube.com/watch?v=CYWOKPRnP5o |
| 12 | Placement | 4:35 | https://www.youtube.com/watch?v=bJUoc8GR18E |
| 13 | Gemstones | 11:34 | https://www.youtube.com/watch?v=QPD_oASJuUM |
| 14 | Mask Extraction | 7:13 | https://www.youtube.com/watch?v=yYHTw4IKyAM |
| 15 | Imperfections | 10:25 | https://www.youtube.com/watch?v=EgvCOGkaN9E |
| 16 | Colors | 17:13 | https://www.youtube.com/watch?v=8S2TTbTuqYk |
| 17 | Roughness/Metal | 12:46 | https://www.youtube.com/watch?v=TWSXb94wH-Q |
| 18 | Displacement | 7:14 | https://www.youtube.com/watch?v=med5kNfGPWk |
| 19 | Parameters | 9:35 | https://www.youtube.com/watch?v=6AVxsMTwKrk |
| 20 | Presets | 14:27 | https://www.youtube.com/watch?v=sDy1xYqTMP8 |
| 21 | Export | 10:56 | https://www.youtube.com/watch?v=QEoUSOTcM1Q |
