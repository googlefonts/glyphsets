import pytest
import subprocess
import os

DATA_FP = os.path.join(os.path.dirname(__file__), "data")
FONT_PATH = os.path.join(DATA_FP, "MavenPro[wght].ttf")


@pytest.mark.parametrize(
    "cmd",
    [
        ("glyphsets", "missing-in-font", FONT_PATH),
        ("glyphsets", "missing-in-font", "-t", "0.1", FONT_PATH),
    ],
)
def test_cli_missing_in_font(cmd):
    res = subprocess.call(cmd)
    assert res == 0
