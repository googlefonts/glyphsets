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
from fontTools.unicodedata.Scripts import NAMES as SCRIPT_NAMES

# Insert local module path at beginning of sys.path
# so that up-to-date version of glyphsets package is used
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "Lib"))
from glyphsets import (
    get_script,
    defined_glyphsets,
    get_glyphset_definition,
    unicodes_per_glyphset,
    languages_per_glyphset,
    read_nam_file,
)  # noqa: E402


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

    if info_a.category is None:
        return -1
    elif info_b.category is None:
        return 1

    value = sorted([info_a.category, info_b.category]).index(info_a.category)
    if value == 0:
        value = -1
    value *= -1

    return value


def assemble_characterset(root_folder, glyphset_name):

    script = get_script(glyphset_name)
    glyphset_definition = get_glyphset_definition(glyphset_name)
    language_codes = languages_per_glyphset(glyphset_name)
    use_aux = glyphset_definition.get("use_auxiliary", False)

    nam_stub_path = os.path.join(
        root_folder, "definitions", "per_glyphset", f"{glyphset_name}.stub.nam"
    )
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
    glyphs_stub_path = os.path.join(
        root_folder, "definitions", "per_glyphset", f"{glyphset_name}.stub.glyphs"
    )
    glyphs_path = os.path.join(
        root_folder, "results", "glyphs", f"{glyphset_name}.glyphs"
    )
    glyphs_empty_path = os.path.join(root_folder, f"empty_font.glyphs")
    txt_nicenames_path = os.path.join(
        root_folder, "results", "txt", "nice-names", f"{glyphset_name}.txt"
    )
    txt_prodnames_path = os.path.join(
        root_folder, "results", "txt", "prod-names", f"{glyphset_name}.txt"
    )
    plist_path = os.path.join(
        root_folder, "results", "plist", f"CustomFilter_GF_{script}.plist"
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
                    | (set(chars.auxiliary) if use_aux else set())
                )
                if c not in (" ", "{", "}", "◌")
            }
        )

    # Call get_glyph once so that GLYPHDATA gets filled in glyphsLib
    get_glyph("A")
    # If I import GLYPHDATA at the top of the file, it doesn't get filled
    from glyphsLib.glyphdata import GLYPHDATA

    assert type(GLYPHDATA) is glyphsLib.glyphdata.GlyphData

    def _font_has_unicode(font, unicode):
        for glyph in font.glyphs:
            if glyph.unicode:
                if int(glyph.unicode, 16) == unicode:
                    return True

    # Create or open glyphs file and add characters
    if os.path.exists(glyphs_stub_path):
        font = glyphsLib.load(glyphs_stub_path)
        for glyph in font.glyphs:
            if glyph.unicodes:
                for unicode in glyph.unicodes:
                    character_set.update({int(unicode, 16)})
    else:
        font = glyphsLib.load(glyphs_empty_path)

    font.familyName = glyphset_name

    # Add language-specific glyphs
    for language_code in language_codes:
        per_language_glyphs_stub_path = os.path.join(
            root_folder, "definitions", "per_language", f"{language_code}.stub.glyphs"
        )
        if os.path.exists(per_language_glyphs_stub_path):
            per_language_font = glyphsLib.load(per_language_glyphs_stub_path)

            for glyph in per_language_font.glyphs:

                # Add encoded characters to character_set
                if glyph.unicodes:
                    for unicode in glyph.unicodes:
                        character_set.update({int(unicode, 16)})

                # Add unencoded glyphs to .glyphs file
                else:
                    new_glyph = glyphsLib.GSGlyph(glyph.name)
                    font.glyphs.append(new_glyph)

    # Add encoded characters to .glyphs file
    for _i, unicode in enumerate(sorted(list(character_set))):
        if not _font_has_unicode(font, unicode):
            unicode = f"{unicode:#0{6}X}".replace("0X", "")
            glyph_info = _lookup_attributes_by_unicode(unicode, GLYPHDATA)
            if "name" in glyph_info:
                new_glyph = glyphsLib.GSGlyph(glyph_info["name"])
            else:
                new_glyph = glyphsLib.GSGlyph(f"uni{unicode}")
            new_glyph.unicode = unicode
            font.glyphs.append(new_glyph)

    # Sort
    font.glyphs = sorted(font.glyphs, key=functools.cmp_to_key(sort_by_category))
    unicode_sorted_glyphs = sorted(font.glyphs, key=functools.cmp_to_key(sort_unicodes))
    glyph_names = [glyph.name for glyph in unicode_sorted_glyphs]
    production_glyph_names = [
        get_glyph(glyph.name).production_name for glyph in unicode_sorted_glyphs
    ]

    # Save glyphs file
    os.makedirs(os.path.dirname(glyphs_path), exist_ok=True)
    font.save(glyphs_path)

    # Output sorted character set to .nam file
    os.makedirs(os.path.dirname(nam_path), exist_ok=True)
    os.makedirs(os.path.dirname(nam_in_package_path), exist_ok=True)
    with open(nam_path, "w") as f:
        f.write(
            "# This file is auto-generated; do not edit. See /README.md for instructions.\n"
        )
        for i, unicode in enumerate(sorted(list(character_set))):
            unicode_string = f"{unicode:#0{6}X}".replace("0X", "0x")
            try:
                unicode_name = unicodedata.name(chr(unicode))
            except ValueError:
                unicode_name = ""
            f.write(f"{unicode_string} {unicode_name}")
            if i < len(character_set) - 1:
                f.write("\n")
    shutil.copyfile(nam_path, nam_in_package_path)

    # Output txt files
    os.makedirs(os.path.dirname(txt_nicenames_path), exist_ok=True)
    with open(txt_nicenames_path, "w") as f:
        f.write(
            "# This file is auto-generated; do not edit. See /README.md for instructions.\n"
        )
        f.write("\n".join(glyph_names))
    os.makedirs(os.path.dirname(txt_prodnames_path), exist_ok=True)
    with open(txt_prodnames_path, "w") as f:
        f.write(
            "# This file is auto-generated; do not edit. See /README.md for instructions.\n"
        )
        f.write("\n".join(production_glyph_names))

    # Adjust .plist
    os.makedirs(os.path.dirname(plist_path), exist_ok=True)
    if os.path.exists(plist_path):
        with open(plist_path, "rb") as f:
            plist = plistlib.load(f)
    else:
        plist = []
    found_list = False
    for plist_glyphset in plist:
        if "name" in plist_glyphset and plist_glyphset["name"] == glyphset_name:
            plist_glyphset["list"] = glyph_names
            found_list = True
    if not found_list:
        plist.append({"name": glyphset_name, "list": glyph_names})
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

    root_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))

    for glyphset_name in defined_glyphsets():
        print(f"Assembling '{glyphset_name}'...")
        assemble_characterset(root_folder, glyphset_name)
        # Proof of work:
        # assert unicodes_per_glyphset(glyphset_name) != []
