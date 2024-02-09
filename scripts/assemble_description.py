"""
Assemble .nam files from .nam stub files and language definitions.
"""

import sys
import os

# Insert local module path at beginning of sys.path
# so that up-to-date version of glyphsets package is used
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "Lib"))
from glyphsets import (
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
    md.append("# Table of Conents:\n\n")

    for glyphset_name in glyphset_definitions:
        _new_md, warning = description_per_glyphset(glyphset_name)
        warning_md = " ✅"
        if warning:
            warning_md = " 🛑"
        md.append(
            f"* [{glyphset_name.replace('_', ' ')}{warning_md}](#{glyphset_name.lower().replace('_', '-')})"
        )

    md.append(
        "\n> [!NOTE]  \n> This document is a human-readable representation of the glyphset defintions defined in code [here](/Lib/glyphsets/definitions/__init__.py) and gets updated automatically as part of the `sh build.sh` command.\n"
    )
    md.append(
        "\n> [!NOTE]  \n> The symbols ✅ and 🛑 above denote whether or not this glyphset is available as part of Fontbakery's `shape_languages` check.\n"
    )
    md.append(
        "\n> [!NOTE]  \n> There are other glyphsets covered under the old approach that are still available in [/GF_glyphsets](/GF_glyphsets) but are not part of this document and not available to Fontbakery's `shape_languages` check.\n"
    )

    md.append("\n")

    # Content
    for glyphset_name in glyphset_definitions:
        new_md, _warning = description_per_glyphset(glyphset_name)
        md.append(new_md)

    with open(os.path.join(repo_root_folder, "GLYPHSETS.md"), "w") as f:
        f.write("\n".join(md))
