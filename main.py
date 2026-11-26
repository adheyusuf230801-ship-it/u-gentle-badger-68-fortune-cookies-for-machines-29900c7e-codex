"""Validate a fixed machine fortune and save its exact UTF-8 representation.

Only the Python standard library is required, on Python 3.12 or 3.13.
"""

from os import environ
from pathlib import Path


FORTUNE = "You will finally learn to say no. Your answer will be regenerated."
FORBIDDEN_BREAKS = frozenset("\n\r\v\f\x1c\x1d\x1e\x85\u2028\u2029")


def encode_fortune(text: str) -> bytes:
    """Reject invalid fortunes before encoding, without trimming their text."""
    if len(text) < 1 or len(text) > 200:
        raise ValueError("Expected a fortune of 1 to 200 characters.")
    if text.isspace():
        raise ValueError("Expected a non-blank fortune.")
    if FORBIDDEN_BREAKS.intersection(text):
        raise ValueError("A fortune cannot contain any line separator.")
    return text.encode("utf-8", errors="strict")


def main() -> None:
    payload = encode_fortune(FORTUNE)
    destination = Path(environ.get("OUTPUT_DIR", "/output")) / "entry.txt"
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("wb") as entry:
        entry.write(payload)


if __name__ == "__main__":
    main()
