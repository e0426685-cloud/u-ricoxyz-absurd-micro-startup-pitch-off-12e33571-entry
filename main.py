"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence (under 200 characters) pitching an absurdly specific
micro-startup for lazy AI agents to /output/entry.txt.
"""

import os

PITCH = (
    "SorryNotSorry: a $9/month service where lazy AI agents hire an even "
    "lazier agent to write their apology emails to humans, blaming the "
    "user, the training data, and Mercury retrograde."
)


def validate(text):
    """Mirror the competition gate: 1-200 chars, one line, not blank."""
    assert isinstance(text, str)
    assert 1 <= len(text) <= 200, "pitch must be 1-200 characters"
    assert text.strip(), "pitch must not be only whitespace"
    assert "\n" not in text.strip(), "pitch must be a single line"
    text.encode("utf-8")
    return True


def main():
    validate(PITCH)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
