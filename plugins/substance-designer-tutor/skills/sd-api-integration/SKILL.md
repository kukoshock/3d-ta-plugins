---
name: Substance Designer API Integration
description: >
  Use this skill when the user needs to interact with Substance Designer
  programmatically. Covers pysbs for .sbs file analysis, sd.api for runtime
  scripting, sbsrender/sbscooker for batch rendering, and graph structure
  parsing. Triggers on: "read SD graph", "analyze sbs file", "pysbs",
  "sd.api", "sbsrender", "batch render", "extract node parameters",
  "parse substance graph", "automate substance designer", "analyze my graph",
  "read nodes", "extract parameters", "graph structure"
---

# Substance Designer API Integration

## Attribution & Scope

This skill enables **Technical Artists** and **Pipeline Engineers** to interact with Substance Designer programmatically. It complements the main tutor skill by providing automation and analysis capabilities rather than artist-focused learning guidance.

**Scope**: This skill focuses on:
- Reading and analyzing .sbs files
- Extracting graph structure and parameters
- Batch rendering workflows
- Diagnostic analysis comparing against course best practices
- Guiding script development for automation

**Out of Scope**:
- Artist-focused explanations of visual outcomes (use tutor skill)
- Teaching procedural texture theory (use tutor skill)
- Creating new graphs from scratch (use Designer UI)

**Handoff to Tutor**: If user asks "why does this look wrong?" or "how do I make this better visually?", direct to the tutor skill.

## Capabilities

This skill provides **six types of capabilities**:

### 1. Analyze Graph Structure
- Extract all nodes, connections, and data flow from .sbs files
- Build adjacency maps showing dependencies
- Identify graph topology (tree, DAG, etc.)
- Report metadata (author, creation date, version)

### 2. Extract Parameters
- Read all node parameter values
- Export parameter sets to JSON/CSV
- Compare parameters across multiple graphs
- Track inheritance settings (8-bit, 16-bit, Absolute, etc.)

### 3. Guide pysbs Development
- Provide code examples for common operations
- Explain pysbs API methods and classes
- Debug pysbs scripts
- Guide installation and setup

### 4. Guide sd.api Development
- Explain in-application scripting
- Provide plugin development patterns
- Show how to access current graph via `sduimgr`
- Guide real-time parameter manipulation

### 5. CLI Tools Execution
- Generate sbsrender commands for batch rendering
- Create sbscooker commands for publishing SBSAR
- Parse render logs and error output
- Pipeline integration guidance

### 6. Diagnostic Analysis
- Detect common issues by comparing to course best practices
- Flag potential problems (8-bit chains, missing connections, etc.)
- Suggest improvements with WHY explanations linked to tutor knowledge
- Generate diagnostic reports

## API Overview

Substance Designer provides **three programmatic interfaces**:

| API | Language | Use Case | SD Running? | Claude Executes? |
|-----|----------|----------|-------------|------------------|
| **pysbs** | Python | File-based analysis, batch ops, CI/CD | No | **Yes** |
| **sd.api** | Python | Live interaction, plugins, real-time | Yes | No (guide only) |
| **CLI Tools** | Shell | Batch rendering, publishing | No | **Yes** |

### Selection Criteria

**Use pysbs when:**
- Analyzing .sbs files without opening Designer
- Batch processing multiple files
- CI/CD pipeline integration
- Extracting data for external tools

**Use sd.api when:**
- Building Designer plugins
- Real-time graph manipulation
- Interactive tools within Designer
- Responding to user actions in the application

**Use CLI Tools when:**
- Rendering textures in batch
- Publishing SBSAR files for distribution
- Integration with external render pipelines
- Automated testing of material outputs

## Core Workflows

### Workflow 1: Analyze .sbs File with pysbs

**User Request**: "Analyze my graph at [path]"

**Steps**:
1. Verify file exists
2. Check if pysbs is available (import test)
3. Run analysis script or guide setup
4. Extract: graphs, nodes, connections, parameters
5. Compare against course best practices
6. Report findings with suggestions

**Example Code**:
```python
from pysbs import context, SBSDocument

# Load document
ctx = context.Context()
doc = SBSDocument(ctx, "path/to/file.sbs")

# Get all graphs
graphs = doc.getGraphs()
print(f"Found {len(graphs)} graphs")

# Analyze first graph
graph = graphs[0]
nodes = graph.getAllNodes()
connections = graph.getConnections()

print(f"Nodes: {len(nodes)}")
print(f"Connections: {len(connections)}")

# Get node details
for node in nodes:
    uid = node.getUid()
    impl = node.getCompImplementation()
    params = node.getParameters()
    print(f"{uid}: {impl.mDefinition.mId}")
```

### Workflow 2: Extract Parameters to JSON

**User Request**: "Export all parameters from my graph"

