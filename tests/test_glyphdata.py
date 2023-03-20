import pytest
from glyphsLib import GSFont, GSGlyph
from defcon import Font
from . import *


def glyphs_src1():
    font = GSFont()
    font.glyphs.append(GSGlyph("A"))
    return font


def ufo_src1():
    font = Font()
    font.newGlyph("A")
    return font


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (["GFLatinVietnamese"], ["0x0041 LATIN CAPITAL LETTER A"]),
        (
            ["GFLatinAfrican"],
            [
                "0x0041 LATIN CAPITAL LETTER A",
                "0x1E1F LATIN SMALL LETTER F WITH DOT ABOVE",
            ],
        ),
        (
            ["GFLatinVietnamese", "GFLatinAfrican"],
            [
                "0x0041 LATIN CAPITAL LETTER A",
                "0x1E1F LATIN SMALL LETTER F WITH DOT ABOVE",
            ],
        ),
        (["foobar"], []),
    ],
)
def test_build_name_file(glyph_data, test_input, expected):
    nam_data = glyph_data.build_nam_file(test_input)
    assert nam_data == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (["GFLatinVietnamese"], ["A", "brevecomb_acutecomb"]),
        (
            ["GFLatinVietnamese", "GFLatinAfrican"],
            ["A", "brevecomb_acutecomb", "fdotaccent"],
        ),
        (["foobar"], []),
    ],
)
def test_glyphsapp_filter_lists(glyph_data, test_input, expected):
    filter_list = glyph_data.build_glyphsapp_filter_list(test_input)
    assert filter_list == expected


@pytest.mark.parametrize(
    "src, test_input, expected",
    [
        (GSFont(), ["GFLatinVietnamese"], ["A", "brevecomb_acutecomb"]),
        (GSFont(), ["GFLatinCore"], ["A"]),
        (
            GSFont(),
            ["GFLatinVietnamese", "GFLatinAfrican"],
            ["A", "brevecomb_acutecomb", "fdotaccent"],
        ),
        (GSFont(), [], []),
        (Font(), ["GFLatinVietnamese"], ["A", "brevecomb_acutecomb"]),
        (Font(), ["GFLatinCore"], ["A"]),
        (
            Font(),
            ["GFLatinVietnamese", "GFLatinAfrican"],
            ["A", "brevecomb_acutecomb", "fdotaccent"],
        ),
        (Font(), [], []),
        # Repeat tests on sources which already contain a glyph
        (glyphs_src1(), ["GFLatinCore"], ["A"]),
        (ufo_src1(), ["GFLatinCore"], ["A"]),
    ],
)
def test_update_source_glyphset(glyph_data, src, test_input, expected):
    glyph_data.update_source_glyphset(src, test_input)

    if isinstance(src, GSFont):
        assert [g.name for g in src.glyphs] == expected
    elif isinstance(src, Font):
        # inserting new glyphs into a ufo are not ordered
        assert len(src) == len(expected)
        assert set(g.name for g in src) == set(expected)


def test_update_glyph_data(glyph_data):
    glyphs = [g["nice_name"] for g in glyph_data._data["glyphs"]]
    assert glyphs == ["A", "brevecomb_acutecomb", "fdotaccent"]

    # Add a new glyphset to an already existing glyph
    src1 = GSFont()
    src1.filepath = "NewGlyphSet.glyphs"
    src1.glyphs.append(GSGlyph("A"))
    glyph_data.update_db_from_sources([src1])
    assert "NewGlyphSet" in glyph_data["glyphs"][0]["glyphsets"]

    # Add duplicate glyphs
    glyph_data_size = len(glyph_data["glyphs"])
    src2 = GSFont()
    src2.filepath = "GFLatinCore.glyphs"
    src2.glyphs.append(GSGlyph("A"))
    src2.glyphs.append(GSGlyph("brevecomb_acutecomb"))
    src2.glyphs.append(GSGlyph("fdotaccent"))
    glyph_data.update_db_from_sources([src2])
    assert len(glyph_data["glyphs"]) == glyph_data_size

    # Add new glyphs
    src3 = GSFont()
    src3.filepath = "Greek.glyphs"
    src3.glyphs.append(GSGlyph("Alpha"))
    src3.glyphs.append(GSGlyph("Beta"))
    glyph_data.update_db_from_sources([src3])
    assert len(glyph_data["glyphs"]) == glyph_data_size + 2

    # TODO ufo sources


def test_glyphsets_missing_in_font(glyph_data, ttFont):
    # TODO use fonttools fontbuilder and make a font from scratch
    missing = glyph_data.missing_glyphsets_in_font(ttFont, threshold=0)
    assert missing == {
        "GFLatinAfrican": [
            {
                "nice_name": "fdotaccent",
                "production_name": "uni1E1F",
                "character": "ḟ",
                "unicode": 7711,
                "glyphsets": ["GFLatinAfrican"],
            }
        ]
    }
