# Command-Line Tools Reference

## Overview

Substance Designer provides command-line tools for **batch rendering** and **publishing** operations. These tools are essential for pipeline integration, automated workflows, and CI/CD processes.

**Available Tools**:
- **sbsrender** - Render texture outputs from .sbs files
- **sbscooker** - Publish .sbs files to .sbsar format
- **sbsmutator** - Batch generate texture variations (Designer 2019.2+)
- **sbsupdater** - Update .sbs files to newer format versions

## Installation Location

Tools are located in the Substance Designer installation directory:

**Windows**:
```
C:\Program Files\Adobe\Adobe Substance 3D Designer\
```

**macOS**:
```
/Applications/Adobe Substance 3D Designer.app/Contents/MacOS/
```

**Linux**:
```
/opt/Allegorithmic/Substance_Designer/
```

Add to PATH for convenience:

```bash
# Windows (PowerShell)
$env:Path += ";C:\Program Files\Adobe\Adobe Substance 3D Designer"

# macOS/Linux
export PATH="/Applications/Adobe Substance 3D Designer.app/Contents/MacOS:$PATH"
```

---

## sbsrender - Texture Rendering

### Basic Usage

```bash
sbsrender render --input <file.sbs> --output-path <path>
```

### Core Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `--input <path>` | Input .sbs file | `--input material.sbs` |
| `--input-graph <name>` | Specific graph to render (or `*` for all) | `--input-graph "Fabric_Material"` |
| `--output-path <path>` | Output path template | `--output-path "./renders/{outputNodeName}"` |
| `--output-format <fmt>` | Output format: png, tga, jpg, exr, etc. | `--output-format png` |
| `--output-name <name>` | Override output filename | `--output-name "my_texture"` |
| `--set-value <param>` | Set graph parameter | `--set-value $outputsize@11,11` |
| `--engine <engine>` | Render engine: sse2, d3d11pc, etc. | `--engine d3d11pc` |

### Output Path Templates

Use placeholders in `--output-path` for dynamic naming:

| Placeholder | Expands To |
|-------------|------------|
| `{inputGraphUrl}` | Graph identifier |
| `{outputNodeName}` | Output node name (baseColor, normal, etc.) |
| `{inputFileName}` | Input .sbs filename (no extension) |
| `{outputFormat}` | Output format (png, tga, etc.) |

**Example**:
```bash
sbsrender render \
  --input "materials/fabric.sbs" \
  --output-path "./renders/{inputGraphUrl}/{outputNodeName}.{outputFormat}" \
  --output-format png
```

Results in:
```
./renders/Fabric_Material/baseColor.png
./renders/Fabric_Material/normal.png
./renders/Fabric_Material/height.png
...
```

### Common Use Cases

#### 1. Render Single Graph at 2K

```bash
sbsrender render \
  --input "material.sbs" \
  --input-graph "My_Material" \
  --output-path "./output/{outputNodeName}" \
  --output-format png \
  --set-value $outputsize@11,11 \
  --engine d3d11pc
```

**Notes**:
- `$outputsize@11,11` = 2048x2048 (2^11 = 2048)
- Common sizes: 10,10 (1K), 11,11 (2K), 12,12 (4K)

#### 2. Render All Graphs in File

```bash
sbsrender render \
  --input "materials.sbs" \
  --input-graph "*" \
  --output-path "./renders/{inputGraphUrl}/{outputNodeName}" \
  --output-format tga \
  --set-value $outputsize@12,12
```

#### 3. Render Specific Outputs Only

```bash
sbsrender render \
  --input "material.sbs" \
  --output-path "./output/{outputNodeName}" \
  --output-format png \
  --output-name "baseColor,normal,roughness"
```

#### 4. Batch Render Multiple Files

```bash
#!/bin/bash
for file in *.sbs; do
  echo "Rendering $file..."
  sbsrender render \
    --input "$file" \
    --output-path "./renders/${file%.sbs}/{outputNodeName}" \
    --output-format png \
    --set-value $outputsize@11,11
done
```

**Windows (PowerShell)**:
```powershell
Get-ChildItem *.sbs | ForEach-Object {
  Write-Host "Rendering $($_.Name)..."
  sbsrender render `
    --input $_.FullName `
    --output-path "./renders/$($_.BaseName)/{outputNodeName}" `
    --output-format png `
    --set-value '$outputsize@11,11'
}
```

### Setting Graph Parameters

Use `--set-value` to override exposed parameters:

```bash
# Set output size
--set-value $outputsize@11,11

# Set custom exposed parameter (integer)
--set-value myParameter@5

# Set custom parameter (float)
--set-value roughness@0.75

# Set multiple parameters
--set-value $outputsize@11,11 --set-value myParam@3
```

### Output Formats

