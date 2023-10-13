"""
Assemble .nam files from .nam stub files and language definitions.
"""

global GLYPHDATA

import yaml
import os
import gflanguages
import unicodedata
import glyphsLib
import functools
from glyphsLib.glyphdata import get_glyph, _lookup_attributes_by_unicode

def assemble_characterset(languages_yaml_path):

    glyphset_name = os.path.basename(languages_yaml_path).replace(".yaml", "")
    nam_stub_path = languages_yaml_path.replace(".yaml", ".stub.nam")
    nam_path = languages_yaml_path.replace(".yaml", ".nam").replace("definitions", "nam")
    glyphs_stub_path = languages_yaml_path.replace(".yaml", ".stub.glyphs")
    glyphs_path = languages_yaml_path.replace(".yaml", ".glyphs").replace("definitions", "glyphs")
    txt_nicenames_path = languages_yaml_path.replace(".yaml", ".txt").replace("definitions", "txt/nice-names")
    txt_prodnames_path = languages_yaml_path.replace(".yaml", ".txt").replace("definitions", "txt/prod-names")

    character_set = set()

    # Read language definitions
    with open(languages_yaml_path, "r") as stream:
        language_definitions = yaml.safe_load(stream)

    # Assemble character sets from gflanguages
    languages = gflanguages.LoadLanguages()
    for language_code in language_definitions["language_codes"]:
        chars = languages[language_code].exemplar_chars
        character_set.update(
            {
                ord(c)
                for c in list(
                    set(chars.base)
                    | set(
                        chars.base.upper()
                    )  # This is important because many Latin languages don't contain a complete set of uppercase letters in "index"
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
    assert type(GLYPHDATA) == glyphsLib.glyphdata.GlyphData

    # Create glyphs file and add characters
    if os.path.exists(glyphs_stub_path):
        font = glyphsLib.load(glyphs_stub_path)
    else:
        font = glyphsLib.GSFont()
        font.familyName = glyphset_name
    for i, unicode in enumerate(sorted(list(character_set))):
        unicode = f"{unicode:#0{6}X}".replace("0X", "")
        glyph_info = _lookup_attributes_by_unicode(unicode, GLYPHDATA)
        glyph = glyphsLib.GSGlyph()
        glyph.name = glyph_info["name"]
        glyph.unicode = unicode
        font.glyphs.append(glyph)

    # Save glyphs file
    font.axes = []
    font.save(glyphs_path)

    # Output sorted character set to .nam file
    with open(nam_path, "w") as f:
        for i, unicode in enumerate(sorted(list(character_set))):
            unicode_string = f"{unicode:#0{6}X}".replace("0X", "0x")
            f.write(f"{unicode_string} {unicodedata.name(chr(unicode))}")
            if i < len(character_set) - 1:
                f.write("\n")

    def sort_unicodes(a, b):
        if a.unicode and b.unicode:
            return int(a.unicode, 16) - int(b.unicode, 16)
        elif a.unicode:
            return -1
        elif b.unicode:
            return 1
        else:
            return 0

    # Output txt files
    with open(txt_nicenames_path, "w") as f:
        glyphs = sorted(font.glyphs, key=functools.cmp_to_key(sort_unicodes))
        f.write("\n".join([glyph.name for glyph in glyphs]))
    with open(txt_prodnames_path, "w") as f:
        glyphs = sorted(font.glyphs, key=functools.cmp_to_key(sort_unicodes))
        f.write("\n".join([get_glyph(glyph.name).production_name for glyph in glyphs]))


if __name__ == "__main__":
    for root, dir, files in os.walk(
        os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "GF_Glyphsets"))
    ):
        for file in files:
            if file.endswith(".yaml"):

                # Find definition file
                languages_yaml_path = os.path.abspath(
                    os.path.join(
                        root, "..", "definitions", file)
                    )

                assemble_characterset(languages_yaml_path)
