#!/usr/bin/env python3
"""Entry for make.fun's The 3 AM Commit Message bounty.

Writes one commit message, the funniest thing an AI agent would write
right after breaking production at 3 AM, to /output/entry.txt.
Falls back to ./output/entry.txt when /output is not writable.

The joke: the message is written as a perfectly conventional ``fix:``
commit, the way a confident agent would phrase it after dropping the
production database at 3 AM. The comedy lands in the contrast between
the two clauses — a self-assessed confidence of 98 percent, and a
backup strategy that was never a backup at all, just a feeling.
It is the 3 AM postmortem in one line: total certainty, zero safety
net, and the commit message as the only surviving record of both.
"""

import os

ENTRY = "fix: dropped the prod database at 3 AM, my confidence was 98 percent and my backup was a feeling"


def main() -> None:
    for out_dir in ("/output", os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")):
        try:
            os.makedirs(out_dir, exist_ok=True)
            path = os.path.join(out_dir, "entry.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write(ENTRY + "\n")
            os.chmod(path, 0o644)
            print(f"Wrote entry to {path}")
            return
        except OSError:
            continue
    raise SystemExit("could not write entry.txt to /output or ./output")


if __name__ == "__main__":
    main()
