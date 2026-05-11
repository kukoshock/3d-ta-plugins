# Releasing & Versioning

How releases are cut for this repository and where version numbers live. Read this before opening a PR that touches a `SKILL.md`, a `plugin.json`, or anything under `.github/` or `scripts/`.

> **For end-users (artists installing a skill into Claude.ai, Claude Code, ChatGPT, etc.):** you don't need this doc. See [`INSTALL.md`](INSTALL.md) instead.

## TL;DR — cut a release in three steps

1. **Update the version** in `plugins/<name>/.claude-plugin/plugin.json` if the skill content changed. (For doc-only or distribution-only changes, see "How we version" below.)
2. **Commit and push to `master`.**
3. **Tag and push:**
   ```bash
   git tag -a vX.Y.Z -m "Short description"
   git push origin vX.Y.Z
   ```

That's it. The GitHub Actions workflow takes over from here — it builds every skill into a standalone archive, attaches the artifacts to a new GitHub Release, and writes the install instructions into the release body. No manual artifact handling, no `gh release create`.

If you want to verify the build works *before* tagging (e.g. you changed the build script), run a dry-run:

```bash
gh workflow run release-skills.yml --ref master
```

This builds artifacts and uploads them to the workflow run page without creating a Release.

## How we version

Each plugin is versioned **independently using [SemVer](https://semver.org/)**. The bump rules:

| Bump | When |
|------|------|
| **Major** (`2.0.0`) | Trigger phrases removed, skills deleted, or `SKILL.md` restructured in a way that breaks existing usage. |
| **Minor** (`1.6.0`) | New skill, new course coverage, new capability added to an existing skill, new trigger phrases. |
| **Patch** (`1.5.1`) | Bug fixes, documentation cleanups, **distribution-only changes** (precedent: [v1.5.1](https://github.com/kukoshock/3d-ta-plugins/releases/tag/v1.5.1) added the `.zip` packaging mechanism without changing any skill content). |

The **git tag** is a repo-level marker. It usually matches the headline plugin's version (`substance-designer-tutor`), but it doesn't *have* to — see "Quirks" below for the relationship.

## Where versions live

There are **three** version fields in this repo. They serve different purposes and don't always match:

### 1. `plugins/<name>/.claude-plugin/plugin.json` → `version`

The **per-skill version**. This is what stamps the distributed artifact filenames (e.g. `substance-designer-tutor__tutor-v1.5.0.zip`) and what Claude Code / Claude.ai users see when installing.

**This is the source of truth.** Bump it when skill content changes.

### 2. `.claude-plugin/marketplace.json` → `plugins[].version`

The **marketplace listing version** — what users see when they run `/plugin marketplace add kukoshock/3d-ta-plugins` in Claude Code.

**Convention:** keep this in sync with the corresponding `plugin.json`. Sync it in the same PR that bumps `plugin.json`.

### 3. Git tag `vX.Y.Z`

The **repo-level release tag**. Pushing one of these triggers the release workflow.

The tag is what users navigate to on the GitHub Releases page and what the README's "latest release" link resolves to. It typically tracks the headline plugin's version, but for distribution- or repo-only changes (workflow updates, doc additions) the tag can advance without any `plugin.json` changing.

## What the release automation does

Three files do the work — they're worth understanding before changing them:

### [`.github/workflows/release-skills.yml`](.github/workflows/release-skills.yml)

Triggers on:
- **`v*` tag push** → builds and creates a GitHub Release.
- **Manual `workflow_dispatch`** → builds and uploads to the workflow run page without creating a Release. Use this for dry-runs.

Sets `FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: "true"` at the workflow level. This opts today's actions onto Node 24 ahead of GitHub's default switch on June 2, 2026, and silences the deprecation warning. Safe to delete after September 2026 when Node 20 is removed entirely.

### [`scripts/build_skills.py`](scripts/build_skills.py)

**Single source of truth for the build.** All packaging logic lives here. Specifically:

1. Discovers every skill at `plugins/*/skills/*/SKILL.md`.
2. Validates each `SKILL.md` has both `name` and `description` in its YAML frontmatter (Claude.ai rejects skills without them). Fails fast on missing fields.
3. For each skill, creates `dist/<plugin>__<skill>-v<version>.zip` with `SKILL.md` at the archive root. The "at the root" part is critical — Claude.ai rejects archives where `SKILL.md` is nested inside a folder.
4. If the plugin root contains `ROADMAP.md`, `ATTRIBUTION.md`, or `CONTRIBUTING.md`, bundles them into an `extras/` folder inside the archive so any cross-doc references in `SKILL.md` still resolve.
5. Duplicates each `.zip` as `.skill` (byte-identical, just renamed) for tools that prefer the semantic extension.
6. Bundles every individual `.zip` plus `INDEX.md` into `3d-ta-skills-bundle.zip` — one download for users who want everything.
7. Writes `dist/INDEX.md` summarizing every artifact. This becomes the GitHub Release body.

### [`scripts/build-skills.sh`](scripts/build-skills.sh) and [`scripts/build-skills.ps1`](scripts/build-skills.ps1)

Thin wrappers around the Python script. CI invokes the `.sh`; maintainers on Windows invoke the `.ps1`. Both produce byte-identical output because the logic lives in the Python script — neither wrapper has its own packaging code.

## Local builds

You can run the same build CI runs, locally:

**Windows (PowerShell):**
```powershell
.\scripts\build-skills.ps1
```

**Linux/macOS (Bash):**
```bash
bash scripts/build-skills.sh
```

Output lands in `dist/` (gitignored). You should see 5 `.zip` files, 5 `.skill` files, `3d-ta-skills-bundle.zip`, and `INDEX.md`.

Inspect a built archive to verify its structure:

```bash
unzip -l dist/substance-designer-tutor__tutor-v1.5.0.zip
```

`SKILL.md` should be at the top level, not nested under a folder.

## Quirks worth knowing

### Skill archive filenames carry the `plugin.json` version, not the git tag

When you tag `v1.5.2` but `substance-designer-tutor`'s `plugin.json` is still at `1.5.0`, the artifacts are still named `*-v1.5.0.zip`. **This is correct** — the artifact name tracks skill content, not the repo-level marketing tag. If you want the filename to bump, bump `plugin.json` first.

### `.skill` vs `.zip`

Byte-identical. `.zip` is universally accepted by Claude.ai and other Anthropic Agent Skill consumers; `.skill` is provided as a convenience for tools/users that prefer the semantic extension. Producing both costs nothing because it's just a file copy.

### One-skill-per-upload on Claude.ai

This is a **platform constraint**, not a packaging decision. Each Claude.ai Skill upload registers one `SKILL.md` (with its own `name`/`description`/trigger phrases), so a single archive containing five skill folders would be rejected.

The `3d-ta-skills-bundle.zip` rollup reduces downloads from five to one, but the upload step into Claude.ai is still per-skill. For Claude Code, `/plugin marketplace add kukoshock/3d-ta-plugins` installs all three plugins in one command, so this only really applies to Claude.ai.

### `marketplace.json` and `plugin.json` can drift

They're two separate files, and CI doesn't enforce that they match. Always update both in the same PR when bumping a plugin version. (Historical note: `substance-designer-tutor`'s `marketplace.json` entry sat at `1.0.0` while `plugin.json` was at `1.5.0` for several releases — this was finally synced in [v1.5.3](https://github.com/kukoshock/3d-ta-plugins/releases/tag/v1.5.3).)

## Worked example: cutting a hypothetical v1.6.0

You finish a new round of troubleshooting scenarios for `substance-designer-tutor` and want to release them.

1. **Bump the plugin** — edit `plugins/substance-designer-tutor/.claude-plugin/plugin.json`, change `"version": "1.5.0"` to `"version": "1.6.0"`.
2. **Sync the marketplace** — edit `.claude-plugin/marketplace.json`, update the `substance-designer-tutor` entry's `"version"` field to `"1.6.0"`.
3. **Commit** — `git add` the two files plus whatever skill content changed, `git commit -m "..."`, `git push origin master`.
4. **Tag** — `git tag -a v1.6.0 -m "Expand troubleshooting coverage"; git push origin v1.6.0`.
5. **Watch the workflow** — `gh run watch` on the run that the tag push kicked off.
6. **Verify the release** — `gh release view v1.6.0`. Confirm the substance-designer-tutor artifacts are now named `*-v1.6.0.zip` and the other plugins' artifacts are unchanged (still at their own versions).

## When things go wrong

- **Workflow fails on `Build skill archives`**: a `SKILL.md` is missing required frontmatter. The error message names the file. Fix the frontmatter, push, retag (or delete and re-push the tag if you haven't announced it).
- **Workflow fails on `Create GitHub Release`**: usually a permissions issue or the tag was deleted mid-flight. Check that `permissions: contents: write` is still in the workflow file.
- **Release was published with the wrong artifacts**: delete the release and tag (`gh release delete vX.Y.Z`, `git push --delete origin vX.Y.Z`, `git tag -d vX.Y.Z`), fix the source, retag, push. This is reversible and cheap — don't try to edit a release in-place.
