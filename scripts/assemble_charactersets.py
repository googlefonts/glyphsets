"""
Assemble .nam files from .nam stub files and language definitions.
"""

import sys
import os
import shutil
import gflanguages
import unicodedata
import glyphsLib
import functools
import plistlib
from glyphsLib.glyphdata import get_glyph, _lookup_attributes_by_unicode

# Insert local module path at beginning of sys.path
# so that up-to-date version of glyphsets package is used
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "Lib"))
from glyphsets.definitions import glyphset_definitions  # noqa: E402
from glyphsets.definitions import unicodes_per_glyphset  # noqa: E402


def sort_unicodes(a, b):
    if a.unicode and b.unicode:
        return int(a.unicode, 16) - int(b.unicode, 16)
    elif a.unicode:
        return -1
    elif b.unicode:
        return 1
    else:
        return 0


def sort_by_category(a, b):
    info_a = get_glyph(a.name)
    info_b = get_glyph(b.name)

    value = sorted([info_a.category, info_b.category]).index(info_a.category)
    if value == 0:
        value = -1
    value *= -1

    return value


def assemble_characterset(root_folder, glyphset_name):
    script = glyphset_definitions[glyphset_name]["script"]
    language_codes = glyphset_definitions[glyphset_name]["language_codes"]

    nam_stub_path = os.path.join(
        root_folder, script, "definitions", f"{glyphset_name}.stub.nam"
    )
    nam_path = os.path.join(root_folder, script, "nam", f"{glyphset_name}.nam")
    nam_in_package_path = os.path.abspath(
        os.path.join(
            root_folder,
            "..",
            "Lib",
            "glyphsets",
            "definitions",
            "nam",
            f"{glyphset_name}.nam",
        )
    )
    glyphs_stub_path = os.path.join(
        root_folder, script, "definitions", f"{glyphset_name}.stub.glyphs"
    )
    glyphs_path = os.path.join(root_folder, script, "glyphs", f"{glyphset_name}.glyphs")
    glyphs_empty_path = os.path.join(root_folder, f"empty_font.glyphs")
    txt_nicenames_path = os.path.join(
        root_folder, script, "txt", "nice-names", f"{glyphset_name}.txt"
    )
    txt_prodnames_path = os.path.join(
        root_folder, script, "txt", "prod-names", f"{glyphset_name}.txt"
    )
    plist_path = os.path.join(
        root_folder, script, "glyphs", f"CustomFilter_GF_{script}.plist"
    )

    character_set = set()

    # Assemble character sets from gflanguages
    languages = gflanguages.LoadLanguages()
    for language_code in language_codes:
        chars = languages[language_code].exemplar_chars
        # chars.base.upper() is important because many Latin languages don't
        # contain a complete set of uppercase letters in "index"
        character_set.update(
            {
                ord(c)
                for c in list(
                    set(chars.base)
                    | set(chars.base.upper())
                    | set(chars.index)
                    | set(chars.marks)
                    | set(chars.numerals)
                    | set(chars.punctuation)
                    # | set(chars.auxiliary) # Not to be part of charsets
                )
                if c not in (" ", "{", "}", "◌")
            }
        )

    # Read .stub.nam file
    if os.path.exists(nam_stub_path):
        with open(nam_stub_path, "r") as f:
            nam_stub_lines = f.readlines()
        for line in nam_stub_lines:
            unicode = line.split(" ")[0]
            if unicode.startswith("0x"):
                character_set.add(int(unicode[2:], 16))

    # Call get_glyph once so that GLYPHDATA gets filled in glyphsLib
    get_glyph("A")
    # If I import GLYPHDATA at the top of the file, it doesn't get filled
    from glyphsLib.glyphdata import GLYPHDATA

    assert type(GLYPHDATA) is glyphsLib.glyphdata.GlyphData

    # Create glyphs file and add characters
    if os.path.exists(glyphs_stub_path):
        font = glyphsLib.load(glyphs_stub_path)
    else:
        font = glyphsLib.load(glyphs_empty_path)
        font.familyName = glyphset_name
    for _i, unicode in enumerate(sorted(list(character_set))):
        unicode = f"{unicode:#0{6}X}".replace("0X", "")
        glyph_info = _lookup_attributes_by_unicode(unicode, GLYPHDATA)
        glyph = glyphsLib.GSGlyph(glyph_info["name"])
        glyph.unicode = unicode
        font.glyphs.append(glyph)

    # Sort
    font.glyphs = sorted(font.glyphs, key=functools.cmp_to_key(sort_by_category))
    unicode_sorted_glyphs = sorted(font.glyphs, key=functools.cmp_to_key(sort_unicodes))
    glyph_names = [glyph.name for glyph in unicode_sorted_glyphs]
    production_glyph_names = [
        get_glyph(glyph.name).production_name for glyph in unicode_sorted_glyphs
    ]

    # Save glyphs file
    font.save(glyphs_path)

    # Output sorted character set to .nam file
    with open(nam_path, "w") as f:
        f.write(
            "# This file is auto-generated; do not edit. See /README.md for instructions.\n"
        )
        for i, unicode in enumerate(sorted(list(character_set))):
            unicode_string = f"{unicode:#0{6}X}".replace("0X", "0x")
            f.write(f"{unicode_string} {unicodedata.name(chr(unicode))}")
            if i < len(character_set) - 1:
                f.write("\n")
    shutil.copyfile(nam_path, nam_in_package_path)

    # Output txt files
    with open(txt_nicenames_path, "w") as f:
        f.write(
            "# This file is auto-generated; do not edit. See /README.md for instructions.\n"
        )
        f.write("\n".join(glyph_names))
    with open(txt_prodnames_path, "w") as f:
        f.write(
            "# This file is auto-generated; do not edit. See /README.md for instructions.\n"
        )
        f.write("\n".join(production_glyph_names))

    # Adjust .plist
    with open(plist_path, "rb") as f:
        plist = plistlib.load(f)
    for plist_glyphset in plist:
        if plist_glyphset["name"] == glyphset_name:
            plist_glyphset["list"] = glyph_names
    with open(plist_path, "wb") as f:
        plistlib.dump(plist, f)


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

    root_folder = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "GF_Glyphsets")
    )

    for glyphset_name in glyphset_definitions:
        print(f"Assembling '{glyphset_name}'...")
        assemble_characterset(root_folder, glyphset_name)
        # Proof of work:
        assert unicodes_per_glyphset(glyphset_name) != []
