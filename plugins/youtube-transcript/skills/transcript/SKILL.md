---
name: YouTube Transcript
description: >
  Use this skill when the user wants to download a transcript from a YouTube video,
  extract subtitles, get captions, or needs video text content.
  Triggers on: "get youtube transcript", "download transcript", "extract subtitles",
  "youtube captions", "get video text", "transcribe youtube"
---

# YouTube Transcript Downloader

Download transcripts from YouTube videos using yt-dlp.

## Integration with Substance Designer Tutor

This skill provides transcripts for the **substance-designer-tutor** skill. When downloading transcripts for the Designer First Steps course:

**Output Directory:**
```
../substance-designer-tutor/skills/tutor/sources/transcripts/
```

**Naming Convention:** `NN-topic-name.txt`
- `00-course-overview.txt`
- `05-creating-thread.txt`
- `09-fabric-embroidery.txt`

**Course Playlist:** https://www.youtube.com/playlist?list=PLB0wXHrWAmCxBw92VSRjqsbqYXgkF8puC

---

## Prerequisites

### Check if yt-dlp is installed
```bash
yt-dlp --version
```

### Installation (if needed)

**Windows:**
```bash
# Download from GitHub releases
curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe -o yt-dlp.exe
# Or with winget
winget install yt-dlp
```

**macOS:**
```bash
brew install yt-dlp
```

**Linux:**
```bash
sudo apt install yt-dlp
# or
pip install yt-dlp
```

## Workflow

### Step 1: List Available Subtitles
```bash
yt-dlp --list-subs "VIDEO_URL"
```

This shows what subtitles are available (manual vs auto-generated, languages).

### Step 2: Download Subtitles

**Prefer manual subtitles (higher quality):**
```bash
yt-dlp --write-sub --sub-lang en --skip-download --convert-subs vtt -o "%(title)s" "VIDEO_URL"
```

**Fallback to auto-generated:**
```bash
yt-dlp --write-auto-sub --sub-lang en --skip-download --convert-subs vtt -o "%(title)s" "VIDEO_URL"
```

**For other languages, replace `en` with language code (e.g., `es`, `fr`, `de`).**

### Step 3: Convert VTT to Plain Text

The downloaded .vtt file needs cleaning:

1. Remove the `WEBVTT` header line
2. Remove timestamp lines (format: `00:00:00.000 --> 00:00:05.000`)
3. Remove duplicate consecutive lines (auto-captions repeat text)
4. Strip HTML tags like `<c>`, `</c>`, `<00:00:00.000>`
5. Decode HTML entities (`&amp;` → `&`, etc.)

**Simple approach - read the .vtt file and process:**
- Read file content
- Use regex or line-by-line processing
- Output clean text

### Step 4: Save Transcript

Save the cleaned transcript to the desired location, e.g.:
- `transcripts/video-title.txt`
- `sources/transcripts/part-01-transcript.md`

## Quick Reference

| Task | Command |
|------|---------|
| Check installation | `yt-dlp --version` |
| List subtitles | `yt-dlp --list-subs "URL"` |
| Download manual subs | `yt-dlp --write-sub --sub-lang en --skip-download --convert-subs vtt -o "%(title)s" "URL"` |
| Download auto subs | `yt-dlp --write-auto-sub --sub-lang en --skip-download --convert-subs vtt -o "%(title)s" "URL"` |

## Common Issues

| Problem | Solution |
|---------|----------|
| yt-dlp not found | Install using commands above |
| No subtitles available | Video may not have captions; try different language |
| Private/age-restricted video | May need authentication or different approach |
| Rate limiting | Wait and retry, or use `--sleep-interval` |

## Example Usage

"Download the transcript from https://www.youtube.com/watch?v=km-aBsLvG-c and save it to transcripts/"

