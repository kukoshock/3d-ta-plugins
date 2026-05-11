"""Sync the Credits & Support footer into every SKILL.md from a single template.

Source of truth: templates/credits-footer.md
Target files:    plugins/*/skills/*/SKILL.md

Each SKILL.md gets a block delimited by HTML-comment markers:

    <!-- BEGIN_CREDITS_FOOTER ... -->
    ...rendered template content (fully visible in the prompt)...
    <!-- END_CREDITS_FOOTER -->

The visible content between the markers is what the assistant reads at runtime.
The markers themselves are HTML comments so they don't render on GitHub.

Usage:
    python scripts/sync_credits.py            # apply (rewrites SKILL.md files in place)
    python scripts/sync_credits.py --check    # report only; exit 1 if any file is out of sync
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = REPO_ROOT / "templates" / "credits-footer.md"
SKILL_GLOB = "plugins/*/skills/*/SKILL.md"

BEGIN_MARKER = "<!-- BEGIN_CREDITS_FOOTER (generated from templates/credits-footer.md — edit there, then run `python scripts/sync_credits.py`) -->"
END_MARKER = "<!-- END_CREDITS_FOOTER -->"


def render_block(template_body: str) -> str:
    body = template_body.strip("\n")
    return f"---\n\n{BEGIN_MARKER}\n\n{body}\n\n{END_MARKER}\n"


def replace_or_append(skill_text: str, block: str) -> str:
    begin = skill_text.find(BEGIN_MARKER)
    end = skill_text.find(END_MARKER)

    if begin == -1 and end == -1:
        # First-time injection: strip any trailing whitespace, then append.
        trimmed = skill_text.rstrip() + "\n\n"
        return trimmed + block

    if begin == -1 or end == -1 or end < begin:
        raise ValueError(
            "SKILL.md has mismatched credit markers — manual cleanup needed "
            f"(begin={begin}, end={end})"
        )

    # Walk back from BEGIN to also consume the preceding `---` separator and
    # any blank lines so the rendered block (which provides its own `---`)
    # doesn't leave a double divider behind.
    cut = begin
    while cut > 0 and skill_text[cut - 1] in (" ", "\t", "\n"):
        cut -= 1
    # If the prior non-blank line is exactly `---`, strip it too.
    line_start = skill_text.rfind("\n", 0, cut) + 1
    prior_line = skill_text[line_start:cut].rstrip()
    if prior_line == "---":
        cut = line_start
        # And the blank line before that, if any.
        while cut > 0 and skill_text[cut - 1] in (" ", "\t", "\n"):
            cut -= 1
    before = skill_text[:cut].rstrip() + "\n\n"

    after_marker = end + len(END_MARKER)
    # Drop trailing whitespace after the end marker; we'll add a single newline.
    after = skill_text[after_marker:].lstrip("\n").rstrip()
    if after:
        after = "\n\n" + after + "\n"
    else:
        after = ""

    return before + block + after


def sync(check: bool = False) -> int:
    """Render the template into every SKILL.md (or in --check mode, report drift only).

    Importable from build_skills.py so the release pipeline can ensure credits
    are fresh before packaging. Returns the same exit codes as the CLI:
      0 — success / in sync
      1 — drift detected (only in check mode)
      2 — fatal error (missing template, no SKILL.md, malformed markers)
    """
    if not TEMPLATE_PATH.is_file():
        print(f"ERROR: template not found at {TEMPLATE_PATH}", file=sys.stderr)
        return 2

    template_body = TEMPLATE_PATH.read_text(encoding="utf-8")
    block = render_block(template_body)

    skill_mds = sorted(REPO_ROOT.glob(SKILL_GLOB))
    if not skill_mds:
        print(f"ERROR: no SKILL.md files matched {SKILL_GLOB}", file=sys.stderr)
        return 2

    changed: list[Path] = []
    for skill_md in skill_mds:
        original = skill_md.read_text(encoding="utf-8")
        try:
            updated = replace_or_append(original, block)
        except ValueError as e:
            print(f"ERROR in {skill_md.relative_to(REPO_ROOT)}: {e}", file=sys.stderr)
            return 2

        if updated != original:
            changed.append(skill_md)
            if not check:
                skill_md.write_text(updated, encoding="utf-8")

    rel = lambda p: p.relative_to(REPO_ROOT).as_posix()  # noqa: E731

    if check:
        if changed:
            print("Out of sync with templates/credits-footer.md:", file=sys.stderr)
            for p in changed:
                print(f"  {rel(p)}", file=sys.stderr)
            print(
                "\nRun `python scripts/sync_credits.py` to regenerate.",
                file=sys.stderr,
            )
            return 1
        print(f"All {len(skill_mds)} SKILL.md files are in sync.")
        return 0

    if changed:
        print(f"Updated {len(changed)} of {len(skill_mds)} SKILL.md file(s):")
        for p in changed:
            print(f"  {rel(p)}")
    else:
        print(f"All {len(skill_mds)} SKILL.md files already in sync.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Do not write; exit 1 if any SKILL.md would change.",
    )
    args = parser.parse_args()
    return sync(check=args.check)


if __name__ == "__main__":
    sys.exit(main())
