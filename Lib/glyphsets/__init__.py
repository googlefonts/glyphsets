"""
GF Glyph Database
"""
import json
import os
from re import L
from glyphsLib import GSFont, GSGlyph
from defcon import Font
import logging
import unicodedata2 as uni
from glyphsLib.glyphdata import get_glyph

try:
    from ._version import version as __version__  # type: ignore
except ImportError:
    __version__ = "0.0.0+unknown"


DATA_FP = os.path.join(os.path.dirname(__file__), "data.json")
log = logging.getLogger(__file__)


class _GFGlyphData:
    def __init__(self, data=json.load(open(DATA_FP))):
        self._data = data
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

    def build_glyphsapp_filter_list(self, glyphsets, out=None):
        "Build filter lists for glyphs app"
        glyphs = self.glyphs_in_glyphsets(glyphsets)
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
