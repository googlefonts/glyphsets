"""
Assemble .nam files from .nam stub files and language definitions.
"""

import sys
import os
import shutil
import gflanguages
import unicodedata
import plistlib

# Insert local module path at beginning of sys.path
# so that up-to-date version of glyphsets package is used
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "Lib"))
from glyphsets import extended_glyphsets, GlyphSet  # noqa: E402


def add_to_plist_file(plist_path, glyphset_name, final_glyphnames):
    os.makedirs(os.path.dirname(plist_path), exist_ok=True)
    if os.path.exists(plist_path):
        with open(plist_path, "rb") as f:
            plist = plistlib.load(f)
    else:
        plist = []
    plist.append({"name": glyphset_name, "list": final_glyphnames})
    with open(plist_path, "wb") as f:
        plistlib.dump(plist, f)


def assemble_characterset(root_folder, glyphset_name):

    glyphset = GlyphSet.load(glyphset_name)

    nam_path = os.path.join(root_folder, "results", "nam", f"{glyphset_name}.nam")
    nam_in_package_path = os.path.abspath(
        os.path.join(
            root_folder,
            "..",
            "Lib",
            "glyphsets",
            "results",
            "nam",
            f"{glyphset_name}.nam",
        )
    )
    txt_in_package_path = os.path.abspath(
        os.path.join(
            root_folder,
            "..",
            "Lib",
            "glyphsets",
            "results",
            "txt",
            "nice-names",
            f"{glyphset_name}.txt",
        )
    )
    glyphs_path = os.path.join(root_folder, "results", "glyphs", f"{glyphset_name}.glyphs")
    txt_nicenames_path = os.path.join(root_folder, "results", "txt", "nice-names", f"{glyphset_name}.txt")
    txt_prodnames_path = os.path.join(root_folder, "results", "txt", "prod-names", f"{glyphset_name}.txt")
    plist_path = os.path.join(root_folder, "results", "plist", f"CustomFilter_GF_{glyphset.script}.plist")
    plist_all_path = os.path.join(root_folder, "results", "plist", "CustomFilter_GF_All.plist")

    final_glyphnames = glyphset.get_final_glyphnames()

    if not glyphset.modifier:

        font = glyphset.get_final_glyphs_font()

        # Save glyphs file
        os.makedirs(os.path.dirname(glyphs_path), exist_ok=True)
        font.save(glyphs_path)

        # Just make sure there are no duplicates
        duplicates = [
            glyph.name for glyph in font.glyphs if [glyph.name for glyph in font.glyphs].count(glyph.name) > 1
        ]
        assert duplicates == [], f"Duplicate glyph names in {glyphset_name}: {duplicates}"

        # Output sorted character set to .nam file
        os.makedirs(os.path.dirname(nam_path), exist_ok=True)
        os.makedirs(os.path.dirname(nam_in_package_path), exist_ok=True)
        with open(nam_path, "w") as f:
            f.write("# This file is auto-generated; do not edit. See /README.md for instructions.\n")
            for i, unicode in enumerate(glyphset.get_final_unicodes()):
                # unicode_string = f"{unicode:#0{6}X}".replace("0X", "0x")
                unicode_string = f"0x{unicode}"
                try:
                    unicode_name = unicodedata.name(chr(int(unicode, 16)))
                except ValueError:
                    unicode_name = ""
                f.write(f"{unicode_string} # {unicode_name}")
                if i < len(glyphset.get_final_unicodes()) - 1:
                    f.write("\n")
        shutil.copyfile(nam_path, nam_in_package_path)

        # Output txt files
        os.makedirs(os.path.dirname(txt_nicenames_path), exist_ok=True)
        with open(txt_nicenames_path, "w") as f:
            f.write("# This file is auto-generated; do not edit. See /README.md for instructions.\n")
            f.write("\n".join(final_glyphnames))
        os.makedirs(os.path.dirname(txt_prodnames_path), exist_ok=True)
        with open(txt_prodnames_path, "w") as f:
            f.write("# This file is auto-generated; do not edit. See /README.md for instructions.\n")
            f.write("\n".join(glyphset.get_final_productionglyphnames()))
        os.makedirs(os.path.dirname(txt_in_package_path), exist_ok=True)
        shutil.copyfile(txt_nicenames_path, txt_in_package_path)

    add_to_plist_file(plist_path, glyphset.complete_name(), final_glyphnames)
    add_to_plist_file(plist_all_path, glyphset.complete_name(), final_glyphnames)


if __name__ == "__main__":
    # Check for gflanguages version
    installed = None
    latest = None
    for line in os.popen("pip index versions gflanguages").read().split("\n"):
        if "INSTALLED" in line:
            installed = line.split(" ")[-1].strip()
        if "LATEST" in line:
            latest = line.split(" ")[-1].strip()
    print(
        f"""
*************************************************************
*
*   WARNING:
*   Make sure you're using the correct version of gflanguages,
*   otherwise the glyphsets will be incorrect.
*
*   You have: {installed}
*   Location: {gflanguages.__file__}
*
*************************************************************
"""
    )

    root_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))

    # Delete all plists so that they can be regenerated in order in case os added glyphsets
    plist_folder = os.path.join(root_folder, "results", "plist")
    for file in os.listdir(plist_folder):
        if file.endswith(".plist"):
            os.remove(os.path.join(plist_folder, file))

    for glyphset_name in extended_glyphsets():

        print(f"Assembling '{glyphset_name}'...")
        assemble_characterset(root_folder, glyphset_name)
