# sd.api - In-Application Scripting Reference

## Overview

The **sd.api** module provides Python scripting capabilities **within the Substance Designer application**. Unlike pysbs (which works offline), sd.api allows real-time interaction with the running application, the current graph, and the user interface.

**Primary Use Cases**:
- Building Designer plugins
- Creating custom tools and workflows
- Automating repetitive tasks within Designer
- Real-time parameter manipulation
- Responding to user actions

**Important**: sd.api is **only available when scripts run inside Substance Designer**. It cannot be used in standalone Python scripts.

## Accessing sd.api

### Method 1: Python Console (Designer 2019.2+)

1. Open Substance Designer
2. Go to **Window > Views > Python Console**
3. Type Python code directly:

```python
import sd
from sd.api.sdapplication import SDApplication

app = sd.getContext().getSDApplication()
print(f"Designer version: {app.getVersion()}")
```

### Method 2: Plugin Development

Create a plugin that loads when Designer starts:

```
plugins/
└── my_plugin/
    ├── __init__.py
    └── plugin.py
```

**__init__.py**:
```python
from . import plugin

def initializeSDPlugin():
    plugin.register()

def uninitializeSDPlugin():
    plugin.unregister()
```

### Method 3: Execute Script File

**Tools > Scripting > Run Script...** then select a .py file.

## Core Modules

### sd.getContext()

Entry point for accessing the Designer application context.

```python
import sd

ctx = sd.getContext()
app = ctx.getSDApplication()
```

**Returns**: `SDContext` object

---

### SDApplication

Represents the Substance Designer application. Access to UI manager, package manager, and preferences.

```python
from sd.api.sdapplication import SDApplication

app = sd.getContext().getSDApplication()

# Get version
version = app.getVersion()
print(f"Designer version: {version}")

# Get UI manager
ui_mgr = app.getUIMgr()

# Get package manager
pkg_mgr = app.getPackageMgr()
```

**Key Methods**:

| Method | Returns | Description |
|--------|---------|-------------|
| `getVersion()` | `str` | Get Designer version string |
| `getUIMgr()` | `SDUIMgr` | Get UI manager for graph/view access |
| `getPackageMgr()` | `SDPackageMgr` | Get package manager |
| `getPath(path_type)` | `str` | Get application paths |

---

### SDUIMgr - UI Manager

Access to current graph, selected nodes, and UI state.

```python
from sd.api.sduimgr import SDUIMgr

ui_mgr = sd.getContext().getSDApplication().getUIMgr()

# Get current graph
current_graph = ui_mgr.getCurrentGraph()

# Get selected nodes
selected = ui_mgr.getCurrentGraphSelection()
```

**Key Methods**:

| Method | Returns | Description |
|--------|---------|-------------|
| `getCurrentGraph()` | `SDGraph` | Get currently active graph |
| `getCurrentGraphSelection()` | `list[SDNode]` | Get selected nodes |
| `selectNodes(nodes)` | `None` | Set node selection |

**Example: Process Selected Nodes**

```python
import sd
from sd.api.sduimgr import SDUIMgr

ui_mgr = sd.getContext().getSDApplication().getUIMgr()

# Get current graph
graph = ui_mgr.getCurrentGraph()
if not graph:
    print("No graph open")
else:
    # Get selected nodes
    selected = ui_mgr.getCurrentGraphSelection()
    print(f"Selected {len(selected)} nodes:")

    for node in selected:
        definition = node.getDefinition()
        print(f"  - {definition.getId()}")
```

---

### SDGraph

Represents a graph within Designer. Access to nodes, properties, connections.

```python
graph = ui_mgr.getCurrentGraph()

# Get all nodes
nodes = graph.getNodes()

# Get specific node
node = graph.getNodeFromId("node_id")

# Get properties
props = graph.getProperties(sd.api.sdproperty.SDPropertyCategory.Input)
```

**Key Methods**:

| Method | Returns | Description |
|--------|---------|-------------|
| `getNodes()` | `list[SDNode]` | Get all nodes in graph |
| `getNodeFromId(id)` | `SDNode` | Get node by identifier |
| `getProperties(category)` | `list[SDProperty]` | Get properties by category |
| `getIdentifier()` | `str` | Get graph identifier |

