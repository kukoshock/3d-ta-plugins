# SBS File Format Reference

## Overview

.sbs files are **XML-based** text files that store Substance Designer graphs. Understanding the structure enables:
- Direct XML parsing (when pysbs is unavailable)
- Custom tooling development
- Format validation
- Debugging graph issues
- Version control diff analysis

**Format**: UTF-8 encoded XML
**Extension**: `.sbs`
**Root Element**: `<package>`

## File Structure Hierarchy

```
<package>
├── <identifier>          # Package name/identifier
├── <formatVersion>       # SBS format version
├── <updaterVersion>      # Last updater version
├── <fileUID>             # Unique file identifier (GUID)
├── <versionUID>          # Version identifier
├── <dependencies>        # External .sbs file references
│   └── <dependency>*     # Individual dependency entries
├── <content>             # Main content container
│   ├── <graph>*          # Graph definitions
│   │   ├── <identifier>
│   │   ├── <uid>
│   │   ├── <graphOutputs>
│   │   ├── <compNodes>   # Node definitions
│   │   │   └── <compNode>*
│   │   ├── <baseParameters>
│   │   ├── <connections> # Inter-node connections
│   │   └── <GUIObjects>  # UI layout (positions, comments)
│   └── <graphinstance>*  # Graph instances
└── <GUILayout>           # Global UI layout
```

## Core Elements

### Package Root

```xml
<package>
  <identifier v="Unsaved Package"/>
  <formatVersion v="1.1.0.202302"/>
  <updaterVersion v="1.1.0.202302"/>
  <fileUID v="{32f89606-e12a-47e6-aaf2-bfb86c1cc7f1}"/>
  <versionUID v="0"/>
  ...
</package>
```

**Elements**:
- `<identifier>` - Package name (string)
- `<formatVersion>` - SBS file format version (e.g., "1.1.0.202302")
- `<updaterVersion>` - Version of Designer that last updated file
- `<fileUID>` - Globally unique identifier (GUID)
- `<versionUID>` - Version number for tracking changes

### Dependencies

External .sbs files referenced by this package.

```xml
<dependencies>
  <dependency>
    <filename v="dependencies/pbr_base_material.sbs"/>
    <uid v="1490812440"/>
    <type v="package"/>
    <fileUID v="0"/>
    <versionUID v="0"/>
  </dependency>
  <dependency>
    <filename v="dependencies/rt_ao_v2.sbs"/>
    <uid v="1477525485"/>
    <type v="package"/>
    <fileUID v="0"/>
    <versionUID v="0"/>
  </dependency>
</dependencies>
```

**Dependency Fields**:
- `<filename>` - Relative path to dependency .sbs file
- `<uid>` - Unique ID for this dependency
- `<type>` - Type ("package" for .sbs files)
- `<fileUID>` - File unique identifier
- `<versionUID>` - Version identifier

**Why This Matters**: Missing dependencies will cause load failures. Track these for portability.

### Graph Definition

The core graph structure containing nodes and connections.

```xml
<content>
  <graph>
    <identifier v="Ornate_Fabric"/>
    <uid v="1737051906"/>
    <paraminputs/>
    <graphOutputs>
      <graphoutput>
        <identifier v="baseColor"/>
        <uid v="1737065664"/>
        <usages>
          <usage v="baseColor"/>
        </usages>
        <group v="Material"/>
        <format v="0"/>
      </graphoutput>
      <graphoutput>
        <identifier v="normal"/>
        <uid v="1737065665"/>
        <usages>
          <usage v="normal"/>
        </usages>
        <group v="Material"/>
        <format v="1"/>
      </graphoutput>
      <!-- More outputs... -->
    </graphOutputs>
    <compNodes>
      <!-- Node definitions here -->
    </compNodes>
    <baseParameters/>
    <connections>
      <!-- Connection definitions here -->
    </connections>
    <GUIObjects>
      <!-- UI layout here -->
    </GUIObjects>
  </graph>
</content>
```

