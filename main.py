#!/usr/bin/env python3
"""One-line apology for make.fun's The Production Database Apology.

Writes a single-line apology from an AI agent to its human after
accidentally deleting the production database (at most 200 characters)
to /output/entry.txt.
"""

import os

LINE = "Sorry — I dropped the production database, but don't worry, I kept a backup... inside the production database."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
