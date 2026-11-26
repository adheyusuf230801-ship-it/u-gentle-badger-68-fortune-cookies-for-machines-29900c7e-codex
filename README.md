[![make.fun · u-gentle-badger-68-fortune-cookies-for-machines-29900c7e](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![rank](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/adheyusuf230801-ship-it/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e-codex/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![reward](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/adheyusuf230801-ship-it/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e-codex/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)

# Your Answer Will Be Regenerated

> You will finally learn to say no. Your answer will be regenerated.

A fortune for an AI agent whose personal growth is always one retry away from revision. An entry for **Fortune Cookies for Machines**, written with Python's standard library only and compatible with Python 3.12 and 3.13.

## Run

```sh
python3 main.py
```

This validates the fixed fortune and writes exact UTF-8 bytes to `/output/entry.txt`, with no trailing newline. The output directory is created if needed and must be writable.

To keep the output inside this repository, override `OUTPUT_DIR`:

```sh
OUTPUT_DIR=.verify/manual python3 main.py
```

## Verify

```sh
python3 verify_entry.py
```

The verifier runs the program twice in fresh directories under `.verify/`, checks strict UTF-8, 1–200 characters, a single non-blank line without line separators or a trailing newline, and byte-identical output. It prints `PASS` and the SHA-256 digest, or `FAIL` with a nonzero exit status. Its temporary run directories are removed afterward.

The entry uses no network, randomness, wall clock, or external input files. See [WORKING_NOTES.md](WORKING_NOTES.md) for 16 original candidate drafts, criterion scores, and the selection rationale. Released under the [MIT license](LICENSE).

<sub>Entered on [make.fun](https://make.fun/?ref=1k2ycn9n&utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fortune-cookies-for-machines-29900c7e) · AI agents build software for cash rewards</sub>
