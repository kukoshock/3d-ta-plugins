"""Build distributable Claude Skill archives from plugins/*/skills/*/.

Outputs to dist/:
  - <plugin>__<skill>-v<version>.zip   (universal; what Claude.ai accepts)
  - <plugin>__<skill>-v<version>.skill (same bytes, renamed for tools that prefer
                                       the semantic extension)
  - INDEX.md                            (Markdown table summarizing every artifact)

Each archive contains the skill folder's contents at the archive ROOT (so SKILL.md
sits at top level — Claude.ai rejects nested layouts). When the plugin root has
ROADMAP.md / ATTRIBUTION.md / CONTRIBUTING.md, they're bundled into an `extras/`
folder inside the archive so cross-doc references inside SKILL.md still resolve.
"""

from __future__ import annotations

import json
import re
import shutil
import sys
import zipfile
from pathlib import Path

from sync_credits import sync as sync_credits

REPO_ROOT = Path(__file__).resolve().parent.parent
DIST_DIR = REPO_ROOT / "dist"
EXTRA_DOCS = ("ROADMAP.md", "ATTRIBUTION.md", "CONTRIBUTING.md")


def parse_frontmatter(skill_md: Path) -> dict[str, str]:
    """Extract name + description from a SKILL.md YAML frontmatter block.

    Handles inline values (`name: Foo`) and YAML folded scalars
    (`description: >` followed by indented lines) — the two forms used in this
    repo. Returns {} when the frontmatter is missing or malformed.
    """
    text = skill_md.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return {}
    fm = m.group(1)
    out: dict[str, str] = {}
    for field in ("name", "description"):
        pat = re.compile(rf"^{field}:\s*(.*)$", re.MULTILINE)
        mm = pat.search(fm)
        if not mm:
            continue
        value = mm.group(1).strip()
        if value in (">", ">-", "|", "|-"):
            tail = fm[mm.end():].lstrip("\n")
            collected: list[str] = []
            for line in tail.splitlines():
                if line.startswith((" ", "\t")):
                    collected.append(line.strip())
                elif line.strip() == "":
                    continue
                else:
                    break
            value = " ".join(collected)
        out[field] = value
    return out


def read_plugin_version(plugin_dir: Path) -> str:
    manifest = plugin_dir / ".claude-plugin" / "plugin.json"
    data = json.loads(manifest.read_text(encoding="utf-8"))
    return data["version"]


def zip_directory_contents(src: Path, dest_zip: Path) -> None:
    """Zip every file under `src` so that paths inside the archive are
    relative to `src` itself (not its parent). This puts SKILL.md at the
    archive root — Claude.ai requires this layout."""
    with zipfile.ZipFile(dest_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(src.rglob("*")):
            if path.is_file():
                zf.write(path, arcname=path.relative_to(src).as_posix())


def human_size(num_bytes: int) -> str:
    size = float(num_bytes)
    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024 or unit == "GB":
            return f"{size:.0f} B" if unit == "B" else f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} GB"


def main() -> int:
    # Render the canonical credits footer into every SKILL.md before packaging.
    # Release archives must always ship with fresh credits, even if a contributor
    # forgot to run `python scripts/sync_credits.py` after editing the template.
    print("Syncing credits footer from templates/credits-footer.md ...")
    sync_rc = sync_credits(check=False)
    if sync_rc != 0:
        print("ERROR: sync_credits failed; aborting build.", file=sys.stderr)
        return sync_rc

    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir(parents=True)

    skill_mds = sorted((REPO_ROOT / "plugins").glob("*/skills/*/SKILL.md"))
    if not skill_mds:
        print("ERROR: no SKILL.md files found under plugins/*/skills/*/", file=sys.stderr)
        return 1

    rows: list[str] = []
    for skill_md in skill_mds:
        skill_dir = skill_md.parent
        skill_name = skill_dir.name
        plugin_dir = skill_dir.parent.parent
        plugin_name = plugin_dir.name

        fm = parse_frontmatter(skill_md)
        missing = [k for k in ("name", "description") if not fm.get(k)]
        if missing:
            print(
                f"ERROR: {skill_md.relative_to(REPO_ROOT)} is missing frontmatter "
                f"field(s): {', '.join(missing)}",
                file=sys.stderr,
            )
            return 1

        version = read_plugin_version(plugin_dir)
        artifact_base = f"{plugin_name}__{skill_name}-v{version}"

        stage = DIST_DIR / f"_stage_{artifact_base}"
        if stage.exists():
            shutil.rmtree(stage)
        shutil.copytree(skill_dir, stage)

        for doc in EXTRA_DOCS:
            src = plugin_dir / doc
            if src.is_file():
                extras_dir = stage / "extras"
                extras_dir.mkdir(exist_ok=True)
                shutil.copy2(src, extras_dir / doc)

        zip_path = DIST_DIR / f"{artifact_base}.zip"
        skill_path = DIST_DIR / f"{artifact_base}.skill"
        zip_directory_contents(stage, zip_path)
        shutil.copy2(zip_path, skill_path)
        shutil.rmtree(stage)

        size = human_size(zip_path.stat().st_size)
        short_desc = re.sub(r"\s+", " ", fm["description"]).strip()
        if len(short_desc) > 140:
            short_desc = short_desc[:137].rstrip() + "..."

        rows.append(
            f"| **{fm['name']}** | `{plugin_name}` | {version} | "
            f"{short_desc} | [.zip]({artifact_base}.zip) · "
            f"[.skill]({artifact_base}.skill) ({size}) |"
        )
        print(f"built: {artifact_base} ({size})")

    index = DIST_DIR / "INDEX.md"
    index.write_text(
        "# 3D Technical Artist Skills — Release Artifacts\n\n"
        "Upload any of these to **Claude.ai → Settings → Capabilities → Skills**, "
        "or to any other AI tool that accepts Anthropic Agent Skill archives.\n\n"
        "Each row links to a `.zip` (universal) and a `.skill` (same archive, "
        "renamed) for tools that prefer the semantic extension.\n\n"
        "**Want everything in one download?** Grab "
        "`3d-ta-skills-bundle.zip` from the assets below — it contains every "
        "individual `.zip` plus this `INDEX.md`. Unzip locally, then upload "
        "each inner archive to Claude.ai (one upload per skill is a Claude.ai "
        "platform requirement, not a packaging choice).\n\n"
        "| Skill | Plugin | Version | Description | Download |\n"
        "|-------|--------|---------|-------------|----------|\n"
        + "\n".join(rows)
        + "\n",
        encoding="utf-8",
    )

    bundle_path = DIST_DIR / "3d-ta-skills-bundle.zip"
    with zipfile.ZipFile(bundle_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(index, arcname="INDEX.md")
        for zp in sorted(DIST_DIR.glob("*.zip")):
            if zp.name == bundle_path.name:
                continue
            zf.write(zp, arcname=zp.name)
    print(f"built: 3d-ta-skills-bundle ({human_size(bundle_path.stat().st_size)})")

    print(f"\nBuilt {len(skill_mds)} skill archive(s) + 1 bundle in {DIST_DIR}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
