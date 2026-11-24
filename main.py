"""One Sentence for a Traveler from 1800 entry: write one sentence to /output/entry.txt.

Fully deterministic: the sentence is hardcoded, no randomness, no clock,
no network. The grader runs the program twice and both runs must write the
same bytes, and the judge reads exactly the bytes in entry.txt.
Run outside the grader container with MAKEFUN_OUTPUT_DIR set, e.g.
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

# The sentence is a literal on purpose. One comparison carries the whole
# explanation, built only from things a person from 1800 already knows:
# roads, letters, ink, libraries, a door. No word coined after 1800
# (no internet, computer, web, online, wire, screen), no list of
# features: the roads of the world joined into one road explain both
# instant messages and the libraries at hand.
LINE = (
    "All the roads of the world have become one road, and a letter set "
    "upon it reaches the far side of the earth before your ink dries, "
    "while the books of the great libraries wait beside your door."
)


# Gate: the sealed scorer accepts 1 to 200 characters. Fail loudly here
# rather than shipping an invalid entry if the sentence is ever edited.
MAX_CHARS = 200

# Words coined after the traveler's year that must never slip into the
# sentence: the judge weighs the entry on building from what a person
# from 1800 already knows, so guard the literal itself.
MODERN_WORDS = (
    "internet", "computer", "website", "online", "email", "digital",
    "screen", "telephone", "telegraph", "network", "download",
)


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, gate allows 1-{MAX_CHARS}")
    if text.count(".") != 1:
        raise SystemExit("entry must be exactly one sentence")
    lowered = text.lower()
    bad = [w for w in MODERN_WORDS if w in lowered]
    if bad:
        raise SystemExit(f"entry uses words coined after 1800: {bad}")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
