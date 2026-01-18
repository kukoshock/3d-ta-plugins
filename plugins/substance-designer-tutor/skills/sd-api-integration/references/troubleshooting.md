# Troubleshooting Guide

## Overview

Common issues when working with Substance Designer APIs (pysbs, sd.api, CLI tools) and their solutions.

## Categories

1. [pysbs Installation & Import](#pysbs-installation--import)
2. [sd.api Availability](#sdapi-availability)
3. [File Loading Errors](#file-loading-errors)
4. [Permission & Access Issues](#permission--access-issues)
5. [CLI Tool Errors](#cli-tool-errors)
6. [Data Extraction Issues](#data-extraction-issues)
7. [Performance Problems](#performance-problems)

---

## pysbs Installation & Import

### Error: "ModuleNotFoundError: No module named 'pysbs'"

**Cause**: pysbs not installed or not in PYTHONPATH

**Solution 1: Install via pip**
```bash
pip install substance-automation-toolkit
```

**Solution 2: Use Designer's Python environment**

Windows:
```powershell
$env:PYTHONPATH = "C:\Program Files\Adobe\Adobe Substance 3D Designer\resources\python-packages"
python your_script.py
```

macOS:
```bash
export PYTHONPATH="/Applications/Adobe Substance 3D Designer.app/Contents/Resources/python-packages"
python your_script.py
```

Linux:
```bash
export PYTHONPATH="/opt/Allegorithmic/Substance_Designer/resources/python-packages"
python your_script.py
```

**Solution 3: Use Designer's Python directly**

Windows:
```powershell
& "C:\Program Files\Adobe\Adobe Substance 3D Designer\resources\pythonsdk\python.exe" your_script.py
```

macOS:
```bash
"/Applications/Adobe Substance 3D Designer.app/Contents/Resources/pythonsdk/bin/python" your_script.py
```

**Verification**:
```bash
python -c "import pysbs; print('pysbs available')"
```

---

### Error: "ImportError: DLL load failed while importing pysbs"

**Cause**: Missing dependencies or incompatible Python version

**Solution 1**: Use Python 3.7-3.10 (pysbs compatibility range)

**Solution 2**: Use Designer's bundled Python (guaranteed compatible)

**Solution 3**: Install required dependencies
```bash
pip install --upgrade substance-automation-toolkit
```

**Windows Specific**: Install Visual C++ Redistributable
- Download from Microsoft website
- Install both x86 and x64 versions

---

### Error: "AttributeError: module 'pysbs' has no attribute 'context'"

**Cause**: Incorrect import or outdated pysbs version

**Fix**:
```python
# Correct import
from pysbs import context

# NOT:
import pysbs
pysbs.context.Context()  # This won't work
```

**Update pysbs**:
```bash
pip install --upgrade substance-automation-toolkit
```

---

## sd.api Availability

### Error: "ModuleNotFoundError: No module named 'sd'"

**Cause**: sd.api only available within Substance Designer

**Solution**: sd.api cannot be used in standalone Python scripts. Options:

1. **Run script inside Designer**:
   - Tools > Scripting > Run Script...
   - Select your .py file

2. **Use Python Console**:
   - Window > Views > Python Console
   - Type code directly or paste

3. **Create a plugin**:
   - See [sd-api.md](./sd-api.md) for plugin structure

**For offline analysis**: Use pysbs instead of sd.api

---

### Error: "AttributeError: 'NoneType' object has no attribute..."

**Cause**: Trying to access Designer context without active graph

**Fix**: Check if graph exists first
```python
import sd

ui_mgr = sd.getContext().getSDApplication().getUIMgr()
graph = ui_mgr.getCurrentGraph()

if graph is None:
    print("ERROR: No graph currently open")
else:
    # Safe to use graph
    nodes = graph.getNodes()
```

---

## File Loading Errors

### Error: "FileNotFoundError: [Errno 2] No such file or directory"

**Cause**: Incorrect file path or file doesn't exist

**Solution 1**: Use absolute paths
```python
# Instead of:
doc = SBSDocument(ctx, "material.sbs")

# Use:
import os
filepath = os.path.abspath("material.sbs")
doc = SBSDocument(ctx, filepath)
```

**Solution 2**: Verify file exists
```python
from pathlib import Path

filepath = "path/to/material.sbs"
if not Path(filepath).exists():
    print(f"ERROR: File not found: {filepath}")
else:
    doc = SBSDocument(ctx, filepath)
```

**Solution 3**: Check working directory
```python
import os
print(f"Current directory: {os.getcwd()}")
```

---

### Error: "Failed to load package dependencies"

**Cause**: Referenced .sbs files not found at expected paths

**Diagnosis**:
```python
from pysbs import context, SBSDocument

ctx = context.Context()
doc = SBSDocument(ctx, "material.sbs")

# List dependencies
deps = doc.getDependencies()
for dep in deps:
    print(f"Dependency: {dep.mFilePath}")
    # Check if file exists
    from pathlib import Path
    if not Path(dep.mFilePath).exists():
        print(f"  ⚠ MISSING: {dep.mFilePath}")
```

**Solution**: Ensure all dependency .sbs files are in correct locations relative to main file

**Workaround**: Copy missing dependencies from Designer installation:
```
C:\Program Files\Adobe\Adobe Substance 3D Designer\resources\packages\
```

---

### Error: "XML parsing error" or "Invalid SBS format"

**Cause**: Corrupted .sbs file or incompatible version

**Solution 1**: Open in Designer and re-save
- Fixes most corruption issues
- Updates to current format version

**Solution 2**: Check file format version
```bash
# Windows (PowerShell)
Select-String -Path "material.sbs" -Pattern "formatVersion" | Select-Object -First 1

# macOS/Linux
grep "formatVersion" material.sbs | head -n 1
```

**Solution 3**: Use sbsupdater to update format
```bash
sbsupdater --input old_material.sbs --output updated_material.sbs
```

---

## Permission & Access Issues

### Error: "PermissionError: [Errno 13] Permission denied"

**Cause**: File locked by another process or insufficient permissions

**Solution 1**: Close Designer (file may be locked)

**Solution 2**: Check file permissions
```bash
# Windows
icacls material.sbs

# macOS/Linux
ls -l material.sbs
```

**Solution 3**: Run as administrator (Windows) or with sudo (macOS/Linux)
```bash
# Windows (Run PowerShell as Administrator)
python script.py

# macOS/Linux
sudo python script.py
```

**Solution 4**: Copy file to temp location
```python
import shutil
shutil.copy("locked_file.sbs", "temp_copy.sbs")
# Work with temp_copy.sbs instead
```

---

### Error: "Cannot write to output directory"

**Cause**: Output directory doesn't exist or no write permissions

**Solution**: Create directory first
```python
from pathlib import Path

output_dir = Path("./output")
output_dir.mkdir(parents=True, exist_ok=True)

# Now safe to write
with open(output_dir / "result.json", "w") as f:
    f.write(data)
```

---

## CLI Tool Errors

### Error: "'sbsrender' is not recognized as an internal or external command"

**Cause**: CLI tools not in system PATH

**Solution**: Add Designer installation to PATH

Windows (PowerShell):
```powershell
$env:Path += ";C:\Program Files\Adobe\Adobe Substance 3D Designer"
sbsrender --version
```

macOS:
```bash
export PATH="/Applications/Adobe Substance 3D Designer.app/Contents/MacOS:$PATH"
sbsrender --version
```

**Permanent Solution**:
- Windows: Add to System Environment Variables
- macOS/Linux: Add export to ~/.bashrc or ~/.zshrc

---

### Error: "No valid license found"

**Cause**: Designer not activated

**Solution**: Run Designer GUI to activate license
1. Open Substance Designer
2. Sign in with Adobe account
3. Activate license
4. Close Designer
5. Try CLI command again

**Note**: CLI tools use same license as GUI application

---

### Error: "Failed to initialize D3D11 engine"

**Cause**: GPU rendering unavailable or driver issues

**Solution 1**: Use CPU renderer
```bash
sbsrender render \
  --input material.sbs \
  --output-path ./output/{outputNodeName} \
  --engine sse2
```

**Solution 2**: Update GPU drivers

**Solution 3**: Use OpenGL renderer
```bash
--engine ogl3
```

---

### Error: "Cannot find graph 'GraphName'"

**Cause**: Graph identifier doesn't match

**Diagnosis**: List available graphs
```bash
sbsrender info --input material.sbs
```

**Solution**: Use exact graph identifier
```bash
sbsrender render \
  --input material.sbs \
  --input-graph "Exact_Graph_Name" \
  --output-path ./output/{outputNodeName}
```

**Or**: Render all graphs
```bash
--input-graph "*"
```

---

## Data Extraction Issues

### Error: "AttributeError: 'SBSNode' object has no attribute 'mIdentifier'"

**Cause**: Not all objects have mIdentifier attribute

**Fix**: Use getUid() instead
```python
# Instead of:
node_id = node.mIdentifier  # May not exist

# Use:
node_id = node.getUid()  # Always exists
```

---

### Error: "KeyError: 'outputformat'"

**Cause**: Not all nodes have all parameters

**Fix**: Check if parameter exists first
```python
# Instead of:
output_format = params['outputformat']  # May not exist

# Use:
params = {}
for param in node.getParameters():
    params[param.mId] = param.mValue

if 'outputformat' in params:
    output_format = params['outputformat']
else:
    print("Node doesn't have outputformat parameter")
```

---

### Error: "Cannot access parameter value"

**Cause**: Different parameter types have different value access patterns

**Fix**: Handle different types
```python
param_value = param.mValue

# Try different access patterns
value = None

if hasattr(param_value, 'mValues'):
    # Vector type (float2, float3, float4)
    value = list(param_value.mValues)
elif hasattr(param_value, 'mValue'):
    # Scalar type (int, float, string)
    value = param_value.mValue
else:
    # Fallback to string representation
    value = str(param_value)
```

---

## Performance Problems

### Issue: "Script takes too long to analyze large graphs"

**Cause**: Repeated graph traversals or inefficient algorithms

**Solution 1**: Build connection map once
```python
# Build once
conn_map = build_connection_map(graph)

# Reuse multiple times
for node_uid in node_list:
    if node_uid in conn_map:
        # Fast lookup
        connections = conn_map[node_uid]
```

**Solution 2**: Filter nodes early
```python
# Instead of analyzing all nodes then filtering:
all_nodes = graph.getAllNodes()
for node in all_nodes:
    if node_type == "tile_sampler":
        analyze(node)

# Filter first:
tile_samplers = [n for n in graph.getAllNodes()
                 if n.getCompImplementation().mDefinition.mId == "tile_sampler"]
for node in tile_samplers:
    analyze(node)
```

**Solution 3**: Cache results
```python
# Cache node type lookups
node_types = {}
for node in graph.getAllNodes():
    uid = node.getUid()
    node_types[uid] = node.getCompImplementation().mDefinition.mId

# Fast lookup later
if node_types[some_uid] == "tile_sampler":
    # ...
```

---

### Issue: "Out of memory when processing large .sbs files"

**Cause**: Loading entire file into memory

**Solution 1**: Process graphs one at a time
```python
for graph in doc.getGraphs():
    # Process graph
    result = analyze_graph(graph)

    # Write result immediately
    with open(f"{graph.mIdentifier}.json", "w") as f:
        json.dump(result, f)

    # Free memory (help garbage collector)
    del result
```

**Solution 2**: Use generators for large collections
```python
def analyze_nodes_generator(graph):
    """Yield results one at a time instead of storing all"""
    for node in graph.getAllNodes():
        yield analyze_node(node)

# Use generator
for result in analyze_nodes_generator(graph):
    print(result)  # Process immediately, don't accumulate
```

---

## Encoding Issues

### Error: "UnicodeDecodeError: 'utf-8' codec can't decode byte"

**Cause**: .sbs file has non-UTF-8 characters

**Solution**: Specify encoding
```python
# If reading as text (XML parsing)
with open("material.sbs", "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()
```

**For pysbs**: Usually handles automatically, but if issues persist:
```python
# Normalize file first
import codecs

with codecs.open("material.sbs", "r", encoding="utf-8", errors="replace") as f:
    content = f.read()

with codecs.open("normalized.sbs", "w", encoding="utf-8") as f:
    f.write(content)

# Use normalized file
doc = SBSDocument(ctx, "normalized.sbs")
```

---

## Version Compatibility

### Issue: "pysbs works in Designer 2022 but not 2023"

**Cause**: API changes between versions

**Solution**: Check Designer version and adapt
```python
from pysbs import context

ctx = context.Context()
# Check version-specific behavior

try:
    # Try new API (2023+)
    result = new_api_method()
except AttributeError:
    # Fall back to old API (2022-)
    result = old_api_method()
```

**Best Practice**: Test with target Designer version

---

## Debugging Tips

### Enable Verbose Logging

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('sbs_analysis')

logger.debug("Loading document...")
doc = SBSDocument(ctx, filepath)
logger.debug(f"Loaded {len(doc.getGraphs())} graphs")
```

### Print Available Methods

```python
# See what methods an object has
print(dir(node))

# Check if method exists
if hasattr(node, 'getParameters'):
    params = node.getParameters()
```

### Use Try-Except for Graceful Errors

```python
try:
    value = param.mValue.mValue
except AttributeError:
    try:
        value = param.mValue.mValues
    except AttributeError:
        value = str(param.mValue)
        print(f"Unexpected parameter type: {type(param.mValue)}")
```

---

## Getting Help

### Check Designer Version
```python
# In Designer Python Console
import sd
app = sd.getContext().getSDApplication()
print(app.getVersion())
```

### Verify pysbs Version
```bash
pip show substance-automation-toolkit
```

### Community Resources
- Substance 3D Community Forum
- Adobe Substance documentation
- GitHub issues for automation toolkit

### Report Issues
When reporting issues, include:
1. Designer version
2. pysbs version
3. Python version
4. Operating system
5. Complete error message
6. Minimal reproducible example

---

## Quick Reference: Common Fixes

| Problem | Quick Fix |
|---------|-----------|
| pysbs not found | `pip install substance-automation-toolkit` |
| sd.api not available | Run script inside Designer, not standalone |
| File not found | Use absolute paths: `os.path.abspath()` |
| Permission denied | Close Designer, check file permissions |
| CLI tool not found | Add Designer to PATH |
| GPU rendering fails | Use `--engine sse2` |
| No license found | Run Designer GUI to activate |
| Attribute error | Check if attribute exists with `hasattr()` |
| Slow performance | Build connection map once, cache results |
| Unicode errors | Use `encoding="utf-8", errors="ignore"` |

---

## Further Reading

- [pysbs-api.md](./pysbs-api.md) - Complete API reference
- [sd-api.md](./sd-api.md) - In-application scripting
- [cli-tools.md](./cli-tools.md) - Command-line tools
- Official Substance Designer documentation
