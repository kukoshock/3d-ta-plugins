# Graph Analysis Patterns

## Overview

This document provides **ready-to-use code recipes** for common graph analysis tasks using pysbs. Each pattern includes a complete working example that can be adapted for specific needs.

## Pattern Index

1. [Trace Upstream Dependencies](#pattern-1-trace-upstream-dependencies)
2. [Find Nodes by Type](#pattern-2-find-nodes-by-type)
3. [Extract All Parameters](#pattern-3-extract-all-parameters)
4. [Build Connection Map](#pattern-4-build-connection-map)
5. [Detect 8-bit Inheritance Chains](#pattern-5-detect-8-bit-inheritance-chains)
6. [Find Unconnected Nodes](#pattern-6-find-unconnected-nodes)
7. [Export Graph to JSON](#pattern-7-export-graph-to-json)
8. [Compare Two Graphs](#pattern-8-compare-two-graphs)
9. [Extract Output Node Info](#pattern-9-extract-output-node-info)
10. [Find Nodes with Specific Parameter](#pattern-10-find-nodes-with-specific-parameter)

---

## Pattern 1: Trace Upstream Dependencies

**Use Case**: Find all nodes that contribute to a specific output node.

```python
from pysbs import context, SBSDocument

def trace_upstream(graph, node_uid, visited=None):
    """
    Recursively trace all upstream nodes that feed into target node.

    Args:
        graph: SBSGraph instance
        node_uid: UID of node to trace from
        visited: Set of already visited UIDs (for recursion)

    Returns:
        Set of all upstream node UIDs
    """
    if visited is None:
        visited = set()

    if node_uid in visited:
        return visited

    visited.add(node_uid)

    # Get node
    node = graph.getNodeFromUid(node_uid)
    if not node:
        return visited

    # Get incoming connections
    incoming = graph.getConnectionsToNode(node)

    for conn in incoming:
        source_uid = conn.getSourceNodeUID()
        trace_upstream(graph, source_uid, visited)

    return visited

# Example usage
ctx = context.Context()
doc = SBSDocument(ctx, "material.sbs")
graph = doc.getGraphs()[0]

# Trace from baseColor output
output_nodes = graph.getAllOutputNodes()
for output in output_nodes:
    if output.getUid().startswith("baseColor"):
        deps = trace_upstream(graph, output.getUid())
        print(f"baseColor depends on {len(deps)} nodes")
        break
```

**Output**:
```
baseColor depends on 23 nodes
```

---

## Pattern 2: Find Nodes by Type

**Use Case**: Locate all nodes of a specific type (e.g., all Tile Samplers).

```python
from pysbs import context, SBSDocument

def find_nodes_by_type(graph, node_type):
    """
    Find all nodes of specific type.

    Args:
        graph: SBSGraph instance
        node_type: Node type identifier (e.g., "tile_sampler")

    Returns:
        List of matching SBSNode instances
    """
    matching = []

    for node in graph.getAllNodes():
        impl = node.getCompImplementation()
        if impl.mDefinition.mId == node_type:
            matching.append(node)

    return matching

# Example usage
ctx = context.Context()
doc = SBSDocument(ctx, "material.sbs")
graph = doc.getGraphs()[0]

# Find all Tile Samplers
tile_samplers = find_nodes_by_type(graph, "tile_sampler")
print(f"Found {len(tile_samplers)} Tile Sampler nodes:")

for node in tile_samplers:
    uid = node.getUid()
    print(f"  - {uid}")

# Find all Blend nodes
blends = find_nodes_by_type(graph, "blend")
print(f"\nFound {len(blends)} Blend nodes")
```

**Output**:
```
Found 3 Tile Sampler nodes:
  - Tile_Sampler_1
  - Pattern_Tile_1
  - Scatter_1

Found 12 Blend nodes
```

---

## Pattern 3: Extract All Parameters

**Use Case**: Export all node parameters to a structured format.

```python
import json
from pysbs import context, SBSDocument

def extract_all_parameters(graph):
    """
    Extract all parameters from all nodes.

    Args:
        graph: SBSGraph instance

    Returns:
        Dict mapping node UIDs to parameter dicts
    """
    result = {}

    for node in graph.getAllNodes():
        uid = node.getUid()
        node_type = node.getCompImplementation().mDefinition.mId

        params = {}
        for param in node.getParameters():
            param_id = param.mId
            param_value = param.mValue

            # Handle different value types
            if hasattr(param_value, 'mValues'):
                # Vector type
                value = list(param_value.mValues)
            elif hasattr(param_value, 'mValue'):
                # Scalar type
                value = param_value.mValue
            else:
                value = str(param_value)

            params[param_id] = value

        result[uid] = {
            "type": node_type,
            "parameters": params
        }

    return result

# Example usage
ctx = context.Context()
doc = SBSDocument(ctx, "material.sbs")
graph = doc.getGraphs()[0]

params = extract_all_parameters(graph)

# Export to JSON
print(json.dumps(params, indent=2))

# Or filter for specific node type
tile_sampler_params = {
    uid: data for uid, data in params.items()
    if data["type"] == "tile_sampler"
}
print(f"\nTile Sampler parameters:")
print(json.dumps(tile_sampler_params, indent=2))
```

**Output**:
```json
{
  "Tile_Sampler_1": {
    "type": "tile_sampler",
    "parameters": {
      "pattern": 0,
      "x_amount": 5,
      "y_amount": 5,
      "scale": 1.0,
      "scale_random": 0.2
    }
  }
}
```

---

## Pattern 4: Build Connection Map

**Use Case**: Create an adjacency list showing which nodes connect to which.

```python
from pysbs import context, SBSDocument

def build_connection_map(graph):
    """
    Build adjacency map of graph connections.

    Args:
        graph: SBSGraph instance

    Returns:
        Dict mapping source UIDs to lists of connection dicts
    """
    conn_map = {}

    for conn in graph.getConnections():
        source = conn.getSourceNodeUID()
        target = conn.getTargetNodeUID()
        source_out = conn.getSourceOutputIdentifier()
        target_in = conn.getTargetInputIdentifier()

        if source not in conn_map:
            conn_map[source] = []

        conn_map[source].append({
            "target": target,
            "source_output": source_out,
            "target_input": target_in
        })

    return conn_map

# Example usage
ctx = context.Context()
doc = SBSDocument(ctx, "material.sbs")
graph = doc.getGraphs()[0]

conn_map = build_connection_map(graph)

# Print connections for specific node
target_node = "Blur_HQ_Grayscale_1"
if target_node in conn_map:
    print(f"{target_node} connects to:")
    for conn in conn_map[target_node]:
        print(f"  -> {conn['target']}")
        print(f"     via {conn['source_output']} -> {conn['target_input']}")

# Count fan-out for each node
print("\nNodes by connection count:")
for uid, conns in sorted(conn_map.items(), key=lambda x: len(x[1]), reverse=True):
    print(f"  {uid}: {len(conns)} connections")
```

---

## Pattern 5: Detect 8-bit Inheritance Chains

**Use Case**: Find nodes using 8-bit output that could cause banding.

```python
from pysbs import context, SBSDocument

def detect_8bit_inheritance(graph):
    """
    Detect nodes using 8-bit output format.

    Args:
        graph: SBSGraph instance

    Returns:
        List of dicts with issue details
    """
    issues = []

    for node in graph.getAllNodes():
        uid = node.getUid()
        node_type = node.getCompImplementation().mDefinition.mId

        # Check parameters
        for param in node.getParameters():
            if param.mId in ["outputformat", "output_format"]:
                value_obj = param.mValue
                if hasattr(value_obj, 'mValue'):
                    value = value_obj.mValue
                    # 0 = 8-bit, 1 = 16-bit
                    if value == 0 or "8" in str(value):
                        issues.append({
                            "node": uid,
                            "type": node_type,
                            "format": "8-bit",
                            "severity": "high"
                        })

    return issues

# Example usage
ctx = context.Context()
doc = SBSDocument(ctx, "material.sbs")
graph = doc.getGraphs()[0]

issues = detect_8bit_inheritance(graph)

if issues:
    print(f"WARNING: Found {len(issues)} nodes using 8-bit output:")
    for issue in issues:
        print(f"  - {issue['node']} ({issue['type']})")
        print(f"    Risk: Potential banding in grayscale operations")
else:
    print("✓ No 8-bit inheritance issues detected")
```

---

## Pattern 6: Find Unconnected Nodes

**Use Case**: Detect orphaned nodes not contributing to any output.

```python
from pysbs import context, SBSDocument

def find_unconnected_nodes(graph):
    """
    Find nodes not connected to any output.

    Args:
        graph: SBSGraph instance

    Returns:
        List of unconnected node UIDs
    """
    # Get all nodes
    all_nodes = {node.getUid() for node in graph.getAllNodes()}

    # Trace from all outputs
    connected = set()
    for output in graph.getAllOutputNodes():
        output_uid = output.getUid()
        # Use trace_upstream from Pattern 1
        deps = trace_upstream(graph, output_uid)
        connected.update(deps)

    # Find difference
    unconnected = all_nodes - connected

    return list(unconnected)

def trace_upstream(graph, node_uid, visited=None):
    """Helper from Pattern 1"""
    if visited is None:
        visited = set()
    if node_uid in visited:
        return visited
    visited.add(node_uid)
    node = graph.getNodeFromUid(node_uid)
    if node:
        for conn in graph.getConnectionsToNode(node):
            trace_upstream(graph, conn.getSourceNodeUID(), visited)
    return visited

# Example usage
ctx = context.Context()
doc = SBSDocument(ctx, "material.sbs")
graph = doc.getGraphs()[0]

orphans = find_unconnected_nodes(graph)

if orphans:
    print(f"Found {len(orphans)} unconnected nodes:")
    for uid in orphans:
        node = graph.getNodeFromUid(uid)
        node_type = node.getCompImplementation().mDefinition.mId
        print(f"  - {uid} ({node_type})")
else:
    print("✓ All nodes connected to outputs")
```

---

## Pattern 7: Export Graph to JSON

**Use Case**: Create a complete structural representation for external tools.

```python
import json
from pysbs import context, SBSDocument

def export_graph_to_json(graph):
    """
    Export complete graph structure to JSON.

    Args:
        graph: SBSGraph instance

    Returns:
        JSON string with full graph data
    """
    structure = {
        "identifier": graph.mIdentifier,
        "nodes": [],
        "connections": [],
        "outputs": []
    }

    # Export nodes
    for node in graph.getAllNodes():
        node_data = {
            "uid": node.getUid(),
            "type": node.getCompImplementation().mDefinition.mId,
            "position": node.getPosition(),
            "parameters": {}
        }

        # Add parameters
        for param in node.getParameters():
            param_id = param.mId
            param_value = param.mValue

            if hasattr(param_value, 'mValues'):
                value = list(param_value.mValues)
            elif hasattr(param_value, 'mValue'):
                value = param_value.mValue
            else:
                value = str(param_value)

            node_data["parameters"][param_id] = value

        structure["nodes"].append(node_data)

    # Export connections
    for conn in graph.getConnections():
        structure["connections"].append({
            "source": conn.getSourceNodeUID(),
            "target": conn.getTargetNodeUID(),
            "source_output": conn.getSourceOutputIdentifier(),
            "target_input": conn.getTargetInputIdentifier()
        })

    # Export outputs
    for output in graph.getAllOutputNodes():
        structure["outputs"].append({
            "uid": output.getUid(),
            "identifier": output.mIdentifier if hasattr(output, 'mIdentifier') else "unknown"
        })

    return json.dumps(structure, indent=2)

# Example usage
ctx = context.Context()
doc = SBSDocument(ctx, "material.sbs")
graph = doc.getGraphs()[0]

json_output = export_graph_to_json(graph)

# Save to file
with open("graph_structure.json", "w") as f:
    f.write(json_output)

print("Graph exported to graph_structure.json")
```

---

## Pattern 8: Compare Two Graphs

**Use Case**: Diff two versions of a graph to find changes.

```python
from pysbs import context, SBSDocument

def compare_graphs(graph1, graph2):
    """
    Compare two graphs and report differences.

    Args:
        graph1: First SBSGraph instance
        graph2: Second SBSGraph instance

    Returns:
        Dict with comparison results
    """
    # Get node UIDs
    nodes1 = {node.getUid() for node in graph1.getAllNodes()}
    nodes2 = {node.getUid() for node in graph2.getAllNodes()}

    # Get connection pairs
    conns1 = {
        (c.getSourceNodeUID(), c.getTargetNodeUID())
        for c in graph1.getConnections()
    }
    conns2 = {
        (c.getSourceNodeUID(), c.getTargetNodeUID())
        for c in graph2.getConnections()
    }

    return {
        "nodes_added": list(nodes2 - nodes1),
        "nodes_removed": list(nodes1 - nodes2),
        "nodes_unchanged": list(nodes1 & nodes2),
        "connections_added": list(conns2 - conns1),
        "connections_removed": list(conns1 - conns2)
    }

# Example usage
ctx = context.Context()
doc1 = SBSDocument(ctx, "material_v1.sbs")
doc2 = SBSDocument(ctx, "material_v2.sbs")

graph1 = doc1.getGraphs()[0]
graph2 = doc2.getGraphs()[0]

diff = compare_graphs(graph1, graph2)

print(f"Nodes added: {len(diff['nodes_added'])}")
print(f"Nodes removed: {len(diff['nodes_removed'])}")
print(f"Connections added: {len(diff['connections_added'])}")
print(f"Connections removed: {len(diff['connections_removed'])}")

if diff['nodes_added']:
    print("\nAdded nodes:")
    for uid in diff['nodes_added']:
        print(f"  + {uid}")
```

---

## Pattern 9: Extract Output Node Info

**Use Case**: Get details about all graph outputs.

```python
from pysbs import context, SBSDocument

def extract_output_info(graph):
    """
    Extract information about all output nodes.

    Args:
        graph: SBSGraph instance

    Returns:
        List of dicts with output details
    """
    outputs = []

    for output in graph.getAllOutputNodes():
        output_info = {
            "uid": output.getUid(),
            "identifier": getattr(output, 'mIdentifier', 'unknown'),
            "parameters": {}
        }

        # Get output parameters
        for param in output.getParameters():
            param_id = param.mId
            param_value = param.mValue

            if hasattr(param_value, 'mValue'):
                value = param_value.mValue
            else:
                value = str(param_value)

            output_info["parameters"][param_id] = value

        outputs.append(output_info)

    return outputs

# Example usage
ctx = context.Context()
doc = SBSDocument(ctx, "material.sbs")
graph = doc.getGraphs()[0]

outputs = extract_output_info(graph)

print(f"Graph has {len(outputs)} outputs:")
for output in outputs:
    print(f"\n  {output['identifier']} ({output['uid']})")
    if 'outputformat' in output['parameters']:
        fmt = output['parameters']['outputformat']
        bit_depth = "16-bit" if fmt == 1 else "8-bit"
        print(f"    Format: {bit_depth}")
```

---

## Pattern 10: Find Nodes with Specific Parameter

**Use Case**: Locate nodes that have a parameter set to a specific value.

```python
from pysbs import context, SBSDocument

def find_nodes_with_parameter(graph, param_name, param_value=None):
    """
    Find nodes with specific parameter (optionally matching value).

    Args:
        graph: SBSGraph instance
        param_name: Parameter identifier to search for
        param_value: Optional value to match (None = any value)

    Returns:
        List of dicts with matching nodes
    """
    matches = []

    for node in graph.getAllNodes():
        uid = node.getUid()
        node_type = node.getCompImplementation().mDefinition.mId

        for param in node.getParameters():
            if param.mId == param_name:
                current_value = None
                if hasattr(param.mValue, 'mValue'):
                    current_value = param.mValue.mValue
                elif hasattr(param.mValue, 'mValues'):
                    current_value = list(param.mValue.mValues)

                # Check if value matches (if specified)
                if param_value is None or current_value == param_value:
                    matches.append({
                        "uid": uid,
                        "type": node_type,
                        "parameter": param_name,
                        "value": current_value
                    })

    return matches

# Example usage
ctx = context.Context()
doc = SBSDocument(ctx, "material.sbs")
graph = doc.getGraphs()[0]

# Find all nodes with blendingmode parameter
blend_nodes = find_nodes_with_parameter(graph, "blendingmode")
print(f"Found {len(blend_nodes)} nodes with blendingmode:")
for node in blend_nodes:
    print(f"  - {node['uid']}: mode={node['value']}")

# Find nodes with specific blend mode (e.g., Multiply = 13)
multiply_nodes = find_nodes_with_parameter(graph, "blendingmode", 13)
print(f"\nFound {len(multiply_nodes)} nodes using Multiply blend")
```

---

## Combining Patterns

### Example: Full Diagnostic Report

```python
from pysbs import context, SBSDocument
import json

def generate_diagnostic_report(filepath):
    """Generate comprehensive diagnostic report"""
    ctx = context.Context()
    doc = SBSDocument(ctx, filepath)

    report = {
        "file": filepath,
        "graphs": []
    }

    for graph in doc.getGraphs():
        graph_report = {
            "identifier": graph.mIdentifier,
            "node_count": len(graph.getAllNodes()),
            "connection_count": len(graph.getConnections()),
            "output_count": len(graph.getAllOutputNodes()),
            "issues": []
        }

        # Check for 8-bit inheritance (Pattern 5)
        eight_bit_issues = detect_8bit_inheritance(graph)
        graph_report["issues"].extend(eight_bit_issues)

        # Check for unconnected nodes (Pattern 6)
        orphans = find_unconnected_nodes(graph)
        if orphans:
            graph_report["issues"].append({
                "type": "unconnected_nodes",
                "count": len(orphans),
                "nodes": orphans
            })

        # Node type distribution (Pattern 2)
        node_types = {}
        for node in graph.getAllNodes():
            node_type = node.getCompImplementation().mDefinition.mId
            node_types[node_type] = node_types.get(node_type, 0) + 1
        graph_report["node_types"] = node_types

        report["graphs"].append(graph_report)

    return json.dumps(report, indent=2)

# Usage
report = generate_diagnostic_report("material.sbs")
print(report)

# Save to file
with open("diagnostic_report.json", "w") as f:
    f.write(report)
```

---

## Performance Tips

1. **Cache results**: Store node lists, connection maps to avoid repeated traversals
2. **Filter early**: Use type filtering before parameter extraction
3. **Lazy evaluation**: Only compute what's needed for the task
4. **Batch operations**: Process all graphs in a document together

## Error Handling

Always wrap analysis in try-except:

```python
from pysbs import context, SBSDocument

def safe_analyze(filepath):
    try:
        ctx = context.Context()
        doc = SBSDocument(ctx, filepath)
        # ... analysis code ...
        return result
    except FileNotFoundError:
        print(f"ERROR: File not found: {filepath}")
        return None
    except Exception as e:
        print(f"ERROR: {e}")
        return None
```

## Further Reading

- See [pysbs-api.md](./pysbs-api.md) for API reference
- See [diagnostic-rules.md](./diagnostic-rules.md) for issue detection patterns
- See [analysis-script.py](./analysis-script.py) for complete standalone example
