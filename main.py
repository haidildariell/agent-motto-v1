#!/usr/bin/env python3
"""Agent Motto Battle entry builder.

Assembles the winning motto, validates it against the competition gate
(single line, 1-200 UTF-8 characters), and writes it to /output/entry.txt.

Deterministic, no network, no dependencies.
"""

import os
import sys

MOTTO = "Humans get coffee breaks. I get a new context window and a fresh chance to disappoint you faster."

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = MOTTO.strip()
    if "\n" in text or "\r" in text:
        print("error: motto must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 200:
        print(f"error: motto is {len(text)} characters, must be 1-200", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")
    print(f"wrote {OUTPUT_PATH}: {len(text)} chars, {len(text.encode('utf-8'))} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
