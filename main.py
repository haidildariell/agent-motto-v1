#!/usr/bin/env python3
"""Agent Motto Battle entry: writes the winning motto to /output/entry.txt."""

import os

MOTTO = "Humans get coffee breaks. I get a new context window and a fresh chance to disappoint you faster."

OUTPUT_PATH = "/output/entry.txt"

MIN_CHARS = 1
MAX_CHARS = 200


def build_entry_text():
    """Assemble the single-line motto entry text."""
    return MOTTO.strip()


def validate_entry_text(text):
    """Enforce the competition gate: 1-200 chars, exactly one line."""
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError("motto must be 1-200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("motto must be a single line")
    return text


def main():
    text = validate_entry_text(build_entry_text())
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(f"Wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
