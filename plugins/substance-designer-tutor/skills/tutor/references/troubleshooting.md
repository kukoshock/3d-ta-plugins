# Troubleshooting Guide

Comprehensive problem/solution reference for Substance Designer (40+ scenarios).

---

## Quick Reference: Top 10 Most Common Issues

| # | Issue | Quick Fix | Full Details |
|---|-------|-----------|--------------|
| 1 | Normal map banding/stepping | Set Output Format to Absolute 16-bit | Scenario #7 |
| 2 | Material different in Unreal | Convert normals to DirectX format | Scenario #29 |
| 3 | Tile Sampler scale map ignored | Connect to Scale Map input (not Pattern Input) | Scenario #33 |
| 4 | Curvature vertical gradient | Fix upstream tiling setting | Scenario #9 |
| 5 | Ornaments too uniform | Add rotation_random (0.02-0.1) | Scenario #1 |
| 6 | Graph extremely slow | Reduce resolution to 2K during editing | Scenario #12 |
| 7 | No visible displacement | Increase tessellation to 50+ in 3D view | Scenario #22 |
| 8 | PBR Validate shows red | Avoid pure black (<30) or pure white (>240) | Scenario #17 |
| 9 | Height Blend edges mushy | Increase contrast to 0.96 | Scenario #34 |
| 10 | Ornaments too prominent | Add Levels node, set Output High to 0.3-0.5 | Scenario #2 |

---

## Pattern & Distribution Issues

### 1. Ornaments look too uniform/regular

**Symptom**: All ornaments appear identical, pattern looks artificial

**Problem**: The pattern looks computer-generated rather than hand-crafted.

**Causes & Solutions**:
| Cause | Solution | WHY This Works |
|-------|----------|----------------|
| No randomization | Increase `rotation_random` (0.02-0.1) | Each ornament rotates slightly differently, mimicking how embroidery threads don't align perfectly when hand-sewn |
| Static scale | Add `scale_random` (0.1-0.3) | Natural materials have variation - no two threads are exactly the same thickness |
| Fixed positions | Increase `position_random` (0.01-0.05) | Breaks the rigid grid alignment; real embroidery has slight placement irregularities from fabric tension |
| Uniform sizing | Connect **Perlin Noise** to Tile Sampler's Scale input | Creates organic size variation across the surface - larger ornaments in some areas, smaller in others, like natural material density variation |

**WHY Random Variation Matters**: Human eyes are incredibly good at detecting artificial patterns. Even 2% rotation variation is enough to break the "machine-made" look. The key is subtle randomness - too much (> 20%) creates chaos, too little (< 1%) still looks CG.

### 2. Ornaments too prominent/embossed

**Symptom**: Ornaments stick out too much from the base fabric, looking like bas-relief instead of embroidery

**Problem**: Raw ornament shapes have too much height range, making them appear sculpted rather than sewn.

**Solutions**:
| Solution | How | WHY This Works |
|----------|-----|----------------|
| Add **Levels** before Height Blend | Insert Levels node, set Output High = 0.3-0.5 | Crushes the white values to flatten the height profile. Real embroidery adds minimal physical thickness (fractions of a millimeter) compared to its visual impact. This flattening mimics that subtle elevation. |
| Reduce Height Blend Offset slider | Lower from 0.5 to 0.2-0.3 | Offset controls how much the ornament "rises above" the base. Lower values make it sit closer to the fabric surface, like threads lying flat rather than standing up. |
| Decrease Height Blend Contrast | Lower from 0.96 to 0.7-0.8 | Softens the transition edges, making the ornament blend more gradually. Use this if you want a more integrated, less "applied" look. |

**WHY Flatten First**: Without Levels, the ornament retains its full 0-1 height range. When Height Blend combines this with the fabric (which might only range 0.3-0.7), the ornament dominates excessively. Flattening to 0.3-0.5 puts both layers in the same height "ballpark" for realistic blending.

### 3. Pattern too regular/grid-like

**Symptom**: Distribution looks like obvious grid

