# FAQ Entry Template

Standard format for extracted FAQ entries. This template ensures consistency and includes all necessary information.

---

## Template Structure

```markdown
### [Number]. [Concise Question - Use Title Case]

**Symptom**: [What the artist sees or experiences - be specific and visual]

**Cause**: [Why this happens - artist-friendly explanation, not overly technical]

**Solution**:
| Step | Action | WHY This Works |
|------|--------|----------------|
| 1 | [Specific action to take] | [Explanation of underlying mechanism] |
| 2 | [Next step if multi-step solution] | [Why this step is necessary] |

**Source**: [Forum Name] - [URL] (Posted: [YYYY-MM], [Engagement metric])

**Related**: [Link to existing troubleshooting.md section if applicable, or "None"]
```

---

## Field Descriptions

### Number
- Sequential numbering within extraction batch
- Or continuation of troubleshooting.md numbering if adding to existing file
- Format: Plain number followed by period (e.g., "1.", "47.")

### Question
- **Concise**: 5-12 words maximum
- **Clear**: User should immediately recognize their problem
- **Use Title Case**: "Why Does My Normal Map Have Stepping?"
- **Avoid jargon**: Prefer "normal map has steps" over "quantization artifacts in tangent space normals"

**Examples**:
- Good: "Why does my normal map have stepping?"
- Good: "Material looks different in Unreal Engine"
- Good: "Tile Sampler scale map not working"
- Bad: "Posterization issues in derivative maps" (too technical)
- Bad: "Help with normal" (too vague)

### Symptom
- **What the artist sees**: Describe the visual problem or error message
- **Be specific**: Not "looks wrong" but "ornaments appear too raised, like bas-relief sculpture"
- **User's perspective**: Describe from artist's viewpoint, not from technical diagnosis
- **1-2 sentences**: Keep it brief but descriptive

**Examples**:
```
Symptom: Visible steps or bands appear in the normal map, making curved surfaces look faceted instead of smooth.

Symptom: Ornaments stick out too much from the base fabric, looking like raised sculpture instead of embroidery.

Symptom: The connected Perlin Noise has no effect on tile sizing - all tiles remain the same size regardless of the scale map input.
```

### Cause
- **Explain WHY**: This is the educational component
- **Artist-friendly language**: Explain technical concepts in visual terms
- **Root cause**: Not just the immediate trigger, but the underlying mechanism
- **1-3 sentences**: Detailed enough to understand, concise enough to digest

**Examples**:
```
Cause: Insufficient color precision due to 8-bit image in the primary input. 8-bit provides only 256 height levels, which creates visible steps when stretched across smooth gradients. The primary input's bit depth propagates downstream through inheritance.

Cause: Raw ornament shapes have too much height range (0-1), making them dominate when blended with the fabric (which might only range 0.3-0.7). Without flattening, the ornament retains full elevation.

Cause: The noise is connected to the wrong input, or the base scale parameter is too low for the scale map multiplication to have visible effect.
```

### Solution Table
- **Step-by-step**: Break complex solutions into discrete actions
- **Action column**: Specific, actionable instruction
- **WHY column**: Educational explanation of mechanism
- **Single-step solutions**: Use one row
- **Multi-step solutions**: Multiple rows in logical order

**Format**:
```
| Step | Action | WHY This Works |
|------|--------|----------------|
| 1 | Set Output Format to Absolute 16-bit | Overrides inheritance, forcing this node and all downstream to use 16-bit (65,536 levels). Provides 256× more precision for smooth gradients. |
```

**Multi-step example**:
```
| Step | Action | WHY This Works |
|------|--------|----------------|
| 1 | Insert Levels node before Height Blend | Allows you to compress the height range of the ornament independently before combining layers. |
| 2 | Set Output High to 0.3-0.5 | Crushes the white values to flatten the height profile. Real embroidery adds minimal physical thickness (fractions of a millimeter) compared to visual impact. |
| 3 | Reduce Height Blend Offset to 0.2-0.3 | Offset controls how much the ornament "rises above" the base. Lower values make it sit closer to the fabric surface. |
```

### Source
- **Forum name**: Full name (not abbreviation)
- **URL**: Direct link to the post/thread
- **Date**: YYYY-MM format (year-month)
- **Engagement metric**: Relevant metric for that forum

