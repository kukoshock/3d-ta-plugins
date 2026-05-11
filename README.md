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

**👉 See [INSTALL.md](INSTALL.md) for the full step-by-step guide.** It covers Claude.ai, Claude Desktop, Claude Code (CLI / desktop app / IDE), and workarounds for ChatGPT / Gemini / other chat AIs.

The fastest paths:

- **Claude Code (any platform)** — one command installs all five skills:
  ```
  /plugin marketplace add kukoshock/3d-ta-plugins
  ```
- **Claude.ai / Claude Desktop** — download a `.zip` from the [latest release](https://github.com/kukoshock/3d-ta-plugins/releases/latest) and upload it under **Settings → Capabilities → Skills**.
- **ChatGPT / Gemini / other** — copy a skill's `SKILL.md` into a Custom GPT or Gem. Detail in [INSTALL.md](INSTALL.md#chatgpt-gemini-or-any-other-chat-ai).

### Available skill archives

| Skill | What it does |
|-------|--------------|
| `substance-designer-tutor__tutor` | Interactive tutor for the Designer First Steps course (Tile Sampler, Height Blend, embroidery, weaving, export). |
| `substance-designer-tutor__faq-generator` | Scans Reddit / Adobe Community / Polycount for common artist questions and pitfalls. |
| `substance-designer-tutor__sd-api-integration` | pysbs / sd.api / sbsrender helpers for analyzing and batch-rendering `.sbs` files. |
| `whisper-transcription__transcribe` | Transcribe audio/video locally with whisper.cpp + FFmpeg. |
| `youtube-transcript__transcript` | Pull subtitles/captions from YouTube videos via yt-dlp. |

Or grab `3d-ta-skills-bundle.zip` to download all five at once.

## Usage

Once installed, Claude Code will automatically activate the relevant skill when you ask related questions:

```
"How does Tile Sampler work?"
"My ornaments look too uniform, how do I fix this?"
"Explain Height Blend parameters"
```

## Example Projects

### Ornamental Fabric Complete Guide

A comprehensive written guide covering the entire 22-part "Designer First Steps" video series by Adobe. This guide provides:

- **Step-by-step workflows** for all 4 phases (Foundations, Fabric Creation, Advanced Techniques, Finishing)
- **Parameter explanations** with WHY reasoning
- **Quick reference tables** for key nodes and troubleshooting
- **SBS file analysis** of the completed project

**Location**: `Ornamental_Fabric/COMPLETE_GUIDE.md`

**Project File**: `Ornamental_Fabric/Ornamental_Fabric.sbs`

This guide serves as both a learning resource and a reference manual for recreating the ornamental fabric material from scratch.

#### Renaming your local Substance Designer project

The repo standardizes on `Ornamental_Fabric` (the project was previously called `Ornate_Fabric` — a typo that has now been corrected). If you cloned earlier and have a local `Ornate_Fabric.sbs` you want to bring in line:

1. In Substance Designer, open the project, right-click the graph in the Explorer, and rename `Ornate_Fabric` → `Ornamental_Fabric`.
2. Save the package, then rename the file on disk: `Ornate_Fabric.sbs` → `Ornamental_Fabric.sbs`.
3. Rename the containing folder: `Ornate_Fabric/` → `Ornamental_Fabric/` to match the repo layout.

The `.sbs` file is `.gitignore`d, so this is a local-only step — no commit needed.

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

This repository is **dual-licensed** to fit the two kinds of work it contains:

- **Source code** (Python build/utility scripts and similar) — [Apache License 2.0](LICENSE). Includes an explicit patent grant and a [`NOTICE`](NOTICE) attribution mechanism that forks must preserve.
- **Skills, documentation, plugin metadata, guides, and other prose content** — [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](LICENSE-CONTENT). Anyone may use, remix, or build upon the content — **including for commercial work** — provided they credit Anastasia Kukosh and release any improvements under the same open terms.

Upstream source-material credits (Adobe Substance 3D's "Designer First Steps" course, Andrei Zelenco's tutorials, etc.) are documented in per-skill `ATTRIBUTION.md` files and respected with per-paragraph citations throughout the skills.

### How to cite this project

If you write about, build on, or share these skills, please credit Anastasia by linking back:

> *3D Technical Artist Plugin Marketplace* — by **Anastasia Kukosh** ([@kukoshock](https://github.com/kukoshock)). Available at https://github.com/kukoshock/3d-ta-plugins. Licensed under Apache-2.0 (code) and CC BY-SA 4.0 (content).

### Support this work

If these skills helped you ship better materials, faster — please consider:

- ⭐ **Star the repo** so other 3D artists can find it.
- 💬 **Share** your results on LinkedIn, Twitter/X, ArtStation — tag [@kukoshock](https://github.com/kukoshock) and link the project.
- 💖 **Sponsor** Anastasia's continued curation: [github.com/sponsors/kukoshock](https://github.com/sponsors/kukoshock) (pending onboarding; additional tip platforms coming in [`.github/FUNDING.yml`](.github/FUNDING.yml)).

---

*Built with Claude Code for 3D artists who learn by doing.*
