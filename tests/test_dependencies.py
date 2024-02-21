import subprocess
import os
import re
import requests
import json

SETUP_PY = os.path.join(os.path.dirname(__file__), "..", "setup.py")
with open(SETUP_PY, "r") as f:
    setup_py = f.read()


def get_setup_py_version(package_name):
    version = re.findall(
        rf"{package_name}(>=|~=|==)([0-9]+\.[0-9]+\.[0-9]+)",
        setup_py,
    )
    return version[0][1]


def get_latest_version(package_name):
    return json.loads(requests.get(f"https://pypi.org/pypi/{package_name}/json").text)[
        "info"
    ]["version"]


def check_version(package_name):
    setup_py_version = get_setup_py_version(package_name)
    latest_version = get_latest_version(package_name)
    assert (
        setup_py_version == latest_version
    ), f"{package_name} version in setup.py is not the latest version on PyPI ({latest_version})"


# def test_dependencies():
#     check_version("gflanguages")


if __name__ == "__main__":
    test_dependencies()
