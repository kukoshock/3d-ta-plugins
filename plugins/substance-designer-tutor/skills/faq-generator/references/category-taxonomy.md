# Category Taxonomy

Comprehensive taxonomy for categorizing Substance Designer FAQs from a 3D artist perspective.

---

## Overview

This taxonomy focuses on **3D ARTIST concerns** - visual outcomes, node workflows, and creative problem-solving. It explicitly **excludes Technical Artist** topics like scripting, automation, and pipeline code.

**Purpose**: Organize extracted FAQs into logical categories that match how artists think about their problems.

---

## Primary Categories

### 1. Visual Quality

**Focus**: Artifacts, banding, blur, and other visual problems in the output

**Typical Questions**:
- "Why does my normal map have stepping/banding?"
- "Material looks posterized in 3D view"
- "Height map appears blurry/soft"
- "Output has noise/grain artifacts"
- "Gradients show visible bands"

**Key Nodes Involved**:
- Levels, Histogram Range (fixing ranges)
- Blur nodes (reducing artifacts)
- Blend nodes (bit depth inheritance)

**Common Causes**:
- 8-bit vs 16-bit inheritance
- Over-compression
- Insufficient blur/smoothing
- Wrong color space

**Subcategories**:
- Banding & Stepping
- Blur & Softness
- Noise & Grain
- Artifacts & Glitches

---

### 2. Nodes & Parameters

**Focus**: Confusion about specific nodes, parameters not working as expected

**Typical Questions**:
- "Tile Sampler scale map not working"
- "Height Blend edges too soft/hard"
- "Curvature Smooth shows vertical gradient"
- "What does [parameter] actually do?"
- "Fibers node produces no output"

**Key Nodes Involved**:
- Tile Sampler
- Height Blend
- Curvature Smooth
- Gradient Map
- Directional Noise
- Fibers, Shape, Transform

**Common Causes**:
- Wrong input connected
- Inheritance issues
- Parameter range misunderstanding
- Missing prerequisites

**Subcategories**:
- Tile Sampler Issues
- Blend Node Problems
- Generator Node Confusion
- Filter Node Issues
- Transform Problems

---

### 3. Tiling & Seams

**Focus**: Problems with tiling, visible seams, edge artifacts

**Typical Questions**:
- "Visible seams where pattern repeats"
- "Tiling breaks at edges"
- "Pattern doesn't tile smoothly"
- "Offset not working correctly"
- "Elements cut off at boundaries"

**Key Nodes Involved**:
- Tile Generator
- Safe Transform 2D
- Offset nodes
- Make It Tile

**Common Causes**:
- Tiling mode disabled upstream
- Wrong offset values
- Non-tiling transform
- Inheritance issues

**Subcategories**:
- Seam Visibility
- Tiling Mode Issues
- Edge Cutoffs
- Offset Problems

---

### 4. Export & Integration

**Focus**: Materials looking different in game engines, export problems

**Typical Questions**:
- "Material looks different in Unreal Engine"
- "Normal map inverted/flipped in Unity"
- "Colors washed out after export"
- "SBSAR won't load"
- "Parameters missing in external software"

**Key Integration Points**:
- Unreal Engine
- Unity
- Blender
- Substance Painter

**Common Causes**:
- Normal map format (DirectX vs OpenGL)
- Color space mismatch
- Missing output nodes
- Plugin version mismatch

**Subcategories**:
- Normal Map Orientation
- Color Space Issues
- SBSAR Problems
- Plugin Integration
- Live Link Issues

---

### 5. Performance

**Focus**: Slow computation, preview lag, optimization

**Typical Questions**:
- "Graph is extremely slow to compute"
- "Preview not updating/laggy"
- "Displacement makes everything crawl"
- "How to optimize for faster iteration?"

**Key Factors**:
- Resolution (8K vs 2K)
- Tile Sampler density
- Displacement/tessellation
- Complex node chains

**Common Solutions**:
- Reduce resolution during work
- Lower tile counts
- Disable heavy preview outputs
- Simplify graph sections

**Subcategories**:
- Slow Computation
- Preview Lag
- Optimization Strategies
- Resolution Issues

---

### 6. Color & PBR

**Focus**: Color problems, PBR validation, material properties

