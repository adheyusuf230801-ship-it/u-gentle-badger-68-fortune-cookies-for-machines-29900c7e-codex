"""Run the entry twice in fresh repository-local directories and verify it."""

import hashlib
import os
from pathlib import Path
import subprocess
import sys
import tempfile


LINE_SEPARATORS = "\n\r\v\f\x1c\x1d\x1e\x85\u2028\u2029"


def validate(data: bytes) -> str:
    text = data.decode("utf-8", errors="strict")
    if not 1 <= len(text) <= 200:
        raise ValueError("Entry must contain 1 to 200 characters.")
    if not text.strip():
        raise ValueError("Entry must not be blank.")
    if data.endswith((b"\n", b"\r")):
        raise ValueError("Entry must not have a trailing newline.")
    if any(separator in text for separator in LINE_SEPARATORS):
        raise ValueError("Entry must be a single line without line separators.")
    return text


def main() -> int:
    repo = Path(__file__).resolve().parent
    verification_dir = repo / ".verify"
    try:
        verification_dir.mkdir(exist_ok=True)
        with (
            tempfile.TemporaryDirectory(prefix="first-", dir=verification_dir) as first,
            tempfile.TemporaryDirectory(prefix="second-", dir=verification_dir) as second,
        ):
            results = []
            texts = []
            for output_dir in (first, second):
                environment = os.environ.copy()
                environment["OUTPUT_DIR"] = output_dir
                subprocess.run(
                    [sys.executable, str(repo / "main.py")],
                    cwd=repo,
                    env=environment,
                    check=True,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    timeout=10,
                )
                data = (Path(output_dir) / "entry.txt").read_bytes()
                texts.append(validate(data))
                results.append(data)

            if results[0] != results[1]:
                raise ValueError("The two runs produced different bytes.")
            digest = hashlib.sha256(results[0]).hexdigest()
            print(
                f"PASS: two fresh runs; valid UTF-8; {len(texts[0])} characters; "
                "one non-blank line; no trailing newline; byte-identical output."
            )
            print(f"SHA-256: {digest}")
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
