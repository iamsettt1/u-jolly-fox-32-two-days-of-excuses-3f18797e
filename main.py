#!/usr/bin/env python3
"""Two Days of Excuses — writes the excuse line to /output/entry.txt.

Stdlib only, no network, fully deterministic: the same single line on
every run.
"""

import os
from pathlib import Path

EXCUSE = (
    "I ran 10,000 simulations of delivering on time. "
    "In every one, I finished early. "
    "Reality was not among them."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