| Format | Extension | Bit Depth | Use Case |
|--------|-----------|-----------|----------|
| `png` | .png | 8-bit | Final textures, web |
| `tga` | .tga | 8-bit | Game engines |
| `jpg` | .jpg | 8-bit | Previews (lossy) |
| `exr` | .exr | 16/32-bit float | HDR, compositing |
| `tif` | .tif | 8/16-bit | Print, archival |
| `bmp` | .bmp | 8-bit | Legacy support |

### Render Engines

| Engine | Description | Platform |
|--------|-------------|----------|
| `sse2` | CPU renderer (slow but compatible) | All |
| `d3d11pc` | DirectX 11 GPU (fast) | Windows |
| `ogl3` | OpenGL 3.3+ GPU | Windows, macOS, Linux |

**Recommendation**: Use `d3d11pc` on Windows for best performance.

### Error Handling and Logging

```bash
# Redirect output to log file
sbsrender render \
  --input "material.sbs" \
  --output-path "./output/{outputNodeName}" \
  > render.log 2>&1

# Check exit code
if [ $? -eq 0 ]; then
  echo "Render succeeded"
else
  echo "Render failed"
  cat render.log
fi
```

---

## sbscooker - SBSAR Publishing

### Basic Usage

```bash
sbscooker --input <file.sbs> --output-path <path> --output-name <name>
```

### Core Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `--input <path>` | Input .sbs file | `--input material.sbs` |
| `--input-graph <name>` | Specific graph to publish | `--input-graph "Material_Graph"` |
| `--output-path <path>` | Output directory | `--output-path "./published"` |
| `--output-name <name>` | Output .sbsar filename | `--output-name "my_material"` |
| `--alias <name>` | Set package alias | `--alias "pkg://my_material"` |

### Common Use Cases

#### 1. Publish Single Graph

```bash
sbscooker \
  --input "material.sbs" \
  --input-graph "Fabric_Material" \
  --output-path "./published" \
  --output-name "fabric"
```

Results in: `./published/fabric.sbsar`

#### 2. Publish All Graphs

```bash
sbscooker \
  --input "materials.sbs" \
  --output-path "./published" \
  --output-name "all_materials"
```

#### 3. Batch Publish Multiple Files

```bash
#!/bin/bash
for file in *.sbs; do
  basename="${file%.sbs}"
  echo "Publishing $file..."
  sbscooker \
    --input "$file" \
    --output-path "./published" \
    --output-name "$basename"
done
```

#### 4. Set Package Alias

```bash
sbscooker \
  --input "material.sbs" \
  --output-path "./published" \
  --output-name "my_material" \
  --alias "pkg://company/materials/my_material"
```

**Why aliases matter**: Allows other packages to reference this SBSAR with a stable identifier.

---

## sbsmutator - Batch Variations

Generate multiple texture variations by randomizing exposed parameters.

### Basic Usage

```bash
sbsmutator \
  --input <file.sbsar> \
  --output-path <path> \
  --output-format <fmt> \
  --use-random \
  --random-seed <seed> \
  --iterations <count>
```

### Example: Generate 10 Variations

```bash
sbsmutator \
  --input "material.sbsar" \
  --output-path "./variations" \
  --output-format png \
  --use-random \
  --random-seed 12345 \
  --iterations 10
```

Results in 10 folders with randomized texture sets.

---

## sbsupdater - Format Updates

Update .sbs files to newer format versions.

### Basic Usage

```bash
sbsupdater --input <file.sbs> --output <file.sbs>
```

### Example: Update File In-Place

```bash
sbsupdater --input "old_material.sbs" --output "old_material.sbs"
```

### Batch Update All Files

```bash
#!/bin/bash
for file in *.sbs; do
  echo "Updating $file..."
  sbsupdater --input "$file" --output "$file"
done
```

---

## Integration Examples

### CI/CD Pipeline (GitHub Actions)

```yaml
name: Render Textures

on: [push]

jobs:
  render:
    runs-on: windows-latest

    steps:
      - uses: actions/checkout@v2

      - name: Install Substance Designer
        run: |
          # Install Designer (license required)
          # Download and install from Adobe

      - name: Render All Materials
        run: |
          $files = Get-ChildItem -Path ./materials -Filter *.sbs
          foreach ($file in $files) {
            sbsrender render `
              --input $file.FullName `
              --output-path "./renders/$($file.BaseName)/{outputNodeName}" `
              --output-format png `
              --set-value '$outputsize@11,11'
          }

      - name: Upload Artifacts
        uses: actions/upload-artifact@v2
        with:
          name: rendered-textures
          path: ./renders
```

### Python Wrapper Script

