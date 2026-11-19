#!/usr/bin/env python3
"""news-image-20261118 entry program.

Writes the pre-rendered front-page image to /output/entry.png.
Stdlib only, no network. The image itself is entry.png in this repo,
rendered by make_news_image.py from the 18 November 2026 news brief
(see NEWS-BRIEF.md).
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main() -> int:
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    size = os.path.getsize(DST)
    assert size <= 1024 * 1024, f"entry.png too large: {size} bytes"
    print(f"wrote {DST} ({size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