**Format Examples**:
```
Source: Reddit r/SubstanceDesigner - https://reddit.com/... (Posted: 2025-08, 847 upvotes, 23 comments)

Source: Adobe Community - https://community.adobe.com/... (Posted: 2025-11, 1247 views, Accepted Solution)

Source: Polycount - https://polycount.com/... (Posted: 2024-06, 18 replies)
```

### Related
- **Link to troubleshooting.md section**: If similar issue already covered
- **Cross-reference**: Use markdown anchor links
- **"None"**: If no related entries exist

**Examples**:
```
Related: See troubleshooting.md #7 (Banding/stepping artifacts)

Related: troubleshooting.md #33 (Tile Sampler Scale map not working)

Related: None
```

---

## Complete Examples

### Example 1: Visual Quality Issue

```markdown
### 1. Why Does My Normal Map Have Stepping?

**Symptom**: Visible steps or bands appear in the normal map, making curved surfaces look faceted like low-poly geometry instead of smooth.

**Cause**: Insufficient color precision due to 8-bit image in the primary input. 8-bit provides only 256 height levels, which creates visible "steps" when stretched across smooth gradients. The primary input's bit depth propagates downstream through inheritance - if your primary input is 8-bit, all connected nodes inherit that limitation.

**Solution**:
| Step | Action | WHY This Works |
|------|--------|----------------|
| 1 | Swap Blend inputs using X key | Blend nodes inherit from their PRIMARY input (dark dot). Swapping makes the 16-bit input primary, so downstream nodes inherit 16-bit precision instead of 8-bit. |
| 2 | Alternative: Set Output Format to Absolute 16-bit | Overrides inheritance entirely, forcing this node and all downstream to use 16-bit (65,536 levels). This provides 256× more precision for smooth gradients without banding. |

**Source**: Reddit r/SubstanceDesigner - https://reddit.com/r/SubstanceDesigner/comments/xyz (Posted: 2025-08, 847 upvotes, 23 comments)

**Related**: See troubleshooting.md #7 (Banding/stepping artifacts)
```

### Example 2: Node Parameter Issue

```markdown
### 2. Tile Sampler Scale Map Not Working

**Symptom**: The connected Perlin Noise has no effect on tile sizing - all tiles remain the same size regardless of the scale map input.

**Cause**: The noise is connected to the wrong input (pattern input instead of scale map input), or the base scale parameter is too low for the scale map multiplication to have visible effect. Scale Map works multiplicatively - it multiplies the base scale value, so a base of 0.1 produces tiny results even with maximum map values.

**Solution**:
| Step | Action | WHY This Works |
|------|--------|----------------|
| 1 | Verify connection is to "Scale Map" input slot | The main pattern input just provides the shape to tile. Scale Map is a separate input that multiplies the base scale parameter to create size variation. |
| 2 | Check noise preview shows gray values (not pure black) | Black (value 0) in scale map = zero size (invisible tiles). If noise is mostly black, most tiles will be tiny or invisible. Invert if needed. |
| 3 | Increase base Scale parameter to 3.0+ | Scale Map multiplies this base value. Need a reasonable base for multiplication to have visible effect. |

**Source**: Reddit r/SubstanceDesigner - https://reddit.com/r/SubstanceDesigner/comments/abc (Posted: 2025-09, 134 upvotes, 11 comments)

**Related**: See troubleshooting.md #33 (Tile Sampler Scale map not working)
```

### Example 3: Integration Issue

```markdown
### 3. Material Looks Different in Unreal Engine

**Symptom**: Material that looks correct in Substance Designer appears wrong in Unreal - surfaces are inverted, lighting is incorrect, or details face the wrong direction.

**Cause**: Normal map format mismatch. Substance Designer uses OpenGL format (Y-up, green channel points up) while Unreal Engine uses DirectX format (Y-down, green channel points down). The different coordinate systems cause normals to point in opposite directions, inverting the perceived surface detail.

**Solution**:
| Step | Action | WHY This Works |
|------|--------|----------------|
| 1 | In Substance Designer, add "Normal Convert" node before export | Converts from OpenGL to DirectX format by inverting the green channel. This flips the Y-axis to match Unreal's coordinate system. |
| 2 | Alternative: In Unreal, enable "Flip Green Channel" in texture import settings | Achieves the same conversion on import. Both methods work - choose based on workflow preference. |

**Source**: Adobe Community - https://community.adobe.com/t5/substance-3d-designer/... (Posted: 2025-10, 1523 views, Accepted Solution)

**Related**: See troubleshooting.md #29 (Material looks different in external software)
```

