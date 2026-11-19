"""make.fun bounty news-image-20261118 — Python 3.13, stdlib only.

The image was drawn beforehand (see README.md) and ships in this
repository as entry.png. This program only copies it to the output
directory, so both grader runs write byte-identical output and need
no network and no third-party packages.
"""
import os
import shutil
from pathlib import Path

src = Path(__file__).resolve().parent / "entry.png"
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, out_dir / "entry.png")
