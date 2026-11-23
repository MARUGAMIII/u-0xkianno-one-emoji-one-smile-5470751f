#!/usr/bin/env python3
"""One Emoji, One Smile entry.

Writes exactly one emoji to /output/entry.txt: the single emoji most
likely to make a stranger smile.

The pick is heart hands: a small heart made with two hands, sent
straight to whoever is looking at the screen. It is warm at first
glance, needs no context, reads the same to any age or background,
and is clearly a deliberate choice rather than the first default
smiley. A heart gesture from a stranger reads as friendly goodwill,
not romance or flirtation.
"""

import os

EMOJI = "🫶"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI + "\n")
    # Read back and verify: exactly one emoji, nothing else.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written.strip() != EMOJI or len(written.strip()) != 1:
        raise SystemExit(f"bad entry: {written!r}")


if __name__ == "__main__":
    main()
