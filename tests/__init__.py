from glyphsets import _GFGlyphData
from fontTools.ttLib import TTFont
import os
import pytest

DATA_FP = os.path.join(os.path.dirname(__file__), "data")


@pytest.fixture
def glyph_data():
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
