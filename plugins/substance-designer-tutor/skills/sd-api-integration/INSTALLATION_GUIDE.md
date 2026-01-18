# Substance Designer API Integration - Installation Guide

## Overview

This guide explains how to access the Substance Automation Toolkit (pysbs) for use with the SD API Integration skill.

**IMPORTANT**: The skill is **fully functional WITHOUT pysbs** using XML parsing. See [Test Results](#test-results-without-pysbs) below.

---

## Understanding the Automation Tools

### What's Included with Designer

✅ **Already Available** (no installation needed):
- **CLI Tools**: sbsrender, sbscooker, sbsupdater, sbsbaker
- **Location**: `C:\Program Files\Adobe\Adobe Substance 3D Designer\`
- **Use Case**: Batch rendering, publishing SBSAR files
- **Documentation**: See [cli-tools.md](./references/cli-tools.md)

✅ **sd.api** (Python API for in-application scripting):
- **Location**: `C:\Program Files\Adobe\Adobe Substance 3D Designer\resources\python\`
- **Use Case**: Building Designer plugins, real-time graph manipulation
- **Availability**: When Designer is running
- **Documentation**: See [sd-api.md](./references/sd-api.md)

❌ **pysbs** (Offline .sbs file analysis):
- **NOT included** with standard Designer installation
- **Requires**: Separate Substance Automation Toolkit download
- **Use Case**: Offline analysis, CI/CD pipelines, advanced diagnostics

---

## Installation Options

### Option 1: Use XML Parsing (Recommended - No Installation)

The SD API Integration skill includes **fully functional XML parsing** that works without pysbs.

**What You Get**:
- ✅ Graph structure analysis
- ✅ Node counting and type identification
- ✅ Output configuration verification
- ✅ Dependency tracking
- ✅ Basic diagnostic checks
- ✅ JSON and text output formats

**Tested Performance**:
- Analyzed 167-node production graph in < 1 second
- 100% accurate node counts, types, and outputs
- Successfully identified 31 dependencies
- Zero errors or crashes

**Usage**:
```bash
# Use Designer's Python
"C:\Program Files\Adobe\Adobe Substance 3D Designer\plugins\pythonsdk\python.exe" \
  plugins/substance-designer-tutor/skills/sd-api-integration/references/analysis-script.py \
  path/to/your/file.sbs

# Or system Python
python plugins/substance-designer-tutor/skills/sd-api-integration/references/analysis-script.py \
  path/to/your/file.sbs
```

**See**: [FINAL_TEST_RESULTS.md](./FINAL_TEST_RESULTS.md) for complete test data

---

### Option 2: Adobe Substance Automation Toolkit (Enterprise)

**For Enterprise Customers Only**

The official Substance Automation Toolkit (SAT) includes the full pysbs library.

#### How to Obtain

1. **Enterprise License Required**
   - Substance 3D Collection for Teams/Enterprise
   - Access via Adobe Admin Console

2. **Download Location**
   - Admin Console → Packages → Tools
   - Download: "Substance 3D Automation Toolkit"
   - File: .zip archive (Windows/macOS) or .tar.gz (Linux)

3. **Installation**
   - Windows: Extract to any location (e.g., `C:\Program Files\Adobe\Substance Automation Toolkit`)
   - Set environment variable: `SAT_INSTALL_PATH=C:\path\to\toolkit`
   - Install wheel: `pip install "C:\path\to\toolkit\Python API\pysbs-<version>.whl"`

4. **Verification**
   ```bash
   python -c "from pysbs import context; print('pysbs available')"
   ```

#### What's Included

- ✅ Full pysbs Python API
- ✅ Advanced CLI tools
- ✅ Batch processing utilities
- ✅ Complete API documentation
- ✅ Sample scripts and examples

**Documentation**:
- [Adobe SAT Setup Guide](https://helpx.adobe.com/substance-3d-sat/setup-and-getting-started.html)
- [pysbs API Reference](https://helpx.adobe.com/substance-3d-sat/pysbs-python-api.html)

---

### Option 3: Individual License Limitations

**Current Status** (as of 2026):

❌ **pysbs NOT Available for**:
- Substance 3D Collection (Individual/Indie plans)
- Standalone Designer licenses
- Free trials

⚠️ **Conflicting Information**:
- Some documentation suggests pysbs is included with Indie licenses
- Adobe Community forums confirm it's enterprise-only
- Standard Designer installation does NOT include pysbs wheel files

**Alternatives for Individual Users**:
1. Use XML parsing (Option 1 - works perfectly)
2. Use sd.api for in-Designer automation
3. Use CLI tools (sbsrender, sbscooker) included with Designer
4. Upgrade to Enterprise license for full SAT access

---

## What About PyPI?

### ⚠️ Warning: PyPI Package is NOT Official

A package called `pysbs` exists on PyPI, but it is:
- ❌ **NOT the official Adobe package**
- ❌ Incomplete/broken installation (no actual module files)
- ❌ Third-party library by "wer310Libs"
- ❌ Minimal functionality (1.1 KB wheel file)

**Do NOT install**:
```bash
pip install pysbs  # This is NOT the Adobe pysbs!
```

The official Adobe pysbs is **only distributed as a .whl file** with the Substance Automation Toolkit, not via PyPI.

---

## Test Results Without pysbs

### Actual Analysis of Ornate_Fabric.sbs

Using **only XML parsing** (no pysbs), the skill successfully analyzed:

**Package Information**:
- Name: "Unsaved Package"
- Format: 1.1.0.202302
- Dependencies: 31 external .sbs files

**Graph 1: Ornate_Fabric**
- Nodes: 167
- Node Types: 31 unique
- Outputs: 7 (basecolor, normal, roughness, metallic, height, AO, translucency)
- Top Node Types:
  - blur_hq_grayscale: 7
  - threshold: 6
  - shape: 5
  - switch_grayscale: 5

**Graph 2: Ornaments**
- Nodes: 28
- Node Types: 10 unique
- Outputs: 2 (Floral_ornament, geometrical_pattern)

**Diagnostics**: ✅ No issues detected

**Performance**: < 1 second analysis time

**See**: [FINAL_TEST_RESULTS.md](./FINAL_TEST_RESULTS.md) for complete report

---

## Recommendations by Use Case

### For Learning & Basic Analysis
→ **Use XML Parsing** (Option 1)
- Already included with the skill
- No installation required
- Fully functional for most use cases
- Fast and reliable

### For Pipeline Integration (Individual License)
→ **Use CLI Tools** + **XML Parsing**
- sbsrender for batch rendering
- XML parsing for analysis
- sd.api for custom Designer tools
- See [cli-tools.md](./references/cli-tools.md)

### For Enterprise Workflows
→ **Install Substance Automation Toolkit** (Option 2)
- Full pysbs API access
- Advanced diagnostics
- Enhanced parameter extraction
- CI/CD integration

### For In-Designer Automation
→ **Use sd.api** (already available)
- Build Designer plugins
- Real-time graph manipulation
- Interactive tools
- See [sd-api.md](./references/sd-api.md)

---

## Troubleshooting

### Error: "pysbs not found"

✅ **Expected** - This is normal if you haven't installed SAT

**Solution**: The skill automatically falls back to XML parsing

**Output**:
```
INFO: pysbs not available, using XML parsing fallback
For full capabilities, install: pip install substance-automation-toolkit
```

This is **not an error** - the skill continues to work normally.

### Error: "ModuleNotFoundError: No module named 'pysbs'"

✅ **This confirms XML parsing mode is active**

The skill has been designed to gracefully handle missing pysbs and provide full functionality through XML parsing.

### Want to Enable pysbs?

1. **Check your license**: Enterprise/Teams only
2. **Access Admin Console**: Download SAT package
3. **Install wheel**: `pip install path/to/pysbs.whl`
4. **Verify**: Run test script again

---

## Comparison: XML Parsing vs pysbs

| Feature | XML Parsing | pysbs (SAT) |
|---------|-------------|-------------|
| Graph structure | ✅ Full | ✅ Full |
| Node counting | ✅ 100% | ✅ 100% |
| Node types | ✅ Complete | ✅ Complete |
| Outputs | ✅ All | ✅ All |
| Dependencies | ✅ All | ✅ All |
| Basic diagnostics | ✅ Working | ✅ Enhanced |
| Parameter extraction | ⚠️ Limited | ✅ Full |
| Connection tracing | ⚠️ Basic | ✅ Advanced |
| Performance | ✅ Fast | ✅ Fast |
| Installation | ✅ None | ❌ Complex |
| Cost | ✅ Free | ❌ Enterprise |

---

## Sources & References

### Official Adobe Documentation
- [Substance 3D Automation Toolkit](https://substance3d.adobe.com/documentation/sat)
- [SAT Setup and Getting Started](https://helpx.adobe.com/substance-3d-sat/setup-and-getting-started.html)
- [pysbs Python API](https://helpx.adobe.com/substance-3d-sat/pysbs-python-api.html)
- [Getting Started with pysbs](https://helpx.adobe.com/substance-3d-sat/pysbs-python-api/getting-started.html)

### Community Resources
- [SAT Samples on GitHub](https://github.com/razluta/substance-automation-toolkit_samples)
- [Adobe Community Discussion: Getting SAT](https://community.adobe.com/t5/substance-3d-designer-discussions/getting-substance-3d-automation-toolkit/m-p/14813891)

### Skill Documentation
- [pysbs-api.md](./references/pysbs-api.md) - Complete API reference (for when available)
- [sd-api.md](./references/sd-api.md) - In-application scripting (available now)
- [cli-tools.md](./references/cli-tools.md) - Batch tools (available now)
- [troubleshooting.md](./references/troubleshooting.md) - Error solutions

---

## Conclusion

### ✅ You Can Use This Skill Right Now

The SD API Integration skill is **fully functional without pysbs installation**. The XML parsing fallback provides:

- Complete graph structure analysis
- Accurate node and output identification
- Dependency tracking
- Basic diagnostic checks
- Fast performance (< 1 second)
- Zero installation requirements

### When to Install pysbs

Only install the Substance Automation Toolkit if you:
- Have an Enterprise/Teams license
- Need advanced parameter extraction
- Require enhanced diagnostics (all 11 rules)
- Want connection graph visualization
- Are building CI/CD pipelines with full API access

For most users, **XML parsing is sufficient and recommended**.

---

**Last Updated**: 2026-01-17
**Tested With**: Substance Designer 13.x, Python 3.11-3.12
**Skill Version**: 1.0.0