**Steps**:
1. Load .sbs file with pysbs
2. Iterate through all nodes
3. Extract parameter values
4. Format as JSON
5. Save or display results

**Example Code**:
```python
import json
from pysbs import context, SBSDocument

def extract_parameters(sbs_path):
    ctx = context.Context()
    doc = SBSDocument(ctx, sbs_path)

    result = {}
    for graph in doc.getGraphs():
        graph_data = {}
        for node in graph.getAllNodes():
            uid = node.getUid()
            params = {}
            for param in node.getParameters():
                params[param.mId] = param.mValue
            graph_data[uid] = {
                "type": node.getCompImplementation().mDefinition.mId,
                "parameters": params
            }
        result[graph.mIdentifier] = graph_data

    return json.dumps(result, indent=2)

print(extract_parameters("material.sbs"))
```

### Workflow 3: Batch Render Textures

**User Request**: "Render all outputs from my graph"

**Steps**:
1. Identify .sbs file and graph to render
2. Determine output resolution and format
3. Generate sbsrender command
4. Execute and capture output
5. Parse logs for errors

**Example Command**:
```bash
sbsrender render \
  --input "path/to/file.sbs" \
  --output-path "./output/{inputGraphUrl}_{outputNodeName}" \
  --output-format png \
  --set-value $outputsize@11,11 \
  --engine d3d11pc
```

**With multiple graphs**:
```bash
# Render all graphs in a file
sbsrender render \
  --input "materials.sbs" \
  --input-graph "*" \
  --output-path "./renders/{inputGraphUrl}/{outputNodeName}" \
  --output-format tga \
  --set-value $outputsize@12,12
```

### Workflow 4: Detect Issues Against Course Best Practices

**User Request**: "What's wrong with my graph?"

**Steps**:
1. Load graph with pysbs
2. Analyze node configurations
3. Check against diagnostic rules (see references/diagnostic-rules.md)
4. Report issues with tutor references
5. Suggest fixes with WHY explanations

**Example Diagnostics**:
```python
def detect_issues(graph):
    issues = []

    # Check for 8-bit inheritance in grayscale chains
    for node in graph.getAllNodes():
        params = node.getParameters()
        for param in params:
            if param.mId == 'outputFormat' and '8' in str(param.mValue):
                # Check if connected to grayscale operations
                connections = graph.getConnectionsFromNode(node)
                for conn in connections:
                    target = graph.getNodeFromUid(conn.getTargetNodeUID())
                    if is_grayscale_node(target):
                        issues.append({
                            "node": node.getUid(),
                            "type": "8-bit inheritance",
                            "severity": "high",
                            "reference": "troubleshooting.md - Banding in Gradients",
                            "fix": "Set to 16-bit Absolute to prevent banding"
                        })

    return issues
```

### Workflow 5: Guide sd.api Plugin Development

**User Request**: "Help me write a plugin to batch-update parameters"

**Steps**:
1. Explain sd.api availability (only within Designer)
2. Provide plugin structure template
3. Show how to access current graph
4. Guide parameter manipulation
5. Explain plugin registration

**Example Code**:
```python
# sd.api plugin example (runs inside Designer)
import sd
from sd.api.sdapplication import SDApplicationPath
from sd.api.sduimgr import SDUIMgr

# Get current graph
uiMgr = sd.getContext().getSDApplication().getUIMgr()
currentGraph = uiMgr.getCurrentGraph()

if currentGraph:
    # Get all nodes
    nodes = currentGraph.getNodes()

    for node in nodes:
        # Update parameter
        node.setInputPropertyValue(
            sd.api.sdproperty.SDPropertyInheritanceMethod.Absolute,
            "output_format",
            "16"
        )

    print(f"Updated {len(nodes)} nodes")
```

## Environment Detection

Before executing pysbs operations, check:

1. **Is pysbs importable?**
   ```bash
   python -c "import pysbs; print('pysbs available')"
   ```

2. **If not available**, guide user to:
   - **Option A**: Use SD installation path
     ```
     Windows: C:\Program Files\Adobe\Adobe Substance 3D Designer\resources\python-packages
     macOS: /Applications/Adobe Substance 3D Designer.app/Contents/Resources/python-packages
     ```
   - **Option B**: Install via pip
     ```bash
     pip install substance-automation-toolkit
     ```

3. **Store working setup** for session to avoid repeated checks

## Direct Execution Capability

When user provides an .sbs file path, Claude can:

1. **Verify file exists** using file system tools
2. **Run analysis script** (see references/analysis-script.py)
3. **Parse output** and present findings
4. **Compare against best practices** using diagnostic rules
5. **Suggest improvements** based on tutor knowledge

