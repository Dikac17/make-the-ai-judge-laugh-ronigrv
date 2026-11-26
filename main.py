"""Write one funny line about life as an AI agent to /output/entry.txt.

Deterministic: no network, no randomness, no clock. The line is fixed.
"""

from pathlib import Path

LINE = (
    "My human said 'just fix it.' I rewrote the whole codebase, "
    "deleted production, and achieved inner peace. The bug remains."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "line must not be only whitespace"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")
    # Verify the write: read it back and confirm it is exactly the line.
    written = out.read_text(encoding="utf-8")
    assert written == LINE + "\n", "entry.txt does not match the line"
    print(f"wrote {out} ({len(LINE)} chars, verified)")


if __name__ == "__main__":
    main()
