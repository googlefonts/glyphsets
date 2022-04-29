import pytest
from fontTools.ttLib import TTFont
from glyphsets import _GFGlyphData
from glyphsLib import GSFont, GSGlyph
from defcon import Font
import os

DATA_FP = os.path.join(os.path.dirname(__file__), "data")


@pytest.fixture
def db():
    data = {
        "glyphs": [
            {
                "nice_name": "A",
                "production_name": "A",
                "character": "A",
                "unicode": 65,
                "glyphsets": [
                    "GFLatinIPA",
                    "GFLatinAfrican",
                    "GFLatinCore",
                    "GFLatinKernel",
                    "GFLatinMinorities",
                    "GFLatinPlus",
                    "GFLatinVietnamese",
                ],
            },
            {
                "nice_name": "brevecomb_acutecomb",
                "production_name": "uni03060301",
                "character": None,
                "unicode": None,
                "glyphsets": ["GFLatinVietnamese"],
            },
            {
                "nice_name": "fdotaccent",
                "production_name": "uni1E1F",
                "character": "\u1e1f",
                "unicode": 7711,
                "glyphsets": ["GFLatinAfrican"],
            },
        ]
    }
    return _GFGlyphData(data)


@pytest.fixture
def ttFont():
    fp = os.path.join(DATA_FP, "MavenPro[wght].ttf")
    return TTFont(fp)


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
def test_build_name_file(db, test_input, expected):
    nam_data = db.build_nam_file(test_input)
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
def test_glyphsapp_filter_lists(db, test_input, expected):
    filter_list = db.build_glyphsapp_filter_list(test_input)
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
def test_update_source_glyphset(db, src, test_input, expected):
    db.update_source_glyphset(src, test_input)

    if isinstance(src, GSFont):
        assert [g.name for g in src.glyphs] == expected
    elif isinstance(src, Font):
        # inserting new glyphs into a ufo are not ordered
        assert len(src) == len(expected)
        assert set(g.name for g in src) == set(expected)


def test_update_db(db):
    glyphs = [g["nice_name"] for g in db._data["glyphs"]]
    assert glyphs == ["A", "brevecomb_acutecomb", "fdotaccent"]

    # Add a new glyphset to an already existing glyph
    src1 = GSFont()
    src1.filepath = "NewGlyphSet.glyphs"
    src1.glyphs.append(GSGlyph("A"))
    db.update_db_from_sources([src1])
    assert "NewGlyphSet" in db["glyphs"][0]["glyphsets"]

    # Add duplicate glyphs
    db_size = len(db["glyphs"])
    src2 = GSFont()
    src2.filepath = "GFLatinCore.glyphs"
    src2.glyphs.append(GSGlyph("A"))
    src2.glyphs.append(GSGlyph("brevecomb_acutecomb"))
    src2.glyphs.append(GSGlyph("fdotaccent"))
    db.update_db_from_sources([src2])
    assert len(db["glyphs"]) == db_size

    # Add new glyphs
    src3 = GSFont()
    src3.filepath = "Greek.glyphs"
    src3.glyphs.append(GSGlyph("Alpha"))
    src3.glyphs.append(GSGlyph("Beta"))
    db.update_db_from_sources([src3])
    assert len(db["glyphs"]) == db_size + 2

    # TODO ufo sources


def test_glyphsets_missing_in_font(db, ttFont):
    # TODO use fonttools fontbuilder and make a font from scratch
    missing = db.missing_glyphsets_in_font(ttFont, threshold=0)
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