### Example 4: Workflow/Beginner Issue

```markdown
### 4. Where Should I Start When Creating a Material?

**Symptom**: Overwhelmed by node options and unsure what order to build material components in. Graph becomes messy and difficult to manage.

**Cause**: Substance Designer's node-based workflow requires a different thinking approach than layer-based tools. Without understanding the height-first workflow and graph flow direction, beginners often work inefficiently or create disconnected elements.

**Solution**:
| Step | Action | WHY This Works |
|------|--------|----------------|
| 1 | Always start with the height map | Height is the backbone - it drives normal, AO, masks, roughness, and color. Building height first ensures all other maps derive from a consistent 3D structure. |
| 2 | Build grayscale information methodically: macro → medium → micro details | This mirrors how real materials are structured - large shapes first, then medium details, then surface texture. Prevents getting lost in details before establishing the base. |
| 3 | Add Base Material node early for preview | Immediate visual feedback in 3D view. Connect Normal and AO outputs (not Height initially - it's computationally heavy). This lets you see results as you work. |
| 4 | Use Dot nodes and Frames to organize graph | Pin connections with Dot nodes (Alt+click), group related nodes in Frames. Keeps graph readable as it grows. Good organization prevents mistakes and makes troubleshooting easier. |

**Source**: Reddit r/SubstanceDesigner - https://reddit.com/r/SubstanceDesigner/comments/def (Posted: 2025-07, 234 upvotes, 15 comments)

**Related**: See SKILL.md "Height-First Workflow" section
```

---

## WHY Explanation Guidelines

The "WHY This Works" column is critical for education. Follow these principles:

### Explain the Mechanism
- Not just "this fixes it" - explain HOW and WHY
- Connect to underlying technical concepts in accessible language
- Help user build mental models

**Examples**:

❌ Bad: "This fixes the banding"

✅ Good: "Provides 256× more precision (65,536 levels vs 256), enough that human eyes can't distinguish individual steps in gradients"

### Use Visual Analogies
- Compare to real-world equivalents when possible
- Help 3D artists connect technical concepts to physical materials

**Examples**:

✅ "Real embroidery adds minimal physical thickness (fractions of a millimeter) compared to visual impact. Flattening mimics that subtle elevation."

✅ "This mimics how real embroidery threads enter and exit the fabric surface - tapered transitions, not cookie-cutter edges."

### Show the Contrast
- Explain what happens WITHOUT the solution
- Makes the reason for the solution clearer

**Examples**:

✅ "Without tiling, pixels at the edge have no valid neighbors on one side, creating false edge detection. Tiling wraps the image so every pixel has valid neighbors in all directions."

✅ "If you used the Mask Input instead, you'd get hard cookie-cutter cutouts with no transition."

---

## Category Tags

Include category tag in extraction for organization:

```markdown
### 47. [Question]
**Category**: Visual Quality

**Symptom**: ...
```

**Valid Categories** (from category-taxonomy.md):
1. Visual Quality
2. Nodes & Parameters
3. Tiling & Seams
4. Export & Integration
5. Performance
6. Color & PBR
7. Height & Displacement
8. Workflow Basics

---

## Validation Checklist

Before finalizing an FAQ entry:

- [ ] Question is concise and clear (5-12 words)
- [ ] Symptom describes what user experiences (not diagnosis)
- [ ] Cause explains WHY the problem occurs
- [ ] Solution steps are specific and actionable
- [ ] WHY explanations are educational and accessible
- [ ] Source includes URL, date, engagement metrics
- [ ] Related field checked against troubleshooting.md
- [ ] Category assigned correctly
- [ ] Markdown table formatting correct (pipes aligned)
- [ ] No artist-inappropriate content (scripting/automation)
