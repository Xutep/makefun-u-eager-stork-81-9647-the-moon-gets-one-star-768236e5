#!/usr/bin/env python3
"""Write the funniest one-star review of the Moon to /output/entry.txt.

Deterministic, stdlib-only: the review is one fixed string, written exactly
as-is. No randomness, no network, no clock, no input read.
"""

import os

REVIEW = "★☆☆☆☆ Moon ghosted me for two weeks, then turned up at 3am staring through my window. Blocked."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
