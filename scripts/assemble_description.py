"""
Assemble .nam files from .nam stub files and language definitions.
"""

import sys
import os

# Insert local module path at beginning of sys.path
# so that up-to-date version of glyphsets package is used
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "Lib"))
from glyphsets import (
    defined_glyphsets,
    defined_scripts,
    glyphsets_per_script,
    GlyphSet,
)  # noqa: E402

if __name__ == "__main__":
    root_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "GF_Glyphsets"))

    repo_root_folder = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
        )
    )

    md = []

    # TOC
    md.append("# Table of Contents:\n\n")

    # Get scripts
    scripts = defined_scripts()
    script_dict = {}
    max_glyphsets = 0
    md.append("| " + " | ".join(scripts) + " |")
    md.append("| " + " | ".join(["---"] * len(scripts)) + " |")
    for script in scripts:
        max_glyphsets = max(max_glyphsets, len(glyphsets_per_script(script)))
        script_dict[script] = glyphsets_per_script(script)
    for i in range(max_glyphsets):
        row = []
        for script in scripts:
            if i < len(script_dict[script]):
                glyphset_name = script_dict[script][i]
                glyphset = GlyphSet.load(glyphset_name)
                abbr = glyphset_name.split("_")[-1]
                _new_md, warning = glyphset.get_description()
                warning_md = "✅"
                if warning:
                    warning_md = "🛑"
                row.append(f"[{warning_md} {abbr}](#{glyphset_name.lower().replace('_', '-')})")
            else:
                row.append("")
        md.append("| " + " | ".join(row) + " |")

    md.append(
        "\n> [!NOTE]  \n> This document is a human-readable representation of the glyphset defintions defined in `.yaml` files [here](/Lib/glyphsets/definitions/) and gets updated automatically as part of the `sh build.sh` command.\n"
    )
    md.append(
        "\n> [!NOTE]  \n> The symbols ✅ and 🛑 above denote whether or not this glyphset is available as part of Fontbakery's `shape_languages` check; in other words, whether or not language codes are defined for it.\n"
    )

    md.append("\n")

    # Content
    for glyphset_name in defined_glyphsets():
        glyphset = GlyphSet.load(glyphset_name)
        new_md, _warning = glyphset.get_description()
        md.append(new_md)

    with open(os.path.join(repo_root_folder, "GLYPHSETS.md"), "w") as f:
        f.write("\n".join(md))
