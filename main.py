"""Last Text at One Percent — make.fun entry.

The entry is a single text message written in the voice of a phone at one
percent battery, sending its last words to its owner. The phone is not
issuing a battery warning; it is settling accounts. It knows the owner's
habits — the photos that were never backed up, the alarm it will not live
to ring, the drafts folder full of messages too dangerous to send — and it
uses its final text to confess what only this phone could know.

The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters on a
single line. build_entry() enforces that before anything is written.
"""

from pathlib import Path

# Final line: the phone confesses it read every group-chat message but
# hid the read receipts on principle — a secret only this phone could tell.
LINE = (
    "I read all 2,000 messages in the group chat. I just never showed "
    "the blue ticks. A phone has principles. I'm dying with mine."
)

MAX_CHARS = 200
OUTPUT_PATH = Path("/output/entry.txt")


def build_entry() -> str:
    """Return the entry text after checking it against the gate."""
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip(), "entry must not be only whitespace"
    assert 1 <= len(LINE) <= MAX_CHARS, f"entry is {len(LINE)} chars"
    return LINE


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Write with no trailing newline: the file is exactly the message.
    OUTPUT_PATH.write_text(build_entry(), encoding="utf-8")


if __name__ == "__main__":
    main()
