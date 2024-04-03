import os
from glyphsets import (
    unicodes_per_glyphset,
    languages_per_glyphset,
    get_glyphsets_fulfilled,
    defined_glyphsets,
)

DATA_FP = os.path.join(os.path.dirname(__file__), "data")
FONT_PATH = os.path.join(DATA_FP, "MavenPro[wght].ttf")


def test_definitions():
    assert len(unicodes_per_glyphset("GF_Latin_Core")) == 319

    assert len(languages_per_glyphset("GF_Arabic_Plus")) == 5
    assert len(languages_per_glyphset("GF_Latin_African")) == 598

    # accidental double definitions
    for code in defined_glyphsets():
        assert len(languages_per_glyphset(code)) == len(
            set(languages_per_glyphset(code))
        )
    assert len(defined_glyphsets()) == len(set(defined_glyphsets()))

    assert "GF_Latin_Core" in defined_glyphsets()


def test_coverage():
    from fontTools.ttLib import TTFont

    ttFont = TTFont(FONT_PATH)
    assert get_glyphsets_fulfilled(ttFont)["GF_Latin_Core"]["percentage"] > 0.99