**Typical Questions**:
- "Colors look washed out"
- "PBR Validate shows red"
- "Metal looks plastic/wrong"
- "Gradient Map has artifacts"
- "Eye dropper samples wrong color"

**Key Concepts**:
- PBR rules (no pure black/white in base color)
- Metallic workflow
- Roughness interpretation
- Color space

**Common Causes**:
- Wrong color values
- Tiling artifacts in Gradient Map
- Incorrect metallic/roughness values
- Color space mismatch

**Subcategories**:
- PBR Compliance
- Metal & Roughness
- Color Accuracy
- Gradient Map Issues

---

### 7. Height & Displacement

**Focus**: Displacement not working, height artifacts, depth issues

**Typical Questions**:
- "No visible displacement despite connection"
- "Spiky/jagged displacement artifacts"
- "Height blend not working correctly"
- "Wrong elements getting displaced"
- "Displacement too blobby/soft"

**Key Concepts**:
- Tessellation requirements
- Displacement scale
- Height map range
- Selective displacement

**Common Causes**:
- Tessellation too low
- Missing blur on displacement
- Wrong height range
- All elements displacing (should be selective)

**Subcategories**:
- No Displacement Visible
- Displacement Artifacts
- Height Blend Issues
- Tessellation Problems

---

### 8. Workflow Basics

**Focus**: Getting started, best practices, fundamental workflows

**Typical Questions**:
- "Where should I start when creating a material?"
- "How to organize complex graphs?"
- "What's the proper workflow order?"
- "Common beginner mistakes?"
- "How to use inheritance effectively?"

**Key Concepts**:
- Height-first workflow
- Left-to-right graph flow
- Inheritance system
- Graph organization (Dot nodes, Frames)
- Preview setup

**Common Mistakes**:
- Starting with color instead of height
- Not understanding inheritance
- Poor graph organization
- Skipping preview setup

**Subcategories**:
- Getting Started
- Graph Organization
- Inheritance Understanding
- Best Practices
- Preview Setup

---

## Exclusions (NOT for This Taxonomy)

These topics are **explicitly excluded** from the FAQ generator scope:

### ❌ Technical Artist Topics

**Scripting & Automation**:
- Python scripting
- Command-line batch processing
- API integration
- Automated pipelines

**Why Excluded**: This tutor serves 3D artists learning material creation, not technical artists building tools.

### ❌ Substance Painter Questions

**Different Tool**:
- Painter-specific workflows
- Painting techniques
- Painter brushes and tools

**Why Excluded**: This tutor covers Substance Designer (procedural node-based), not Substance Painter (hand-painting).

### ❌ Engine-Specific Rendering

**Beyond Material Authoring**:
- Unreal material graph setup (post-import)
- Unity shader code
- Engine-specific rendering features

**Why Excluded**: Focus is on Designer output, not engine implementation. Covers export/integration but not engine-side setup.

### ❌ Advanced Programming

**Outside Artist Scope**:
- Custom node development
- Plugin creation
- SDK usage

**Why Excluded**: Artist-focused, not developer-focused.

---

## Category Assignment Guidelines

### How to Categorize an FAQ

**Step 1: Identify the Core Problem**
- What is the user trying to achieve?
- What went wrong or confused them?

**Step 2: Match to Primary Symptom**
- Is it a visual artifact? → Visual Quality
- Is it a specific node not working? → Nodes & Parameters
- Is it about tiling/seams? → Tiling & Seams
- Is it integration with another tool? → Export & Integration
- Is it about speed/performance? → Performance
- Is it about colors/materials? → Color & PBR
- Is it about height/displacement? → Height & Displacement
- Is it a fundamental workflow question? → Workflow Basics

**Step 3: Check Exclusions**
- Does it involve scripting/automation? → EXCLUDE (not artist-focused)
- Is it about Substance Painter? → EXCLUDE (different tool)
- Is it engine-specific post-import? → EXCLUDE (beyond material authoring)

**Step 4: Assign Subcategory** (if applicable)
- Provides finer granularity for organization

### Edge Cases

**Overlapping Categories**:

Some FAQs might fit multiple categories. Use this priority:

