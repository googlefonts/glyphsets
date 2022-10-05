from glyphsets.codepoints import (
    CodepointsInSubset,
    CodepointFileForSubset,
    ReadNameList,
    nam_dir,
)
from fontTools.unicodedata.Scripts import NAMES
import pytest
import unicodedata
from collections import defaultdict
import glob
import warnings
import os
import sys

try:
    import gflanguages
except Exception as e:
    pytest.skip(
        "Coverage test requires gflanguages to be installed",
        allow_module_level=True,
    )

MAGIC_CODEPOINTS = set([0x2010, 0xA])


def codepoints_and_optionally_ext(subset):
    cps_in_subset = CodepointsInSubset(subset, unique_glyphs=False)
    ext_file = os.path.join(nam_dir, "%s-ext_unique-glyphs.nam" % subset)
    if os.path.isfile(ext_file):
        cps_in_subset |= CodepointsInSubset(subset + "-ext")
    cps_in_subset |= MAGIC_CODEPOINTS
    return cps_in_subset


def test_coverage():
    langs = gflanguages.LoadLanguages()
    missing = defaultdict(set)
    bad_langs = defaultdict(list)
    failed = False
    for langname, metadata in langs.items():
        cps_used_in_sample = set()

        for _, sample in metadata.sample_text.ListFields():
            for cp in sample:
                cps_used_in_sample.add(ord(cp))

        lang, script = langname.split("_")
        # Get Unicode name for script
        if script not in NAMES:
            continue
        if NAMES[script] == "Hani":
            # Too generic, pass
            continue
        namefile = NAMES[script].lower().replace(" ", "-").replace("_", "-")
        cps_in_subset = codepoints_and_optionally_ext(namefile)
        if not cps_in_subset:
            warnings.warn(f"No codepoints for {langname}")
            failed = True
        cps_in_subset = set(cps_in_subset)
        cps_not_available = cps_used_in_sample - cps_in_subset
        if cps_not_available:
            failed = True
            missing[namefile] |= cps_not_available
            bad_langs[namefile].append(langname)

    if not failed:
        return

    for namefile, missing_cps in missing.items():

        print(
            f"\n{namefile} missing the following codepoints to render samples "
            f"in {', '.join(bad_langs[namefile])}:\n",
            file=sys.stderr,
        )
        for x in missing_cps:
            print(
                "0x%04X  %s %s" % (x, chr(x), unicodedata.name(chr(x))), file=sys.stderr
            )
    assert False, "Coverage test failed"
