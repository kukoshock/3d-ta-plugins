# Troubleshooting Guide

Comprehensive problem/solution reference for Substance Designer (40+ scenarios).

---

## Pattern & Distribution Issues

### 1. Ornaments look too uniform/regular

**Symptom**: All ornaments appear identical, pattern looks artificial

**Causes & Solutions**:
| Cause | Solution |
|-------|----------|
| No randomization | Increase `rotation_random` (0.02-0.1) |
| Static scale | Add `scale_random` (0.1-0.3) |
| Fixed positions | Increase `position_random` (0.01-0.05) |
| Uniform sizing | Connect **Perlin Noise** to Tile Sampler's Scale input |

### 2. Ornaments too prominent/embossed

**Symptom**: Ornaments stick out too much from the base fabric

**Solutions**:
1. Add **Levels** before Height Blend
2. Crush white values: Output High = 0.3-0.5
3. Reduce Height Blend Offset slider
4. Decrease Height Blend Contrast

### 3. Pattern too regular/grid-like

**Symptom**: Distribution looks like obvious grid

**Solutions**:
- Change Tile Sampler Pattern mode (try mode 2 = brick)
- Increase Position Random significantly
- Use Offset slider to stagger rows
- Add **Warp** with subtle Perlin Noise as intensity

### 4. Tiled elements don't connect smoothly

**Symptom**: Visible seams where repeated elements meet

**Solutions**:
1. Offset element by 0.5 on tiling axis
2. Blend with original using Max mode
3. Ensure tiling is set correctly (Vertical only, Horizontal only, etc.)

### 5. Elements cut off at edges

**Symptom**: Shapes get clipped at tile boundaries

**Solutions**:
- Use **Safe Transform 2D** instead of regular Transform
- Check tiling mode (should NOT be "None" if tiling needed)
- Reduce element scale so it fits within tile

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

**Symptom**: Visible steps in gradients, like posterization

**Causes & Solutions**:
| Cause | Solution |
|-------|----------|
| 8-bit primary input | Swap Blend inputs (X key) |
| 8-bit propagation | Set Output Format to Absolute 16-bit |
| Low bit depth source | Check source image bit depth |

**From Course**: "If your primary input has 8-bit depth, that propagates downstream"

### 8. Wrong resolution downstream

**Symptom**: Output appears wrong size or blurry

**Solutions**:
1. Check primary input resolution
2. Set Output Size to Absolute with desired resolution
3. Verify parent graph resolution settings

### 9. Vertical gradient in Curvature Smooth

**Symptom**: Curvature map shows gradient bands instead of proper edges

**Cause**: Tiling disabled somewhere upstream

**Solutions**:
1. Find node with tiling disabled (trace upstream from Curvature)
2. Swap Blend inputs if commutative operation (X key)
3. Set Curvature Smooth to Absolute full tiling
4. **From Course**: "Make sure your node is set to full tiling"

### 10. Tiling breaks unexpectedly

**Symptom**: Material that should tile has seams

**Solutions**:
- Check inheritance chain for tiling settings
- Find Transform 2D with partial tiling disabled
- Set affected nodes to Absolute full tiling

### 11. Node ignores parameter changes

**Symptom**: Adjusting sliders has no effect

**Solutions**:
- Check if parameter is exposed (blue highlight = controlled elsewhere)
- Right-click → Recompute
- Check inheritance (might be overridden by input)

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

**Symptom**: Material in Blender/Unreal doesn't match Designer

**Solutions**:
- Check normal map orientation (DirectX vs OpenGL)
- Verify color space settings
- Review roughness interpretation
- Compare under similar lighting

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

**Symptom**: Connected noise has no effect on sizing

**Solutions**:
- Verify connection is to Scale Map input (not main input)
- Check noise range (should be 0-1 grayscale)
- Increase Scale Random to see effect
- Verify Scale parameter isn't at minimum

### 34. Height Blend edges too soft

**Symptom**: Ornaments blend too gradually into fabric

**Solution**: Increase Contrast slider (0.96 = very crisp)

### 35. Height Blend edges too hard

**Symptom**: Ornaments have harsh, unnatural edges

**Solutions**:
- Decrease Contrast slider
- **Blur** the foreground input slightly
- Adjust Offset slider

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
