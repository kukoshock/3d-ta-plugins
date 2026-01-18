# Troubleshooting Guide

Common problems and solutions for Substance Designer fabric materials.

## Tile Sampler Issues

### Problem: Ornaments Look Too Uniform / Mechanical

**Symptoms:**
- Pattern looks artificial
- All ornaments identical in size
- Grid-like appearance

**Solutions:**

1. **Increase Randomization Parameters**
   ```
   rotation_random: 0.02 → 0.05-0.1
   scale_random: 0.19 → 0.25-0.35
   position_random: 0.01 → 0.03-0.05
   ```

2. **Add Perlin Noise to Scale Input**
   - Create Perlin Noise node
   - Connect to Tile Sampler's Scale Map input
   - Adjust Perlin scale (5-10) for desired variation size

3. **Use Different Pattern Mode**
   - Try pattern modes 2 (brick) or 3 (hexagonal)
   - Breaks up the grid regularity

---

### Problem: Ornaments Too Sparse or Too Dense

**Symptoms:**
- Large gaps between ornaments
- Ornaments overlapping too much
- Embroidery looks wrong scale

**Solutions:**

1. **Adjust Tile Counts**
   ```
   Too sparse: Increase x_amount and y_amount (try 600-800)
   Too dense: Decrease x_amount and y_amount (try 200-400)
   ```

2. **Modify Base Scale**
   ```
   Too small: Increase scale (3.0 → 5.0)
   Too large: Decrease scale (3.0 → 1.5)
   ```

3. **Check Input Shape Size**
   - Ensure ornament mask fills reasonable portion of its space
   - Too small input = sparse appearance even with many tiles

---

### Problem: Ornaments Clipping / Cutting Off at Edges

**Symptoms:**
- Ornaments appear cropped
- Pattern doesn't tile seamlessly

**Solutions:**

1. **Enable Proper Tiling Mode**
   - Check Tile Sampler's tiling settings
   - Ensure input shape has proper margins

2. **Reduce Scale**
   - Large scale + high tile count = edge clipping
   - Try reducing scale or tile counts

---

## Height Blend Issues

### Problem: Ornaments Don't Sit on Fabric Realistically

**Symptoms:**
- Ornaments look pasted on
- No depth integration
- Harsh edges around ornaments

**Solutions:**

1. **Use Levels Before Height Blend**
   ```
   Input High: 0.5-0.7 (compress range)
   Output High: 0.3-0.5 (flatten peaks)
   ```
   Creates "something a bit more flat"

2. **Adjust Height Blend Contrast**
   ```
   Too harsh: Reduce contrast (0.96 → 0.7-0.8)
   Too soft: Increase contrast (0.6 → 0.9)
   ```

3. **Check Input Order**
   - Background input: Base weave height
   - Foreground input: Ornament height (after Levels)

---

### Problem: Ornaments Invisible or Barely Visible

**Symptoms:**
- Can't see embroidery on fabric
- Ornaments too subtle

**Solutions:**

1. **Check Height Blend Sliders**
   - Increase foreground prominence slider
   - Verify both inputs are connected

2. **Adjust Levels Output**
   ```
   Output High too low: Increase to 0.5-0.7
   ```

3. **Verify Ornament Mask**
   - Check that ornament input has actual values (not all black)
   - Preview the mask directly

---

### Problem: Ornaments Appear Inverted (Indented Instead of Raised)

**Symptoms:**
- Embroidery looks pressed into fabric
- Depth is wrong direction

**Solutions:**

1. **Invert Height Values**
   - Add Invert node before Height Blend
   - Or swap Levels input/output values

2. **Check Input Connections**
   - Foreground and background may be swapped

---

## Performance Issues

### Problem: Graph is Extremely Slow

**Symptoms:**
- Long computation times
- Unresponsive interface
- Memory warnings

**Solutions:**

1. **Reduce Resolution**
   ```
   8K → 4K or 2K for development
   Only use 8K for final output
   ```
   8K makes things "extremely heavy"

2. **Lower Tile Counts**
   ```
   600x700 → 300x350 for testing
   ```

3. **Simplify During Development**
   - Disconnect heavy nodes temporarily
   - Use lower quality previews
   - Work on sections independently

4. **Check for Feedback Loops**
   - Circular connections cause infinite computation
   - Verify graph flow is directional

---

### Problem: Preview Not Updating

**Symptoms:**
- Changes don't appear
- Old values shown

**Solutions:**

1. **Force Recompute**
   - Right-click node → Recompute
   - Or modify any parameter slightly

2. **Check Node Connections**
   - Ensure all inputs connected
   - Verify output node is selected

---

## Weaving Issues

### Problem: Threads Don't Interweave Properly

**Symptoms:**
- Warp and weft don't cross correctly
- One direction always on top

**Solutions:**

1. **Check Tile Generator Offset**
   - Offset parameter creates interlocking
   - Try offset = 0.5 for proper weave

2. **Verify Height Values**
   - Warp and weft need alternating heights
   - Use different height values for each direction

---

### Problem: Weave Pattern Too Regular

**Symptoms:**
- Fabric looks artificial
- No organic variation

**Solutions:**

1. **Add Directional Noise**
   ```
   Turns: 2-4
   Distance: 0.1-0.2
   Angle Random: 0.1-0.15
   ```

2. **Apply Subtle Warp**
   - Use Warp node with low intensity
   - Adds organic imperfection

---

## Shape Design Issues

### Problem: Spline Shape Has Sharp Corners

**Symptoms:**
- Angular instead of smooth curves
- Visible control point locations

**Solutions:**

1. **Increase Segment Amount**
   ```
   Low (8) → Higher (24-32)
   ```
   More segments = smoother curves

2. **Adjust Control Point Positions**
   - Move intermediate points for better flow
   - Use Show Tangents to visualize

---

### Problem: Edge Detection Fails on Ornament

**Symptoms:**
- Edges look wrong in final material
- Normal map artifacts around ornament

**Solutions:**

1. **Design with Edges in Mind**
   - Avoid "shapeless blobs"
   - Create clear, defined boundaries

2. **Add Edge Processing**
   - Use Edge Detect node
   - Apply subtle blur to soften harsh edges

---

## General Debugging Steps

1. **Isolate the Problem**
   - Disconnect downstream nodes
   - Preview each node individually

2. **Check Input Values**
   - View each input's actual output
   - Verify expected ranges (0-1 for most)

3. **Compare to Working Example**
   - Reference Ornate_Fabric project
   - Match parameter values

4. **Reset to Defaults**
   - Right-click parameter → Reset
   - Start from known working state

5. **Check Documentation**
   - Hover over parameters for tooltips
   - Reference node-parameters.md for actual values
