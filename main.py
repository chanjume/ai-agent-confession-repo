#!/usr/bin/env python3
"""Write the one-line AI agent confession to /output/entry.txt.

Entry (114 chars, limit 200): the agent confesses it spent 6 hours and
14,000 tokens "thinking" about a bug, then fixed it by deleting the line
it added yesterday.
"""
import os

ENTRY = (
    "I spent 6 hours and 14,000 tokens 'thinking' about your bug, "
    "then fixed it by deleting the line I added yesterday."
)


def main() -> None:
    # Gate: the sealed scorer only accepts 1-200 chars of non-blank UTF-8.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, limit 200"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
