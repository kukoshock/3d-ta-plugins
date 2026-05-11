# Install Guide for Artists

A short, click-by-click guide to using these skills in whatever AI tool you already chat with. Pick the section for your tool — most people only need one.

If you maintain the project, see [`RELEASING.md`](RELEASING.md) instead.

---

## Claude.ai (browser) or Claude Desktop (Mac / Windows app)

**Recommended for artists.** Same flow in both places.

1. Go to the [latest release](https://github.com/kukoshock/3d-ta-plugins/releases/latest).
2. Under "Assets", click the `.zip` for the skill you want. Most artists want:
   - **`substance-designer-tutor__tutor-v1.5.0.zip`** — the headline tutor for the Designer First Steps course.
3. In Claude.ai (or Claude Desktop), open **Settings → Capabilities → Skills** and upload the file you just downloaded.
4. Start a new chat and ask a trigger phrase, e.g. *"How does Tile Sampler work?"* The tutor will activate.

### Want all five skills at once?

Download **`3d-ta-skills-bundle.zip`** from the same release page. Unzip it, then upload each inner `.zip` to Claude.ai one at a time. Claude.ai requires one upload per skill — that's a platform rule, not a packaging choice.

### Prefer the `.skill` extension?

Every `.zip` is also published as `.skill` (same file, renamed). Pick whichever your tool prefers — Claude.ai accepts both.

---

## Claude Code (CLI, IDE, or desktop app)

**Recommended if you already have Claude Code installed.** This installs all three plugins (five skills total) in one command.

### From a terminal (Mac, Windows, or Linux)

```
/plugin marketplace add kukoshock/3d-ta-plugins
```

Run that inside a `claude` session. Restart Claude Code, then ask a trigger phrase in any chat.

### From the Claude Code desktop app (Mac or Windows)

1. Launch Claude Code from your Applications folder (Mac) or Start menu (Windows).
2. In any conversation, type the same slash command:
   ```
   /plugin marketplace add kukoshock/3d-ta-plugins
   ```
3. Pick the plugins you want from the Discover tab, then restart the app.

### From VS Code or JetBrains

1. Open the Claude Code panel.
2. Type the slash command into the prompt.
3. Reload the panel after install.

### Where the files land

On all platforms, plugins install into your user home directory:
- **Mac / Linux**: `~/.claude/plugins/`
- **Windows**: `%USERPROFILE%\.claude\plugins\`

You don't need to touch these files. The marketplace command handles install, updates, and removal.

---

## ChatGPT, Gemini, or any other chat AI

**Honest answer:** these tools don't accept the Anthropic Skill `.zip` format. You can still use the tutor content — it just takes one manual step.

### Workaround

1. Download `substance-designer-tutor__tutor-v1.5.0.zip` from the [latest release](https://github.com/kukoshock/3d-ta-plugins/releases/latest).
2. Unzip it. Open the file named `SKILL.md` in any text editor.
3. Copy the entire contents of `SKILL.md`.
4. Paste it as:
   - **ChatGPT** → instructions for a new [Custom GPT](https://help.openai.com/en/articles/8554407-creating-a-gpt)
   - **Gemini** → instructions for a new [Gem](https://gemini.google.com/gems/view)
   - **Anything else** → the tool's "system prompt" / "custom instructions" / "persona" field
5. Start a chat with your new persona and ask a trigger phrase.

### What you lose

- The skill's `references/` and `sources/` folders contain extra detail that Claude can read at runtime. ChatGPT/Gemini can't see those, so the persona only has what's in `SKILL.md` itself. For the tutor, that's still ~700 lines of guidance — plenty for most questions, but deep dives into specific course parts may be thinner.
- Trigger phrases don't auto-activate the persona. Lead each new chat with *"You are the Substance Designer tutor as described above."*

---

## Troubleshooting

**The upload was rejected by Claude.ai.**
Make sure you downloaded the `.zip` (or `.skill`) — not the source `.tar.gz`. Open the archive locally and confirm `SKILL.md` is at the **top level** of the archive, not inside a folder.

**The tutor isn't activating when I ask a question.**
Try one of the explicit trigger phrases from the skill's description: *"explain Tile Sampler"*, *"how does Height Blend work"*, *"troubleshoot my graph"*, *"fabric material help"*. Trigger matching is keyword-based.

**Claude.ai doesn't show a Skills option in Settings.**
Skills must be enabled for your Claude.ai account. Check **Settings → Feature Preview** (or the equivalent for your plan) for a Skills toggle. Free-tier accounts may not have access yet.

**I installed via Claude Code but no skill is firing.**
After `/plugin marketplace add`, you need to install the specific plugin from the Discover tab (the marketplace command only registers the source). Then restart Claude Code.

**Where can I report a bug or request a new skill?**
[Open an issue](https://github.com/kukoshock/3d-ta-plugins/issues/new) describing what's not working or what you'd like to learn. Include which AI tool you're using and which skill.