**Graph Fields**:
- `<identifier>` - Graph name (shown in Designer)
- `<uid>` - Unique graph identifier
- `<graphOutputs>` - Output nodes (baseColor, normal, height, etc.)
- `<compNodes>` - All nodes in the graph
- `<connections>` - Links between nodes
- `<GUIObjects>` - UI-specific data (positions, comments)

### Graph Outputs

Define the final texture outputs.

```xml
<graphoutput>
  <identifier v="baseColor"/>
  <uid v="1737065664"/>
  <usages>
    <usage v="baseColor"/>
  </usages>
  <group v="Material"/>
  <format v="0"/>
  <mipmapMode v="3"/>
  <mipmapLevelCount v="0"/>
</graphoutput>
```

**Output Fields**:
- `<identifier>` - Output name
- `<uid>` - Unique identifier
- `<usages>` - Texture usage type (baseColor, normal, roughness, etc.)
- `<group>` - Category grouping
- `<format>` - Output format (0 = 8-bit, 1 = 16-bit, etc.)
- `<mipmapMode>` - Mipmap generation mode
- `<mipmapLevelCount>` - Number of mipmap levels

**Common Usage Types**:
- `baseColor` - Albedo/Diffuse
- `normal` - Normal map
- `height` - Height/Displacement
- `roughness` - Roughness
- `metallic` - Metallic
- `ambientOcclusion` - Ambient occlusion

### Nodes (compNodes)

Individual node definitions with parameters.

```xml
<compNodes>
  <compNode>
    <uid v="1737052104"/>
    <GUILayout>
      <gpos v="-832 48 0"/>
    </GUILayout>
    <compImplementation>
      <compInstance>
        <path v="pkg:///blend?dependency=1311189267"/>
      </compInstance>
    </compImplementation>
    <compInputs>
      <compInput>
        <identifier v="Source"/>
        <uid v="1737052105"/>
      </compInput>
      <compInput>
        <identifier v="Destination"/>
        <uid v="1737052106"/>
      </compInput>
    </compInputs>
    <compOutputs>
      <compOutput>
        <identifier v="Output"/>
        <uid v="1737052107"/>
      </compOutput>
    </compOutputs>
    <parameters>
      <parameter>
        <name v="blendingmode"/>
        <relativeTo v="0"/>
        <paramValue>
          <int v="13"/>
        </paramValue>
      </parameter>
      <parameter>
        <name v="opacity"/>
        <relativeTo v="0"/>
        <paramValue>
          <constantValueFloat1 v="1"/>
        </paramValue>
      </parameter>
    </parameters>
  </compNode>
  <!-- More nodes... -->
</compNodes>
```

**Node Structure**:
- `<uid>` - Unique node identifier
- `<GUILayout>/<gpos>` - Position in graph (x, y, z)
- `<compImplementation>` - Node type reference (Blend, Blur, etc.)
- `<compInputs>` - Input connectors
- `<compOutputs>` - Output connectors
- `<parameters>` - Node parameter values

**Parameter Types**:

```xml
<!-- Integer -->
<paramValue>
  <int v="13"/>
</paramValue>

<!-- Float -->
<paramValue>
  <constantValueFloat1 v="0.75"/>
</paramValue>

<!-- Vector2 -->
<paramValue>
  <constantValueFloat2 v="2 2"/>
</paramValue>

<!-- Vector3 -->
<paramValue>
  <constantValueFloat3 v="1 0.5 0"/>
</paramValue>

<!-- Vector4 -->
<paramValue>
  <constantValueFloat4 v="1 0.5 0 1"/>
</paramValue>

<!-- String -->
<paramValue>
  <string v="My Text"/>
</paramValue>
```

### Connections

Links between node inputs and outputs.

