import os
from glyphsets import (
    unicodes_per_glyphset,
    get_glyphsets_fulfilled,
    defined_glyphsets,
    compare_glyphsets,
    build_glyphsapp_filter_list,
    glyphs_in_glyphset,
    GlyphSet,
    analyze_font,
    find_character,
    languages_per_glyphset,
)
import plistlib

import glyphsets

print(glyphsets)

DATA_FP = os.path.join(os.path.dirname(__file__), "data")
FONT_PATH = os.path.join(DATA_FP, "MavenPro[wght].ttf")


def test_definitions():
    assert len(unicodes_per_glyphset("GF_Latin_Core")) == 319

    assert len(languages_per_glyphset("GF_Arabic_Plus")) >= 8
    assert len(languages_per_glyphset("GF_Latin_African")) >= 617

    # accidental double definitions
    for code in defined_glyphsets():
        assert len(GlyphSet.load(code).get_language_codes()) == len(set(GlyphSet.load(code).get_language_codes()))
    assert len(defined_glyphsets()) == len(set(defined_glyphsets()))

    assert "GF_Latin_Core" in defined_glyphsets()


# def test_order():
#     """Assert that the order of the glyphsets is consistent"""
#     for glyphset_name in extended_glyphsets():
#         print(f"Testing {glyphset_name}")
#         assert id(GlyphSet.load(glyphset_name)) == id(GlyphSet.load(glyphset_name))
#         assert id(GlyphSet.load(glyphset_name, reload=True)) != id(GlyphSet.load(glyphset_name, reload=True))

#         assert GlyphSet.load(glyphset_name, reload=True).get_final_glyphnames(exclusive=False) == GlyphSet.load(
#             glyphset_name, reload=True
#         ).get_final_glyphnames(exclusive=False)
#         assert GlyphSet.load(glyphset_name, reload=True).get_final_glyphnames(exclusive=True) == GlyphSet.load(
#             glyphset_name, reload=True
#         ).get_final_glyphnames(exclusive=True)


def test_coverage():
    from fontTools.ttLib import TTFont

    ttFont = TTFont(FONT_PATH)
    assert get_glyphsets_fulfilled(ttFont)["GF_Latin_Core"]["percentage"] > 0.99
    assert get_glyphsets_fulfilled(ttFont)["GF_Latin_Kernel"]["percentage"] == 1
    assert get_glyphsets_fulfilled(ttFont)["GF_Latin_Vietnamese"]["percentage"] == 1
    analyze_font(ttFont)


def test_compare():
    compare_glyphsets(["GF_Latin_Kernel", "GF_Latin_Core", "GF_Latin_Plus"])
    compare_glyphsets(["GF_Cyrillic_Core", "GF_Cyrillic_Plus", "GF_Cyrillic_Pro"])


def test_filter_lists():
    build_glyphsapp_filter_list(["GF_Latin_Kernel", "GF_Latin_Core", "GF_Latin_Plus"], "test.plist", False)
    assert os.path.exists("CustomFiltertest.plist")
    test = plistlib.load(open("CustomFiltertest.plist", "rb"))
    assert len(test) == 3
    assert test[0]["name"] == "GF_Latin_Core"
    assert test[1]["name"] == "GF_Latin_Kernel"
    assert test[2]["name"] == "GF_Latin_Plus"
    assert test[0]["list"] == glyphs_in_glyphset("GF_Latin_Core")
    assert test[1]["list"] == glyphs_in_glyphset("GF_Latin_Kernel")
    assert test[2]["list"] == glyphs_in_glyphset("GF_Latin_Plus")
    os.remove("CustomFiltertest.plist")


def test_find():
    find_character("ß")
    find_character("0x00DF")