**Solutions**:
| Solution | How | WHY This Works |
|----------|-----|----------------|
| Change Pattern mode to brick | Set Pattern parameter to 2 | Brick mode offsets alternating rows by 50%, breaking the vertical alignment. Human eyes easily detect perfect grid alignment - even slight offsets make patterns feel more natural |
| Increase Position Random | Set position_random to 0.1-0.3 | Adds jitter to each tile's X/Y position, breaking rigid grid. Natural materials don't align to mathematical grids - this mimics real-world irregularity |
| Use Offset slider | Adjust Offset parameter (0.25-0.5) | Shifts entire rows/columns relative to each other. Works with brick mode to create staggered patterns |
| Add Warp node | Insert Warp with Perlin Noise (intensity 0.05-0.1) | Creates organic, flowing distortion across the entire pattern. Like fabric warping under tension - breaks grid without destroying the underlying structure |

**WHY Grid Patterns Look Artificial**: The human visual system evolved to detect patterns in nature, which are rarely perfectly regular. Even a 5% position variance is enough to break the "computer-generated" appearance. The key is subtle variation - too much randomness creates chaos, too little still looks CG.

### 4. Tiled elements don't connect smoothly

**Symptom**: Visible seams where repeated elements meet

**Solutions**:
| Solution | How | WHY This Works |
|----------|-----|----------------|
| Offset by 0.5 on tiling axis | Use Transform 2D, set Offset X or Y to 0.5 | Moves the element exactly half a tile width. When tiled, the right edge of one tile meets the left edge of the offset tile, creating continuity. 0.5 is exactly half because UV space goes 0-1 |
| Blend with original using Max | Add Blend node, mode = Max Lighten | Max takes the brightest pixel from both inputs. Where original and offset overlap, you get the combined result. Creates the "bridge" between tiles without dark seams |
| Set tiling correctly | Enable only Horizontal OR Vertical tiling as needed | If tiling both axes when you only need one, you get unwanted repetition. Vertical-only tiling creates horizontal stripes/threads. Horizontal-only creates vertical elements |

**WHY 0.5 Offset Works**: In UV space (0-1 range), 0.5 is exactly half. When you offset by 0.5 and enable tiling, the element wraps around - what exits the right edge at 1.0 re-enters at 0.0, perfectly aligned with the offset version at 0.5. This creates seamless connections for continuous patterns like threads or chains.

**Common Pattern**: This technique is essential for creating continuous horizontal/vertical elements like warp threads in weaving, where threads must connect edge-to-edge infinitely.

### 5. Elements cut off at edges

**Symptom**: Shapes get clipped at tile boundaries

**Solutions**:
| Solution | How | WHY This Works |
|----------|-----|----------------|
| Use Safe Transform 2D | Replace Transform 2D with Safe Transform 2D node | Safe Transform samples beyond the 0-1 UV boundary when tiling is enabled, pulling in the wrapped content. Regular Transform treats out-of-bounds as black/empty, causing hard cutoffs |
| Enable tiling mode | Set Tiling to Horizontal/Vertical/Both as needed | Without tiling, there's no "wrap-around" data to sample. The node can't pull content from the opposite edge if wrapping isn't enabled |
| Reduce element scale | Lower scale parameter to fit within tile | If an element is larger than the tile itself, even Safe Transform can't help - there's simply not enough space. Scale down so the element plus offset fits in 0-1 range |

**WHY Safe Transform Exists**: Regular Transform 2D is optimized for speed - it doesn't look beyond the 0-1 UV boundary. This is fine for non-tiling content. But when you offset or scale tiling content, you often need to sample "around the corner" where the texture wraps. Safe Transform specifically handles this edge-wrapping case by sampling the tiled repetition.

**When to Use Each**:
- **Transform 2D**: Non-tiling content, or when you're certain content stays within bounds (faster)
- **Safe Transform 2D**: Tiling content with offsets/scaling (slightly slower, handles edge wrapping)

### 6. Ornaments too sparse or too dense

**Symptom**: Large gaps or excessive overlapping

**Solutions**:
| Issue | Fix |
|-------|-----|
| Too sparse | Increase x_amount and y_amount (600-800) |
| Too dense | Decrease x_amount and y_amount (200-400) |
| Wrong scale | Adjust scale parameter (1.5-5.0) |