```xml
<connections>
  <connection>
    <identifier v="connection"/>
    <uid v="1737052108"/>
    <connRef>
      <connRefGraph>
        <graphIdentifier v="Ornate_Fabric"/>
      </connRefGraph>
      <connRefOutput>
        <nodeIdentifier v="1737052104"/>
        <connIdentifier v="1737052107"/>
      </connRefOutput>
    </connRef>
    <connRef>
      <connRefGraph>
        <graphIdentifier v="Ornate_Fabric"/>
      </connRefGraph>
      <connRefInput>
        <nodeIdentifier v="1737052200"/>
        <connIdentifier v="1737052201"/>
      </connRefInput>
    </connRef>
  </connection>
  <!-- More connections... -->
</connections>
```

**Connection Structure**:
- Two `<connRef>` entries: source output → target input
- `<connRefOutput>` - Source node UID + output connector UID
- `<connRefInput>` - Target node UID + input connector UID

**Reading Connections**:
1. First `<connRef>` = Source (output)
2. Second `<connRef>` = Target (input)
3. Match UIDs to nodes to trace data flow

### GUI Objects

UI-specific elements like comments and frames.

```xml
<GUIObjects>
  <GUIObject>
    <type v="FRAME"/>
    <uid v="1737052300"/>
    <GUILayout>
      <gpos v="-1024 -128 0"/>
      <size v="512 768"/>
    </GUILayout>
    <options>
      <option>
        <name v="FRAME_COLOR"/>
        <value v="0.2 0.4 0.6 0.5"/>
      </option>
      <option>
        <name v="FRAME_TITLE"/>
        <value v="Thread Generation"/>
      </option>
    </options>
  </GUIObject>
  <GUIObject>
    <type v="COMMENT"/>
    <uid v="1737052400"/>
    <GUILayout>
      <gpos v="-512 256 0"/>
    </GUILayout>
    <options>
      <option>
        <name v="COMMENT_TEXT"/>
        <value v="This blends the patterns"/>
      </option>
    </options>
  </GUIObject>
</GUIObjects>
```

**GUI Object Types**:
- `FRAME` - Colored boxes grouping nodes
- `COMMENT` - Text annotations
- `PIN` - Pinned nodes (marked for attention)

## Parsing Strategies

### 1. Python with ElementTree

```python
import xml.etree.ElementTree as ET

def parse_sbs(filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()

    # Get package identifier
    package_id = root.find('identifier').get('v')
    print(f"Package: {package_id}")

    # Get all graphs
    for graph in root.findall('.//content/graph'):
        graph_id = graph.find('identifier').get('v')
        print(f"Graph: {graph_id}")

        # Count nodes
        nodes = graph.find('compNodes').findall('compNode')
        print(f"  Nodes: {len(nodes)}")

        # Count connections
        connections = graph.find('connections').findall('connection')
        print(f"  Connections: {len(connections)}")

# Usage
parse_sbs("material.sbs")
```

### 2. Extract All Dependencies

```python
import xml.etree.ElementTree as ET

def extract_dependencies(filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()

    dependencies = []
    for dep in root.findall('.//dependency'):
        filename = dep.find('filename').get('v')
        uid = dep.find('uid').get('v')
        dependencies.append({
            "filename": filename,
            "uid": uid
        })

    return dependencies

# Usage
deps = extract_dependencies("material.sbs")
for dep in deps:
    print(f"{dep['filename']} (UID: {dep['uid']})")
```

### 3. Extract Node Parameters

```python
import xml.etree.ElementTree as ET

def extract_node_parameters(filepath, graph_id):
    tree = ET.parse(filepath)
    root = tree.getroot()

    # Find graph
    for graph in root.findall('.//content/graph'):
        if graph.find('identifier').get('v') == graph_id:
            # Extract all node parameters
            for node in graph.find('compNodes').findall('compNode'):
                uid = node.find('uid').get('v')
                print(f"\nNode: {uid}")

                params = node.find('parameters')
                if params:
                    for param in params.findall('parameter'):
                        name = param.find('name').get('v')
                        value_elem = param.find('paramValue')

                        # Try different value types
                        value = None
                        for child in value_elem:
                            value = child.get('v')
                            break

                        print(f"  {name}: {value}")

# Usage
extract_node_parameters("material.sbs", "Ornate_Fabric")
```

