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
