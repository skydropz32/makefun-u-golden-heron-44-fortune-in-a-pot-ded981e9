"""Fortune in a Pot: writes one kind, funny fortune for a houseplant to /output/entry.txt."""

from pathlib import Path

LINE = "Your roots will outgrow this pot, your keeper will buy a bigger one, and you will pretend it was your idea all along."


def main() -> None:
    # Gate: the entry must be 1-120 characters of non-blank UTF-8 text.
    if not 1 <= len(LINE) <= 120 or not LINE.strip():
        raise ValueError("entry line must be 1-120 characters")
    Path("/output").mkdir(parents=True, exist_ok=True)
    Path("/output/entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