1. If it's primarily a visual artifact → **Visual Quality**
2. If it's about a specific node → **Nodes & Parameters**
3. If it's about integration/export → **Export & Integration**
4. If it's a fundamental misunderstanding → **Workflow Basics**

**Example**: "Curvature Smooth shows vertical gradient"
- Could be Visual Quality (artifact) OR Nodes & Parameters (specific node)
- Assign to: **Nodes & Parameters** (problem is with understanding the node's behavior)
- Cross-reference in Visual Quality if needed

---

## Category Distribution Expectations

Based on typical community questions, expected distribution:

| Category | Expected % | Typical Volume per Forum |
|----------|-----------|--------------------------|
| Nodes & Parameters | 30% | 30-40 posts/year on Reddit |
| Visual Quality | 25% | 25-30 posts/year |
| Export & Integration | 15% | 15-20 posts/year |
| Tiling & Seams | 10% | 10-15 posts/year |
| Workflow Basics | 10% | 10-15 posts/year |
| Height & Displacement | 5% | 5-10 posts/year |
| Color & PBR | 3% | 3-5 posts/year |
| Performance | 2% | 2-5 posts/year |

**Note**: These are estimates based on general community activity. Actual distribution may vary.

---

## Cross-Referencing

### Between Categories

Some solutions span multiple categories. Use "Related" field to cross-reference:

**Example**:
```
FAQ #7 (Visual Quality): Banding in normal map
Related: See FAQ #15 (Nodes & Parameters - Blend inheritance)

FAQ #15 (Nodes & Parameters): Blend node inheritance issues
Related: See FAQ #7 (Visual Quality - Banding artifacts)
```

### With Existing Troubleshooting

Always check `troubleshooting.md` for existing coverage:

```
Related: See troubleshooting.md #7 (Banding/stepping artifacts)
```

If the FAQ is already well-covered in troubleshooting.md, consider:
- Skipping the extraction (duplicate)
- Adding supplementary information if forum post has new insights
- Cross-referencing only

---

## Taxonomy Evolution

This taxonomy may evolve as:
- New Substance Designer features are released
- Community questions shift focus
- New integration points emerge (new game engines, tools)

**Process for Adding New Categories**:
1. Identify emerging pattern (10+ similar questions)
2. Verify it's artist-focused (not TA/scripting)
3. Define category scope and typical questions
4. Update this taxonomy document
5. Recategorize existing FAQs if needed

**Potential Future Categories**:
- AI Integration (if SD adds AI features)
- Real-time Rendering (if real-time preview evolves significantly)
- Mobile/Console (if mobile export becomes common)

---

## Examples by Category

### Visual Quality Example
```
Question: Why does my normal map have stepping?
Symptom: Visible steps or bands in curved surfaces
Root Cause: 8-bit precision insufficient for smooth gradients
Category: Visual Quality → Banding & Stepping
```

### Nodes & Parameters Example
```
Question: Tile Sampler scale map not working
Symptom: Connected noise has no effect on tile sizing
Root Cause: Wrong input or insufficient base scale
Category: Nodes & Parameters → Tile Sampler Issues
```

### Export & Integration Example
```
Question: Material looks different in Unreal Engine
Symptom: Normal map appears inverted
Root Cause: OpenGL vs DirectX normal format mismatch
Category: Export & Integration → Normal Map Orientation
```

### Workflow Basics Example
```
Question: Where should I start when creating a material?
Symptom: Overwhelmed by node options, messy graph
Root Cause: Lack of height-first workflow understanding
Category: Workflow Basics → Getting Started
```

---

## Category Quick Reference

| Category | Icon/Keyword | Typical Fix Type |
|----------|--------------|------------------|
| Visual Quality | 👁️ Artifacts | Bit depth, blur, levels |
| Nodes & Parameters | ⚙️ Settings | Parameter adjustment, connection fix |
| Tiling & Seams | 🔁 Repetition | Tiling mode, offset, safe transform |
| Export & Integration | 🔄 Platform | Format conversion, plugin update |
| Performance | ⚡ Speed | Resolution, optimization |
| Color & PBR | 🎨 Appearance | Color values, PBR rules |
| Height & Displacement | 🏔️ Depth | Tessellation, blur, selective displacement |
| Workflow Basics | 📚 Learning | Process understanding, best practices |
