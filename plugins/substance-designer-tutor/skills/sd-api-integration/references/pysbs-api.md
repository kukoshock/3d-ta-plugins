# pysbs API Reference

## Overview

The **pysbs** library (part of the Substance Automation Toolkit) provides Python bindings for reading and manipulating Substance Designer .sbs files **without running the Designer application**.

**Primary Use Cases**:
- CI/CD pipeline integration
- Batch analysis of .sbs files
- Parameter extraction for documentation
- Automated validation and testing
- Data migration and format conversion

## Installation

### Option 1: Use Designer's Python Environment

```bash
# Windows
cd "C:\Program Files\Adobe\Adobe Substance 3D Designer\resources\python-packages"
set PYTHONPATH=%CD%

# macOS
cd "/Applications/Adobe Substance 3D Designer.app/Contents/Resources/python-packages"
export PYTHONPATH=$(pwd)
```

### Option 2: Install via pip

```bash
pip install substance-automation-toolkit
```

## Core Classes

### Context

The entry point for all pysbs operations. Manages the environment for document manipulation.

```python
from pysbs import context

# Create context (required for all operations)
ctx = context.Context()
```

**Methods**:
- `Context()` - Constructor, initializes the pysbs environment

---

### SBSDocument

Represents an entire .sbs file (package). Contains graphs, dependencies, and metadata.

```python
from pysbs import SBSDocument

# Load document
doc = SBSDocument(ctx, "path/to/file.sbs")

# Save document (if modified)
doc.writeDoc()
```

**Key Methods**:

| Method | Returns | Description |
|--------|---------|-------------|
| `getGraphs()` | `list[SBSGraph]` | Get all graphs in document |
| `getGraph(identifier)` | `SBSGraph` | Get specific graph by identifier |
| `getDependencies()` | `list[SBSDependency]` | Get external .sbs dependencies |
| `getMetaData()` | `dict` | Get package metadata (author, description, etc.) |
| `getPackageUrl()` | `str` | Get package identifier |
| `writeDoc(filepath=None)` | `None` | Save document to file |

**Example: Load and Inspect Document**

```python
from pysbs import context, SBSDocument

ctx = context.Context()
doc = SBSDocument(ctx, "materials/fabric.sbs")

# Get all graphs
graphs = doc.getGraphs()
print(f"Package contains {len(graphs)} graphs:")

for graph in graphs:
    print(f"  - {graph.mIdentifier}")

# Get dependencies
deps = doc.getDependencies()
print(f"\nExternal dependencies: {len(deps)}")
for dep in deps:
    print(f"  - {dep.mFilePath}")

# Get metadata
metadata = doc.getMetaData()
print(f"\nAuthor: {metadata.get('author', 'Unknown')}")
```

---

### SBSGraph

Represents a single graph within an .sbs file. Contains nodes, connections, and parameters.

```python
# Get graph from document
graph = doc.getGraph("Material_Graph")

# Or get all graphs and iterate
for graph in doc.getGraphs():
    process_graph(graph)
```

**Key Methods**:

| Method | Returns | Description |
|--------|---------|-------------|
| `getAllNodes()` | `list[SBSNode]` | Get all nodes in graph |
| `getNodeFromUid(uid)` | `SBSNode` | Get specific node by UID |
| `getConnections()` | `list[SBSConnection]` | Get all connections |
| `getConnectionsFromNode(node)` | `list[SBSConnection]` | Get outgoing connections from node |
| `getConnectionsToNode(node)` | `list[SBSConnection]` | Get incoming connections to node |
| `getInputParameters()` | `list[SBSParameter]` | Get graph input parameters |
| `getAllOutputNodes()` | `list[SBSNode]` | Get all output nodes |
| `getAllComments()` | `list[SBSComment]` | Get all comment frames |
| `getMetaData()` | `dict` | Get graph metadata |
| `getGraphSize()` | `tuple` | Get graph output size |

**Attributes**:
- `mIdentifier` - Graph identifier/name
- `mAttributes` - Graph attributes dictionary

**Example: Analyze Graph Structure**

```python
def analyze_graph(graph):
    print(f"\n=== Graph: {graph.mIdentifier} ===")

    # Count nodes
    nodes = graph.getAllNodes()
    print(f"Total nodes: {len(nodes)}")

    # Count by type
    node_types = {}
    for node in nodes:
        node_type = node.getCompImplementation().mDefinition.mId
        node_types[node_type] = node_types.get(node_type, 0) + 1

    print("\nNode types:")
    for node_type, count in sorted(node_types.items()):
        print(f"  {node_type}: {count}")

    # Count connections
    connections = graph.getConnections()
    print(f"\nTotal connections: {len(connections)}")

    # List outputs
    outputs = graph.getAllOutputNodes()
    print(f"\nOutput nodes ({len(outputs)}):")
    for output in outputs:
        print(f"  - {output.getUid()}")

# Usage
for graph in doc.getGraphs():
    analyze_graph(graph)
```

