import os
from glyphsets import (
    unicodes_per_glyphset,
    languages_per_glyphset,
    get_glyphsets_fulfilled,
    defined_glyphsets,
    compare_glyphsets,
    build_glyphsapp_filter_list,
    glyphs_in_glyphset,
)
import plistlib

DATA_FP = os.path.join(os.path.dirname(__file__), "data")
FONT_PATH = os.path.join(DATA_FP, "MavenPro[wght].ttf")


def test_definitions():
    assert len(unicodes_per_glyphset("GF_Latin_Core")) == 319

    assert len(languages_per_glyphset("GF_Arabic_Plus")) == 5
    assert len(languages_per_glyphset("GF_Latin_African")) == 601

    # accidental double definitions
    for code in defined_glyphsets():
        assert len(languages_per_glyphset(code)) == len(set(languages_per_glyphset(code)))
    assert len(defined_glyphsets()) == len(set(defined_glyphsets()))

    assert "GF_Latin_Core" in defined_glyphsets()


def test_coverage():
    from fontTools.ttLib import TTFont

    ttFont = TTFont(FONT_PATH)
    assert get_glyphsets_fulfilled(ttFont)["GF_Latin_Core"]["percentage"] > 0.99


def test_compare():
    compare_glyphsets(["GF_Latin_Kernel", "GF_Latin_Core", "GF_Latin_Plus"])


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
