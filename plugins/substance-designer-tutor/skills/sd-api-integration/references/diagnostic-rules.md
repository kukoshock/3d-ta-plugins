# Diagnostic Rules

## Overview

This document defines **detection rules** for common Substance Designer issues and links them to the tutor skill's knowledge base for WHY-based explanations and fixes.

Each rule includes:
- **Detection logic**: How to identify the issue programmatically
- **Tutor reference**: Link to relevant tutor documentation
- **Severity**: Impact level (high/medium/low)
- **Recommendation**: Suggested fix with explanation

## Rule Categories

1. [Bit Depth & Inheritance](#bit-depth--inheritance)
2. [Node Connections](#node-connections)
3. [Parameter Configuration](#parameter-configuration)
4. [Graph Structure](#graph-structure)
5. [Output Configuration](#output-configuration)

---

## Bit Depth & Inheritance

### Rule 1: 8-bit Output in Grayscale Chain

**Detection**:
```python
# Node has outputformat parameter set to 8-bit (0)
# AND feeds into grayscale operations (Blur, Levels, Curve, etc.)
def detect_8bit_in_grayscale_chain(graph):
    issues = []
    for node in graph.getAllNodes():
        for param in node.getParameters():
            if param.mId == "outputformat":
                if param.mValue.mValue == 0:  # 8-bit
                    # Check if connected to grayscale ops
                    for conn in graph.getConnectionsFromNode(node):
                        target = graph.getNodeFromUid(conn.getTargetNodeUID())
                        target_type = target.getCompImplementation().mDefinition.mId
                        if target_type in ["blur_hq_grayscale", "levels", "curve", "warp"]:
                            issues.append({
                                "node": node.getUid(),
                                "rule": "8bit_grayscale_chain"
                            })
    return issues
```

**Tutor Reference**: `${CLAUDE_PLUGIN_ROOT}/skills/tutor/references/troubleshooting.md` - "Banding or Stepping in Gradients"

**Severity**: High

**WHY This Matters**:
- 8-bit = 256 possible values per pixel
- Grayscale operations amplify subtle differences
- Results in visible banding/stepping in smooth gradients
- Inheritance: downstream nodes inherit 8-bit precision

**Recommendation**:
```
Set outputformat to "16-bit Absolute" to prevent banding.

WHY: 16-bit provides 65,536 values instead of 256, making gradual
transitions smooth even after multiple blur/level operations.

Where: Node parameters → Output Format → 16-bit Absolute
```

---

### Rule 2: Repeated 8-bit Conversions

**Detection**:
```python
# Multiple nodes in chain using 8-bit output
def detect_repeated_8bit_conversions(graph):
    # Build upstream chain for each output
    # Count 8-bit nodes in each chain
    # Flag chains with 3+ 8-bit nodes
    pass
```

**Tutor Reference**: `${CLAUDE_PLUGIN_ROOT}/skills/tutor/references/troubleshooting.md` - "Cumulative Precision Loss"

**Severity**: Medium

**WHY This Matters**:
- Each 8-bit conversion loses precision
- Cumulative loss becomes noticeable after 3+ conversions
- Particularly bad in height map workflows

**Recommendation**:
```
Use 16-bit Absolute throughout the chain, convert to 8-bit only
at final output if needed for target platform.
```

---

## Node Connections

### Rule 3: Tile Sampler Without Scale Map

**Detection**:
```python
def detect_tile_sampler_without_scale_map(graph):
    issues = []
    for node in graph.getAllNodes():
        node_type = node.getCompImplementation().mDefinition.mId
        if node_type == "tile_sampler":
            # Check if scale_map input is connected
            incoming = graph.getConnectionsToNode(node)
            has_scale_map = any(
                conn.getTargetInputIdentifier() == "scale_map"
                for conn in incoming
            )
            if not has_scale_map:
                issues.append({
                    "node": node.getUid(),
                    "rule": "tile_sampler_no_scale_map"
                })
    return issues
```

**Tutor Reference**: `${CLAUDE_PLUGIN_ROOT}/skills/tutor/references/node-parameters.md` - "Tile Sampler: Scale Map vs Mask Input"

**Severity**: Medium

**WHY This Matters**:
- Without scale variation, all instances are identical size
- Looks artificial and repetitive
- Organic materials need size variation

**Recommendation**:
```
Connect Perlin Noise to Scale Map input for organic size variation.

WHY: Scale Map uses grayscale values to control instance size.
Perlin Noise creates natural-looking variation (0.5-2.0x scale range).

Setup:
1. Add Perlin Noise node
2. Connect to Tile Sampler → Scale Map input
3. Adjust Noise Scale to control variation frequency
```

---

### Rule 4: Height Blend Without Height Input

**Detection**:
```python
def detect_height_blend_missing_height(graph):
    issues = []
    for node in graph.getAllNodes():
        if node.getCompImplementation().mDefinition.mId == "height_blend":
            incoming = graph.getConnectionsToNode(node)

            # Check if any connector has "height" in its identifier
            has_height_input = any(
                "height" in conn.getTargetInputIdentifier().lower()
                for conn in incoming
            )

            if not has_height_input:
                issues.append({
                    "node": node.getUid(),
                    "rule": "height_blend_no_height"
                })
    return issues
```

**Tutor Reference**: `${CLAUDE_PLUGIN_ROOT}/skills/tutor/references/workflows.md` - "Height Blend: Height-First Workflow"

**Severity**: High

**WHY This Matters**:
- Height Blend uses height data to determine blend boundaries
- Without height input, falls back to linear blend (defeats purpose)
- Misses the key advantage: depth-based masking

**Recommendation**:
```
Connect height data to Height Blend's height inputs.

WHY: Height Blend analyzes height values to create natural
overlap boundaries. Without height, it's just a regular Blend node.

Setup:
1. Connect pattern height to "Height 1" input
2. Connect background height to "Height 2" input
3. Height values determine which pattern appears "on top"
```

---

### Rule 5: Output Node Disconnected

**Detection**:
```python
def detect_disconnected_output(graph):
    issues = []
    for output in graph.getAllOutputNodes():
        incoming = graph.getConnectionsToNode(output)
        if not incoming:
            issues.append({
                "node": output.getUid(),
                "rule": "disconnected_output"
            })
    return issues
```

**Tutor Reference**: `${CLAUDE_PLUGIN_ROOT}/skills/tutor/references/workflows.md` - "Setup Stage"

**Severity**: High

**WHY This Matters**:
- Disconnected output won't render anything
- Common mistake after restructuring graph
- Easy to miss in large graphs

**Recommendation**:
```
Connect a source node to this output.

Typical connections:
- baseColor → Final color result
- normal → Normal Combine output
- height → Height processing chain
- roughness → Roughness value or texture
- metallic → Metallic value or mask
- ambientOcclusion → AO calculation output
```

---

## Parameter Configuration

### Rule 6: Extreme Blur Intensity

**Detection**:
```python
def detect_extreme_blur_intensity(graph):
    issues = []
    for node in graph.getAllNodes():
        node_type = node.getCompImplementation().mDefinition.mId
        if "blur" in node_type:
            for param in node.getParameters():
                if param.mId == "intensity":
                    value = param.mValue.mValue
                    if value > 10.0:  # Threshold
                        issues.append({
                            "node": node.getUid(),
                            "rule": "extreme_blur_intensity",
                            "value": value
                        })
    return issues
```

**Tutor Reference**: `${CLAUDE_PLUGIN_ROOT}/skills/tutor/references/node-parameters.md` - "Blur Intensity Guidelines"

**Severity**: Low

**WHY This Matters**:
- Extreme blur (>10) is usually unintentional
- Can hide important detail
- Performance impact (large kernel sizes)

**Recommendation**:
```
Consider reducing blur intensity.

Typical ranges:
- Subtle softening: 0.5-2.0
- Moderate blur: 2.0-5.0
- Heavy blur: 5.0-10.0
- Extreme blur (>10): Rarely needed

If intentional, consider using lower resolution input first
to improve performance.
```

---

### Rule 7: Identical Tiling Values

**Detection**:
```python
def detect_uniform_tiling(graph):
    issues = []
    for node in graph.getAllNodes():
        tiling_x = None
        tiling_y = None

        for param in node.getParameters():
            if param.mId == "tiling":
                # Vector2 parameter
                values = param.mValue.mValues
                tiling_x, tiling_y = values[0], values[1]

        # Check if both are 1,1 (default, often unchanged)
        if tiling_x == 1.0 and tiling_y == 1.0:
            issues.append({
                "node": node.getUid(),
                "rule": "uniform_tiling",
                "severity": "info"
            })
    return issues
```

**Tutor Reference**: `${CLAUDE_PLUGIN_ROOT}/skills/tutor/references/node-parameters.md` - "Tiling and Offset"

**Severity**: Info

**WHY This Matters**:
- Default 1,1 tiling may be intentional but often overlooked
- Adjusting tiling changes pattern frequency
- Common first step in texture customization

**Recommendation**:
```
Consider adjusting tiling to control pattern frequency.

Higher values (2,2 or 4,4): Smaller, more frequent patterns
Lower values (0.5,0.5): Larger, less frequent patterns
Non-uniform (2,1): Stretches pattern in one direction
```

---

## Graph Structure

### Rule 8: Orphaned Nodes

**Detection**:
```python
def detect_orphaned_nodes(graph):
    # Use Pattern 6 from graph-analysis-patterns.md
    # Find nodes not in upstream chain of any output
    from graph_analysis_patterns import find_unconnected_nodes
    return find_unconnected_nodes(graph)
```

**Tutor Reference**: N/A (structural issue)

**Severity**: Low

**WHY This Matters**:
- Orphaned nodes don't affect final render
- May indicate incomplete work or forgotten experiments
- Adds clutter to graph

**Recommendation**:
```
Review orphaned nodes:
- If experimental: Move to separate test graph
- If obsolete: Delete to reduce clutter
- If intended for future use: Add comment frame explaining

Orphaned nodes found:
{list of node UIDs}
```

---

### Rule 9: Excessive Fan-Out

**Detection**:
```python
def detect_excessive_fanout(graph):
    issues = []
    conn_map = build_connection_map(graph)  # From Pattern 4

    for source_uid, connections in conn_map.items():
        if len(connections) > 5:  # Threshold
            issues.append({
                "node": source_uid,
                "rule": "excessive_fanout",
                "connection_count": len(connections)
            })
    return issues
```

**Tutor Reference**: `${CLAUDE_PLUGIN_ROOT}/skills/tutor/references/workflows.md` - "Graph Organization"

**Severity**: Info

**WHY This Matters**:
- High fan-out (>5 connections) may indicate:
  - Shared resource (good, but consider caching)
  - Graph organization issue (could benefit from intermediate nodes)
- Not inherently bad, just worth reviewing

**Recommendation**:
```
Review high fan-out node usage:

If frequently reused calculation:
- Consider adding comment explaining its importance
- Ensure it's named clearly

If many connections make graph hard to read:
- Consider adding intermediate "hub" nodes
- Use frames to group related nodes
```

---

## Output Configuration

### Rule 10: Output Size Mismatch

**Detection**:
```python
def detect_output_size_mismatch(graph):
    issues = []
    output_sizes = {}

    for output in graph.getAllOutputNodes():
        for param in output.getParameters():
            if param.mId == "outputsize":
                size = param.mValue.mValues
                output_sizes[output.getUid()] = size

    # Check if all outputs have same size
    unique_sizes = set(tuple(s) for s in output_sizes.values())
    if len(unique_sizes) > 1:
        issues.append({
            "rule": "output_size_mismatch",
            "sizes": {uid: list(size) for uid, size in output_sizes.items()}
        })

    return issues
```

**Tutor Reference**: `${CLAUDE_PLUGIN_ROOT}/skills/tutor/references/workflows.md` - "Setup Stage: Output Size"

**Severity**: Medium

**WHY This Matters**:
- Mixed output sizes in same material can cause issues
- Some game engines expect uniform texture set resolution
- May be intentional (roughness at lower res) but worth flagging

**Recommendation**:
```
Review output size settings. Detected different sizes:
{list of outputs with sizes}

Common practices:
- All outputs same resolution: Most compatible
- Height/Normal full res, others half res: Performance optimization
- Roughness/Metallic lower res: Acceptable if detail not critical

If intentional, this is fine. If not, standardize to same resolution.
```

---

### Rule 11: Missing Standard PBR Outputs

**Detection**:
```python
def detect_missing_pbr_outputs(graph):
    # Standard PBR outputs
    expected_outputs = {
        "baseColor", "normal", "roughness",
        "metallic", "height", "ambientOcclusion"
    }

    # Get actual outputs
    actual_outputs = {
        output.mIdentifier for output in graph.getAllOutputNodes()
        if hasattr(output, 'mIdentifier')
    }

    missing = expected_outputs - actual_outputs

    if missing:
        return [{
            "rule": "missing_pbr_outputs",
            "missing": list(missing)
        }]
    return []
```

**Tutor Reference**: `${CLAUDE_PLUGIN_ROOT}/skills/tutor/references/workflows.md` - "Setup Stage: PBR Outputs"

**Severity**: Info

**WHY This Matters**:
- Standard PBR workflow expects 6 outputs
- Missing outputs may be intentional (e.g., metal doesn't need height)
- Flagged as reminder, not error

**Recommendation**:
```
Consider adding missing PBR outputs:
{list of missing outputs}

Typical uses:
- baseColor: Albedo/Diffuse color
- normal: Surface detail normals
- height: Displacement/parallax
- roughness: Surface glossiness (inverted)
- metallic: Metal vs non-metal mask
- ambientOcclusion: Crevice darkening

Not all materials need all outputs. This is informational only.
```

---

## Applying Diagnostic Rules

### Integration with Analysis

```python
from pysbs import context, SBSDocument
import json

def run_all_diagnostics(filepath):
    """Run all diagnostic rules on .sbs file"""
    ctx = context.Context()
    doc = SBSDocument(ctx, filepath)

    all_issues = []

    for graph in doc.getGraphs():
        graph_issues = {
            "graph": graph.mIdentifier,
            "issues": []
        }

        # Run each diagnostic rule
        graph_issues["issues"].extend(detect_8bit_in_grayscale_chain(graph))
        graph_issues["issues"].extend(detect_tile_sampler_without_scale_map(graph))
        graph_issues["issues"].extend(detect_height_blend_missing_height(graph))
        graph_issues["issues"].extend(detect_disconnected_output(graph))
        graph_issues["issues"].extend(detect_extreme_blur_intensity(graph))
        # ... run all other rules ...

        all_issues.append(graph_issues)

    return all_issues

# Usage
issues = run_all_diagnostics("material.sbs")

# Format report
for graph_issue in issues:
    print(f"\n=== {graph_issue['graph']} ===")
    if not graph_issue['issues']:
        print("✓ No issues detected")
    else:
        for issue in graph_issue['issues']:
            print(f"⚠ {issue['rule']}: {issue['node']}")
```

### Generating WHY Explanations

```python
# Map rule IDs to tutor references
RULE_REFERENCES = {
    "8bit_grayscale_chain": {
        "tutor_file": "troubleshooting.md",
        "section": "Banding or Stepping in Gradients",
        "why": "8-bit precision causes visible stepping in smooth gradients"
    },
    "tile_sampler_no_scale_map": {
        "tutor_file": "node-parameters.md",
        "section": "Tile Sampler: Scale Map",
        "why": "Uniform sizes look artificial; organic materials need variation"
    },
    # ... more mappings ...
}

def explain_issue(issue):
    """Generate WHY-based explanation for issue"""
    rule_id = issue['rule']
    if rule_id in RULE_REFERENCES:
        ref = RULE_REFERENCES[rule_id]
        return f"""
Issue: {rule_id}
Node: {issue['node']}

WHY This Matters:
{ref['why']}

Learn More:
See tutor skill → {ref['tutor_file']} → {ref['section']}
"""
    return f"Issue: {rule_id} at {issue['node']}"
```

## Severity Levels

| Level | Meaning | Action |
|-------|---------|--------|
| **High** | Likely to cause visual artifacts or errors | Fix recommended |
| **Medium** | May cause issues or suboptimal results | Review and consider fixing |
| **Low** | Minor issue or potential improvement | Optional improvement |
| **Info** | Informational, not a problem | Awareness only |

## Customizing Rules

Users can define custom rules by extending the patterns:

```python
# Custom rule: Detect nodes with default names
def detect_default_node_names(graph):
    issues = []
    for node in graph.getAllNodes():
        uid = node.getUid()
        # Default names often contain numbers like "Blend_1", "Blur_2"
        if any(char.isdigit() for char in uid):
            issues.append({
                "node": uid,
                "rule": "default_node_name",
                "severity": "info"
            })
    return issues
```

## Further Reading

- [graph-analysis-patterns.md](./graph-analysis-patterns.md) - Detection implementations
- [troubleshooting.md](./troubleshooting.md) - Common SD issues
- Tutor skill references for WHY explanations
