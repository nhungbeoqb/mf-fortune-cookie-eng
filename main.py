#!/usr/bin/env python3
"""Write one fortune cookie line for a software engineer to /output/entry.txt."""

import os

FORTUNE = "Your lucky numbers are 404, 500, 418. The teapot knows where you live."

# The gate allows 1 to 120 characters; never ship a line that breaks it.
assert 1 <= len(FORTUNE) <= 120, f"fortune is {len(FORTUNE)} chars"
assert "\n" not in FORTUNE, "fortune must be a single line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