**Property Categories**:
- `SDPropertyCategory.Input` - Graph input parameters
- `SDPropertyCategory.Output` - Output nodes
- `SDPropertyCategory.Annotation` - Comments and frames

---

### SDNode

Represents a node in the graph. Access to properties, connections, definition.

```python
node = graph.getNodeFromId("Blend_1")

# Get node definition (type)
definition = node.getDefinition()
node_type = definition.getId()

# Get properties
props = node.getProperties(sd.api.sdproperty.SDPropertyCategory.Input)
```

**Key Methods**:

| Method | Returns | Description |
|--------|---------|-------------|
| `getDefinition()` | `SDNodeDefinition` | Get node type definition |
| `getProperties(category)` | `list[SDProperty]` | Get node properties |
| `getPropertyValue(prop)` | varies | Get property value |
| `setInputPropertyValue(method, prop_id, value)` | `None` | Set property value |
| `getIdentifier()` | `str` | Get node identifier |

**Example: Read Node Parameters**

```python
import sd
from sd.api.sdproperty import SDPropertyCategory

ui_mgr = sd.getContext().getSDApplication().getUIMgr()
graph = ui_mgr.getCurrentGraph()

# Get all nodes
for node in graph.getNodes():
    print(f"\nNode: {node.getIdentifier()}")
    print(f"Type: {node.getDefinition().getId()}")

    # Get input properties
    inputs = node.getProperties(SDPropertyCategory.Input)
    print(f"Input properties: {len(inputs)}")

    for prop in inputs:
        prop_id = prop.getId()
        value = node.getPropertyValue(prop)
        print(f"  {prop_id}: {value}")
```

---

### SDProperty

Represents a node property (parameter).

```python
props = node.getProperties(SDPropertyCategory.Input)

for prop in props:
    prop_id = prop.getId()
    prop_type = prop.getType()
    print(f"{prop_id} ({prop_type})")
```

**Key Methods**:

| Method | Returns | Description |
|--------|---------|-------------|
| `getId()` | `str` | Get property identifier |
| `getType()` | `SDType` | Get property type |
| `getLabel()` | `str` | Get display label |

---

## Common Operations

### 1. Get Current Graph and Nodes

```python
import sd

ctx = sd.getContext()
ui_mgr = ctx.getSDApplication().getUIMgr()

# Get current graph
graph = ui_mgr.getCurrentGraph()
if graph:
    print(f"Current graph: {graph.getIdentifier()}")

    # Get all nodes
    nodes = graph.getNodes()
    print(f"Total nodes: {len(nodes)}")
else:
    print("No graph currently open")
```

### 2. Modify Node Parameters

```python
import sd
from sd.api.sdproperty import SDPropertyInheritanceMethod

ui_mgr = sd.getContext().getSDApplication().getUIMgr()
graph = ui_mgr.getCurrentGraph()

# Get specific node
node = graph.getNodeFromId("Blur_HQ_Grayscale_1")

if node:
    # Set parameter value
    # Method: Absolute (override), Relative (inherit), or RelativeToParent
    node.setInputPropertyValue(
        SDPropertyInheritanceMethod.Absolute,
        "intensity",  # parameter ID
        0.5           # new value
    )
    print("Parameter updated")
```

### 3. Batch Update Selected Nodes

```python
import sd
from sd.api.sdproperty import SDPropertyInheritanceMethod

ui_mgr = sd.getContext().getSDApplication().getUIMgr()

# Get selected nodes
selected = ui_mgr.getCurrentGraphSelection()

if not selected:
    print("No nodes selected")
else:
    print(f"Updating {len(selected)} nodes...")

    for node in selected:
        # Set all to 16-bit output
        try:
            node.setInputPropertyValue(
                SDPropertyInheritanceMethod.Absolute,
                "outputformat",
                "1"  # 16-bit
            )
            print(f"  Updated: {node.getIdentifier()}")
        except:
            # Not all nodes have outputformat
            pass

    print("Batch update complete")
```

