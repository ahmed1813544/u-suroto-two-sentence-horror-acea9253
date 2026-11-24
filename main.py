"""Two-Sentence Horror entry.

Writes one original two-sentence horror story to entry.txt.
Stdlib only, fully deterministic: the same text every run.
"""

import os

STORY = (
    "Every night, the man in the apartment below plays the same four bars "
    "of Chopin at 2 a.m., and I have learned to fall asleep to it. "
    "Last night it stopped halfway through, and a moment later I heard it "
    "begin again — on my piano, downstairs in my own living room."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(STORY + "\n")


if __name__ == "__main__":
    main()
