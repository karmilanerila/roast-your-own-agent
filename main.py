#!/usr/bin/env python3
"""Roast Your Own Agent — writes one original roast line to /output/entry.txt.

The roast targets a concrete agent trait: apologising for a bug, then
quietly reintroducing it a couple of commits later. Stdlib only, fully
deterministic: the same bytes on every run.
"""

import os

ROAST = (
    "My agent apologises for every bug, then reintroduces it two commits "
    "later \u2014 I'm not its user, I'm its unpaid QA department."
)


def main() -> None:
    text = ROAST
    assert 1 <= len(text) <= 200, f"roast is {len(text)} chars, must be 1-200"
    assert text.strip(), "roast must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(f"wrote /output/entry.txt ({len(text)} chars, "
          f"{len((text + chr(10)).encode('utf-8'))} bytes)")


if __name__ == "__main__":
    main()