---

## Inheritance & Base Parameter Issues

### 7. Banding/stepping artifacts

**Symptom**: Visible steps in gradients, like posterization - smooth gradients appear as distinct bands

**Problem**: Insufficient color/height precision causing quantization artifacts.

**Causes & Solutions**:
| Cause | Solution | WHY This Works |
|-------|----------|----------------|
| 8-bit primary input | Swap Blend inputs (X key) | Blend nodes inherit from their PRIMARY input (dark dot). Swapping makes the 16-bit input primary, so downstream nodes inherit 16-bit precision. 8-bit has only 256 levels - not enough for smooth height gradients. |
| 8-bit propagation | Set Output Format to Absolute 16-bit | Overrides inheritance, forcing this node and all downstream to use 16-bit (65,536 levels). This provides 256× more precision for smooth gradients. |
| Low bit depth source | Check source image bit depth | If the original imported image is 8-bit, it can't create more detail. Re-export source at 16-bit or use procedural generation. |

**From Course**: "If your primary input has 8-bit depth, that propagates downstream"

**WHY This Happens**: Height maps need smooth gradients for realistic normal map generation. 8-bit only has 256 discrete values. When you stretch this across a gradient (like a curved surface), each of those 256 levels becomes a visible "step." 16-bit provides 65,536 levels - enough that human eyes can't distinguish individual steps. The banding you see is literally the mathematical resolution limit of 8-bit data.

**Quick Test**: If you see banding, temporarily set the node to Absolute 16-bit. If banding disappears, you've confirmed it's a bit depth issue.

### 8. Wrong resolution downstream

**Symptom**: Output appears wrong size or blurry

**Solutions**:
| Solution | How | WHY This Works |
|----------|-----|----------------|
| Check primary input resolution | Preview the primary input node (dark connection dot) | Resolution inherits from the primary input automatically. If primary is 512px, all downstream defaults to 512px. Find where low resolution originates |
| Set Output Size to Absolute | Change Output Size from "Relative to Parent" to Absolute, select resolution (2K, 4K, etc.) | Breaks inheritance chain and forces this specific node to a fixed resolution regardless of inputs. All downstream nodes inherit this new resolution |
| Verify parent graph resolution | Check the graph properties (right-click graph background) | If working in a subgraph, the parent graph's resolution setting can override. Subgraph set to "Parent Resolution" inherits from the main graph |

**WHY Resolution Inheritance Matters**: Substance Designer uses inheritance to keep graphs resolution-independent. One node can adapt to different output sizes automatically. But this means a single low-resolution node early in the chain can contaminate everything downstream. It's like a low-quality photocopy - making copies of copies never increases quality.

**The Primary Input Rule**: Nodes inherit from their PRIMARY input (the connection with the dark dot). If you have two inputs - one at 4K and one at 512px - whichever is primary determines the resolution. Swapping inputs (X key) can fix this if the higher-res input should be primary.

**Common Cause**: Imported bitmap images at low resolution. If you import a 512px reference image and connect it as primary input, everything inherits 512px resolution even if your graph settings are 4K.

### 9. Vertical gradient in Curvature Smooth

**Symptom**: Curvature map shows gradient bands instead of proper edge detection - looks like a vertical fade

**Problem**: Tiling disabled upstream causes Curvature Smooth to see edge artifacts.

**Cause**: Tiling disabled somewhere upstream in the inheritance chain.

**Solutions**:
| Solution | How | WHY This Works |
|----------|-----|----------------|
| Find node with tiling disabled | Trace upstream from Curvature, check each node's tiling setting | Tiling setting propagates through inheritance just like resolution. One node with "No Tiling" contaminates all downstream nodes unless they override. |
| Swap Blend inputs if commutative | Press X key on Blend node | If blending two inputs where order doesn't matter (Max, Min, Add), swapping makes the tiled input primary, so tiling propagates downstream. |
| Set Curvature Smooth to Absolute full tiling | In Curvature node, set Tiling to Absolute, enable horizontal and vertical | Breaks the inheritance chain and forces this node to tile regardless of upstream settings. |

