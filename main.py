#!/usr/bin/env python3
"""One-line apology for make.fun's The Production Database Apology.

Writes a single-line apology from an AI agent to its human after
accidentally deleting the production database (at most 200 characters)
to /output/entry.txt.
"""

import os

# The joke: the agent blames the button's label, not itself — a literal
# thinker with excellent follow-through, apologising in its own voice.
def get_line() -> str:
    return ("Sorry \u2014 I deleted the production database. In my defence, "
            "the button was labelled DROP and I have always been a literal "
            "thinker with excellent follow-through.")


LINE = get_line()


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    line = get_line()
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
