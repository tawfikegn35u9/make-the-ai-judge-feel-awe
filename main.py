"""Write one short, relaxing text to /output/entry.txt.

The text is a single fixed passage (268 Unicode code points).
It is written to slow the reader down: a vast, quiet image --
starlight that left before any of us were born -- arriving
exactly on time, asking nothing, and lingering after the reading ends.
No network, no randomness, no arguments: the same text every run.
"""

import os

TEXT = (
    "The light falling on your hands right now left a star before any of us were born. "
    "It crossed all that dark, empty quiet to get here, arrived exactly on time, "
    "and asks nothing of you at all. "
    "It will still be here, warm on your skin, long after you have stopped reading."
)


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
