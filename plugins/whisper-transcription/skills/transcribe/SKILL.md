---
name: Whisper Transcription
description: >
  Use this skill when the user wants to transcribe audio or video files,
  convert speech to text, extract subtitles from video, or process media
  files through whisper.cpp.
  Triggers on: "transcribe audio", "transcribe video", "speech to text",
  "convert speech", "extract transcript", "whisper transcribe"
---

# Whisper.cpp Transcription Skill

Transcribe audio and video files using whisper.cpp with FFmpeg preprocessing.

## Supported Formats

- **Video:** mp4, mkv, avi, mov, webm
- **Audio:** mp3, wav, flac, aac, ogg, m4a

## Prerequisites Installation

### 1. FFmpeg (Windows)

```bash
winget install FFmpeg
```

Or download from https://ffmpeg.org/download.html and add to PATH.

### 2. Whisper.cpp (Windows)

```bash
# Clone the repository
git clone https://github.com/ggml-org/whisper.cpp.git
cd whisper.cpp

# Build with CMake
cmake -B build
cmake --build build --config Release
```

The executable will be at `build/bin/Release/whisper-cli.exe`

### 3. Download Model

Using Git Bash or WSL:
```bash
cd whisper.cpp
sh ./models/download-ggml-model.sh large-v3
```

Or download manually from Hugging Face:
https://huggingface.co/ggerganov/whisper.cpp/tree/main

## Workflow

### Step 1: Verify Prerequisites

```bash
# Check FFmpeg
ffmpeg -version

# Check whisper-cli (adjust path as needed)
path/to/whisper.cpp/build/bin/Release/whisper-cli.exe --help
```

### Step 2: Convert Input to WAV

FFmpeg converts any audio/video to 16kHz mono WAV (optimal for Whisper):

```bash
ffmpeg -i "input.mp4" -ar 16000 -ac 1 -c:a pcm_s16le "output.wav"
```

### Step 3: Transcribe

```bash
whisper-cli -m models/ggml-large-v3.bin -f audio.wav
```

### Step 4: Output Options

- Default: prints to stdout
- `-otxt` - Save as .txt file
- `-osrt` - Save as .srt subtitles
- `-ovtt` - Save as .vtt subtitles
- `-ojson` - Save as JSON with timestamps

## Configuration

### Default Paths (adjust per system)

```
WHISPER_CLI = C:\path\to\whisper.cpp\build\bin\Release\whisper-cli.exe
WHISPER_MODELS = C:\path\to\whisper.cpp\models
```

### Model Selection

Use `-m` flag to specify model:

| Model | Download Size | VRAM | Accuracy | Use Case |
|-------|---------------|------|----------|----------|
| tiny | ~75MB | ~1GB | Basic | Quick tests |
| base | ~150MB | ~1GB | Good | Fast transcription |
| small | ~500MB | ~2GB | Better | Balanced |
| medium | ~1.5GB | ~5GB | Great | High quality |
| large-v3 | ~3GB | ~6GB | Best | Maximum accuracy |

### Language Options

- Auto-detect: (default)
- Specify: `-l en` for English, `-l ja` for Japanese, etc.
- Translate to English: `--translate`

## Quick Reference Commands

| Task | Command |
|------|---------|
| Check FFmpeg | `ffmpeg -version` |
| Convert to WAV | `ffmpeg -i input.mp4 -ar 16000 -ac 1 -c:a pcm_s16le output.wav` |
| Basic transcribe | `whisper-cli -m models/ggml-large-v3.bin -f audio.wav` |
| With SRT output | `whisper-cli -m models/ggml-large-v3.bin -f audio.wav -osrt` |
| Specify language | `whisper-cli -m models/ggml-large-v3.bin -f audio.wav -l en` |
| Translate to English | `whisper-cli -m models/ggml-large-v3.bin -f audio.wav --translate` |

## Example Workflow

For a video file at `D:\Videos\interview.mp4`:

```bash
# 1. Convert to WAV
ffmpeg -i "D:\Videos\interview.mp4" -ar 16000 -ac 1 -c:a pcm_s16le "D:\Videos\interview_audio.wav"

# 2. Transcribe with SRT output
whisper-cli -m "C:\whisper.cpp\models\ggml-large-v3.bin" -f "D:\Videos\interview_audio.wav" -osrt

# 3. Output will be saved as interview_audio.wav.srt
```

## Troubleshooting

### FFmpeg not found
- Ensure FFmpeg is installed: `winget install FFmpeg`
- Restart terminal after installation
- Verify PATH includes FFmpeg directory

### whisper-cli not found
- Build whisper.cpp following installation steps
- Use full path to executable
- On Windows: `build\bin\Release\whisper-cli.exe`

### Model file missing
```bash
# Download in whisper.cpp directory
sh ./models/download-ggml-model.sh large-v3
```

Or download manually from Hugging Face and place in `models/` folder.

### CUDA out of memory
- Try smaller model: `tiny`, `base`, or `small`
- Force CPU mode (no GPU flags)
- Close other GPU applications

### Audio format issues
Ensure FFmpeg conversion uses correct flags:
```bash
ffmpeg -i input.file -ar 16000 -ac 1 -c:a pcm_s16le output.wav
```
- `-ar 16000` - 16kHz sample rate (required)
- `-ac 1` - Mono channel
- `-c:a pcm_s16le` - 16-bit PCM encoding

### Long audio files
For files over 30 minutes, consider:
- Splitting into chunks first
- Using `--max-len` to limit segment length
- Processing overnight for very long files
