from glyphsets.definitions import unicodes_per_glyphset, languages_per_glyphset


def test_definitions():
    assert len(unicodes_per_glyphset("GF_Latin_Core")) == 319

    assert len(languages_per_glyphset("GF_Arabic_Plus")) == 5
    assert len(languages_per_glyphset("GF_Latin_African")) == 603
