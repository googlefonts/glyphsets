"""
Assemble .nam files from .nam stub files and language definitions.
"""

import sys
import os

# Insert local module path at beginning of sys.path
# so that up-to-date version of glyphsets package is used
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "Lib"))
from glyphsets.definitions import (
    glyphset_definitions,
    description_per_glyphset,
)  # noqa: E402


if __name__ == "__main__":
    root_folder = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "GF_Glyphsets")
    )

    repo_root_folder = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
        )
    )

    md = []

    # TOC
    md.append("###Table of Conents:\n\n")

    for glyphset_name in glyphset_definitions:
        md.append(f"* [{glyphset_name.replace('_', ' ')}](#{glyphset_name.lower()})")

    md.append("\n")

    # Content
    for glyphset_name in glyphset_definitions:
        md.append(description_per_glyphset(glyphset_name))

    with open(os.path.join(repo_root_folder, "GLYPHSETS.md"), "w") as f:
        f.write("\n".join(md))
