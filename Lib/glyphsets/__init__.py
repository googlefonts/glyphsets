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

    def update_db_from_sources(self, sources):
        """Update the database by using the glyphsets from source files.

        Please note that you may need to edit some data by hand"""
        for src in sources:
            if isinstance(src, GSFont):
                glyphset = os.path.basename(src.filepath).split(".")[0]
                for g in src.glyphs:
                    self._add_glyph(glyphset, g.name, unicodes=g.unicode)
            elif isinstance(src, Font):
                glyphset = os.path.basename(src.path).split(".")[0]
                for g in src:
                    self._add_glyph(glyphset, g.name, unicodes=g.unicode)
            else:
                raise NotImplementedError(f"{src} not supported yet!")

    def _add_glyph(self, glyphset, nice_name=None, unicodes=None):
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
            self._data["glyphs"].append(
                {
                    "nice_name": nice_name,
                    "production_name": glyphslib_data.production_name,
                    "character": character,
                    "unicode": uni_char,
                    "glyphsets": [glyphset],
                }
            )

    def build_glyphsapp_filter_lists(self, glyphset, out=None):
        "Build filter lists for glyphs app"
        res = []
        for g in self._data["glyphs"]:
            if glyphset not in g["glyphsets"]:
                continue
            res.append(g["nice_name"])
        if out:
            with open(out, "w") as doc:
                doc.write("\n".join(res))
        return res

    def build_nam_file(self, glyphsets, out=None):
        "Build GF nam files from glyphsets"
        res = []
        seen = set()
        for glyphset in glyphsets:
            for g in self._data["glyphs"]:
                if not g["unicode"] or g["unicode"] in seen:
                    continue
                seen.add(g["unicode"])
                if glyphset in g["glyphsets"]:
                    code = "0x" + hex(ord(g['character'])).replace("0x", "").zfill(4).upper()
                    res.append(f"{code} {uni.name(g['character'])}")
        if out:
            res.sort()
            with open(out, "w") as doc:
                doc.write("\n".join(res))
        return res

    def update_source_glyphset(self, src, glyphset):
        """Add glyphs to a source file"""
        if isinstance(src, Font):
            glyphs_in_font = set(g.name for g in src)
            for g in self._data["glyphs"]:
                if g["nice_name"] not in glyphs_in_font and glyphset in g["glyphsets"]:
                    new_glyph = src.newGlyph(g["nice_name"])
                    new_glyph.color = "Red"
            src.save()
        elif isinstance(src, GSFont):
            glyphs_in_font = set(g.name for g in src.glyphs)
            for g in self._data["glyphs"]:
                if g["nice_name"] not in glyphs_in_font and glyphset in g["glyphsets"]:
                    new_glyph = GSGlyph(g["nice_name"])
                    new_glyph.color = 1
                    src.glyphs.append(new_glyph)
        else:
            raise NotImplementedError(f"Cannot add glyphs font source not supported!")

    def build_fea(self, glyphset):
        """Generate a .fea file based on a glyphset"""
        # TODO this is 2022 Q3/4 goal
        raise NotImplementedError()


GFGlyphData = _GFGlyphData()