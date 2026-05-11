"""Clean YouTube auto-caption VTT to plain text.

YouTube auto-captions duplicate text across cues so the reader sees a
"rolling" subtitle. Plain text only needs each new line once. This
script strips:
  - VTT/Kind/Language headers
  - Cue-time lines (HH:MM:SS.mmm --> HH:MM:SS.mmm ...)
  - Inline word-level timestamps (<00:00:04.080>) and <c> tags
  - Empty lines
  - Consecutive duplicate lines

Usage: python scripts/vtt_to_text.py <input.vtt> [output.txt]
       (omit output to print to stdout)
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

CUE_TIME = re.compile(r"^\d{2}:\d{2}:\d{2}\.\d{3} -->")
INLINE_TS = re.compile(r"<\d{2}:\d{2}:\d{2}\.\d{3}>")
HTML_TAG = re.compile(r"</?[a-zA-Z][^>]*>")


def clean(vtt_text: str) -> str:
    out: list[str] = []
    last: str | None = None
    for raw in vtt_text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("WEBVTT") or line.startswith("Kind:") or line.startswith("Language:"):
            continue
        if CUE_TIME.match(line):
            continue
        line = INLINE_TS.sub("", line)
        line = HTML_TAG.sub("", line)
        line = line.strip()
        if not line:
            continue
        if line == last:
            continue
        out.append(line)
        last = line
    return "\n".join(out) + "\n"


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr)
        return 2
    src = Path(sys.argv[1])
    text = clean(src.read_text(encoding="utf-8"))
    if len(sys.argv) >= 3:
        Path(sys.argv[2]).write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
