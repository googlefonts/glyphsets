import pytest
from . import *


def test_test_strings_in_font(test_string_data, ttFont):
    res = test_string_data.test_strings_in_font(ttFont)
    assert "GFLatinKernel" in res

    # Drop threshold so we pick up GFLatinAfrican
    res = test_string_data.test_strings_in_font(ttFont, 0.4)
    assert "GFLatinAfrican" in res