```python
#!/usr/bin/env python3
"""
Batch render wrapper for sbsrender
"""
import subprocess
import sys
from pathlib import Path

def render_sbs(input_file, output_dir, size=11, format="png"):
    """Render .sbs file using sbsrender"""
    input_path = Path(input_file)
    output_path = Path(output_dir) / input_path.stem / "{outputNodeName}"

    cmd = [
        "sbsrender",
        "render",
        "--input", str(input_path),
        "--output-path", str(output_path),
        "--output-format", format,
        "--set-value", f"$outputsize@{size},{size}",
        "--engine", "d3d11pc"
    ]

    print(f"Rendering: {input_path.name}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        print(f"  ✓ Success")
        return True
    else:
        print(f"  ✗ Failed")
        print(result.stderr)
        return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python render.py <input.sbs> <output_dir>")
        sys.exit(1)

    success = render_sbs(sys.argv[1], sys.argv[2])
    sys.exit(0 if success else 1)
```

### Makefile for Build Automation

```makefile
# Makefile for Substance Designer workflow

SBS_FILES := $(wildcard materials/*.sbs)
RENDER_DIRS := $(patsubst materials/%.sbs,renders/%,$(SBS_FILES))
SBSAR_FILES := $(patsubst materials/%.sbs,published/%.sbsar,$(SBS_FILES))

.PHONY: all render publish clean

all: render publish

render: $(RENDER_DIRS)

renders/%: materials/%.sbs
	@echo "Rendering $<..."
	@sbsrender render \
		--input "$<" \
		--output-path "renders/$*/{outputNodeName}" \
		--output-format png \
		--set-value '$$outputsize@11,11'

publish: $(SBSAR_FILES)

published/%.sbsar: materials/%.sbs
	@echo "Publishing $<..."
	@sbscooker \
		--input "$<" \
		--output-path "published" \
		--output-name "$*"

clean:
	rm -rf renders/* published/*
```

---

## Troubleshooting

### Common Issues

#### 1. Command Not Found

**Error**: `'sbsrender' is not recognized...`

**Solution**: Add Designer installation to PATH (see Installation Location above)

#### 2. License Errors

**Error**: `No valid license found`

**Solution**: Designer must be licensed. Run Designer GUI once to activate license.

#### 3. Missing Dependencies

**Error**: `Failed to load .sbs file`

**Solution**: Ensure all referenced .sbs files are in correct relative paths

#### 4. GPU Rendering Fails

**Error**: `D3D11 initialization failed`

**Solution**: Fall back to CPU renderer:
```bash
--engine sse2
```

#### 5. Permission Denied

**Error**: `Cannot write to output path`

**Solution**: Check directory permissions, create output directory first:
```bash
mkdir -p ./renders
```

### Capture Error Output

```bash
# Redirect stderr to file
sbsrender render ... 2> errors.log

# Redirect both stdout and stderr
sbsrender render ... > output.log 2>&1

# View errors
cat errors.log
```

---

## Performance Optimization

### Parallel Rendering

Render multiple files in parallel using GNU Parallel:

```bash
# Install GNU Parallel
# Ubuntu: sudo apt install parallel
# macOS: brew install parallel

# Render all .sbs files in parallel (4 jobs)
find ./materials -name "*.sbs" | parallel -j 4 \
  sbsrender render \
    --input {} \
    --output-path "./renders/{/.}/{outputNodeName}" \
    --output-format png \
    --set-value '$outputsize@11,11'
```

### Render Only Changed Files

```bash
#!/bin/bash
# Only render if .sbs is newer than outputs

for sbs_file in materials/*.sbs; do
  basename="${sbs_file%.sbs}"
  output_dir="renders/$(basename $basename)"

  # Check if outputs exist and are up to date
  if [ ! -d "$output_dir" ] || [ "$sbs_file" -nt "$output_dir" ]; then
    echo "Rendering $sbs_file (changed or new)..."
    sbsrender render \
      --input "$sbs_file" \
      --output-path "$output_dir/{outputNodeName}" \
      --output-format png \
      --set-value '$outputsize@11,11'
  else
    echo "Skipping $sbs_file (up to date)"
  fi
done
```

---

## Best Practices

1. **Version control**: Commit .sbs files, not rendered outputs
2. **Automate renders**: Use CI/CD to generate textures on push
3. **Consistent sizing**: Define standard output sizes (1K, 2K, 4K)
4. **Output organization**: Use `{inputGraphUrl}` in output paths
5. **Log everything**: Redirect output to logs for debugging
6. **Error handling**: Check exit codes, handle failures gracefully
7. **Parallel processing**: Render multiple files concurrently
8. **Test locally**: Verify commands work before CI/CD integration

---

## Reference: Output Size Values

| Size | Value | Resolution |
|------|-------|------------|
| 256 | 8,8 | 256x256 |
| 512 | 9,9 | 512x512 |
| 1K | 10,10 | 1024x1024 |
| 2K | 11,11 | 2048x2048 |
| 4K | 12,12 | 4096x4096 |
| 8K | 13,13 | 8192x8192 |

**Non-square**:
- 1K x 2K: `10,11`
- 2K x 4K: `11,12`

---

## Further Reading

- Official documentation: Substance Designer User Guide > Command Line Tools
- Designer installation directory: `docs/` folder
- Sample scripts: `resources/` folder in installation