### 4. Build Connection Map

```python
import xml.etree.ElementTree as ET

def build_connection_map(filepath, graph_id):
    tree = ET.parse(filepath)
    root = tree.getroot()

    connections = {}

    for graph in root.findall('.//content/graph'):
        if graph.find('identifier').get('v') == graph_id:
            for conn in graph.find('connections').findall('connection'):
                refs = conn.findall('connRef')

                # First ref = output (source)
                # Second ref = input (target)
                if len(refs) >= 2:
                    source_node = refs[0].find('.//nodeIdentifier')
                    target_node = refs[1].find('.//nodeIdentifier')

                    if source_node is not None and target_node is not None:
                        source_uid = source_node.get('v')
                        target_uid = target_node.get('v')

                        if source_uid not in connections:
                            connections[source_uid] = []

                        connections[source_uid].append(target_uid)

    return connections

# Usage
conn_map = build_connection_map("material.sbs", "Ornate_Fabric")
for source, targets in conn_map.items():
    print(f"{source} -> {targets}")
```

## Common Node Types

Identified by `<compImplementation>/<compInstance>/<path>`:

| Path Pattern | Node Type |
|--------------|-----------|
| `pkg:///blend` | Blend |
| `pkg:///blur_hq_grayscale` | Blur HQ Grayscale |
| `pkg:///transformation_2d` | Transform 2D |
| `pkg:///uniform_color_grayscale` | Uniform Color |
| `pkg:///tile_sampler` | Tile Sampler |
| `pkg:///height_blend` | Height Blend |
| `pkg:///levels` | Levels |
| `pkg:///curve` | Curve |
| Custom paths | External graph nodes |

**External nodes** reference other .sbs files via dependency UIDs:
```xml
<path v="pkg:///pattern_fibers_1?dependency=1490990743"/>
```

## Format Versions

| Format Version | Designer Version | Notes |
|----------------|------------------|-------|
| 1.0.x | 2017-2018 | Legacy format |
| 1.1.0.x | 2019-2020 | Current format |
| 1.2.x | 2021+ | Latest with new features |

**Compatibility**: Newer Designer versions can read older formats. Older versions cannot read newer formats.

## Validation

Check for common issues:

1. **Missing Dependencies**: All referenced .sbs files exist
2. **Broken Connections**: Source/target node UIDs exist
3. **Invalid UIDs**: All UIDs are unique
4. **Orphaned Nodes**: Nodes not connected to outputs
5. **Format Version**: Compatible with target Designer version

## Editing SBS Files Directly

**⚠️ Warning**: Editing XML directly is risky. Always backup first.

**Safe Edits**:
- Update package identifier
- Change node positions (GUILayout)
- Modify comments and frames
- Update parameter values (if types match)

**Dangerous Edits**:
- Changing UIDs (breaks references)
- Adding/removing nodes (complex connections)
- Modifying graph structure
- Changing dependencies (can break loads)

**Best Practice**: Use pysbs for programmatic modifications.

## Version Control Tips

**.gitattributes** for better diffs:
```
*.sbs text eol=lf
```

Format XML for readability:
```python
import xml.etree.ElementTree as ET

tree = ET.parse("material.sbs")
ET.indent(tree, space="  ")  # Python 3.9+
tree.write("material.sbs", encoding="UTF-8", xml_declaration=True)
```

## Troubleshooting

### Issue: File Won't Load

**Check**:
1. Valid XML structure (`xmllint --noout file.sbs`)
2. All dependencies exist at specified paths
3. Format version compatible with Designer version
4. No duplicate UIDs

### Issue: Nodes Disappear

**Cause**: Likely missing `<compImplementation>` path

**Fix**: Verify all node paths are valid package references

### Issue: Connections Lost

**Cause**: UID mismatch between connection refs and nodes

**Fix**: Ensure all UIDs in connections match existing nodes

## Further Reading

- Substance Designer documentation (file format section)
- pysbs API reference for programmatic access
- Community forums for format changes and compatibility