---

### SBSNode

Represents a single node within a graph (Blend, Blur, Transform, etc.).

```python
# Get nodes from graph
nodes = graph.getAllNodes()

for node in nodes:
    uid = node.getUid()
    node_type = node.getCompImplementation().mDefinition.mId
    print(f"{uid}: {node_type}")
```

**Key Methods**:

| Method | Returns | Description |
|--------|---------|-------------|
| `getUid()` | `str` | Get unique identifier for node |
| `getParameters()` | `list[SBSParameter]` | Get all node parameters |
| `getParameter(id)` | `SBSParameter` | Get specific parameter by ID |
| `getCompImplementation()` | `SBSCompImplementation` | Get implementation (contains node type) |
| `getPosition()` | `tuple` | Get (x, y) position in graph |
| `getGUILayout()` | `dict` | Get GUI-specific data |

**Example: Extract Node Parameters**

```python
def extract_node_parameters(node):
    uid = node.getUid()
    node_type = node.getCompImplementation().mDefinition.mId

    print(f"\nNode: {uid}")
    print(f"Type: {node_type}")

    # Get all parameters
    params = node.getParameters()
    print(f"Parameters ({len(params)}):")

    for param in params:
        param_id = param.mId
        param_value = param.mValue

        # Handle different parameter types
        if hasattr(param_value, 'mValue'):
            # Integer/Float parameter
            value = param_value.mValue
        elif hasattr(param_value, 'mValues'):
            # Vector parameter
            value = param_value.mValues
        else:
            value = str(param_value)

        print(f"  {param_id}: {value}")

# Extract from specific node type
for node in graph.getAllNodes():
    node_type = node.getCompImplementation().mDefinition.mId
    if node_type == "tile_sampler":
        extract_node_parameters(node)
```

---

### SBSConnection

Represents a connection (edge) between two nodes.

```python
connections = graph.getConnections()

for conn in connections:
    source = conn.getSourceNodeUID()
    target = conn.getTargetNodeUID()
    print(f"{source} -> {target}")
```

**Key Methods**:

| Method | Returns | Description |
|--------|---------|-------------|
| `getSourceNodeUID()` | `str` | Get UID of source node |
| `getTargetNodeUID()` | `str` | Get UID of target node |
| `getSourceOutputIdentifier()` | `str` | Get output connector identifier |
| `getTargetInputIdentifier()` | `str` | Get input connector identifier |

**Example: Build Connection Map**

```python
def build_connection_map(graph):
    """Build adjacency list of connections"""
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

# Usage
conn_map = build_connection_map(graph)

# Find what a specific node connects to
node_uid = "Blur_HQ_Grayscale_1"
if node_uid in conn_map:
    print(f"\n{node_uid} connects to:")
    for conn in conn_map[node_uid]:
        print(f"  -> {conn['target']} (in: {conn['target_input']})")
```

---

### SBSParameter

Represents a parameter value (node property, graph input, etc.).

```python
params = node.getParameters()

for param in params:
    print(f"{param.mId}: {param.mValue}")
```

**Key Attributes**:
- `mId` - Parameter identifier (e.g., "tiling", "rotation", "blendingmode")
- `mValue` - Parameter value (varies by type)

**Parameter Value Types**:

| Type | Python Type | Access |
|------|-------------|--------|
| Integer | `SBSParamValue` | `param.mValue.mValue` |
| Float | `SBSParamValue` | `param.mValue.mValue` |
| Vector2 | `SBSParamValue` | `param.mValue.mValues` (list) |
| Vector3 | `SBSParamValue` | `param.mValue.mValues` (list) |
| Vector4 | `SBSParamValue` | `param.mValue.mValues` (list) |
| String | `SBSParamValue` | `param.mValue.mValue` |
| Enum | `SBSParamValue` | `param.mValue.mValue` |

**Example: Extract All Parameters to Dict**

```python
def extract_all_parameters(graph):
    """Extract all parameters from all nodes"""
    result = {}

    for node in graph.getAllNodes():
        uid = node.getUid()
        node_params = {}

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

            node_params[param_id] = value

        result[uid] = {
            "type": node.getCompImplementation().mDefinition.mId,
            "parameters": node_params
        }

    return result

# Export to JSON
import json
params = extract_all_parameters(graph)
print(json.dumps(params, indent=2))
```

---

## Common Operations

### 1. Find Nodes by Type

```python
def find_nodes_by_type(graph, node_type):
    """Find all nodes of specific type"""
    matching = []

    for node in graph.getAllNodes():
        if node.getCompImplementation().mDefinition.mId == node_type:
            matching.append(node)

    return matching

# Find all Tile Samplers
tile_samplers = find_nodes_by_type(graph, "tile_sampler")
print(f"Found {len(tile_samplers)} Tile Sampler nodes")
```

