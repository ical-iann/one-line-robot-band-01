#!/usr/bin/env python3
"""Name the Robot Band — one funny robot band name + its hit song.

Writes a single line of text (under 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (harness program/v1).
Deterministic: no network, no randomness, identical bytes every run.
"""

import os

TEXT = "The Roombas \u2014 hit single 'Suck It Up' vacuumed up every award, then got stuck under the couch and died mid-solo."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
