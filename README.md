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

**Current Version:** 1.5.0

A tutor for learning Substance Designer through the "Designer First Steps" course by Adobe Substance 3D. Features deep "WHY" explanations that teach the reasoning behind parameter choices, not just the values.

**Covers:**
- Thread creation (Part 5)
- Fabric weaving patterns (Part 6)
- Procedural shape design (Part 7)
- Fabric embroidery with Tile Sampler & Height Blend (Part 9)

**Key Features:**
- **Quick Reference Table**: Top 10 most common issues with instant solutions (v1.5.0)
- **WHY Explanations**: Understand why 600x700 creates dense weave, why Scale Map creates tapered edges
- **Comprehensive Troubleshooting**: 47+ scenarios with root cause analysis and pedagogical explanations
- **Engine-Specific Guides**: DirectX vs OpenGL normal maps, sRGB vs Linear color spaces, engine compatibility tables
- **Parameter Decision Trees**: Choose appropriate values based on artistic intent (Low/Medium/High density guides)
- **Root Cause Troubleshooting**: Learn underlying principles, not just copy-paste solutions
- **Critical Techniques**: Scale Map vs Mask Input, Height Blend contrast, fiber density

**Skills:**

1. **Tutor** - Interactive learning companion for Designer First Steps course
   - Trigger phrases: "explain Tile Sampler", "how does Height Blend work", "troubleshoot my graph"

2. **FAQ Generator** - Scans 3D artist forums (Reddit, Adobe Community, Polycount) for common questions
   - Extracts high-engagement FAQs about visual quality, nodes, tiling, export issues
   - Focus: Artist perspective (visual outcomes), NOT scripting/automation
   - Trigger phrases: "find common questions", "scan forums for FAQs", "what do beginners struggle with"

**Recent Updates (v1.5.0):**
- Added Quick Reference table for instant triage of common issues
- Comprehensive DirectX vs OpenGL normal map guide with engine compatibility table
- Enhanced 7 troubleshooting scenarios with detailed WHY explanations
- All scenarios now provide pedagogical understanding, not just mechanical fixes

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

### Via Claude.ai / Claude Chat (for artists)

If you use Claude in the browser (claude.ai) rather than Claude Code, you can install each skill as a single uploaded file — no terminal, no git.

1. Open the [latest release](https://github.com/kukoshock/3d-ta-plugins/releases/latest) and download the `.zip` (or `.skill`) for the skill you want.
2. In Claude.ai, go to **Settings → Capabilities → Skills** and upload the file.
3. Start a new chat and ask a trigger phrase — e.g. *"How does Tile Sampler work?"* for the tutor.

**Want everything at once?** Download `3d-ta-skills-bundle.zip` from the same release page — it contains all five `.zip` archives plus the index. Unzip locally, then drag each inner archive into Claude.ai's Skills uploader. (Claude.ai requires one upload per skill — that's a platform constraint, not a packaging choice.)

Each skill is a separate, independent download. Grab one, several, or all of them:

| Skill | What it does |
|-------|--------------|
| `substance-designer-tutor__tutor` | Interactive tutor for the Designer First Steps course (Tile Sampler, Height Blend, embroidery, weaving, export). |
| `substance-designer-tutor__faq-generator` | Scans Reddit / Adobe Community / Polycount for common artist questions and pitfalls. |
| `substance-designer-tutor__sd-api-integration` | pysbs / sd.api / sbsrender helpers for analyzing and batch-rendering `.sbs` files. |
| `whisper-transcription__transcribe` | Transcribe audio/video locally with whisper.cpp + FFmpeg. |
| `youtube-transcript__transcript` | Pull subtitles/captions from YouTube videos via yt-dlp. |

The same `.zip` files work with any other AI tool that accepts Anthropic Agent Skill archives.

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

## Example Projects

### Ornate Fabric Complete Guide

A comprehensive written guide covering the entire 22-part "Designer First Steps" video series by Adobe. This guide provides:

- **Step-by-step workflows** for all 4 phases (Foundations, Fabric Creation, Advanced Techniques, Finishing)
- **Parameter explanations** with WHY reasoning
- **Quick reference tables** for key nodes and troubleshooting
- **SBS file analysis** of the completed project

**Location**: `Ornate_Fabric/COMPLETE_GUIDE.md`

**Project File**: `Ornate_Fabric/Ornate_Fabric.sbs`

This guide serves as both a learning resource and a reference manual for recreating the ornate fabric material from scratch.

## Releasing

For maintainers and contributors: see [`RELEASING.md`](RELEASING.md) for the version strategy, where versions live in the repo, and how the GitHub Actions release workflow turns a `vX.Y.Z` tag into a published GitHub Release with all skill archives attached.

## Contributing

Have a 3D tool you'd like tutoring support for? Open an issue or PR with:
1. Video tutorial links and timestamps
2. Key concepts and node/parameter documentation
3. Common troubleshooting scenarios

### Development Attribution

This plugin is developed collaboratively:
- **Initial Development & Domain Expertise**: Anastasia Kukosh
- **Enhancement & Documentation**: Claude Code (Sonnet 4.5)
- **Community Feedback**: 3D artist community via forums and issue reports

All major versions include both human creative direction and AI-assisted implementation.

## Roadmap

### substance-designer-tutor

**v1.6.0 - Planned**
- Expand troubleshooting coverage based on FAQ analysis
- Add visual comparison examples for common issues
- Create decision trees for node selection

**v2.0.0 - Future**
- Coverage of remaining Designer First Steps course parts
- Interactive graph debugging workflows
- PBR material validation checklists

**Community Requests Welcome!**
- Open an issue with specific troubleshooting needs
- Share common problems from your learning journey
- Suggest additional course coverage

## License

MIT License - Use freely, contribute back!

---

*Built with Claude Code for 3D artists who learn by doing.*