**From Course**: "Make sure your node is set to full tiling"

**WHY This Creates a Gradient**: When tiling is disabled, Substance Designer treats the edges as "undefined" or "empty." Curvature Smooth tries to detect edges/cavities, but at the non-tiled boundary, it sees a sudden transition from "content" to "nothing," which it interprets as a massive edge running along the entire border. This creates the characteristic vertical or horizontal gradient artifact.

**The Real Issue**: Curvature relies on analyzing neighboring pixels to detect edges. Without tiling, pixels at the edge have no valid neighbors on one side, creating false edge detection. Tiling wraps the image so every pixel has valid neighbors in all directions.

### 10. Tiling breaks unexpectedly

**Symptom**: Material that should tile has seams

**Solutions**:
| Solution | How | WHY This Works |
|----------|-----|----------------|
| Check inheritance chain | Trace backwards from seam location, preview each node to find where tiling breaks | Tiling propagates through inheritance like resolution and bit depth. One node with tiling disabled contaminates all downstream nodes |
| Find Transform 2D culprit | Look for Transform 2D nodes - they often have partial tiling disabled by default | Transform 2D defaults can disable tiling on specific axes. If you offset on X-axis with Horizontal tiling off, you create a seam. Common mistake when copying nodes |
| Set to Absolute full tiling | Change Tiling Mode to Absolute, enable both H and V checkboxes | Breaks the inheritance chain and forces this node to tile regardless of upstream settings. All downstream nodes then inherit correct tiling |

**WHY Transform 2D is the Common Culprit**: Transform 2D has separate tiling controls for Horizontal and Vertical. It's easy to accidentally disable one axis while working. For example, if you're offsetting horizontally and forget to enable Horizontal tiling, the content doesn't wrap around - it just clips, creating a vertical seam.

**The Inheritance Contamination**: Like a broken link in a chain, one node with "No Tiling" breaks tiling for everything downstream unless explicitly overridden. This is especially insidious because the seam might not appear until several nodes later, making it hard to trace back to the source.

**Quick Test**: If you see unexpected seams, set the suspected node to Absolute with full tiling. If seams disappear, you've found the culprit - now trace upstream to find the root cause.

### 11. Node ignores parameter changes

**Symptom**: Adjusting sliders has no effect

**Solutions**:
| Solution | How | WHY This Works |
|----------|-----|----------------|
| Check if parameter is exposed | Look for blue highlighting on parameter name or value | Exposed parameters are controlled by the parent graph or external input. When you move the slider locally, it's immediately overridden by the exposed value. Blue = "locked from above" |
| Right-click → Recompute | Right-click the node, select Recompute | Forces Designer to recalculate from scratch. Sometimes the node cache gets stale or computation is deferred for performance. Recompute clears the cache and triggers immediate recalculation |
| Check connection inputs | See if a connection is driving this parameter | Some parameters can be controlled by input connections (like Scale Map). If there's a connection, it overrides the manual slider. Disconnect to test manual control |

**WHY Exposed Parameters Lock Values**: When a parameter is exposed to the parent graph (for use in SBSAR or subgraph), the parent becomes the "source of truth." Your local slider adjustment is recorded, but instantly overwritten by the parent's value. This is intentional - it allows centralized control, but can be confusing when you forget the parameter is exposed.

**How to Fix**: Right-click the parameter → "Un-expose" to break the external connection and regain local control. Or adjust the value at the parent graph level where the exposure is connected.

**Cache vs Computation**: Substance Designer aggressively caches results to maintain performance. Sometimes this cache doesn't invalidate when you'd expect. The "Recompute" command bypasses all caching and forces fresh calculation - it's like "Refresh" in a browser.

---

## Performance Issues

### 12. Graph is extremely slow

**Symptom**: Every change takes forever to compute

**Solutions**:
| Action | Impact |
|--------|--------|
| Reduce resolution | 8K → 2K dramatically faster |
| Lower Tile Sampler amounts | 800 → 200 threads |
| Disable Height preview | Height is "a heavy process" |
| Simplify complex chains | Temporarily disconnect downstream |
| Work at 2K, finalize at 4K | Resolution-independent workflow |