### 4. Find Nodes by Type

```python
import sd

ui_mgr = sd.getContext().getSDApplication().getUIMgr()
graph = ui_mgr.getCurrentGraph()

# Find all Tile Sampler nodes
tile_samplers = []
for node in graph.getNodes():
    if node.getDefinition().getId() == "tile_sampler":
        tile_samplers.append(node)

print(f"Found {len(tile_samplers)} Tile Sampler nodes:")
for node in tile_samplers:
    print(f"  - {node.getIdentifier()}")
```

### 5. Export Parameter Values

```python
import sd
import json
from sd.api.sdproperty import SDPropertyCategory

ui_mgr = sd.getContext().getSDApplication().getUIMgr()
graph = ui_mgr.getCurrentGraph()

# Export all parameters to dict
export_data = {}

for node in graph.getNodes():
    node_id = node.getIdentifier()
    node_data = {
        "type": node.getDefinition().getId(),
        "parameters": {}
    }

    # Get input properties
    inputs = node.getProperties(SDPropertyCategory.Input)
    for prop in inputs:
        prop_id = prop.getId()
        try:
            value = node.getPropertyValue(prop)
            # Convert to serializable format
            node_data["parameters"][prop_id] = str(value)
        except:
            pass

    export_data[node_id] = node_data

# Output JSON
print(json.dumps(export_data, indent=2))
```

## Plugin Development

### Basic Plugin Structure

**my_plugin/plugin.py**:

```python
import sd
from sd.api.sduimgr import SDUIMgr

class MyPlugin:
    def __init__(self):
        self.app = sd.getContext().getSDApplication()
        print("MyPlugin initialized")

    def execute(self):
        """Main plugin functionality"""
        ui_mgr = self.app.getUIMgr()
        graph = ui_mgr.getCurrentGraph()

        if graph:
            nodes = graph.getNodes()
            print(f"Current graph has {len(nodes)} nodes")
        else:
            print("No graph open")

# Global instance
_plugin = None

def register():
    global _plugin
    _plugin = MyPlugin()
    print("Plugin registered")

def unregister():
    global _plugin
    _plugin = None
    print("Plugin unregistered")

# For testing in console
if __name__ == "__main__":
    plugin = MyPlugin()
    plugin.execute()
```

### Adding UI Menu Items

```python
import sd
from sd.api.sdapplication import SDApplication
from PySide2 import QtWidgets

def create_menu_action():
    """Add menu item to Designer"""
    app = sd.getContext().getSDApplication()
    ui_mgr = app.getUIMgr()

    # Create action
    action = QtWidgets.QAction("My Custom Tool", None)
    action.triggered.connect(on_menu_triggered)

    # Add to menu (requires Designer 2020.1+)
    # Note: Menu integration varies by Designer version
    return action

def on_menu_triggered():
    """Called when menu item clicked"""
    ui_mgr = sd.getContext().getSDApplication().getUIMgr()
    graph = ui_mgr.getCurrentGraph()

    if graph:
        nodes = len(graph.getNodes())
        QtWidgets.QMessageBox.information(
            None,
            "Graph Info",
            f"Current graph has {nodes} nodes"
        )
    else:
        QtWidgets.QMessageBox.warning(
            None,
            "No Graph",
            "Please open a graph first"
        )
```

## Property Inheritance Methods

When setting property values, specify how the value should be applied:

```python
from sd.api.sdproperty import SDPropertyInheritanceMethod

# Absolute: Override any inheritance
node.setInputPropertyValue(
    SDPropertyInheritanceMethod.Absolute,
    "param_name",
    value
)

# Relative: Inherit from parent and modify
node.setInputPropertyValue(
    SDPropertyInheritanceMethod.Relative,
    "param_name",
    value
)

# RelativeToParent: Inherit from direct parent only
node.setInputPropertyValue(
    SDPropertyInheritanceMethod.RelativeToParent,
    "param_name",
    value
)
```

## Working with Values

### Value Types

Different properties expect different value types:

