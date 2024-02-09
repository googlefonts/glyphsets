from glyphsets import unicodes_per_glyphset, languages_per_glyphset
from glyphsets.definitions import glyphset_definitions


def test_definitions():
    assert len(unicodes_per_glyphset("GF_Latin_Core")) == 319

    assert len(languages_per_glyphset("GF_Arabic_Plus")) == 5
    assert len(languages_per_glyphset("GF_Latin_African")) == 603

    # accidental double definitions
    for code in glyphset_definitions:
        assert len(languages_per_glyphset(code)) == len(
            set(languages_per_glyphset(code))
        )