### 2. Trace Upstream Dependencies

```python
def trace_upstream(graph, node_uid, visited=None):
    """Recursively trace all upstream nodes"""
    if visited is None:
        visited = set()

    if node_uid in visited:
        return visited

    visited.add(node_uid)

    # Get incoming connections
    node = graph.getNodeFromUid(node_uid)
    incoming = graph.getConnectionsToNode(node)

    for conn in incoming:
        source_uid = conn.getSourceNodeUID()
        trace_upstream(graph, source_uid, visited)

    return visited

# Trace dependencies for output node
output_node = graph.getAllOutputNodes()[0]
deps = trace_upstream(graph, output_node.getUid())
print(f"Output depends on {len(deps)} upstream nodes")
```

### 3. Check for 8-bit Inheritance

```python
def check_8bit_inheritance(graph):
    """Detect nodes using 8-bit output format"""
    issues = []

    for node in graph.getAllNodes():
        params = node.getParameters()

        for param in params:
            if param.mId == "outputformat":
                value = str(param.mValue)
                if "8" in value:
                    issues.append({
                        "node": node.getUid(),
                        "type": node.getCompImplementation().mDefinition.mId,
                        "format": value
                    })

    return issues

# Check for potential banding
issues = check_8bit_inheritance(graph)
if issues:
    print("WARNING: Found nodes using 8-bit output:")
    for issue in issues:
        print(f"  - {issue['node']} ({issue['type']})")
```

### 4. Export Graph Structure to JSON

```python
import json

def export_graph_structure(graph):
    """Export complete graph structure"""
    structure = {
        "identifier": graph.mIdentifier,
        "nodes": [],
        "connections": []
    }

    # Export nodes
    for node in graph.getAllNodes():
        structure["nodes"].append({
            "uid": node.getUid(),
            "type": node.getCompImplementation().mDefinition.mId,
            "position": node.getPosition()
        })

    # Export connections
    for conn in graph.getConnections():
        structure["connections"].append({
            "source": conn.getSourceNodeUID(),
            "target": conn.getTargetNodeUID(),
            "source_output": conn.getSourceOutputIdentifier(),
            "target_input": conn.getTargetInputIdentifier()
        })

    return json.dumps(structure, indent=2)

# Usage
json_output = export_graph_structure(graph)
print(json_output)
```

## Error Handling

```python
from pysbs import context, SBSDocument

def safe_load_document(filepath):
    """Load document with error handling"""
    try:
        ctx = context.Context()
        doc = SBSDocument(ctx, filepath)
        return doc
    except FileNotFoundError:
        print(f"ERROR: File not found: {filepath}")
        return None
    except Exception as e:
        print(f"ERROR loading document: {e}")
        return None

# Usage
doc = safe_load_document("material.sbs")
if doc:
    print("Document loaded successfully")
```

## Performance Tips

1. **Cache document context**: Reuse `Context()` instance for multiple documents
2. **Filter early**: Use `find_nodes_by_type()` before parameter extraction
3. **Avoid repeated traversals**: Build connection map once, reuse multiple times
4. **Batch operations**: Process multiple documents in single script run

## Complete Example: Comprehensive Graph Analysis

```python
import json
from pysbs import context, SBSDocument

def analyze_sbs_file(filepath):
    """Complete analysis of .sbs file"""
    # Load document
    ctx = context.Context()
    doc = SBSDocument(ctx, filepath)

    results = {
        "package": doc.getPackageUrl(),
        "graphs": []
    }

    # Analyze each graph
    for graph in doc.getGraphs():
        graph_data = {
            "identifier": graph.mIdentifier,
            "node_count": len(graph.getAllNodes()),
            "connection_count": len(graph.getConnections()),
            "output_count": len(graph.getAllOutputNodes()),
            "node_types": {},
            "parameters": {}
        }

        # Count node types
        for node in graph.getAllNodes():
            node_type = node.getCompImplementation().mDefinition.mId
            graph_data["node_types"][node_type] = \
                graph_data["node_types"].get(node_type, 0) + 1

        # Extract key parameters
        for node in graph.getAllNodes():
            uid = node.getUid()
            node_params = {}

            for param in node.getParameters():
                if hasattr(param.mValue, 'mValue'):
                    node_params[param.mId] = param.mValue.mValue
                elif hasattr(param.mValue, 'mValues'):
                    node_params[param.mId] = list(param.mValue.mValues)

            if node_params:
                graph_data["parameters"][uid] = node_params

        results["graphs"].append(graph_data)

    return json.dumps(results, indent=2)

# Run analysis
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print(analyze_sbs_file(sys.argv[1]))
    else:
        print("Usage: python script.py <path-to-sbs-file>")
```

## Further Reading

- Official documentation: Substance 3D Automation Toolkit docs
- Sample scripts: Check Designer installation `resources/python-samples/`
- API changelog: Track changes between Designer versions
