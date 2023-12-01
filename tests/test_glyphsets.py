from glyphsets.definitions import unicodes_per_glyphset


def test_definitions():
    assert len(unicodes_per_glyphset("GF_Latin_Core")) == 328
