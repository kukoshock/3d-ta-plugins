# 3D Technical Artist Plugin Marketplace

A collection of Claude Code plugins for 3D Technical Artists, developed by **Anastasia Kukosh**.

## About

This marketplace provides specialized tutoring and assistance plugins for 3D artists learning industry-standard tools. Each plugin acts as a knowledgeable tutor that can:

- **Explain concepts** from video tutorials and documentation
- **Troubleshoot issues** when tutorials don't work on your computer
- **Review your progress** and suggest improvements
- **Answer questions** about workflows and best practices

## Available Plugins

### substance-designer-tutor

A tutor for learning Substance Designer through the "Designer First Steps" course by Adobe Substance 3D. Features deep "WHY" explanations that teach the reasoning behind parameter choices, not just the values.

**Covers:**
- Thread creation (Part 5)
- Fabric weaving patterns (Part 6)
- Procedural shape design (Part 7)
- Fabric embroidery with Tile Sampler & Height Blend (Part 9)

**Key Features:**
- **WHY Explanations**: Understand why 600x700 creates dense weave, why Scale Map creates tapered edges
- **Parameter Decision Trees**: Choose appropriate values based on artistic intent (Low/Medium/High density guides)
- **Root Cause Troubleshooting**: Learn underlying principles, not just copy-paste solutions
- **Critical Techniques**: Scale Map vs Mask Input, Height Blend contrast, fiber density

**Trigger phrases:**
- "explain Tile Sampler"
- "how does Height Blend work"
- "troubleshoot my Substance Designer graph"
- "why isn't my embroidery working"
- "why use scale 3.8?"

### whisper-transcription

Audio and video transcription using whisper.cpp CLI with FFmpeg preprocessing.

**Features:**
- Transcribe any audio/video file (mp4, mkv, mp3, wav, etc.)
- Multiple output formats (txt, srt, vtt, json)
- Model selection from tiny to large-v3
- Full installation guide for Windows

**Trigger phrases:**
- "transcribe audio"
- "transcribe video"
- "speech to text"
- "extract transcript"

### youtube-transcript

Download transcripts from YouTube videos using yt-dlp.

**Features:**
- Extract subtitles/captions from any YouTube video
- Auto-generated and manual caption support
- Integrates with substance-designer-tutor for course transcripts

**Trigger phrases:**
- "get youtube transcript"
- "download transcript"
- "extract subtitles"
- "youtube captions"

## Installation

### Via Claude Code Marketplace (Recommended)

1. Add this marketplace to Claude Code:
   ```
   /plugin marketplace add kukoshock/3d-ta-plugins
   ```

2. Install the plugin from the Discover tab, or search for "substance-designer-tutor"

3. Restart Claude Code to load the skill

### Manual Installation

```bash
git clone https://github.com/kukoshock/3d-ta-plugins.git
cd 3d-ta-plugins

# Copy plugin to Claude plugins directory
cp -r plugins/substance-designer-tutor ~/.claude/plugins/
```

## Usage

Once installed, Claude Code will automatically activate the relevant skill when you ask related questions:

```
"How does Tile Sampler work?"
"My ornaments look too uniform, how do I fix this?"
"Explain Height Blend parameters"
```

## Contributing

Have a 3D tool you'd like tutoring support for? Open an issue or PR with:
1. Video tutorial links and timestamps
2. Key concepts and node/parameter documentation
3. Common troubleshooting scenarios

## License

MIT License - Use freely, contribute back!

---

*Built with Claude Code for 3D artists who learn by doing.*
