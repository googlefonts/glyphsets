import json
import pytest
import re
from pathlib import Path
from glyphsLib import GSFont
from glyphsets import GFGlyphData, DATA_FP


GLYPHSETS = [
    str(gs.absolute()) for gs in Path("GF_glyphsets").glob("*/glyphs/*.glyphs")
]


@pytest.mark.parametrize(
    "glyphset",
    GLYPHSETS,
    ids=lambda gs: re.sub(r".*/(.*)\.glyphs", r"\1", gs)
)
def test_gfglyphdata_from_sources(tmpdir, glyphset):
    output_data_fp = tmpdir.join("data.json")
    glyphset = GSFont(glyphset)
    GFGlyphData.update_db_from_sources([glyphset, ])
    GFGlyphData.save(output_data_fp)

    output_data = json.load(open(output_data_fp, encoding="utf-8"))
    current_data = json.load(open(DATA_FP, encoding="utf-8"))
    output_glyphs = sorted(
        output_data.get("glyphs"),
        key=lambda d: d.get("nice_name")
    )
    current_glyphs = sorted(
        current_data.get("glyphs"),
        key=lambda d: d.get("nice_name")
    )
    assert (output_glyphs == current_glyphs)