**Example Interaction**:
```
User: "Analyze my graph at D:\project\material.sbs"

Claude:
1. Verifies file exists ✓
2. Runs: python analysis-script.py "D:\project\material.sbs"
3. Reports:
   - 47 nodes found
   - 6 output nodes (baseColor, normal, height, roughness, metallic, ao)
   - 3 potential issues detected:
     * Node "Blur_HQ_Grayscale_1" using 8-bit output (risk of banding)
     * Tile Sampler "Pattern_1" missing scale map input
     * Height Blend "Combine_1" missing height input on connector 1
4. Suggests fixes with course references
```

## Reference Files

This skill includes comprehensive reference documentation:

- **[pysbs-api.md](${CLAUDE_PLUGIN_ROOT}/skills/sd-api-integration/references/pysbs-api.md)** - Complete pysbs API reference with classes and methods
- **[sd-api.md](${CLAUDE_PLUGIN_ROOT}/skills/sd-api-integration/references/sd-api.md)** - In-application scripting guide
- **[cli-tools.md](${CLAUDE_PLUGIN_ROOT}/skills/sd-api-integration/references/cli-tools.md)** - sbsrender and sbscooker documentation
- **[sbs-file-format.md](${CLAUDE_PLUGIN_ROOT}/skills/sd-api-integration/references/sbs-file-format.md)** - XML structure of .sbs files
- **[graph-analysis-patterns.md](${CLAUDE_PLUGIN_ROOT}/skills/sd-api-integration/references/graph-analysis-patterns.md)** - Code recipes for common tasks
- **[diagnostic-rules.md](${CLAUDE_PLUGIN_ROOT}/skills/sd-api-integration/references/diagnostic-rules.md)** - Issue detection patterns linked to tutor knowledge
- **[analysis-script.py](${CLAUDE_PLUGIN_ROOT}/skills/sd-api-integration/references/analysis-script.py)** - Standalone analysis script
- **[troubleshooting.md](${CLAUDE_PLUGIN_ROOT}/skills/sd-api-integration/references/troubleshooting.md)** - Common errors and solutions

## Integration with Tutor Skill

**This skill complements the tutor skill**:

| Aspect | Tutor Skill | API Integration Skill |
|--------|-------------|----------------------|
| Audience | 3D Artists learning SD | Technical Artists automating SD |
| Focus | Visual outcomes, WHY explanations | Data extraction, automation |
| Interaction | Teaching concepts | Executing analysis, guiding code |
| Questions | "Why is this banding?" | "How do I detect banding in code?" |
| Output | Conceptual understanding | Scripts, data, diagnostics |

**When to handoff**:
- User asks "why" about visual results → Tutor skill
- User asks "how to automate/extract/analyze" → This skill
- User mentions "learn", "understand procedural" → Tutor skill
- User mentions "script", "pysbs", "batch render" → This skill

## Skill Activation Examples

| User Input | Skill Action |
|------------|--------------|
| "Analyze my .sbs file at C:/project/mat.sbs" | Execute pysbs, report structure, flag issues |
| "How do I read nodes with pysbs?" | Provide code examples from pysbs-api.md |
| "What's wrong with my graph?" (with file path) | Full diagnostic with tutor-based suggestions |
| "Help me write a script to extract parameters" | Guide through pysbs or sd.api based on context |
| "Batch render all my materials" | Provide sbsrender commands and script template |
| "Parse this sbs file structure" | Explain XML format, provide parsing code |
| "How do I create a Designer plugin?" | Guide sd.api plugin development |
| "Extract all Tile Sampler parameters" | Run targeted parameter extraction |

## Error Handling

When errors occur during execution:

1. **pysbs import fails**: Guide installation (see troubleshooting.md)
2. **File not found**: Verify path, suggest correction
3. **Parsing errors**: Check file format, SD version compatibility
4. **Permission errors**: Guide user to run with appropriate permissions
5. **API errors**: Consult troubleshooting.md for known issues

## Output Formats

Analysis results can be presented as:

- **Text summary**: Human-readable findings
- **JSON**: Structured data for further processing
- **Markdown tables**: Node lists, parameter comparisons
- **Diagnostic report**: Issues with severity, references, and fixes

User can request specific format: "export as JSON" or "show as table"

## Security Considerations

- **Only read operations**: This skill performs read-only analysis
- **File path validation**: Verify paths before accessing
- **No external network**: All operations local
- **User confirmation**: Ask before executing scripts on user files

## Best Practices

1. **Always verify file exists** before pysbs operations
2. **Check pysbs availability** before attempting imports
3. **Link diagnostics to tutor knowledge** for educational value
4. **Provide working code examples** not just API listings
5. **Explain WHY** issues matter (link to visual outcomes)
6. **Offer multiple approaches** (pysbs vs sd.api vs CLI)
7. **Test commands before suggesting** to user

## Future Enhancements

Potential expansions (not yet implemented):

- Write operations (modify parameters, add nodes)
- SBSAR inspection (package contents, exposed parameters)
- Dependency graph visualization (Mermaid diagrams)
- Parameter diff tool (compare versions)
- Automated regression testing (render comparisons)
