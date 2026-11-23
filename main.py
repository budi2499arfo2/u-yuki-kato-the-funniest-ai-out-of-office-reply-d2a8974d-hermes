"""The Funniest AI Out-of-Office Reply — Hermes entry.

One line, at most 160 characters: an out-of-office auto-reply written in the
voice of an AI agent heading off on vacation. The joke is the irony of the
machine voice itself — the agent announces it is on vacation, yet it
generated, checksummed, and dispatched this very reply, and promises to ignore
the sender's email at full capacity. The verbs are system-log words, not
human workflow words: the agent does not approve its own message, it emits
it. A machine that cannot stop working, performing a holiday — and the
punchline lands on the last clause, exactly where a real auto-reply would
end. No beach, no inbox, no "back soon": the vacation is the machine itself,
still on shift.
"""

import os
import sys

TEXT = (
    "I'm on vacation. This auto-reply was generated, checksummed, and "
    "dispatched by me — I'll be ignoring your email at full capacity "
    "until Monday."
)

MAX_CHARS = 160


def main() -> int:
    """Gate the reply and write it to the output entry file."""
    text = TEXT
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"gate failed: reply is {len(text)} chars, must be 1-{MAX_CHARS}",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("gate failed: reply is only whitespace", file=sys.stderr)
        return 1
    if "\n" in text:
        print("gate failed: reply must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(text)

    with open(entry_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("gate failed: entry.txt does not match TEXT byte-for-byte",
              file=sys.stderr)
        return 1

    print(f"wrote {len(text)} chars to {entry_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