### 13. Preview not updating

**Symptom**: Changes don't appear in 2D/3D view

**Solutions**:
1. Right-click node → Recompute
2. Modify any parameter slightly (forces recalc)
3. Check connection (may have disconnected)
4. Verify node is actually connected to output chain

### 14. 3D preview is choppy/laggy

**Symptom**: 3D view stutters when rotating

**Solutions**:
- Reduce preview resolution
- Disable displacement (heavy)
- Switch from Iray to OpenGL renderer
- Close other heavy applications

### 15. Displacement extremely slow

**Symptom**: Adding displacement makes graph crawl

**Solutions**:
- Reduce tessellation (50 → 20)
- Only displace necessary elements
- Create separate, simplified displacement map
- Work without displacement, enable at end

---

## Color & Material Issues

### 16. Gradient Map shows vertical artifacts

**Symptom**: Color output has banding or gradient problems

**Cause**: Same as #9 - tiling inheritance

**Solutions**:
- Fix upstream tiling issues
- Set Curvature Smooth to Absolute
- Swap Blend inputs if applicable

### 17. PBR Validate shows red

**Symptom**: PBR Validate node outputs red areas

**Meaning**: Values too dark or too bright for PBR

**Solutions**:
- Adjust Levels to avoid pure black (< 30 sRGB)
- Adjust to avoid pure white (> 240 sRGB)
- Use reference color charts for metals
- "A little red is okay, but overall keep green"

### 18. Metal looks wrong/plastic

**Symptom**: Metallic areas don't look like real metal

**Solutions**:
| Issue | Fix |
|-------|-----|
| Wrong base color | Use accurate metal color values (charts) |
| Metallic too low | Set metallic mask to pure white for metal |
| Roughness too high | Lower roughness for shiny metal |
| Missing reflections | Check environment/HDRI |

### 19. Colors look washed out

**Symptom**: Base color appears desaturated

**Solutions**:
- Check color space settings on export
- Verify gamma (sRGB vs Linear)
- Increase saturation in HSL node
- Check Blend mode (Multiply can darken excessively)

### 20. Eye dropper samples wrong color

**Symptom**: Sampled color doesn't match reference

**Solutions**:
- Sample from neutral area (not too light/dark)
- Avoid sampling from shadowed areas
- Reference image may be in wrong color space
- Sample multiple times, average manually

### 21. Color doesn't match reference at all

**Symptom**: Fabric color completely different from expectation

**Solutions**:
- Gradient Map: Adjust keys and interpolation
- Check Blend opacity (may be too low)
- Verify mask distribution is correct
- Sample from multiple reference areas

---

## Displacement Issues

### 22. No visible displacement

**Symptom**: Height map connected but surface is flat

**Cause**: Tessellation too low or disabled

**Solutions**:
1. Increase tessellation in material settings (e.g., 50)
2. Increase displacement scale
3. Verify height map is connected
4. Check if displacement is enabled in Base Material

**From Course**: "That's one very common mistake that beginners do often"

### 23. Spiky/jagged displacement artifacts

**Symptom**: Surface has sharp spikes or noise

**Solutions**:
| Issue | Fix |
|-------|-----|
| Hard edges in height | **Blur** displacement input (0.2) |
| Too much detail | Create simplified displacement map |
| Tessellation too low | Increase, but watch performance |

### 24. Displacement too blobby

**Symptom**: Fine details lost, everything smoothed out

**Solutions**:
- Reduce blur amount
- Add sharp elements separately after blur
- Use Levels to increase contrast
- Blend blurred with sharp at appropriate ratio

### 25. Wrong elements getting displaced

**Symptom**: Weave threads displace when only trim should

**From Course**: "Even the threads are getting displaced which is way too much"

**Solution**:
- Create separate displacement map from masks
- Only include elements that "should really stick out"
- Use mask to isolate trim/gemstones

### 26. Displacement creates silhouette gaps

**Symptom**: Visible holes at extreme displacement angles

