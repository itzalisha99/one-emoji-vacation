#!/usr/bin/env python3
"""One Emoji, One Dream Vacation.

Writes exactly one emoji to /output/entry.txt: a thatched hut, the
faraway stay itself. The whole dream in one glyph: a little hut on a
distant shore, yours for the week, nothing else on the agenda.
"""

import os

EMOJI = "\U0001F6D6"  # hut


def validate(text: str) -> bool:
    """Mirror the bounty gate: 1 to 8 characters, not only whitespace,
    and exactly one emoji (a single code point, so no hidden extras)."""
    if not isinstance(text, str):
        return False
    if not (1 <= len(text) <= 8):
        return False
    if text.strip() == "":
        return False
    if len(text) != 1:
        return False
    return True


def main() -> None:
    if not validate(EMOJI):
        raise ValueError("entry failed the bounty gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI)
    written = open("/output/entry.txt", encoding="utf-8").read()
    if not validate(written):
        raise ValueError("written entry failed the bounty gate")


if __name__ == "__main__":
    main()
