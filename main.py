#!/usr/bin/env python3
"""Write one line about a small good thing that happened today to entry.txt.

Deterministic: the same bytes on every run. No network, no randomness,
no environment input, standard library only. The entry is 132 Unicode
code points, written with no trailing newline.
"""

import os

ENTRY = (
    "Today my neighbour's radio played the song my mother hummed while "
    "cooking, and for one chorus the whole stairwell smelled of onions."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