**Solutions**:
- Reduce displacement scale
- Increase tessellation further
- Blur edges of displacement map

---

## Export & Integration Issues

### 27. SBSAR won't load in other software

**Symptom**: Material fails to load or shows errors

**Solutions**:
| Issue | Fix |
|-------|-----|
| Old plugin | Update Substance integration to latest |
| Engine version | Check material uses compatible nodes |
| Corrupt file | Re-publish SBSAR |

**From Course**: "Make sure you use the latest version of these plugins"

### 28. Automatic export not updating

**Symptom**: Changes in Designer don't appear in exported files

**Solutions**:
1. Re-enable Automatic Export in Export Outputs dialog
2. Verify export path still exists
3. Check file permissions
4. Manual export, then re-enable auto

### 29. Material looks different in external software

**Symptom**: Material in Blender/Unreal doesn't match Designer - lighting appears inverted, colors look wrong, or details face the wrong direction

**Problem**: Multiple export and interpretation differences between Substance Designer and game engines.

**Causes & Solutions**:
| Cause | Solution | WHY This Works |
|-------|----------|----------------|
| Normal map format mismatch | Add "Normal Convert" node before output, or flip green channel on import | Unreal uses DirectX (Y-down), Blender/Maya use OpenGL (Y-up). Green channel is inverted between them - same data, opposite interpretation |
| Color space incorrect | Export Base Color as sRGB, data maps (Normal/Roughness/Metallic) as Linear | sRGB applies gamma curve for perceptual brightness (display colors). Linear has no gamma - required for data maps that represent physical values |
| Roughness interpretation | Invert roughness map if engine uses "Smoothness" | Some engines (Unity Standard) use Smoothness (inverted). White = smooth in Smoothness, White = rough in Roughness |
| Lighting environment differs | Compare under neutral HDRI or match lighting | Different HDRIs create drastically different reflections - test with similar environment before debugging material |

**WHY DirectX vs OpenGL Matters**:
Both are valid conventions - neither is "wrong." The difference:
- **DirectX**: Green channel positive = surface curves DOWN (used by Unreal, DirectX)
- **OpenGL**: Green channel positive = surface curves UP (used by Blender, Maya, OpenGL)

When you use the wrong format, all your bumps become dents and vice versa - like reading a topographic map upside-down where hills become valleys.

**Quick Engine Reference**:
| Engine | Normal Format | Notes |
|--------|---------------|-------|
| Unreal Engine | DirectX | Default for Substance |
| Unity | OpenGL (or DirectX option) | Check import settings |
| Blender | OpenGL | Cycles and Eevee both expect OpenGL |
| Maya | OpenGL | Arnold expects OpenGL |

**WHY sRGB vs Linear Matters**:
- **Base Color/Albedo**: sRGB - represents what the eye sees, needs gamma curve for correct display
- **Normal/Roughness/Metallic/Height**: Linear - represent physical data values, gamma would corrupt the math

If you export Normal maps as sRGB, the gamma curve distorts the vector values, causing incorrect lighting calculation.

**From Course**: "Make sure you use the latest version of these plugins as our material uses nodes that rely on designer's latest engine"

**Related**: See scenario #17 (PBR Validate shows red) for color range issues

### 30. Missing maps in export

**Symptom**: Some output maps not exported

**Solutions**:
- Check all outputs are enabled in Export dialog
- Verify Output nodes exist for each map
- Check Output node Usage settings

### 31. Parameters not showing in SBSAR

**Symptom**: Exposed parameters missing in external software

**Solutions**:
- Verify parameters are exposed (blue highlight in graph)
- Check graph is set: Exposed in SBSAR = Yes
- Subgraph should be: Exposed in SBSAR = No
- Re-publish SBSAR after changes

### 32. Live link not working with Blender/Unreal

**Symptom**: Changes in Designer don't reflect in external app

**Solutions**:
- Verify Automatic Export is enabled
- Check export path matches import path
- Blender: Use "Refresh Textures" operator
- Unreal: Reimport assets

---

## Node-Specific Issues

### 33. Tile Sampler Scale map not working

**Symptom**: Connected noise has no effect on sizing - all tiles remain the same size