1. Check yt-dlp: `yt-dlp --version`
2. List subs: `yt-dlp --list-subs "https://www.youtube.com/watch?v=km-aBsLvG-c"`
3. Download: `yt-dlp --write-auto-sub --sub-lang en --skip-download --convert-subs vtt -o "transcripts/%(title)s" "https://www.youtube.com/watch?v=km-aBsLvG-c"`
4. Convert VTT to plain text
5. Done!

---

## Designer First Steps Course Integration

When downloading transcripts for the Substance Designer tutor skill:

### Complete Video List

| # | Part | URL | Output File |
|---|------|-----|-------------|
| 1 | Overview | `At3FoFcuN6k` | `00-course-overview.txt` |
| 2 | Pt 1 | `UyF5Ie-HJ0Q` | `01-what-is-substance-designer.txt` |
| 3 | Pt 2 | `Wg1gzR3rQeY` | `02-how-to-make-materials.txt` |
| 4 | Pt 3 | `_KlXkHLH5pc` | `03-interface.txt` |
| 5 | Pt 4 | `-DlD476pnxQ` | `04-first-project.txt` |
| 6 | Pt 5 | `km-aBsLvG-c` | `05-creating-thread.txt` |
| 7 | Pt 6 | `N0zw_owXnfE` | `06-fabric-weaving.txt` |
| 8 | Pt 7 | `_tLjvmGcEcc` | `07-procedural-shape-design.txt` |
| 9 | Pt 8 | `eGKl3dcSXxE` | `08-importing-images.txt` |
| 10 | Pt 9 | `YCKO5P-pCfE` | `09-fabric-embroidery.txt` |
| 11 | Pt 10 | `caVvzNg-iRI` | `10-customized-shapes.txt` |
| 12 | Pt 11 | `CYWOKPRnP5o` | `11-inheritance.txt` |
| 13 | Pt 12 | `bJUoc8GR18E` | `12-element-placement.txt` |
| 14 | Pt 13 | `QPD_oASJuUM` | `13-radial-gemstones.txt` |
| 15 | Pt 14 | `yYHTw4IKyAM` | `14-mask-extraction.txt` |
| 16 | Pt 15 | `EgvCOGkaN9E` | `15-imperfections.txt` |
| 17 | Pt 16 | `8S2TTbTuqYk` | `16-colors.txt` |
| 18 | Pt 17 | `TWSXb94wH-Q` | `17-roughness-metallic.txt` |
| 19 | Pt 18 | `med5kNfGPWk` | `18-displacement-translucency.txt` |
| 20 | Pt 19 | `6AVxsMTwKrk` | `19-exposing-parameters.txt` |
| 21 | Pt 20 | `sDy1xYqTMP8` | `20-parameter-presets.txt` |
| 22 | Pt 21 | `QEoUSOTcM1Q` | `21-export-reuse.txt` |

### Workflow for Tutor Integration

1. **Download VTT** to a temp directory
2. **Convert to plain text** (remove timestamps, tags, duplicates)
3. **Save to tutor sources:**
   ```
   ../substance-designer-tutor/skills/tutor/sources/transcripts/NN-topic-name.txt
   ```
4. **Notify the tutor skill** that new content is available

### VTT to Plain Text Conversion

```bash
cat input.vtt | \
  sed '/^WEBVTT/d' | \
  sed '/^Kind:/d' | \
  sed '/^Language:/d' | \
  sed '/^[0-9][0-9]:[0-9][0-9]:[0-9][0-9]/d' | \
  sed 's/<[^>]*>//g' | \
  sed '/^[[:space:]]*$/d' | \
  sed 's/^[[:space:]]*//' | \
  sed 's/[[:space:]]*$//' | \
  uniq \
  > output.txt
```

### After Download: Tutor Analysis

Once transcripts are in place, the tutor skill can:
1. Read transcripts to answer user questions
2. Extract node names, parameters, and workflows
3. Identify troubleshooting tips from instructor explanations
4. Quote relevant passages for learning context