```python
# Integer parameter
node.setInputPropertyValue(method, "param", 5)

# Float parameter
node.setInputPropertyValue(method, "intensity", 0.75)

# String parameter
node.setInputPropertyValue(method, "label", "My Node")

# Enum parameter (as integer index)
node.setInputPropertyValue(method, "blendingmode", 0)

# Vector2 parameter
from sd.api.sdbasetypes import float2
node.setInputPropertyValue(method, "tiling", float2(2.0, 2.0))

# Vector3 parameter
from sd.api.sdbasetypes import float3
node.setInputPropertyValue(method, "color", float3(1.0, 0.5, 0.0))

# Vector4 parameter
from sd.api.sdbasetypes import float4
node.setInputPropertyValue(method, "rgba", float4(1.0, 0.5, 0.0, 1.0))
```

## Complete Example: Parameter Analysis Tool

```python
"""
Parameter Analysis Tool
Analyzes current graph and reports parameter statistics
"""
import sd
from sd.api.sdproperty import SDPropertyCategory
from collections import defaultdict

def analyze_graph_parameters():
    """Analyze all parameters in current graph"""
    ui_mgr = sd.getContext().getSDApplication().getUIMgr()
    graph = ui_mgr.getCurrentGraph()

    if not graph:
        print("ERROR: No graph open")
        return

    print(f"\n=== Graph: {graph.getIdentifier()} ===\n")

    # Statistics
    stats = {
        "total_nodes": 0,
        "total_parameters": 0,
        "parameter_types": defaultdict(int),
        "node_types": defaultdict(int)
    }

    # Analyze each node
    for node in graph.getNodes():
        stats["total_nodes"] += 1
        node_type = node.getDefinition().getId()
        stats["node_types"][node_type] += 1

        # Get input properties
        inputs = node.getProperties(SDPropertyCategory.Input)

        for prop in inputs:
            stats["total_parameters"] += 1
            prop_type = str(prop.getType())
            stats["parameter_types"][prop_type] += 1

    # Print report
    print(f"Total Nodes: {stats['total_nodes']}")
    print(f"Total Parameters: {stats['total_parameters']}")

    print("\nNode Types:")
    for node_type, count in sorted(stats["node_types"].items()):
        print(f"  {node_type}: {count}")

    print("\nParameter Types:")
    for param_type, count in sorted(stats["parameter_types"].items()):
        print(f"  {param_type}: {count}")

# Run analysis
if __name__ == "__main__":
    analyze_graph_parameters()
```

## Limitations

1. **Application must be running**: sd.api only works inside Designer
2. **Version compatibility**: API may change between Designer versions
3. **No file I/O**: Cannot load/save .sbs files directly (use pysbs instead)
4. **Thread safety**: Scripts run on main thread, blocking UI
5. **Limited node creation**: Creating nodes programmatically is complex

## When to Use sd.api vs pysbs

| Task | Use sd.api | Use pysbs |
|------|-----------|-----------|
| Analyze .sbs files offline | ✗ | ✓ |
| Batch process multiple files | ✗ | ✓ |
| CI/CD integration | ✗ | ✓ |
| Real-time parameter tweaking | ✓ | ✗ |
| Respond to user actions | ✓ | ✗ |
| Build Designer plugins | ✓ | ✗ |
| Access current selection | ✓ | ✗ |
| Modify graphs while editing | ✓ | ✗ |

## Debugging Tips

```python
# Print all available methods
import sd
app = sd.getContext().getSDApplication()
print(dir(app))

# Inspect property
prop = node.getProperties(SDPropertyCategory.Input)[0]
print(f"ID: {prop.getId()}")
print(f"Type: {prop.getType()}")
print(f"Label: {prop.getLabel()}")

# Try-except for robustness
try:
    value = node.getPropertyValue(prop)
    print(f"Value: {value}")
except Exception as e:
    print(f"Error getting value: {e}")
```

## Further Reading

- Designer Python API documentation (in Designer: Help > Scripting Documentation)
- Sample scripts: `resources/python-samples/` in Designer installation
- Plugin examples: Check community plugins on Substance Share