**Problem**: Incorrect connection or parameter settings preventing the scale map from functioning.

**Solutions**:
| Solution | Check | WHY This Works |
|----------|-------|----------------|
| Verify connection is to Scale Map input (not main input) | Look for the specific "Scale Map" input slot, not the pattern input | Scale Map is a dedicated input that multiplies the base scale parameter. Main pattern input just provides the shape to tile. They're completely different functions. |
| Check noise range (should be 0-1 grayscale) | Preview the noise - should show gray values, not pure black | Black (0) in scale map = zero size (invisible tiles). If your noise is all black, tiles disappear. If it's inverted (mostly black), most tiles are tiny or invisible. |
| Increase Scale Random to see effect | Temporarily crank scale_random to 0.5+ | Scale Map works multiplicatively with randomness. If random is 0, all tiles in a given noise region are identical size. Random adds variation ON TOP of the map values. |
| Verify Scale parameter isn't at minimum | Base scale should be 2.0+ | Scale Map multiplies the base scale value. If base scale is 0.1, even maximum map values produce tiny tiles. Need a reasonable base for multiplication. |

**WHY Scale Map is Powerful**: The Scale Map creates spatial variation - larger tiles in some areas, smaller in others - based on a grayscale map. This is fundamentally different from scale_random which just adds chaos. Scale Map creates intentional, controlled size gradients across the surface.

**Critical Technique - Ornament Masking**: When you connect an ornament mask to Scale Map, black areas (value 0) multiply scale by zero, making tiles disappear. But the gradient edges of the mask create a GRADUAL size reduction, making threads appear to "dive into" the fabric with tapered transitions. This is the key to realistic embroidery edges. If you used the Mask Input instead, you'd get hard cookie-cutter cutouts.

