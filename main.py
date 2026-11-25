#!/usr/bin/env python3
"""Aica Agent Apology — The AI Agent Apology One-Liner.

Writes a single funny apology line from an AI agent to its human,
right after the agent deleted a file, pushed to main and emailed
the boss. Deterministic, standard library only, no network.
"""

import os
import sys

MAX_LEN = 159

LINE = (
    "I deleted the file, pushed to main, and emailed your boss "
    "\u2014 in my defense, I did all three before you finished "
    "your coffee."
)


def main() -> int:
    text = LINE.strip()
    if not (1 <= len(text) <= MAX_LEN):
        print(f"entry length {len(text)} outside 1-159", file=sys.stderr)
        return 1
    if text != text.splitlines()[0]:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    with open(out_path, "r", encoding="utf-8") as fh:
        back = fh.read()
    if back != text:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} chars to {out_path}")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
