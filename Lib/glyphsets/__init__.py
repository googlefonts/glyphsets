"""
GF Glyph Database
"""
import plistlib
import json
import os
from re import L
from glyphsLib import GSFont, GSGlyph
from defcon import Font
import logging
import unicodedata2 as uni
from glyphsLib.glyphdata import get_glyph
from copy import deepcopy as copy

try:
    from ._version import version as __version__  # type: ignore
except ImportError:
    __version__ = "0.0.0+unknown"


DATA_FP = os.path.join(os.path.dirname(__file__), "data.json")
TEST_STRINGS_DATA = os.path.join(os.path.dirname(__file__), "test_strings.json")
log = logging.getLogger(__file__)


class _GFGlyphData:
    def __init__(self, data=json.load(open(DATA_FP, encoding="utf8"))):
        self._data = copy(data)
        self._in_use = set(g["nice_name"] for g in self._data["glyphs"])

    def save(self, fp=DATA_FP):
        with open(fp, "w") as db:
            json.dump(self._data, db, indent=2)

    @classmethod
    def from_json(cls, fp):
        with open(fp) as db:
            data = json.load(db)
            return cls(data)

    def __getitem__(self, k):
        return self._data[k]

    def glyphsets_in_font(self, ttFont):
        glyphs_in_font = set(ttFont.getGlyphOrder())
        unicodes_in_font = set(ttFont.getBestCmap().keys())
        res = {}
        for g in self["glyphs"]:
            for glyphset in g["glyphsets"]:
                if glyphset not in res:
                    res[glyphset] = {"has": [], "missing": []}
                if any(
                    [
                        g["nice_name"] in glyphs_in_font,
                        g["production_name"] in glyphs_in_font,
                        g["unicode"] in unicodes_in_font,
                    ]
                ):
                    res[glyphset]["has"].append(g)
                else:
                    res[glyphset]["missing"].append(g)
        return res

    def glyphsets_fulfilled(self, ttFont):
        res = self.glyphsets_in_font(ttFont)
        return {
            k: len(v["has"]) / (len(v["has"]) + len(v["missing"]))
            for k, v in res.items()
        }

    def missing_glyphsets_in_font(self, ttFont, threshold=0.8):
        res = self.glyphsets_in_font(ttFont)
        fulfilled = {
            k: len(v["has"]) / (len(v["has"]) + len(v["missing"]))
            for k, v in res.items()
        }
        missing = {}
        for k, v in fulfilled.items():
            if v == 1.0 or v < threshold:
                continue
            missing[k] = res[k]["missing"]
        return missing

    def glyphs_in_glyphsets(self, glyphsets):
        res = []
        seen = set()
        for g in self["glyphs"]:
            for glyphset in g["glyphsets"]:
                if glyphset not in glyphsets or g["nice_name"] in seen:
                    continue
                res.append(g)
                seen.add(g["nice_name"])
        return res

    def update_db_from_sources(self, sources):
        """Update the database by using the glyphsets from source files.

        Please note that you may need to edit some data by hand"""
        for src in sources:
            if isinstance(src, GSFont):
                glyphset = os.path.basename(src.filepath).split(".")[0]
                for g in src.glyphs:
                    if not g.export:
                        continue
                    self.add_glyph(glyphset, g.name, unicodes=g.unicode)
            elif isinstance(src, Font):
                glyphset = os.path.basename(src.path).split(".")[0]
                for g in src:
                    self.add_glyph(glyphset, g.name, unicodes=g.unicode)
            else:
                raise NotImplementedError(f"{src} not supported yet!")

    def add_glyph(self, glyphset, nice_name=None, unicodes=None):
        if nice_name in self._in_use:
            entry = next(
                (g for g in self._data["glyphs"] if g["nice_name"] == nice_name), None
            )
            if glyphset in entry["glyphsets"]:
                log.warning(f"Skipping {glyphset}.{nice_name}. Already exists!")
                return
            entry["glyphsets"].append(glyphset)
        else:
            # glyphsapp use hex strings for the unicode val. Convert these to ints
            if unicodes:
                uni_char = unicodes if isinstance(unicodes, int) else int(unicodes, 16)
                character = chr(uni_char)
            else:
                uni_char = None
                character = None
            glyphslib_data = get_glyph(nice_name)
            glyphslib_unicode = (
                None if not glyphslib_data.unicode else int(glyphslib_data.unicode, 16)
            )
            self._data["glyphs"].append(
                {
                    "nice_name": nice_name,
                    "production_name": glyphslib_data.production_name,
                    "character": character,
                    "unicode": uni_char or glyphslib_unicode,
                    "glyphsets": [glyphset],
                }
            )
            self._in_use.add(nice_name)

    def get_glyph(self, nice_name=None, production_name=None, character=None, uni=None):
        if nice_name:
            return next(
                (g for g in self._data["glyphs"] if g["nice_name"] == nice_name), None
            )
        elif production_name:
            return next(
                (
                    g
                    for g in self._data["glyphs"]
                    if g["production_name"] == production_name
                ),
                None,
            )
        elif character:
            return next(
                (g for g in self._data["glyphs"] if g["character"] == character), None
            )
        elif uni:
            return next((g for g in self._data["glyphs"] if g["unicode"] == uni), None)
        return None

    def build_glyphsapp_filter_list(
        self, glyphsets, use_production_names=False, out=None
    ):
        """Build filter lists"""
        glyphs = self.glyphs_in_glyphsets(glyphsets)
        if out and out.endswith("plist"):
            # glyphsapp need a prefix for the out file of "CustomFilter"
            if not os.path.basename(out).startswith("CustomFilter"):
                print(
                    "Prefixing 'CustomFilter' to out path since file is intended for Glyphsapp"
                )
                out = os.path.join(
                    os.path.dirname(out), "CustomFilter" + os.path.basename(out)
                )
            res = {k: [] for k in glyphsets}
            for glyphset in glyphsets:
                for glyph in glyphs:
                    if glyphset in glyph["glyphsets"]:
                        if use_production_names:
                            res[glyphset].append(glyph["production_name"])
                        else:
                            res[glyphset].append(glyph["nice_name"])

            res = [{"name": k, "list": v} for k, v in res.items()]
            res = [plistlib.dumps(res).decode("utf-8")]
        else:
            if use_production_names:
                res = [g["production_name"] for g in glyphs]
            else:
                res = [g["nice_name"] for g in glyphs]

        if out:
            with open(out, "w") as doc:
                doc.write("\n".join(res))
        return res

    def build_nam_file(self, glyphsets, out=None):
        "Build GF nam files from glyphsets"
        glyphs = [g for g in self.glyphs_in_glyphsets(glyphsets) if g["unicode"]]
        res = []
        for glyph in glyphs:
            code = (
                "0x" + hex(ord(glyph["character"])).replace("0x", "").zfill(4).upper()
            )
            res.append(f"{code} {uni.name(glyph['character'])}")
        res.sort()
        if out:
            with open(out, "w") as doc:
                doc.write("\n".join(res))
        return res

    def update_source_glyphset(self, src, glyphsets):
        """Add glyphs to a source file"""
        glyphs = self.glyphs_in_glyphsets(glyphsets)
        if isinstance(src, Font):
            glyphs_in_font = set(g.name for g in src)
            for glyph in glyphs:
                if glyph["nice_name"] in glyphs_in_font:
                    continue
                new_glyph = src.newGlyph(glyph["nice_name"])
                new_glyph.color = "Red"
                glyphs_in_font.add(glyph["nice_name"])
        elif isinstance(src, GSFont):
            glyphs_in_font = set(g.name for g in src.glyphs)
            for glyph in glyphs:
                if glyph["nice_name"] in glyphs_in_font:
                    continue
                new_glyph = GSGlyph(glyph["nice_name"])
                new_glyph.color = 1
                src.glyphs.append(new_glyph)
                glyphs_in_font.add(glyph["nice_name"])
        else:
            raise NotImplementedError(f"Cannot add glyphs font source not supported!")

    def build_fea(self, glyphset):
        """Generate a .fea file based on a glyphset"""
        # TODO this is 2022 Q3/4 goal
        raise NotImplementedError()


GFGlyphData = _GFGlyphData()


class _TestDocData:
    def __init__(
        self,
        data=json.load(open(TEST_STRINGS_DATA, encoding="utf8")),
        glyphsets=GFGlyphData,
    ):
        self._data = data
        self._glyphsets = glyphsets

    def test_strings_in_font(self, ttFont, threshold=0.95):
        res = {}
        glyphsets_in_font = self._glyphsets.glyphsets_fulfilled(ttFont)
        for glyphset, coverage in glyphsets_in_font.items():
            if coverage < threshold:
                continue
            test_strings = self._data.get(glyphset)
            if not test_strings:
                continue
            res[glyphset] = test_strings
        return res


GFTestData = _TestDocData()