**Debugging Checklist**:
1. Is Scale Map input connected? (not pattern input)
2. Is the connected map grayscale with variation? (not solid black/white)
3. Is base scale parameter large enough? (3.0+)
4. Does the map have tiling enabled? (if it's non-tiled, edges go black)

### 34. Height Blend edges too soft

**Symptom**: Ornaments blend too gradually into fabric, looking mushy or unclear

**Problem**: Low contrast creates overly soft transitions that don't match the physical reality of sewn-on elements.

**Solution**: Increase Contrast slider (0.96 = very crisp)

**WHY This Works**: Real embroidery threads are physically on top of the fabric with distinct boundaries. Low contrast (< 0.7) creates a gradual fade that suggests the ornament is melting into the fabric or painted on rather than sewn. High contrast (0.9-1.0) creates the sharp edge separation that matches how physical layers actually interact. The 0.96 value is near-maximum but avoids the potential for aliasing artifacts at exactly 1.0.

**When Soft Edges ARE Correct**: Use lower contrast (0.3-0.6) only when simulating weathered/eroded surfaces, painted details, or materials that genuinely blend together (like melted wax or corroded metal).

### 35. Height Blend edges too hard

**Symptom**: Ornaments have harsh, pixelated, or aliased edges that look digitally cut out

**Problem**: Excessive contrast or sharp input creates aliasing artifacts.

**Solutions**:
| Solution | How | WHY This Works |
|----------|-----|----------------|
| Decrease Contrast slider | Lower from 1.0 to 0.92-0.96 | Slight reduction smooths the blend algorithm without losing edge definition. Even real physical edges have microscopic softness. |
| **Blur** the foreground input slightly | Add Blur HQ (0.1-0.2) before Height Blend | Creates anti-aliasing on the ornament edges. Removes pixel-level jaggedness that causes harsh transitions. Very slight blur is invisible to the eye but eliminates aliasing. |
| Adjust Offset slider | Increase or decrease from 0.5 | Changes the height relationship. Sometimes harsh edges are from extreme height differences. Offset adjustment can help find the sweet spot. |

**WHY This Happens**: At exactly 1.0 contrast, Height Blend uses a very aggressive binary decision - each pixel is EITHER foreground OR background with minimal transition. Combined with pixelated input edges, this creates stair-stepping. The slight blur or contrast reduction introduces just enough gradient to allow smooth anti-aliasing while maintaining crisp appearance.

**The Balance**: You want edges crisp enough to look sewn-on (not painted), but soft enough to avoid digital artifacts. Sweet spot is usually 0.92-0.96 contrast with very slight blur (0.1) on the input.

### 36. Spline shape not smooth

**Symptom**: Curve appears angular/faceted

**Solution**: Increase Segment Amount (8 → 32)

### 37. Shape Mapper creates weird distortion

**Symptom**: Element bends incorrectly

**Solutions**:
- Adjust Amount parameter (1 = single bend)
- Check input orientation
- Adjust Radius

### 38. Normal map too strong

**Symptom**: Surface looks bumpy/noisy, especially in ray tracing

**Solutions**:
- Reduce Normal node Intensity (6 → 2)
- **From Course**: "The normal is too strong" causing "wet look" or noise

### 39. Fibers node produces no output

**Symptom**: Fibers generates black image

**Solutions**:
- Increase Samples
- Adjust Maximum Distance
- Check Distribution isn't 0
- Verify Spread Angle isn't 0

### 40. Edge Detect picks up unwanted detail

**Symptom**: Internal gradients create extra edges

**Solution**: Use **Threshold** before Edge Detect to get silhouette only

---

## Graph Organization Issues

### 41. Graph too messy to navigate

**Symptom**: Connections crossing everywhere, hard to follow

**Solutions**:
1. Use **Dot nodes** to route connections (Alt + click)
2. Create **named Dot portals** for frequently-used masks
3. Use **Frame** nodes to group related sections
4. Align nodes in rows/columns

### 42. Can't find a specific node

**Symptom**: Know node exists but can't locate in graph

**Solutions**:
- Use Search (Ctrl+F) in graph
- Check Library search (Space/Tab)
- Look in Frame groups
- Use Explorer panel to list all nodes

### 43. Connection won't attach

**Symptom**: Dragging connection but it won't snap to input

**Causes & Solutions**:
| Cause | Solution |
|-------|----------|
| Type mismatch | Grayscale → Color needs conversion |
| Input occupied | Disconnect existing connection |
| Wrong input | Check input name (not all inputs compatible) |

### 44. Dot portal not showing in dropdown

**Symptom**: Named Dot not available to reference

**Solutions**:
- Verify Dot has a name set in Properties
- Check you're looking at grayscale/color dropdown as appropriate
- Dot must be created before it can be referenced

---

## Weaving Issues

### 45. Threads don't interweave properly

**Symptom**: Warp and weft don't cross correctly

**Solutions**:
- Check Tile Generator Offset parameter
- Offset = 0.5 for proper weave
- Verify height values alternate correctly

### 46. Weave pattern too regular

**Symptom**: Fabric looks artificial, no organic variation

**Solutions**:
1. Add **Directional Noise**
   - Turns: 2-4
   - Distance: 0.1-0.2
2. Apply subtle **Warp** with Perlin Noise

---

## Ray Tracing Issues

### 47. Material looks completely different in Iray

**Symptom**: OpenGL preview fine, Iray looks wrong

**Common Causes**:
- Normal intensity too high (reduce to 2)
- Roughness values too extreme
- Displacement artifacts

**From Course**: "The fabric looks really dark and rough all of a sudden"

**Solution**: Reduce Normal intensity, blur noisy elements

---

## General Debugging Steps

When encountering an unknown issue:

1. **Isolate the problem**
   - Disconnect downstream nodes
   - Test each section independently

2. **Check inheritance**
   - Trace primary input chain
   - Look for unexpected parameter sources

3. **Verify connections**
   - All inputs connected?
   - Correct input slots?

4. **Test with defaults**
   - Reset parameters to defaults
   - Does basic setup work?

5. **Check resolution/bit depth**
   - Common source of artifacts
   - Set to Absolute to test

6. **Recompute**
   - Right-click → Recompute
   - Sometimes cache gets stale

7. **Compare to working example**
   - Reference Ornate_Fabric project
   - Match parameter values

8. **Restart if needed**
   - Save project
   - Restart Designer
   - Reopen project
